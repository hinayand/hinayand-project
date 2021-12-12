import sys
sys.path.append('../../')

class AppApi(object):
    def __init__(self):
        pass

class AppNet(AppApi):
    def __init__(self):
        pass
    def appOpen(self,appName):
        from mod import appLib
        appOpenObject=appLib.AppLoader()
        appOpenObject.loadAppByName(appName)
        del appOpenObject
    def showMessage(self,message):
        print(message)
    def getUserInput(self,prompt):
        return input(prompt)

class AppFileIO(AppApi):
    def __init__(self):
        pass
    def writeFile(self,filePath,text,mode):
        self.appFileWriteIO=open(filePath,mode)
        self.appFileWeiteIO.write(text)
        del self.appFileWriteIO
    def readFile(self,filePath):
        self.appFileReadIO=open(filePath)
        return self.appFileReadIO.read()
        del self.appFileReadIO
    def readNetworkFile(self,httpFilePath):
        import requests
        return requests.get(httpFilePath).text
