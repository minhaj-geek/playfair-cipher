import numpy as np
from array import *


list_messag=[]

#Used in Prototype_1 file
def pair_elimi(list_message):
    count=0
    #print(list_messag)
    #print(len(list_message))
    while(count<len(list_message)):
        if(count==len(list_message)-1):
            break;
        if(list_message[count]==list_message[count+1]):
            list_message.insert(count+1,"X")
            count=count+2
        else:
            count=count+1
            continue
    #print(len(list_message))
    #if((len(list_message)/len(list_message)==1)): #LCondition trauma
    if(len(list_message)%2==0):
        pass
    else:
        list_messag.append('X')
    return list_message


#Used in prototype_1 file
def listing_pair(message):
    for i in range(0,len(message)):
        list_messag.append(message[i])
    return list_messag


#new_list=pair_elimi(list_messag)





