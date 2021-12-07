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
    self.appDatabase=configReadObject.readJSONConfig('config/appLib.conf') 
    for key in self.appDatabase:
      if key==appName:
        self.appIO=open(self.appDatabase[key]) 
        self.appResult=self.appIO.readlines() 
        for i in range(len(self.appResult)):
          exec(self.appResult[i])
        del self.appIO
        del self.appResult
      else:
        print('Error:load App fail!')