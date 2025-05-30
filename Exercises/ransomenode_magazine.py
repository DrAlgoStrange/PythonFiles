
'''check weather the target string can be made using base string by using using each of the letter only once from basestring'''


def check_maker(base_str: str, target_str: str) -> bool:
    letter_dict={}
    for i in base_str:
        if i in letter_dict:
            letter_dict[i]+=1
        else:
            letter_dict[i]=1

    for j in target_str:
        if j in letter_dict:
            if letter_dict[j]>1:
                letter_dict[j]-=1
            else:
                del letter_dict[j]
        else:
            return False
    return True


target_str="aabbcce"
base_str="abbbcccccb"

print(check_maker(base_str,target_str))
