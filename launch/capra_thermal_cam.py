from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node',
            name='capra_thermal_cam',
            output='screen',
            parameters=[
                {'video_device': '/dev/video2'},
                {'image_width': 160},
                {'image_height': 120},
                {'pixel_format': 'uyvy'},
                {'camera_frame_id': 'purethermal'},
                {'io_method': 'mmap'},
                {'framerate': 18},
            ]
        )
    ])
