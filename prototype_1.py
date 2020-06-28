import numpy as np
from array import *
import prototype_pairing



message=input("Enter Message: ")
messag1=input("Enter Key: ")

#Message and key Conversion into Uppercase letter for Validity
message=message.upper()
messag1=messag1.upper()



#Involved in Seperating Remaining Character after KEY From all Character list
def func2(list,list2):
    list3=[]
    for i in range(len(list2)):
        if(list2[i] not in list):
            list3.append(list2[i])
    return list3


#Involved in 5x5 Matrix Generation
def func3(alphabet,matrix_cipher):
    list_postion=[]
    if(alphabet=="J"):
        alphabet="I"
    for i in range(0,5):
        for j in range(0,5):
            if(alphabet in matrix_cipher[i][j]):
                list_postion.append(i)
                list_postion.append(j)


    return list_postion


#Involved in Encryption
def func4(list_position_1,list_position2,cipher_matrix):
    #list_position_1 is position of first alphabet in pair
    #list_position_2 is position of first alphabet in pair
    changed_alphabet_list=[]

    #This If Condition is For Rule 1
    if(list_postion1[0]==list_postion2[0]):
        list_postion1[1]=list_postion1[1]+1
        list_postion2[1]=list_postion2[1]+1
        if(list_postion1[1]>=4):
            #var1=list_postion1[0]
            #var1=var1-4
            #list_postion1[1]=list_postion1[1]-4
            list_postion1[1]=0
        elif(list_postion2[1]>=4):
            #list_postion2[1]=list_postion2[1]-4
            list_postion2[1]=0

        changed_alphabet_list.append(cipher_matrix[list_postion1[0]][list_postion1[1]])
        changed_alphabet_list.append(cipher_matrix[list_postion2[0]][list_postion2[1]])

    #This Condition is For Rule 2
    elif(list_postion1[1]==list_postion2[1]):
        list_postion1[0]=list_postion1[0]+1
        list_postion2[0]=list_postion2[0]+1
        if(list_postion1[0]>=4):
            #var1=list_postion1[0]
            #var1=var1-4
            #list_postion1[0]=list_postion1[0]-4
            list_postion1[0]=0
        elif(list_postion2[0]>=4):
            #list_postion2[0]=list_postion2[0]-4
            list_postion2[0]=0

        changed_alphabet_list.append(cipher_matrix[list_postion1[0]][list_postion1[1]])
        changed_alphabet_list.append(cipher_matrix[list_postion2[0]][list_postion2[1]])

    #This is Rule Third
    else:
        var1=list_postion1[1]
        var2=list_postion2[1]
        list_postion1[1]=var2
        list_postion2[1]=var1

        changed_alphabet_list.append(cipher_matrix[list_postion1[0]][list_postion1[1]])
        changed_alphabet_list.append(cipher_matrix[list_postion2[0]][list_postion2[1]])
    return changed_alphabet_list



##Variable Initialization
cipher_matrix=[]
list_key=[]
list_remain=[]
count=0
count_remain_character=0
counter_pair=0
counter_pair1=0
row=0
column=0
available_character=["A","B","C","D","E","F","G","H","I",
                    "K","L","M","N","O","P","Q",
                    "R","S","T","U","V","W","X","Y","Z"]
list_encrypt_mesage=[]
encrypt_message=""



##Converting Key Into List
################################# Alpha 3 Start
for i in range(0,len(messag1)):
    if(messag1[i]=="J"):
        list_key.append("I")
    else:
        list_key.append(messag1[i])
################################# Alpha 1 ENDS


#Replacing White Spaces From Message
message=message.replace(" ","")

#Message Conversion into List for Easiness in Further Processing Method called from Another py file
listing_pair=prototype_pairing.listing_pair(message)
#print(listing_pair)

#Valid Pair List Generation Method called from Another py file
listing_pair_with_replacement=prototype_pairing.pair_elimi(listing_pair)


#print(listing_pair_with_replacement)
#Genration of Valid Matrix with Valid Pair
message=np.asarray(listing_pair_with_replacement)


#Collecting of All Remaining Character in List
list_remain =func2(list_key,available_character)



#Generation of 5x5 Matrix
################################# Alpha 2 Start
for i in range(0,5):
    new=[]
    for j in range(0,5):
        if(count<len(list_key)):
            new.append(list_key[count])
            count=count+1
        else:
            if(count_remain_character<len(list_remain)):
                new.append(list_remain[count_remain_character])
                count_remain_character=count_remain_character+1
    cipher_matrix.append(new)
################################# Alpha 2 ENDS


#Position Finding From 5x5 Matrix and Encryption
################################# Alpha 1 Start
for i in range(len(message)):
    if(counter_pair<len(message)):
        if(counter_pair>=len(message)-1):
            break;
        a=message[counter_pair]
        b=message[counter_pair+1]
        list_postion1=func3(a,cipher_matrix)
        list_postion2=func3(b,cipher_matrix)
        #########################################
        #Encoding Should Be Here Bcz From Here we can Find Position of pair Easily
        list_encrypt_alphabet=func4(list_postion1,list_postion2,cipher_matrix)
        a=list_encrypt_alphabet[0]
        b=list_encrypt_alphabet[1]
        list_encrypt_mesage.append(a)
        list_encrypt_mesage.append(b)
        #########################################
        counter_pair=counter_pair+2

################################# Alpha 1 ENDS


#Message Encode Print
encrypt_message=np.asarray(list_encrypt_mesage)

print("Encrypted:",encrypt_message)
