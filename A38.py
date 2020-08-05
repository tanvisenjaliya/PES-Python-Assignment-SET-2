dict1 ={'Name':'Ramakrish','Age':25}
dict2={'EmpId':1234,'Salary':5000}

dict1.update(dict2)
print ("After merging dict1and dict2, the single dict is",dict1)

dict1['Salary']=dict1['Salary']+(dict1['Salary']*0.1)
print ("\nthe dict after updating salary to 10% is now",dict1)

dict1['Age']=26
print ("\nthe dict after updating age to 26 is now",dict1)

dict1['Grade']='B1'
print("\nNew element inseted in the dict is",dict1)

print ("The keys of dict separately is",dict1.keys())
print ("The values of dict separately is",dict1.values())
del dict1['Age']
print ("\nDict after deleting element with key Age is",dict1)
