

import launch
import launch_ros.actions

def generate_launch_description():
    ros1_dynamic_bridge = launch_ros.actions.Node(package='ros1_bridge',
                                                   executable='dynamic_bridge',
                                                   output='screen',
                                                   arguments=[
                                                              # '--print-pairs',
                                                              # '--show-introspection',
                                                              # '--bridge-all-topics',
                                                              # '--bridge-all-1to2-topics',
                                                              # '--bridge-all-2to1-topics'
                                                              ])

    return launch.LaunchDescription([ros1_dynamic_bridge
                                     ])
