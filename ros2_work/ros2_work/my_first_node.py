#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("first_node")
        #self.get_logger().info("Hello from Ying Terapong potisuwan xzcxzcxzc fffffff")
        self.counter_ = 0
        self.create_timer(1.0, self.time_callback)

    def time_callback(self):
        self.get_logger().info("Hello TOTO " + str(self.counter_))
        self.counter_ += 1
        
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) #มันจะค้างไว้อยู่ จนกว่าจะ control C ออก
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()    
