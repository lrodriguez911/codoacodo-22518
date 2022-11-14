print("****** CADENAS: METODOS ******")

#Join 
'''str = "Lucas Rodriguez"
str = '-'.join(str)
print(str)
'''

#Split
'''str = "Strings of character"
str_list = str.split(' ')
print(str_list)'''


#Replace
'''str = "Programing in Python. Python is the best"
print(str.replace('Python', 'Javascript'))
print(str.replace('Python', 'Javascript', 1))
'''

#Count e Index
'''str= "string of characters"
print("Amount of c: ", str.count("c"))
print("Index of 'i':", str.index("i"))
print("Index of 'a' from position 5:", str.index("a", 5))'''

#isalpha / isdigit / isalnum
'''str = "Python"
str1 = "Python3"
str2 = "1234"
print(str.isalpha())
print(str1.isalpha())
print(str2.isdigit())
print(str1.isalnum())'''

#isupper / islower
'''str = "Python"
str1 = "python"
str2 = "PYTHON"

print(str.isupper())
print(str2.isupper())
print(str1.islower())
print(type(str1))
'''

#center / ljust / rjust / zfill
'''str0 = "Python"
str1 = str0.center(14, '*')
print("Center:",str1)

str2 = str0.ljust(14, '*')
print("Ljust:",str2)

str3 = str0.rjust(14, '*')
print("Rjust:", str3)

num = 345
str4 = str(num).zfill(10)
print("Zfill:", str4)'''

#lstrip / rstrip / strip

'''str0 = "---Hello-World---"
print(str0)
print(str0.lstrip("-"))

str1 = "***Hello-Python***"
print(str1.rstrip("*"))

str2 = "---Hello-Python---"
print(str2.strip("-"))'''



#find y rfind
str0 = "Codo a Codo"

print(str0)
print(str0.find("Codo")) #From left

print(str0.rfind("Codo")) #From right

