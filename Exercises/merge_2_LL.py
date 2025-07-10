from Exercises.Advanced_DataStructures import *
l1=[]
l2=[1]

head1=linked_list().make_ll_from_l(l1)


head2=linked_list().make_ll_from_l(l2)


def merge_two_ll(head1,head2):

    if head1==None and head2==None:
        return None
    elif head1==None:
        return head2
    elif head2==None:
        return head1
    
    else:
        final_head=None
        final_tail=None
        while head1!=None and head2!=None:
            if final_head==None and final_tail==None:
                if head1.data<head2.data:
                    final_head= head1
                    final_tail= head1
                    head1=head1.next
                else:
                    final_head=head2
                    final_tail=head2
                    head2=head2.next
            else:
                if head1.data<head2.data:
                    final_tail.next = head1
                    final_tail=head1
                    head1=head1.next
                else:
                    final_tail.next=head2
                    final_tail=head2
                    head2=head2.next

        while head1!=None:
            final_tail.next = head1
            final_tail=head1
            head1=head1.next
        while head2!=None:
            final_tail.next = head2
            final_tail=head2
            head2=head2.next

    return final_head



head=merge_two_ll(head1,head2)
linked_list().print_rec(head)




                    











