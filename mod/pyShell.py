import asyncio
class PyShell(object):
    def __init__(self):
        self.pyshellCommand=0
        self.pyshellTerminalNum=0 
    async def shell(self):
        while True:
            self.pyshellCommand=input('pyshell$ ')
            if self.pyshellCommand=='exit':
                break
            elif self.pyshellCommand=='run':
                self.appName=input('Please enter App Name:') 
                import appLib
                appLoaderObject=appLib.AppLoader()
                appLoaderObject.loadAppByName(self.appName)
                del self.appName
            elif self.pyshellCommand=='appManaage':
                self.appName=input('Please enter App Name:')
                self.appManaageOpthion=input('What do you want to do?\nUnRegister\nRegister\nGetAppList\n')
                if self.appManaageOpthion=='UnRegister':
                    import appManaage
                    appUnRegisterObject=appManaage.AppManaage()
                    appUnRegisterObject.appUnRegister(self.appName)
                    del appUnRegisterObject
                elif self.appManaageOpthion=='Register':
                    self.appPath=input('Please enter App Path:')
                    import appManaage
                    appRegisterObject=appManaage.AppManaage()
                    appRegisterObject.appRegister(self.appName,self.appPath)	
                    del appRegisterObject
                elif self.appManaageOpthion=='GetAppList':
                    import appManaage
                    getAppListObject=appManaage.AppManaage()
                    getAppListObject.getAppList()
                del self.appName
                del self.appManaageOpthion 
            else:
                exec(self.pyshellCommand)
    def creatShell(self):
         asyncio.run(self.shell())
         self.pyshellTerminalNum=self.pyshellTerminalNum+1
