from task_queue.task import Tasks
from task_queue.process import *
import os.path,os
from multiprocessing import cpu_count,Pool


if __name__ == '__main__':
    Tasks.generate_sessions()
    with open('passwd.pickle','rb') as f:
        session_list = pickle.load(f)
    if cpu_count() >1:
      pool=Pool()
      for tsk in [Tasks(sess) for sess in session_list]:
        pool.apply_async(tsk.run)
      pool.close()
      pool.close()
      pool.join()
    else:
      for sess in session_list:
        Tasks(sess).run()

