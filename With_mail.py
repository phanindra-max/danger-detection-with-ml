# -*- coding: utf-8 -*-
"""
Created on Sun May 3 00:08:15 2021

@author: Phanindra
"""
import os
import cv2
import smtplib
import argparse
import numpy as np
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

parser = argparse.ArgumentParser()
parser.add_argument('--webcam', help="True/False", default=False)
parser.add_argument('--image', help="Tue/False", default=False)
parser.add_argument('--image_path', help="Path of image to detect objects", default="use-this.jpg")
parser.add_argument('--verbose', help="To print statements", default=True)
args = parser.parse_args()

#for the mail feature
mailfrom = "SendersEmail"
gmailpass = "SendersPass"
mailto = "ReciversEmail"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(mailfrom, gmailpass)
sleep(5)       #to give smtp sometime to login to your gmail account

def SendMail(frameImg):
    img_data = open(frameImg, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Alert from Danger Detection Script'
    msg['From']= mailfrom
    msg['To'] = mailto

    text = MIMEText("Alert found something suspicious from your video source. Please have a look at it.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(frameImg))
    msg.attach(image)

    s.send_message(msg)

def load_yolo():
	net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
	classes = []
	with open("obj.names", "r") as f:
		classes = [line.strip() for line in f.readlines()]

	layers_names = net.getLayerNames()
	output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))
	return net, classes, colors, output_layers

def load_image(img_path):
	# image loading
	img = cv2.imread(img_path)
	img = cv2.resize(img, None, fx=0.4, fy=0.4)
	height, width, channels = img.shape
	return img, height, width, channels

def display_blob(blob):
	'''
		Three images each for RED, GREEN, BLUE channel
	'''
	for b in blob:
		for n, imgb in enumerate(b):
			cv2.imshow(str(n), imgb)
            
def detect_objects(img, net, outputLayers):			
	blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
	net.setInput(blob)
	outputs = net.forward(outputLayers)
	return blob, outputs

def get_box_dimensions(outputs, height, width):
	boxes = []
	confs = []
	class_ids = []
	for output in outputs:
		for detect in output:
			scores = detect[5:]
			class_id = np.argmax(scores)
			conf = scores[class_id]
			if conf > 0.3:
				center_x = int(detect[0] * width)
				center_y = int(detect[1] * height)
				w = int(detect[2] * width)
				h = int(detect[3] * height)
				x = int(center_x - w/2)
				y = int(center_y - h / 2)
				boxes.append([x, y, w, h])
				confs.append(float(conf))
				class_ids.append(class_id)
	return boxes, confs, class_ids
			
def draw_labels(boxes, confs, colors, class_ids, classes, img): 
	indexes,a,label = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4), False, False
	font = cv2.FONT_HERSHEY_PLAIN
	for i in range(len(boxes)):
		if i in indexes:
			x, y, w, h = boxes[i]
			label,a = str(classes[class_ids[i]]), True
			color = colors[i]
			cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
			cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
	img=cv2.resize(img, (640,480))
	cv2.imshow("Image", img);return a, label, img
    

def image_detect(img_path): 
	model, classes, colors, output_layers = load_yolo()
	image, height, width, channels = load_image(img_path)
	blob, outputs = detect_objects(image, model, output_layers)
	boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
	draw_labels(boxes, confs, colors, class_ids, classes, image)
	while True:
		key = cv2.waitKey(1)
		if key == ord('q'):
			break

def webcam_detect():
    model, classes, colors, output_layers = load_yolo()
    cap = cv2.VideoCapture(0)
    
    while True:
        _, frame = cap.read()
        height, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        a, label, img= draw_labels(boxes, confs, colors, class_ids, classes, frame)
        key = cv2.waitKey(1)
        if a:
            cv2.imwrite('Alert.jpg', frame)
            SendMail('Alert.jpg')
            print(" \n Mail_Sent!")
            sleep(5)
        elif key == ord('q'):
            break
    cap.release()
    
if __name__ == '__main__':
	webcam = input("Enter Y for Web cam:")
	image = args.image
    
	if webcam == "Y":
		if args.verbose:
			print('---- Starting Web Cam object detection ----')
		webcam_detect()
        
	else :
		image_path = args.image_path
		if args.verbose:
			print("Opening "+image_path+" .... ")
		image_detect(image_path)
        
	cv2.destroyAllWindows();#mailServer.quit()