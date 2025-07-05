from action_msgs.msg import GoalStatusArray
import rclpy
from queue import PriorityQueue
from rclpy.node import Node
from multibot_interfaces.msg import RobotGoal
from multibot_interfaces.srv import Task

class Scheduler(Node):
    def __init__(self):
        super().__init__('scheduler_node')
        self.declare_parameter("no_robots", 2)
        self.task_queue = PriorityQueue()
        self.no_robots = self.get_parameter('no_robots').get_parameter_value().integer_value

        self.bot_status = [0 for _ in range(self.no_robots)]
        self.task_receiver = self.create_service(
            Task,
            'execute_task',
            self.add_tasks
        )

        # Initialize goal sender (publisher)
        self.goal_sender = self.create_publisher(RobotGoal, "/robot_goal", 10)

        # Initialize status subscribers once
        self.status_subscribers = []
        for i in range(self.no_robots):
            sub = self.create_subscription(
                GoalStatusArray,
                f'/bot{i+1}/navigate_to_pose/_action/status',
                lambda msg, idx=i: self.update_status(msg, idx),  # Fix lambda capture
                10
            )
            self.status_subscribers.append(sub)

        self.timer = self.create_timer(0.5, self.execute_tasks)

    def update_status(self, msg, bot_id):
        if msg.status_list:
            self.bot_status[bot_id] = msg.status_list[-1].status  # Get latest status

    def execute_tasks(self):
        if not self.task_queue.empty():
            for i in range(self.no_robots):
                if self.bot_status[i] in [0, 4, 5, 6]:  # IDLE or terminal states
                    _, task = self.task_queue.get()
                    x, y = task
                    goal_msg = RobotGoal()
                    goal_msg.robot_name.data = f"bot{i+1}"
                    goal_msg.pose.position.x = x
                    goal_msg.pose.position.y = y
                    goal_msg.pose.position.z = 0.0
                    goal_msg.pose.orientation.x = 0.0
                    goal_msg.pose.orientation.y = 0.0
                    goal_msg.pose.orientation.z = 0.0
                    goal_msg.pose.orientation.w = 1.0

                    self.goal_sender.publish(goal_msg)
                    break

    def add_tasks(self, request, response):
        self.task_queue.put((request.priority, (request.x, request.y)))
        response.result = "Success"
        return response

def main(args=None):
    
    rclpy.init(args=args)
    node = Scheduler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


