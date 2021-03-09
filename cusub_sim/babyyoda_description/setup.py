from setuptools import setup
from glob import glob

package_name = 'babyyoda_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.launch')),
        ('share/' + package_name + '/urdf', glob('urdf/*')),
        ('share/' + package_name + '/robots', glob('robots/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dryerzinia',
    maintainer_email='mima3079@colorado.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'torpedo_joy = babyyoda_description.torpedo_joy:main',
        ],
    },
)
