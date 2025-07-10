class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def make_ll_from_l(self,l1):   
        for i in l1:
            newnode=node(i)
            if self.head==None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
        return self.head
    
    def print_rec(self,head):
        if head==None:
            raise Exception ("!!No Data Found !!")
        elif head.next==None:
            print(head.data)
            return head
        else:
            print(head.data,end=" -> ")
            head.next=self.print_rec(head.next)
            return head



class stack_LinkedList:
    def __init__(self):
        self.__top=None
        self.__size=0

    def push(self,data):
        newnode=node(data)
        if self.__top==None:
            self.__top=newnode
            self.__size+=1
        else:
            newnode.next=self.__top
            self.__top=newnode
            self.__size+=1


    def pop(self):
        if self.__top==None:
            raise Exception("!!cannot pop from a empty Stack!!")
        else:
            temp=self.__top.data
            self.__top=self.__top.next
        self.__size-=1
        return temp

    def peek(self):
        return self.__top.data
    
    def length(self):
        return self.__size
