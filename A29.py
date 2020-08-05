#1.First 5 string built-in functions
str = "this is a string"
print( "str.capitalize():",str.capitalize())

print( "str.center(60,'x'):",str.center(60,'x'))

sub = "i";
print ("str.count(sub,1,30):",str.count(sub,1,30))
sub = "wow";
print ("str.count(sub):",str.count(sub))

#str = str.encode('base64','strict')
print ("Encoded String:",str)
#print ("Decoded String:",str.decode('base64','strict'),'\n')



#2.Second 5 string built in functions
str = "this is a string"
suffix = "ing"
print ("str.endswith(suffix):",str.endswith(suffix))
print ("str.endswith(suffix,10):",str.endswith(suffix,10))
suffix = "i"
print( "str.endswith(suffix, 1, 4):",str.endswith(suffix, 1, 4))
print ("str.endswith(suffix, 2, 6):",str.endswith(suffix, 2, 6))

print ("\nOriginal string:",str)
print ("Default exapanded tab:",str.expandtabs())
print ("Double exapanded tab:",str.expandtabs(16))

str2 = "ng"
print ("\nstr.find(str2):",str.find(str2))
print ("str.find(str2, 10):",str.find(str2, 10))
print ("str.find(str2, 40):",str.find(str2, 40))

print ("\nstr.index(str2):",str.index(str2))
print ("str.index(str2, 10):",str.index(str2, 10))
#print ("str.index(str2, 40):",str.index(str2, 40))

str = "this2009"
print ("\nstr.isalnum():",str.isalnum())
str = "this is a string";
print ("str.isalnum():",str.isalnum())



#3.Third set of 5 string built in functions
str = "this";  # No space & digit in this string
print( "\nstr.isalpha():",str.isalpha())
str = "this is string example";
print ("str.isalpha():",str.isalpha())

str = "123456";  # Only digit in this string
print ("\nstr.isdigit():",str.isdigit())

str = "this is string example..";
print ("\nstr.isdigit():",str.isdigit())

str = "THIS is string example"; 
print ("\nstr.islower():",str.islower())
str = "this is string example";
print ("str.islower()",str.islower())

str = u"this2009";  # u stands for Unicode.One must prefix u to check for isnumeric
print ("\nstr.isnumeric():",str.isnumeric())
str = u"23443434";
print ("str.isnumeric():",str.isnumeric())

str = "       "; 
print ("\nstr.isspace():",str.isspace())
str = "This is string example";
print ("str.isspace():",str.isspace())



#4.Fourth set of 5 string built in functions
str = "This Is String Example";
print ("\nstr.istitle():",str.istitle())
str = "This is string example";
print ("str.istitle():",str.istitle())

str = "THIS IS STRING EXAMPLE"; 
print( "\nstr.isupper():",str.isupper())
str = "THIS is string example";
print( "str.isupper():",str.isupper())

s = "-";
seq = ('a','b','c'); # This is sequence of strings.
print( "\ns.join(seq):",s.join(seq))

str = "this is string example";
print( "\nLength of the string:",len(str))

print ("\nstr.ljust(50, '1')",str.ljust(50, '1'))



#5.Fifth set of 5 string built in functions
str = "THIS IS STRING EXAMPLE";
print ("\nstr.lower():",str.lower())

str = "     this is string example    ";
print ("\nstr.lstrip():",str.lstrip())
str = "88888888this is string example8888888";
print ("\nstr.lstrip('8'):",str.lstrip('8'))

str = "this is really a  frozen string example";
print ("\nMax character: ",max(str))
str = "this is a string example";
print ("Max character: ",max(str))

str = "this-is-real-string!example";
print ("\nMin character: " + min(str))
str = "this-is-a-string-example";
print ("Min character: " + min(str))



#6.Sixth set of 5 string built in functions
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))

str1 = "this is really a string example....wow!!!";
str2 = "is";
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

str1 = "this is string example....wow!!!";
str2 = "is";
print (str1.rindex(str2))
print (str1.index(str2))

str = "this is string example....wow!!!";
print (str.rjust(50, '0'))

str = "     this is string example....wow!!!     ";
print( str.rstrip())
str = "88888888this is string example....wow!!!8888888";
print (str.rstrip('8'))



#7.Seventh set of 5 string built in functions
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))
print (str.split(' ', 1 ))

str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print (str.splitlines( ))
print (str.splitlines( 0 ))
print (str.splitlines( 3 ))
print (str.splitlines( 4 ))
print (str.splitlines( 5 ))

str = "this is string example....wow!!!";
print (str.startswith( 'this' ))
print (str.startswith( 'is', 2, 4 ))
print (str.startswith( 'this', 2, 4 ))

str = "0000000this is string example....wow!!!0000000";
print (str.strip( '0' ))

str = "this is string example....wow!!!";
print (str.swapcase())
str = "THIS IS STRING EXAMPLE....WOW!!!";
print (str.swapcase())



#8.Eighth set of 5 string built in functions
str = "this is string example!!!";
print ("\nstr.title():",str.title())


str = "this is string example";
print ("\nstr.capitalize():",str.upper())

str = "this is string example";
print ("\nstr.zfill(40):",str.zfill(40))
print ("str.zfill(50):",str.zfill(50))

str = u"this2009";  
print ("\nstr.isdecimal():",str.isdecimal())
str = u"23443434";
print ("str.isdecimal():",str.isdecimal())
