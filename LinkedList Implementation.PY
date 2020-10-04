class Node:
    def __init__(self,data=None):
        self.data=data #data that is passed into the node
        self.next=None #link to the next node, default is none
class LinkedList:
    def __init__(self):
        """ Constructor"""
        self.head= Node() #creating a head node that is currently empty
    def append(self,data):
        """ Function to add data to the linked list"""
        new_node= Node(data) #create a new node and pass the data
        curr=self.head #pointer is at the beginning
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
    def length (self):
        curr=self.head
        total=0
        while curr.next!=None:
            total+=1
            curr=curr.next
        return total
    def display(self):
        elems=[]
        curr_node= self.head
        while curr_node.next!=None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
            print (elems)
    def get(self,index):
        if index>=self.length():
            print("Get Error")
            return None
        curr_index=0
        curr_node=self.head
        while True:
            curr_node=curr_node.next
            if curr_index==index:
                return curr_node.data
            curr_index+=1
    def erase(self,index):
        if index>=self.length():
            print("Index Error")
            return None
            curr_index=0
            curr_node=self.head
            while  True:
                last_node=curr_node
                curr_node=curr_node.next
                curr_index+=1
#test
my_list=LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.get(2)
my_list.erase(2)
my_list.display()
