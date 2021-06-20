#Answer:-02
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=3;
print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print( True is False)
print("False" in "False")
print(((True == False) or (False > True)) and (False <= True))

#Answer:-03
s1 = "Nice to have it"
s2 = "here"
s3 = s1+''+s2
print(s3)

#Answer:-04
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#Answer:-05
s1='Nice to have it'
s2='here'
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s1)
a.append(s2)
print(a)

#Answer:-06
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#Answer:-07
import string
def ispangram (str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False 
    return True
string = 'The five boxing wizards jump quickly'
if (ispangram (string) == True):
    print ("Yes")
else:
    print ("No")
    
#Answer:-08
a=int(input('Enter the number:'))
n1=int('%s'%a)
n2=int('%s%s'%(a,a))
n3=int('%s%s%s'%(a,a,a))
value=n1+n2+n3
print(value)

#Answer:-09
items = input("Enter sequence of words:")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#Answer:-10
d = {'Student': [ "Rahul" , "Kishore" ,  "Vidhya" , "Rakhi"] ,'Marks': [57,87,67,79]}
print(d['Student'][1])
 
