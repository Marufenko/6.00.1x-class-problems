class Queue(object):
  #FIFO Queue

  def __init__(self):
    self.queue = []

  def insert(self,e):
    self.queue.append(e)

  def remove(self):
    try:
      i = self.queue[0]
      self.queue.remove(self.queue[0])
      return i
    except:
      raise ValueError
