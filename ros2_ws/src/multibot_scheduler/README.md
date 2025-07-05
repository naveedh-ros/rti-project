# Multibot Scheduler Package

A ROS 2 package for scheduling multiple robots.

## Using the package
```bash
colcon build
source install/setup.bash
ros2 run multibot_scheduler schedule
```

## Sending the tasks
```bash
ros2 service call /execute_task multibot_interfaces/srv/Task "{x: 0.0, y: 0.0, priority: 0}"
```
