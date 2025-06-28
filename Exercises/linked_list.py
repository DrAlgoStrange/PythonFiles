class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linked_list:
    def __init__(self):#constructor
        self.head=None
        self.tail=None



    def insert_at_end(self,data):#insert data one by one at the end
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node


    
    def insert(self,pos,data):# insert at any position 
        new_node=node(data)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return
        curr=self.head
        i=0
        while curr!=None:
            if i==(pos-1):
                new_node.next=curr.next
                curr.next=new_node
                return
            i+=1
            curr=curr.next

        raise Exception("!!!Index Out of Range!!!") 
    

    
    def pop(self,pos):#will pop a value and return it by default pops the end value
        curr=self.head
        i=0
        temp=curr
        while curr.next!=None:
            if i==pos:
                temp.next=curr.next
                data=curr.data
                del curr
                return data
            temp=curr
            curr=curr.next
            i+=1
        raise Exception("!!!Index Out of Range!!!") 
    

    def lenl(self,head1):# will return the length of the linked list
        if head1.next==None:
            return head1,1
        head1.next,cn_node=self.lenl(head1.next)
        return head1,cn_node+1

        
    def print_rec(self,head2):
        if head2.next==None:
            return head2
        else:
            print(self.print_rec(head2.next).data)
            return head2
            
    

    def __str__(self):# return formatter of the class in a list structure 

        temp=self.head
        link_list_str=""
        while temp!=None:
            link_list_str=link_list_str+str(temp.data)+' -> '
            temp=temp.next
        return link_list_str




if __name__=="__main__":

    l1=linked_list()

    for i in range(5):
        l1.insert_at_end(input(f"enter the data at position {i+1} - "))
    print(l1)
    l1.insert(2,998)
    print(l1)
    l1.insert(0,750)
    print(l1)
    l1.insert(4,334)
    print(l1)
    print(l1.pop(2))
    print(l1)
    print(l1.lenl(l1.head)[1])
    print(l1.print_rec(l1.head))
    print(l1.head)


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

