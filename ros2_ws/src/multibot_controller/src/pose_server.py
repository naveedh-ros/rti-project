#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from multibot_controller.srv import GetRobotPose
from geometry_msgs.msg import PoseWithCovarianceStamped

class PoseServer(Node):
    def __init__(self):
        super().__init__('amcl_pose_server')
        self.poses = {}  # Stores latest poses per robot
        
        # Service
        self.srv = self.create_service(GetRobotPose, '/get_robot_pose', self.get_pose_callback)
        
        # Subscribers for each robot's AMCL pose
        self.create_subscription(
            PoseWithCovarianceStamped,
            '/bot1/amcl_pose',
            lambda msg: self.pose_callback('bot1', msg),
            10
        )
        self.create_subscription(
            PoseWithCovarianceStamped,
            '/bot2/amcl_pose',
            lambda msg: self.pose_callback('bot2', msg),
            10
        )
        
        self.get_logger().info("AMCL Pose Server Ready")

    def pose_callback(self, robot_name, msg):
        self.poses[robot_name] = msg.pose.pose

    def get_pose_callback(self, request, response):
        if request.robot_name in self.poses:
            response.pose = self.poses[request.robot_name]
        else:
            self.get_logger().warn(f"No pose available for {request.robot_name}")
            response.pose = Pose()  # Return empty pose
        return response

def main(args=None):
    rclpy.init(args=args)
    server = PoseServer()
    rclpy.spin(server)
    server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
