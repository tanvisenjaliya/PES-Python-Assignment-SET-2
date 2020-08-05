dict1={'Empid':12382,'Ename':'Tanvi','Band':'B1'}
dict2={'Rollno':116,'Name':'Tanu','Class':11}
dict3={'Kname':'Tavi','Kage':18,'Bgroup':'B+'}
if dict1>dict2 and dict1>dict3:
  print ("dict1 is th biggest",dict1)
elif dict2>dict1 and dict2>dict3:
  print ("dict2 is the biggest",dict2)
else:
  print ("dict3 is the biggest",dict3)
dict1['Experience']=4
dict2['School']='KV bhrukunda'
print ("\ndict1 after adding new elements is",dict1)
print ("\ndict2 after adding new elements is",dict2)
print ("Length of dict1 is",len(dict1))
print ("Length of dict2 is",len(dict2))
print ("Length of dict3 is",len(dict3))
dict1Str=str(dict1)
dict2Str=str(dict2)
dict3Str=str(dict3)
dictStr=dict1Str+dict2Str+dict3Str
print ("the concatenated dicts as strings all together is",dictStr)
