import asyncio
class PyShell(object):
    def __init__(self):
        self.pyshellCommand=0
        self.pyshellTerminalNum=0
    async def shell(self):
        import pyShellLogic
    def creatShell(self):
         asyncio.run(self.shell())
         self.pyshellTerminalNum=self.pyshellTerminalNum+1
