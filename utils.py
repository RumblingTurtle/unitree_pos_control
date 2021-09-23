class InputCommand:
  def __init__(self, linearSpeed,angularSpeed):
      self.linearSpeed = linearSpeed
      self.angularSpeed = angularSpeed
      self.useIMU = True
  
  def transformToPosControl(self):
    inputVec = [0,0,1,0,0,1,0,0]
    buttons = [False]*8

    inputVec[4] = self.linearSpeed[0]
    inputVec[3] = self.linearSpeed[1]
    inputVec[0] = self.angularSpeed

    if self.useIMU == True:
      buttons[7]=True

    return inputVec,buttons