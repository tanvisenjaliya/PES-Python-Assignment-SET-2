list1=[1,32,12,23,45]
list2=[45,21,2,35,56,33]
list3=[22,32,43,12,66]
list1.sort()
list2.sort()
list3.sort()
print( "list1=",list1)
print( "list2=",list2)
print ("list3=",list3)
Maxlist1=list1[-2:]
print( "Maxlist1=",Maxlist1)
Minlist1=list1[:2]
print ("Minlist1=",Minlist1)
Maxlist2=list2[-2:]
print ("Maxlist2=",Maxlist2)
Minlist2=list2[:2]
print ("Minlist2=",Minlist2)
Maxlist3=list3[-2:]
print ("Maxlist3=",Maxlist3)
Minlist3=list3[:2]
print ("Minlist3=",Minlist3)
Maxlist=Maxlist1+Maxlist2+Maxlist3
print ("The Maxlist taking 2 maximum elements from each list is",Maxlist)
Minlist=Minlist1+Minlist2+Minlist3
print ("The Minlist taking 2 minimum elements from each list is",Minlist)
sumMax=0
for each in Maxlist:
  sumMax+=each
#print (sumMax)
SumMaxAvg=float(sumMax/6.0)
print ("Average of Maxlist is",SumMaxAvg)
sumMin=0
for each in Minlist:
  sumMin+=each
#print( sumMin)
sumMinAvg=float(sumMin/6.0)
print ("Average of Minlist is",sumMinAvg)
