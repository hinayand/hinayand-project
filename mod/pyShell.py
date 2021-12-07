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
      else:
       exec(self.pyshellCommand)
  def creatShell(self): 
    asyncio.run(self.shell())
    self.pyshellTerminalNum=self.pyshellTerminalNum   