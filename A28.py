s=input("Enter a string: ")
s=s.lower()
l=list(s)
print(s)
cnt=0
cnta=0
cnte=0
cnti=0
cnto=0
cntu=0
for i in l:
    if i=='a':
        cnt+=1
        cnta+=1
    elif i=='e':
        cnt+=1
        cnte+=1
    elif i=='i':
        cnt+=1
        cnti+=1
    elif i=='o':
        cnt+=1
        cnto+=1
    elif i=='u':
        cnt+=1
        cntu+=1
    else:
        pass
print ("No of total vowels=",cnt)
print ("count of A",cnta)
print ("count of E",cnte)
print ("count of I",cnti)
print ("count of O",cnto)
print ("count of U",cntu)
    
    
    
