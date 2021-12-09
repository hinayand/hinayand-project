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
