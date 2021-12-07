import configTool
configWriteObject=configTool.ConfigWrite()
configReadObject=configTool.ConfigRead()

class AppManaage(object):
    def __init__(self):
        pass
    def appRegister(self,appName,appPath):
        self.appDatabase=configReadObject.readJSONConfig('config/appLib.conf')
        self.appDatabase[appName]=appPath
        configWriteObject.writeByJSON(self.appDatabase,'config/appLib.conf')
        del self.appDatabase
    def appUnRegister(self,appName):
        self.appDatabase=configReadObject.readJSONConfig('config/appLib.conf')
        del self.appDatabase[appName]
        configWriteObject.writeByJSON(self.appDatabase,'config/appLib.conf')
        delself.appDatabase
