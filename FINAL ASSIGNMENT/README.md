# Final Assignment
## Problem Statement
You are a Robot Spy. There a thief that is capable of teleporting from one location to another. The thief stays at one spot only for a minute. You duty is to catch a glimpse of the theif as many times as possible. \\
The spy is a turtlebot. Here is the exact details of the task that you have to perform.
1. The theif's location is published as a `geometry_msgs/PoseStamped` message on the topic `thief_pose`. This is the last known pose of the thief. This changes every minute. Your main goal is to go within `1m` of the thief's position before the position changes again.
2. You are not supposed to go closer than `1m` to the thief (tolerance of 10%)
3. Everytime you approach the thief, you have to publish a message of type `std_msgs/String` saying "Found you!!".

## Technical Description
1. Write a controller node to control your robot based on given path or waypoints. You may either use a PID Controller or Pure Pursuit to achieve this task.
2. You will be required to put all your helper files and/or nodes in a the scripts folder of the `turtlebot_spy` package. You will need to write one launch file, `turtlebot_spy.launch` to launch your solution to the Problem.

## Submission Guidelines
You are required to submit the following.
1. RVIZ Video of any of your succesful run. The pose of the thief must also be visualised.
2. The solution `turtlebot_spy` package.
3. There are no obstacles in this environment. How would tackle a scenario where there are sparse obstacles? Write an explanation of your solution. Pseudo code of the proposed solution will be appreciated. You can submit a .md file name `EXPLANATION.md` in the package.

__Note__: The turtlebot_spy package can be found [here](turtlebot_spy/README.md). Instructions to launch the required files are given there.
