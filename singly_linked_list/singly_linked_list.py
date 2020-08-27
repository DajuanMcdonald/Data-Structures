class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class LinkedList:
    def __init__(self, tail=None, head=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def add_to_tail(self, value):
        self.length += 1
        """

        inserting a new node at tail

        if head and tail are none
        the new node is = head and tail

        if tail is not none:
        the new node is inserting as tail.next
        then the previous tail is new node.prev
        and new_node next is none
        
        """
        new_node = Node(value)
        if not self.head and not self.tail:

            self.head = new_node
            self.tail = new_node

        if self.head and self.tail:
            
            self.head.next = new_node
            new_node.prev = self.tail
            new_node.next = None


        current = self.tail
        if current is None:
            current.next = new_node
            current.prev = new_node.prev
            new_node.prev = current.next
            

        
##
##        if self.head:
##            self.head.next = Node(value)
##            new_node.next = self.tail
##            self.tail = new_node.prev

##        if self.tail:
##            self.tail.next = new_node.prev
##            self.tail.prev = self.tail

        print(new_node.value)
            

##        elif self.tail:
##            self.head.next = Node(value)
##            new_node.prev = self.head.next
##            new_node.next = None
##
        
            

    def remove_head(self):
        if not self.head and not self.tail:
            return

        if self.head == self.tail:
            target = self.head
            self.head = None
            self.head.next = self.tail
            self.head.prev = None
            
            return target.value

        target = self.head
        current = self.head
        while current:
            current = self.head.next
            self.head.next = self.tail
            self.tail = None

        return target.value
        
##        target = self.head
##        
##        if target == self.head:
##            self.head.next = self.head
##            self.head = self.tail
##            self.head = None
##            self.tail.next = None
        pass
            

    def remove_tail(self):
        if not self.head and not self.tail:
            return

        if self.head == self.tail:
            target = self.tail
            self.tail = None
            self.tail.prev = self.tail

            return target.value

        target = self.tail
        current = self.head
        while current.next:
            current = current.next
        current.next = None

        return target.value


    def __repr__(self):
        current = self.tail
        nodes = []
        while current:
            if current is self.head:
                nodes.append(f"[self.head:{current.value}]")
                current = current.next
                
            elif current is self.head.next:
                nodes.append(f"[self.head.next:{current.value}]")
                current = current.next
                
            elif current is self.tail:
                nodes.append(f"[self.tail:{current.value}]")
                current = current.next

            elif current is self.tail.next:
                nodes.append(f"[self.tail.next:{current.value}]")
                
            else:
                nodes.append(f"[Current:{current.value}]")
                current = current.next
                
        return '<p---n>'.join(nodes) 


list = LinkedList()

list.add_to_tail(10) #getting

list.add_to_tail(20) 
list.add_to_tail(25)
list.add_to_tail(30) #getting



print(list)


