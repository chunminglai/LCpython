# LCpython
#Declare Set: 
  buff_set = set()
#Declare Dictionary:
  buff_dict = dict()
  buff_dict = {}
#Declase String
  str=''
#enumerate
  elements = ('foo', 'bar', 'baz')
  >>> for elem in elements:
  ...     print elem
  ... 
  foo
  bar
  baz
  >>> for count, elem in enumerate(elements):
  ...     print count, elem
  ... 
  0 foo
  1 bar
  2 baz
 ---------------------------
 Class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
