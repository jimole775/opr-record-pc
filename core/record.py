from core.mouse import MEvent
from core.keyboard import KEvent
import threading
# class Monitor (threading.Thread):
#     def __init__ (self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter

#     def run (self):
#         if self.name == 'Thread-1':
#             kEvent = KEvent()
#             kEvent.start()
#         if self.name == 'Thread-2':
#             mEvent = MEvent()
#             mEvent.start()

class Record ():
    def __init__ (self):
        pass
    def createThread (self, event):
        thread = threading.Thread(target=event)
        thread.start()

    def keyboardEvent (self):
        kEvent = KEvent()
        kEvent.start()

    def mouseEvent (self):
        mEvent = MEvent()
        mEvent.start()

    def run (self):
        # 创建新线程
        # monitor1 = Monitor(1, 'Thread-1', 1)
        # monitor2 = Monitor(2, 'Thread-2', 2)
        # monitor1.setDaemon(True) # 主线程关闭, 子线程将被摧毁
        # monitor2.setDaemon(True) # 主线程关闭, 子线程将被摧毁
        # monitor1.start()
        # monitor2.start()
        self.createThread(self.keyboardEvent)
        self.createThread(self.mouseEvent)
        # 轮询线程状态, 如果有一个关闭, 则让主线程关闭
        # while True:
        #     if (monitor1.is_alive() == False or monitor2.is_alive() == False):
        #         break


