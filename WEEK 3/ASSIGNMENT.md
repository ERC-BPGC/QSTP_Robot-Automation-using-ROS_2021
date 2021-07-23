# Week 3 Assignment
The task for this week is to write a PID Controller for a differential drive Robot. Below given is a node that publishes three paths in three different topics. The paths `path1`, `path2` , `path3` increase in complexity. However designing a proper controller will ensure that all the paths can be tracked without any changes in Control parameters. The detailed task is as follows:

## 1. Write PID Controller Node [100 Points]
Write a PID Controller node that can track a given path.

1. Subscribe to the various path messages from topics `/path1`, `/path2`, `/path3`.
2. Process the path and publish velocity commands on the topic `/cmd_vel`.
3. Validate the control using simulations. You can use a turtlebot3 empty world simulation for this.

Make a separate ROS package for this week's assignment as `week3` and push this to your repository. Write a launch file called `pid_controller_simple.launch` with an argument `path_topic` that takes in the path topic to follow.
You are required to submit a `rosbag` of the robot tracking `path3`. The path publisher node can be found [here](path_publisher.py).

## 2. Going a Step Further [Optional]
Since you already have a controller ready, can you move the turtlebot wherever it is commanded?
### Task Description
1. Write a launch file `pid_controller_goto.launch` that should launch the controller along with Rviz.
2. From Rviz, send a `2D Nav Goal` to command the turtlebot to go. Refer to this [page](http://wiki.ros.org/navigation/Tutorials/Using%20rviz%20with%20the%20Navigation%20Stack) to know more about the `2D Nav Goal`.
### Submission
1. Place the launch file in the same ros package, push your changes to your repository. If possible add a `Video Recording` of the turtlebot reaching the multiple goals.