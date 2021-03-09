import rclpy
from rclpy.node import Node

from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped
from sensor_msgs.msg import Joy

class TorpedoJoy(Node):

    def __init__(self):

        super().__init__('torpedo_joy')

        self.drive_val = 0.0
        self.drive_f64 = FloatStamped()
        self.drive_f64.data = 0.0
        self.yaw_val = 0.0
        self.yaw_f64 = FloatStamped()
        self.yaw_f64.data = 0.0
        self.pitch_val = 0.0
        self.pitch_f64 = FloatStamped()
        self.pitch_f64.data = 0.0

        self.pub_yaw = self.create_publisher(FloatStamped,
            '/babyyoda/fins/id_0/input',
            10)
        self.pub_pitch = self.create_publisher(FloatStamped,
            '/babyyoda/fins/id_1/input',
            10)
        self.pub_drive = self.create_publisher(FloatStamped,
            '/babyyoda/thrusters/id_0/input',
            10)

        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joystick_state,
            10)
        self.subscription  # prevent unused variable warning

        timer_period = 1 / 30.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def joystick_state(self, data):

        self.drive_val = data.axes[4]
        self.yaw_val = data.axes[0]
        self.pitch_val = data.axes[1]

    def timer_callback(self):

        self.yaw_f64.data = self.yaw_val * -0.7
        self.pub_yaw.publish(self.yaw_f64)

        self.pitch_f64.data = self.pitch_val * 0.7
        self.pub_pitch.publish(self.pitch_f64)

        self.drive_f64.data = self.drive_val * 50.0
        self.pub_drive.publish(self.drive_f64)

def main(args=None):

    rclpy.init(args=args)

    torpedo_joy = TorpedoJoy()

    rclpy.spin(torpedo_joy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    torpedo_joy.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
