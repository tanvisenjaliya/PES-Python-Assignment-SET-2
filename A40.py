import time
import timeit
#40.a
i=12
while i>0:
  localtime = time.asctime(time.localtime(time.time()))
  print ("Local current time :", localtime)
  time.sleep(5)
  i=i-1

#40.b
code = """list1=['Surat','Vyara','Vadodara','Ahmedabad','Div']
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

"""

execution_time = timeit.timeit(code, number=1)

print("Ececution time for the given code: ",execution_time)
