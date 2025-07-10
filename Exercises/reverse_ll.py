from Exercises.Advanced_DataStructures import linked_list
l1=[1,2,3,4,5,6,7]
l=linked_list()
head= l.make_ll_from_l(l1)
l.print_rec(head)


def reverse_ll_recv(head):
    if head==None or head.next==None:
        return head
    else:
        new_head=reverse_ll_recv(head.next)
        temp=head.next
        temp.next=head
        head.next=None
    return new_head

def reverse_ll(head):
    if head==None:
        return head
    elif head.next==None:
        return head
    else:
        curr=head.next
        head.next=None
        while curr!=None:
            temp=curr.next
            curr.next=head
            head=curr
            curr=temp
    return head

l.print_rec(reverse_ll_recv(head))
