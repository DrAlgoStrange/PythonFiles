class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linked_list:
    def __init__(self):
        self.head=None
        self.curr=None

    def insert_at_end(self,data):

        new_node=node(data)
        if self.head==None:
            self.head=new_node
            self.curr=self.head
        else:
            self.curr.next=new_node
            self.curr=new_node
    
    def insert(self,pos,data):
        new_node=node(data)
        self.curr=self.head
        i=0
        prev=None
        while self.curr!=None:
            if i==pos:
                if prev==None:
                    new_node.next=self.head
                    self.head=new_node
                else:
                    prev.next=new_node
                    new_node.next=self.curr
                return
            else:
                prev = self.curr
                self.curr=self.curr.next
                i+=1
        raise Exception("!!!Index Out of Range!!!") 
    

    def __str__(self):
        self.curr=self.head
        link_list_str=""
        while self.curr!=None:
            link_list_str=link_list_str+str(self.curr.data)+' -> '
            self.curr=self.curr.next
        return link_list_str


l1=linked_list()

for i in range(5):
    l1.insert_at_end(input(f"enter the data at position {i+1} - "))
print(l1)
l1.insert(2,998)
print(l1)
l1.insert(0,750)
print(l1)
l1.insert(10,334)
print(l1)


# head=None
# tail=None
# curr=None
# for i in range(5):
#     if i==0:
#         head=node(input(f"enter the data {i+1} position"))
#         curr=head
    
#     else:
#         tail=node(input(f"enter the data at {i+1} position"))
#         curr.next=tail
#         curr=tail

# curr=head
# while curr:
#     print(curr.data)
#     curr=curr.next

