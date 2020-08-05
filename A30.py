s=input("Enter the numbers")
l=list(s)
for each in range(len(l)):
  swap=False
  i = 0
  while i<len(l)-1:
    if l[i]>l[i+1]:
      l[i],l[i+1] = l[i+1],l[i]
      swap = True
    i = i+1
  if swap == False:
    break
print (l)
