class LinkedList:
  class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
      self._element = element
      self._next = next
  def __init__(self):
    self._head = None
    self._size = 0

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0
  def traverse(self):
    if (self.is_empty()):
      print("Linked list is empty")
    else:
      print("\n")
      thead=self._head
      while (True):
        print(thead._element,'-->',end='')
        if (thead._next==None):
          break
        thead=thead._next
  def addfirst(self,element):
    if (self.is_empty()):
      self._head=self._Node(element,None)
    else:
      self._head=self._Node(element,self._head)
    self._size+=1
  def addlast(self,element):
    if(self.is_empty()):
      self._head=self._Node(element,None)
    else:
      thead=self._head
      while(True):
        if(thead._next==None):
          break
        thead=thead._next
      thead._next=self._Node(element,None)
    self._size+=1
  def deletefirst(self):
    if(self.is_empty()):
      print("Linked list is empty")
    else:
      thead=self._head
      self._head=self._head._next
      thead=None
      return self._head
  def deletelast(self):
    if(self.is_empty()):
      print("Linked list is empty")
    else:
      thead=self._head
      if (thead._next==None):
        self._head=self._head._next
        thead=None
        return self._head
      thead=self._head
      while(thead._next._next!=None):
        thead=thead._next
        thead=thead._next
        thead._next=None
        thead=None
        return self._head

  def insert_at_position(self,element,pos):
    if(pos==0):
      self.addfirst(element)
    elif (pos==self._size-1):
      self.addlast(element)
    elif(pos>self._size):
      print("Index out of range")
    else:
      thead=self._head
      counter=0
      while(counter<=pos-1):
        counter+=1
        thead=thead._next
      temp=self._Node(element,thead._next)
      temp._next=thead._next
      thead._next=temp
      return self._head

  def insert_after(self,ele,val):
    if(self.is_empty()):
      print("linked list is empty")
      return
    elif(self._head._next==None):
      if(self._head._element==ele):
        temp=self._Node(val,None)
        self._head._next=temp
      else:
        print("element not found")
        return
    else:
      thead=self._head
      while(True):
        if(thead._element==ele):
          temp=self._Node(val,thead._next)
          thead._next=temp
          break
        #thead=thead._next
        if(thead._next==None):
          print("element not found")
          break
        thead=thead._next
  def delete_after(self,ele):
    if(self.is_empty() or self._head._next==None):
      if(self._head._element==ele):
        self._head=self._head._next
        thead=None
        return self._head
      else:
        print("list is empty/ could not find element")
    else:
      thead=self._head
      while(True):
        if((thead._element==ele) or (thead._next._next!=None)):

          thead._next=thead._next._next

          break
        if(thead._next==None):
          print("element not found")
          break
        thead=thead._next
  def del_pos(self,pos):
      if(pos==0):
        self.deletefirst()
      elif(pos==self._size-1):
        self.deletelast()
      elif(pos>self._size):
        print("index out of range")
      else:
        thead=self._head
        counter=0
        while(counter<=pos-1):
          counter+=1
          thead._next=thead._next._next
          thead=thead._next
  def del_before(self,ele):
    if(self.is_empty()):
      print("list  is empty")
    if((self._head._next._next._element==ele and self._head._next!=None) or (self._head._next._next._element==ele and self._head._next==None)):
      self._head._next=self._head._next._next
      return self._head
    if(self._head._next._next._element!=ele):
      print("element not found")









