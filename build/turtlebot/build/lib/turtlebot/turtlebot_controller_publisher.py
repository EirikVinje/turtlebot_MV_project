#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from geometry_msgs.msg import Twist
import random

class Move_robot(Node):

    def __init__(self):
        
        super().__init__("Move_robot")
        
        self.topic_port = "/cmd_vel"
        self.message_publisher = self.create_publisher(Twist, self.topic_port, 10) #(msg type, topic, queuesize(?))
        
        timer_period = 1  
        self.timer = self.create_timer(timer_period, self.move_callback)
        
        self.vel_msg = Twist()
        self.vel_msg.linear.x = 0.5
        self.vel_msg.angular.z = 0.3
        
        self.linear_x = self.vel_msg.linear.x
        self.angular_z = self.vel_msg.angular.z

        self.r = self.create_rate(30)
        
    def move_callback(self):
        
        self.message_publisher.publish(self.vel_msg)
        self.get_logger().info('linear speed {}, angular speed {}'.format(self.linear_x, self.angular_z))
            
    def shutdown_turtlebot(self):
        self.message_publisher.publish(Twist())
        
        
        
        

def main(args=None):
    
    rclpy.init(args=args)
    
    move = Move_robot()
    
    #move.move_callback()
    
    rclpy.spin(move)

    move.destroy_node()
    
    rclpy.shutdown()

if __name__ == "__main__":
    
    main()
    