# https://www.youtube.com/watch?v=R7B8sSByZGQ&list=PLb50TghpDs5uOn41QIzZKHr5N6VKIS5eW&index=3 
# learned from the upper link 
#to know inside of haarcascade feature and face detection feature watch the above video from 1:42:00 time the ppt is awesome
#https://www.youtube.com/watch?v=hPCTwxF0qf4&t=0s
#this link is by haarcascade it explains the logic

import cv2

from random import randrange
"""
#this code is for image 

#load some pre-trained data on face frontals fronm opencv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect face
img=cv2.imread("RDJ2.png")

#converting image image to grey color as haarcascade is trained on it 
#also face detection doesn't have to do anything with face color or image color
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
#so this will give face coordinates (i.e. upper left coordinates and then ht and width)
face_coordinates=trained_face_data.detectMultiScale(gray_img)
#print(face_coordinates)  


for (x,y,w,h) in face_coordinates:

    #draw rectangle around faces
    #                 it is upper left coordinates, then comes bottom right coordinates by adding height and width , then color , 
    #                 and then width of the box  
    cv2.rectangle(img,(x, y), (x+w, y+h),(randrange(256),randrange(256),randrange(256)),2)
    # func randrange is for random color of the box randrange(128,256) or randrange(256)

#to show image first is name second is image
cv2.imshow('face detection', img)
cv2.waitKey(3000)
print("hello")
"""

#this code is for a video


#load some pre-trained data on face frontals fronm opencv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#in haarcascade haar is the name of the dude but cascade means like a funnel it will 
# search for a property that looks similiar to preloaded face and as soon as it finds it recorganizes the face on screen 

#choose video to detect face 
webcam=cv2.VideoCapture(0)
#we put zero here so that it could capture the web cam ; you can also put a video file
while True:
    
    
    #read the current frame
    successful_frame_read, frame=webcam.read()
    # the read func will return two thing first will be success read part and the actual image or frame
    # 1-successful_frame_read this will be true or false 
    # 2-frame will contain image part
    
    
    #converting image image to grey color as haarcascade is trained on it 
    #also face detection doesn't have to do anything with face color or image color
    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    

    #detect faces
    #so this will give face coordinates (i.e. upper left coordinates and then ht and width)
    face_coordinates=trained_face_data.detectMultiScale(gray_img)
    #print(face_coordinates)  


    for (x,y,w,h) in face_coordinates:

        #draw rectangle around faces
        #                 it is upper left coordinates, then comes bottom right coordinates by adding height and width , then color , 
        #                 and then width of the box  
        cv2.rectangle(frame,(x, y), (x+w, y+h),(randrange(256),randrange(256),randrange(256)),2)
        # func randrange is for random color of the box randrange(128,256) or randrange(256)
        
    

    #to show image first is name second is image
    cv2.imshow('face detection', frame)
    #we put one inside waitkey func because it doesn't go next frame if time is mentioned inside it
    #and if there is no waitkey then u will not able to see your image even if program is running
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break
# release the video capture object
webcam.release()
print("completed")
