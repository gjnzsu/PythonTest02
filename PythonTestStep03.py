#!Data Type Test

var1, var2, var3 = 100, True, 'StringType'
var4 = '''String 4
String 5'''

print(type(var1),type(var2),var4,type(var4),isinstance(var3,str))
#print(var3 + var4);
#print(var3*3)

#Escape character
var_escape_character_test = r'MyTest\n Completed'

print(var_escape_character_test)
#print('r'+var_escape_character_test)

#List test

var_list_1 = ['abcb','123','456','efg', True, 100]
print(var_list_1)
print(var_list_1[0:2])
print(var_list_1[0:-1])
print(var_list_1[1:1])
print(var_list_1[-5:-1])
print(var_list_1[0:])
print(var_list_1[-1:])
print(var_list_1[:-1])

def reverseStringTest(input):
    inputString = input.split(" ")
    inputString = inputString[-1:2:-1]

    output = " ".join(inputString)

    return output

input = 'I have a dream now'
reverseResult = reverseStringTest(input)
print(reverseResult)