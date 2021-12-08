import configTool
configReadObject=configTool.ConfigRead()
configWriteObject=configTool.ConfigWrite() 

class AppLib(object):
  def __init__(self):
    pass

class AppLoader(AppLib):
  def __init__(self):
    pass
  def loadAppByName(self,appName):
    import sys
    sys.path.append('./app/')
    exec('import {}'.format(appName))
