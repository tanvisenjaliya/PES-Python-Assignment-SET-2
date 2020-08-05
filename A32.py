list1=['Surat','Vyara','Vadodara','Ahmedabad','Div']
list2=['Pune','Chennai','Mumbai','Kolkata','Delhi']
list3=['Skikkm','Kalingpong','Gangtok','Bagdogra','Katra']


print ("List1: ",list1)
for each in list1:
    print("City name : ",each," Length : ",len(each))

print ("List2: ",list2)
for each in list2:
    print("City name : ",each," Length : ",len(each))
print ("List3: ",list3)
for each in list3:
    print("City name : ",each," Length : ",len(each))

print("........................................")   
lmax1=0
for each in list1:
    if len(each)>lmax1:
        lmax1=len(each)
print("Max length in List1 : ",lmax1)
lmax2=0
for each in list2:
    if len(each)>lmax2:
        lmax2=len(each)
print("Max length in List2 : ",lmax2)
lmax3=0
for each in list3:
    if len(each)>lmax3:
        lmax3=len(each)
print("Max length in List3 : ",lmax3)

print("........................................")  
if lmax1>lmax2 and lmax1>lmax3:
    print("Max length among three lists is :",lmax1)
elif lmax2>lmax1 and lmax2>lmax3:
    print("Max length among three lists is :",lmax2)
else:
    print("Max length among three lists is :",lmax3)

print("........................................")  
print ("Max of list1=",(max(list1)))
print ("Min of list1=",min(list1))
print ("Max of list2=",max(list2))
print ("Min of list2=",min(list2))
print ("Max of list3=",max(list3))
print ("Min of list3=",min(list3))
print("........................................")
print ("\nList1 before removing 1st and last element using Pop method\n",list1)
print ("\nList1 after removing 1st and last element using pop method")
list1.pop(0);list1.pop(-1)
print (list1)
print ("List2 before removing 1st and last element using Pop method\n",list2)
print ("List2 after removing 1st and last element using pop method")
list2.pop(0);list2.pop(-1)
print (list2)
print ("List3 before removing 1st and last element using Pop method\n")
print (list3)
print ("List3 after removing 1st and last element using pop method")
list3.pop(0);list3.pop(-1)
print (list3    )
"""  
print "Length of list1=",len(list1)
print "Length of list2=",len(list2)
print "Length of list3=",len(list3)
print "Max of list1=",max(list1)
print "Min of list1=",min(list1)
print "Max of list2=",max(list2)
print "Min of list2=",min(list2)
print "Max of list3=",max(list3)
print "Min of list3=",min(list3)
if list1>list2 and list1>list3:
  print "\nlist1 is the biggest",list1
elif list2>list1 and list2>list3:
  print "\nlist2 is the biggest",list2
else:
  print "\nlist3 is the biggest",list3
 
if list1<list2 and list1<list3:
  print "\nlist1 is the smallest",list1
elif list2<list1 and list2<list3:
  print "\nlist2 is the smallest",list2
else:
  print "\nlist3 is the smallest",list3

print "\nList1 before removing 1st and last element using Pop method"
print list1
print "\nList1 after removing 1st and last element using pop method"
list1.pop(0);list1.pop(-1)
print list1
print "List2 before removing 1st and last element using Pop method"
print list2
print "List2 after removing 1st and last element using pop method"
list2.pop(0);list2.pop(-1)
print list2
print "List3 before removing 1st and last element using Pop method"
print list3
print "List3 after removing 1st and last element using pop method"
list3.pop(0);list3.pop(-1)
print list3
"""
