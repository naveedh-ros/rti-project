# MultiBot Controller Package

A ROS 2 package for controlling multiple robots with goal sending and pose monitoring capabilities.

## Using the package
```bash
colcon build
source install/setup.bash
ros2 launch multibot_controller multi_bot_control.launch.py 
```

## Nodes

### 1. `goal_sender.py`
**Purpose**:  
Listens for navigation goals on `/robot_goal` topic and forwards them to the appropriate robot's Nav2 action server.

**Features**:
- Supports multiple robots (e.g., `bot1`, `bot2`)
- Handles `NavigateToPose` action
- Automatic action client management per robot

**Topics**:
- Subscribes to: `/robot_goal` (`multibot_interfaces/msg/RobotGoal`)
- Action Clients: `/<robot_name>/navigate_to_pose`

**Example Usage**:
```bash
ros2 topic pub -1 /robot_goal multibot_interfaces/msg/RobotGoal "
robot_name:
  data: 'bot1'
pose:
  position: {x: 1.5, y: 2.0, z: 0.0}
  orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
"
```

### 2. `pose_server.py`
**Purpose**:

Provides a service to query current robot poses via AMCL.

**Services**:
```bash
/get_robot_pose (multibot_interfaces/srv/GetRobotPose)
```

**Usage**:
```bash
ros2 service call /get_robot_pose multibot_interfaces/srv/GetRobotPose "{robot_name: 'bot1'}"
```
