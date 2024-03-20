def son(mylist:list):
    sons=[]
    for i in mylist:
        if type(i) is int:
            sons.append(i)
    return sons
print(son(['a',1,2,3,4,5]))