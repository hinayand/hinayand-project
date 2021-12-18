import json
class ConfigIO():
  def __init__(self):
    pass

class ConfigWrite(ConfigIO):
  def __init__(self):
    pass
  def writeByJSON(self,JSONData,JSONFilePath):
    self.configIO=open(JSONFilePath,'w')
    self.configIO.write(json.dumps(JSONData))
    self.close()
    del self.configIO

class ConfigRead(ConfigIO):
  def __init__(self):
    pass
  def runConfigFile(self,filename):
    self.configIO=open(filename)
    self.configResult=self.configIO.readlines()
    for i in range(len(self.configResult)):
      exec(self.configResult[i])
    del self.configIO
    del self.configResult
  def readJSONConfig(self,JSONFilePath):
    self.configIO=open(JSONFilePath)
    self.configResult=json.loads(self.configIO.read())
    del self.configIO
    return self.configResult
    del self.configResult
