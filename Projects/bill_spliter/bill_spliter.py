class person:
    def __init__(self, name: str,mysplit: dict):
        self.name=name
        self.mysplit=mysplit

class grouper(person):

    def __init__(self):
        self.group_dict={}

    def group_maker(self,names: list, obj_list: list):
        for i in names:
            #self.group_dict[i]={}
            for k in obj_list:
                if k.name==i:
                    for j in names:
                        if i==j:
                            continue
                        else:
                            k.mysplit[j]=[]
                    self.group_dict[i]=k.mysplit
                    break


def add_a_splitting_expence(splitter_person,object_gr_maker,person_list_obj, person_list, amount_per_person):
    for value in object_gr_maker.group_dict[splitter_person].values():
        value.append(amount_per_person)
    for k in person_list_obj:
        if k.name in person_list:
            if k.name!=splitter_person:
                object_gr_maker.group_dict[k.name][splitter_person].append(-amount_per_person)

    





        
if __name__=="__main__":
    person_obj=[]
    testnames=["surya","sirsha","arka","boomba","tapo"]
    for i in range(0,5):
        person_obj.append(person(testnames[i],{}))
    print("5 persons created")


    group_of=int(input("you want to make a group of how many people"))
    group_people=[]
    for i in range(0,group_of):
        name=input(f"enter name of the {i+1}th person")
        group_people.append(name)
    

    grouper_class=grouper()
    grouper_class.group_maker(group_people,person_obj)


    print(grouper_class.group_dict)
    
    userin=input("do you want to split a expence 'y'/'n'")
    while userin!='n':
        username=input("who is splitting enter your name")
        amount=int(input("what is the amount you want to split"))
        amount_per_person = amount/group_of
        add_a_splitting_expence(username,grouper_class,person_obj,group_people,amount_per_person)
        print(grouper_class.group_dict)


        userin=input("do you want to split a expence 'y'/'n'")

    print("program terminated")

    