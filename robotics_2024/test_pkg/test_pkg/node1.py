#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
        rclpy.init(args=None)
        node = Node("py_test_node")
        node.get_logger().info("Hello ROS2")
        rclpy.shutdown()

if __name__=="__main__":
    main()