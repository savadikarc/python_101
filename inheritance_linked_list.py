class _Node(object):
    
    def __init__(self, data, next_ptr):
        
        # Te base class will contain only the minimum required fields i.e.
        # Data to be stored by the node
        self.data = data
        
        # and the pointer to the next node in the Linked List
        self.next = next_ptr
        
        print(self.data, self.next)


class SLLNode(_Node):
    
    # We dont need to write a constructor
    # If no constructor is written, the default
    # Constructor of the parent class is called.
    pass


class DLLNode(_Node):
    
    def __init__(self, data, next_ptr, previous_ptr):
        
        # Call the costructor of the parent class since
        # data and next can be initialized there
        super(DLLNode, self).__init__(data, next_ptr)
        
        # Only initialize the custom fields, i.e. the pointer
        # to the previous class
        self.previous = previous_ptr


s = SLLNode(1, '9')
s.__dict__

d = DLLNode(2, 5, 7)
d.__dict__

