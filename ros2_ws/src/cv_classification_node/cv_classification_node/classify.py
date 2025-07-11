import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class ClassifyNode(Node):
    def __init__(self):
        super().__init__("classify_node")
        self.subscription = self.create_subscription(
            Image, "test_camera/image_raw", self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()
        self.get_logger().info(
            "cv_classification_node started, listening to /image_raw"
        )

    def listener_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
            cv2.imshow("Camera Feed", cv_image)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = ClassifyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
