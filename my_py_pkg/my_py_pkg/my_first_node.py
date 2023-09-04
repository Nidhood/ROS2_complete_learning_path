#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hello ROS!!!")
        self.create_timer(0.5, self.timer_callback)


    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("Hello " + str(self.counter))

def main(args=None):
    rclpy.init(args=args) # Here goes always as first command.
    node = MyNode()
    rclpy.spin(node) # Spin stop the program and allows to continiuo to be alive.
    rclpy.shutdown() # Here goes always the final command.

if __name__ == "__main__":
    main()