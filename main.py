import sys
sys.path.append('./mod')
from mod import configTool
from mod import pyShell

class Main(object):
  def __init__(self):
    pass
  def mainInit(self):  
    configReadObject.runConfigFile('initConfig.conf')
  def openBasicShell(self):
    shell=pyShell.PyShell()
    shell.creatShell()

mainObject=Main()
configReadObject=configTool.ConfigRead()
mainObject.mainInit()
mainObject.openBasicShell()
