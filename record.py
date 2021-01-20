from util.mouse import MEvent
from util.keyboard import KEvent
import init
import threading
class Monitor (threading.Thread):
  def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter
  def run(self):
    # if (self.name == 'Thread-1'):
      # kEvent = KEvent()
      # kEvent.start()
    if (self.name == 'Thread-2'):
      mEvent = MEvent()
      mEvent.start()
# 创建新线程
monitor1 = Monitor(1, 'Thread-1', 1)
monitor2 = Monitor(2, 'Thread-2', 2)
monitor1.start()
monitor2.start()