# StudyPet
ReadMe / Mini Project Design Document

Title: StudyPet
Authors / Programmers: Cindy Qiu, Gianna Sparks, and Lavanthi Narisman
Date Due: 5/21/2026
Date Submitted: 5/21/2026
Project Overview
High Concept: StudyPet is  a study pet/companion that helps students stay focused while they are working. Using a Raspberry Pi camera and YOLO object detection, the system detects when a user is holding a phone and displays a flashing warning screen telling them to “LOCK IN”. 

Problem or Purpose
Many high school students get distracted with their phones and doomscrolling, while they are trying to study. A few minutes of scrolling ruins their productivity and makes it harder for them to stay focused. We made this project to help them stay focused by making sure they are not on their phone for more than 5 seconds. 

Target User
Who would realistically use this system?
The target users are high school students who get easily distracted while studying, doing homework , especially the ones who do it during the night. 

AI System Design

Model(s) Used:  YOLOv8 Nano(YOLOv8n)
Identify the model(s) used.
Include:
LLM name : n/a
Vision model: YOLOv8
Speech tools: n/a
Why you chose them:  We chose YOLOv8 because it can detect objects quickly and works well on Raspberry Pi. It already knows how to recognize phones so we don’t need to train our own model.
Local Inference Design
Explain how your system runs locally
The entire project runs locally on the Raspberry Pi without internet access. The Raspberry Pi camera captures video frames and YOLO checks each frame to see if a phone is visible. 

What runs on the Pi:
	We run a program on the Pi where the camera connected to it identifies phones, and then outputs a message back to the camera display on the laptop.
What hardware acceleration is used:
	We did not have any hardware acceleration.
Performance observations:
	Our performance observation of the camera shows a small amount of lag, otherwise, the program works pretty well.
Limitations of local hardware:
	Limitations of Raspberry Pi 5 includes power demands (it was to be physically set up and plugged to power supply), thermal management, etc.
Prompting / Logic / Workflow
No prompts were used because YOLO is a vision model, not a language model. The workflow is the camera captures a frame, YOLO checks the frame for objects, the program checks if a cellphone is detected, if the phone stays visible for more than 5 seconds, the warning screen appears. If the user presses SPACE to return to the camera screen. The timer resets if the phone disappears before 5 seconds. 
User Interaction
Inputs:
	Camera feed and keyboard input
Outputs:
	Live camera display, flashing warning screen, LOCK IN message
Interface: 
It starts with a live camera feed. If a phone is detected for too long, the screen changes to a flashy warning screen.
Controls: 
	Space bar- returns back to the camera
	Q key - quits the program
How feedback is given:
	The output tells the user to get back on track, and gives that flashy warning screen.
Implementation
Connect the raspberry pi camera to the raspberry pi 5
Turn on raspberry pi
Open terminal and go to project folder
Type mything 3 main.py
The camera will show
If you have ur phone showing for 5  seconds a warning screen will show
Press space to continue and q to quit the program
Platform / Tools
Python
YOLOv8
OpenCV
Picamera2
Raspberry PI OS
NumPy
Hardware Used
Raspberry Pi 5
Raspberry Pi Camera Module
AI Hat+
MicroSD Card
Lavanthi’s Computer
Evaluation
What Works Well: I would say our code and time management went well.

What are you proud of?: Our team is proud of how consistent we are on keeping on track and within schedule with meeting up to complete the project. We are proud to be in a team with each other + croissant.

What worked better than expected?: How quick completing the coding part was, because the setup part ended up taking longer than the actual coding. The coding went very well, as we had little to no coding errors.

Known Limitations / Issues: The camera will not output sound to get the user’s attention.

Future Improvements: If we had more time, we would add sound alerts, and add an animated virtual pet.  It would use a pomodoro method of studying, so like in the 25 min study time, the phone can't be checked, and during the 5 minute break, then you can check your phone.
Academic Integrity
Honor Statement: Gianna Sparks, Cindy Qiu, Lavanthi Narasimman
AI / Collaboration Disclosure
Youtube tutorial for setting up the raspberry PI and interacting with the terminal
ChatGPT helped with debugging the 2nd problem we had.  I also used chatgpt to learn how to use the terminal and how to set up a porject. 
References
Bibliography
Exam Cheating Detection App | Real-Time Proctoring with Python, OpenCV, YOLOv8 & MediaPipe

CanaKit Raspberry Pi 5 AI HAT+ 2 Kit Software Guide

AI software - Raspberry Pi Documentation

YOLOv8 Full Tutorial Playlist | Object Detection, Segmentation & Classification Explained

How to Train YOLO Object Detection Models in Google Colab (YOLO26, YOLO11, YOLOv8)

Raspberry pi 5 camera module 3 setup for beginners

Master The Raspberry Pi Camera With This Simple Tutorial! 

Raspberry Pi 5: The Complete Beginner Setup Guide (Start to Finish!)

Resources / Tutors: Dr. Belcher & YouTube
Reflection

Cindy’s Reflection:
Although I might not have contributed/know things as much, I tried meeting up every time we have a meetup or need to go to office hours to try to either help or get help with the problems we encountered during the project (Around 15 hours). The biggest problem was just the technical side such as connecting through Raspberry Pi without a terminal or reinserting the camera for the code to run properly. We also had a time limit of two weeks which might not have allowed us to have a lot of functions. We were able to solve the problems through going to office hours and watching YouTube tutorials. I learned that every help is beneficial and there’s a solution to everything. I also learned that teamwork makes the dream work. 

Gianna’s Reflection:
I spent approximately 13 hours on the project; (only) including the times I met with group members and went to office hours. The biggest challenge that I encountered would be split between connecting to the pi through the network and correctly importing the camera into our code. Dr. Belcher hooked the pi up to his TV, then set up the account and network, so that we could access it through the network in raspberry pi connect. For the second issue I wasn’t able to join, the rest of the group went to Dr. Belcher’s office and found that they were referencing the wrong camera type (after Belcher reconnected the camera). I learned about many different types of alarms whenever we were originally trying to add a sound to the “LOCK IN”. I also enjoy learning about basic setup & terminal interaction for a raspberry pi 5 + the wonders of Dr. Belcher’s office hours.

Lavanthi’s Reflection: I wanna say around 15-16 hours. Cause we met for like 8 days, and we worked on together for probably 2 hours whenever we met.  In my opinion, the hardest part was setting up raspberry pi and getting the camera to work correctly with the YOLO detection system. I used chatgpt to give me the steps on how to setup raspberry pi and we also watched youtube videos. We also had to change the line  cv2.VideoCapture(0)  to Picamera 2(). So we used the cable camera instead of the USB webcam.  I learned how to use the terminal code in bash and use raspberry pi.  I also learned about YOLO, which I discovered through google. 
