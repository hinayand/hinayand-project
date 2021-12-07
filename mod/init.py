# 定义一个 "Init" 类，方便 "main.py" 的启动
class Init(object):
  def __init__(self,Coder,Ver):
    self.coderName=Coder
    self.version=Ver
  def init(self):
    print('Thank to {}'.format(self.coderName))
    print('Hinayand Project Ver {}'.format(self.version))
  def quit(self):
    import os
    os._exit()