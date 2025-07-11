#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from multibot_interfaces.msg import RobotGoal
from nav2_msgs.action import NavigateToPose

class GoalForwarder(Node):

    def __init__(self):
        super().__init__('goal_forwarder')
        
        # Subscriber for RobotGoal messages
        self.subscription = self.create_subscription(
            RobotGoal,
            '/robot_goal',
            self.goal_callback,
            10
        )
        
        # Dictionary to store action clients
        self.action_clients = {}
        
        self.get_logger().info("Ready to forward goals to robots")

    def goal_callback(self, msg):
        robot_name = msg.robot_name.data
        target_pose = msg.pose
        
        self.get_logger().info(f"Forwarding goal to {robot_name}: "
                             f"({target_pose.position.x}, {target_pose.position.y})")
        
        # Get or create action client
        if robot_name not in self.action_clients:
            self.action_clients[robot_name] = ActionClient(
                self, 
                NavigateToPose, 
                f'/{robot_name}/navigate_to_pose'
            )
        
        client = self.action_clients[robot_name]
        
        # Prepare the goal
        goal_msg = NavigateToPose.Goal()
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = "map"
        goal_pose.header.stamp = self.get_clock().now().to_msg()
        goal_pose.pose = target_pose
        goal_msg.pose = goal_pose
        
        client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoalForwarder()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
