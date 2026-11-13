import DobotDllType as dType
api = dType.load()
dType.ConnectDobot(api, "", 115200)

GreenBoxXFrontIn = None
BlueBoxXFrontIn = None
RedBoxXFrontIn = None

DobotDefaultX = None

DobotSetBoxUpX = None
DobotSetBoxDownX = None

start = None

GreenBoxYFrontIn = None
BlueBoxYFrontIn = None
RedBoxYFrontIn = None

DobotDefaultY = None

DobotSetBoxUpY = None
DobotSetBoxDownY = None

max2 = None

GreenBoxZFrontIn = None
BlueBoxZFrontIn = None
RedBoxZFrontIn = None

DobotDefaultZ = None

DobotSetBoxUpZ = None
DobotSetBoxDownZ = None

RedButton = None
BlueButton = None
GreenButton = None

GreenBoxXIn = None
BlueBoxXIn = None
RedBoxXIn = None

RedBoxHeight = None
BlueBoxHeight = None
GreenBoxHeight = None

GreenBoxYIn = None
BlueBoxYIn = None
RedBoxYIn = None

GreenBoxZIn = None
BlueBoxZIn = None
RedBoxZIn = None

GreenBoxXFrontOut = None
BlueBoxXFrontOut = None
RedBoxXFrontOut = None

GreenBoxYFrontOut = None
BlueBoxYFrontOut = None
RedBoxYFrontOut = None

GreenBoxZFrontOut = None
BlueBoxZFrontOut = None
RedBoxZFrontOut = None

RedBoxXOut = None
RedBoxYOut = None
RedBoxZOut = None

GreenBoxXOut = None
BlueBoxXOut = None

GreenBoxYOut = None
BlueBoxYOut = None

GreenBoxZOut = None
BlueBoxZOut = None


GreenBoxXFrontIn = 0
GreenBoxYFrontIn = 0
GreenBoxZFrontIn = 0

GreenBoxXIn = 0
GreenBoxYIn = 0
GreenBoxZIn = 0

GreenBoxXFrontOut = 0
GreenBoxYFrontOut = 0
GreenBoxZFrontOut = 0

GreenBoxXOut = 0
GreenBoxYOut = 0
GreenBoxZOut = 0

GreenBoxHeight = 0

BlueBoxXFrontIn = 0
BlueBoxYFrontIn = 0
BlueBoxZFrontIn = 0

BlueBoxXIn = 0
BlueBoxYIn = 0
BlueBoxZIn = 0

BlueBoxXFrontOut = 0
BlueBoxYFrontOut = 0
BlueBoxZFrontOut = 0

BlueBoxXOut = 0
BlueBoxYOut = 0
BlueBoxZOut = 0

BlueBoxHeight = 0

RedBoxXFrontIn = 0
RedBoxYFrontIn = 0
RedBoxZFrontIn = 0

RedBoxXIn = 0
RedBoxYIn = 0
RedBoxZIn = 0

RedBoxXFrontOut = 0
RedBoxYFrontOut = 0
RedBoxZFrontOut = 0

RedBoxXOut = 0
RedBoxYOut = 0
RedBoxZOut = 0

RedBoxHeight = 0

DobotDefaultX = 0
DobotDefaultY = 0
DobotDefaultZ = 0

DobotSetBoxUpX = 0
DobotSetBoxUpY = 0
DobotSetBoxUpZ = 0

DobotSetBoxDownX = 0
DobotSetBoxDownY = 0
DobotSetBoxDownZ = 0

start = 1000
max2 = 0

dType.SetDeviceWithL(api, 1, 1)

if RedButton == True:

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], RedBoxHeight, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, RedBoxXFrontIn, RedBoxYFrontIn, RedBoxZFrontIn, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, RedBoxXIn, RedBoxYIn, RedBoxZIn, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, RedBoxXOut, RedBoxYOut, RedBoxZOut, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, RedBoxXFrontOut, RedBoxYFrontOut, RedBoxZFrontOut, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], start, 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotSetBoxUpX, DobotSetBoxUpY, DobotSetBoxUpZ, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotSetBoxDownX, DobotSetBoxDownY, DobotSetBoxDownZ, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

elif BlueButton == True:

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], BlueBoxHeight, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, BlueBoxXFrontIn, BlueBoxYFrontIn, BlueBoxZFrontIn, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, BlueBoxXIn, BlueBoxYIn, BlueBoxZIn, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, BlueBoxXFrontOut, BlueBoxYFrontOut, BlueBoxZFrontOut, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], start, 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotSetBoxUpX, DobotSetBoxUpY, DobotSetBoxUpZ, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotSetBoxDownX, DobotSetBoxDownY, DobotSetBoxDownZ, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

elif GreenButton == True:

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], GreenBoxHeight, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, GreenBoxXFrontIn, GreenBoxYFrontIn, GreenBoxZFrontIn, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, GreenBoxXIn, GreenBoxYIn, GreenBoxZIn, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, GreenBoxXFrontOut, GreenBoxYFrontOut, GreenBoxZFrontOut, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], start, 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotSetBoxUpX, DobotSetBoxUpY, DobotSetBoxUpZ, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotSetBoxDownX, DobotSetBoxDownY, DobotSetBoxDownZ, current_pose[3], 1)

  dType.SetWAITCmdEx(api, 1, 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

else:

  current_pose = dType.GetPose(api)

  dType.SetPTPCmdEx(api, 2, DobotDefaultX, DobotDefaultY, DobotDefaultZ, current_pose[3], 1)

  current_pose = dType.GetPose(api)

  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], start, 1)