from queue import PriorityQueue 
from task_queue.process import TaskInterface
from task_queue.process import Login
from multiprocessing import cpu_count,Pool
class Tasks(object):

  def __init__(self,session):
    
    self.session=session
  @classmethod
  def generate_sessions(self):
    sess_tsk = Login()
    sess_tsk.run()
  def __loadtasks(self):

    for subclass in TaskInterface.__subclasses__():
      if subclass.priority:
        self.task.put((subclass.priority,subclass.name,subclass,self.session))
 
  def __start(self):
    self.task=PriorityQueue()
    self.__loadtasks()
    while not self.task.empty():
      
      p,name,obj,session=self.task.get()
      print("start %s sid %s task..."%(name,session))
      obj(session).run()
      print("%s task ended"%name)
      # t=__tasks.task.get()[2]().run()
  def run(self):
     self.__start()

if __name__ == '__main__':
    Tasks.generate_sessions()
    with open('passwd.pickle','rb') as f:
        session_list = pickle.load(f)
    if cpu_count() >1:
      pool=Pool()
      for tsk in [Tasks(sess) for sess in session_list]:
        pool.apply_async(tsk.run)
      pool.close()
      p.close()
      p.join()
    else:
      for sess in session_list:
        Tasks(sess).run()
    