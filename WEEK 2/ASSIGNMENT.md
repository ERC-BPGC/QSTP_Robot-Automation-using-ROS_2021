# Week 2 Assignment

You will be making a ROS package om thos assignment called *week2* which will contain all the code for the various nodes you will write. You can use the command `catkin_create_pkg` for this (check out the tutorial [here](http://http://wiki.ros.org/ROS/Tutorials/CreatingPackage "here")). All your code should go in the *scripts* folder inside the package. 

## 1. Publisher - Subscriber Model [10 points]
Like all other assignments, let us start with the 'Hello, World!'. Write two nodes, one which publishes 'Hello,' on topic */hello* and another which publishes 'World!' on topic */world*. 

Now write a third node which will subscribe to the topics */hello* and */world*, and publish the combined message 'Hello, World!' on the topic */helloworld*

## 2. Client - Service Model [10 points]
Write a server which accepts a request with the state of the robot (x, y, theta) as well as the control commands (v, w). The server should have default values (i.e. you can hard code them in the server code) for *dt* (0.05) and *timesteps n* (50). All these parameters are similar to the [week 1](http://https://github.com/ERC-BPGC/QSTP_Robot-Automation-using-ROS_2021/blob/main/WEEK%201/ASSIGNMENT.md "week 1") assignment. The server will return the intermeditate trajectory of the robot (similar to the last week's assignment). You can plot the trajectory in the client node.

For a guide on services, look at Chapter 4 of Morgan Quigley. For more infor on messages, look at [this](http://http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv "this") link or page 39 of Morgan Quigley. You may use the code you
have written in last week's assignment.

## 3. Automation of Turtlebot [80 points]
This question is divided into 3 interrelated parts. All three will work together to make
the turtlebot move in a circular motion in Gazebo

### 3.1 Publisher [5 points]
Write a publisher node which publishes the radius of movement for turtlebot on the
topic */radius.*
### 3.2 Service [5 points]
Write a server which takes in radius and outputs the angular velocity required to move the turtlebot in a circle of that radius on a service named *compute_ang_vel* Assume the linear velocity of the turtlebot will be set to 0.1.
### 3.3 Turtlebot [25 points]
Write a node that subscribes to the /radius topic and is the client to the *compute_ang_vel* service. It will also be a publisher for *cmd_vel*. Whenever a radius message is received, the callback for the subscriber should execute the service proxy function to calculate the required angular velocity. Once the velocity is received from the server you need to publish it to cmd_vel to make turtlebot move. Make sure you set linear velocity to 0.1.
### 3.4 Going a step further [45 points]
You need to write a publisher which makes the turtlebot move in the shape of the number eight/infinity in gazebo. You could create a [launchfile](https://www.youtube.com/watch?v=pCBwos89fI0) for all the nodes.

## Submission
To submit this assignment, you need to push the whole package (not workspace) into you GitHub repo (make a directory called week 2). Additionally for the 3rd subtask, you need to use `rosbag`. Rosbags are files which used to record a stream of messages on any topic. Follow [this](http://http://wiki.ros.org/rosbag/Tutorials/Recording%20and%20playing%20back%20data "this") tutorial to learn how to record and play rosbag files. The bag file recorded should contain the messages published on the topics */radius* and */cmd_vel*. Record a bag file for the case r=1. You can decide the time of the bag file recording after checking out the simulation of your code.

Also, you can submit the link of your GitHub repo in the Google Classroom assignment submission.
