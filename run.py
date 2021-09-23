from A1GazeboInterface import A1GazeboInterface
from utils import InputCommand
import scipy.interpolate
import time

def getSpeedsLinAng(t):
  """Creates an example speed profile based on time for demo purpose."""
  vx = 0.8
  vy = 0.2
  wz = 0.8
  # vx = 0.0
  # vy = 0.0
  # wz = 0.0

  # time_points = (0, 5, 10, 15, 20, 25, 30)
  # speed_points = ((0, 0, 0, 0), (vx, 0, 0, 0), (vx, 0, 0, 0), (0, 0, 0, -wz),
  #                 (0, -vy, 0, 0), (0, 0, 0, 0), (0, 0, 0, wz))

  time_points = (0, 20)
  speed_points = ((0, 0, 0, 0), (vx, 0, 0, 0))

  speed = scipy.interpolate.interp1d(time_points,
                                     speed_points,
                                     kind="linear", # pay attention to kind (default "linear")
                                     fill_value="extrapolate",
                                     axis=0)(t)

  return speed[0:3], speed[3], False

MAX_TIME_SECS = 20
robot = A1GazeboInterface(position_control=True,use_real_robot=True)

startTime = time.time()
currentTime = time.time()

while  currentTime - startTime < MAX_TIME_SECS:
    lin_speed, ang_speed, e_stop = getSpeedsLinAng(currentTime)

    inputCommand = InputCommand(lin_speed,ang_speed)

    if not robot.sendControllerCommand(inputCommand):
        break
    currentTime = time.time()

