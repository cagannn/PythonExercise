def int_to_list(c):
    lst=[]
    basam=bas_say(c)
    bas1=1
    son=0
    for j in range(0,basam-1):
        bas1*=10
        
    for i in range(0,basam):
        son=int(c/bas1)
        print(son)
        c=c-son*bas1
        lst.append(son)
        bas1/=10
    return lst
