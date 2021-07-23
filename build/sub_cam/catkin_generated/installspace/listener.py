#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge

class Follower:
    def __init__(self):
        self.image2_pub = rospy.Publisher('python_cam/image_raw', Image)                    #Publica Topico Imagen Invertida
        self.bridge = cv_bridge.CvBridge()                                                  #Puente Entre OpenCV y ROS
        #cv2.namedWindow("window", 1)                                                       #Muestra Web Cam en una ventana aparte
        self.image_sub = rospy.Subscriber('usb_cam/image_raw', Image, self.image_callback)  #Se subscribe a topico WebCam

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")                                   #Se le transfieren datos de la webcam
        frame = cv2.flip(cv_image, 0)                                                       #Rota la imagen de la WebCam
        cv2.waitKey(3)
        self.image2_pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))                   #Publica la imagen invertidad
    
rospy.init_node('follower')
follower = Follower()
rospy.spin()                                                                                #Ejecuta el nodo hasta que se mate el proceso
cv2.destroyAllWindows()