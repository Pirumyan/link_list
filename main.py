#main.py
from inked_list import *


lst = LinkedList()


lst.append(3)
lst.prepend(3)
lst.insert_after(3, 4)
lst.insert_before(3, 34)
lst.insert_after(3, 100)
lst.delete(3)


lst.display()
