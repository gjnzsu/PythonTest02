# Python Test 04
# Operator Test
print("+++++++++++Operator Test+++++++++++")

var_1 = 12
var_2 = 13
var_3 = 14

if (var_1 == 12):
    print('var1 is 12')
else:
    print('var1 is NOT equals to 12')

if (var_1 != var_2):
    print(str(var_1) + " is NOT equals to " + str(var_2))

if (var_3 > var_2):
    print(str(var_3) + " is bigger than " + str(var_2))

var_2 = 12
if (var_1 == var_2):
    print(str(var_1) + " is equals to " + str(var_2))

var_list_1 = [1, 2, 3, 4, 5]

if (1 in var_list_1):
    print(str(1) + " in the list")
if (6 not in var_list_1):
    print(str(6) + " Not in the list")

var_list_2 = [1, 2, 3, 4, 5]

var_list_3 = var_list_2

if (var_list_1 == var_list_2):
    print("var_list_1 value is the same as var_list_2")
else:
    print("var_list_1 value is NOT the same as var_list_2")

if (var_list_1 is var_list_2):
    print("var_list_1 object is the same as var_list_2")
else:
    print("var_list_1 object is NOT the same as var_list_2")

if (var_list_3 is var_list_2):
    print("var_list_3 object is the same as var_list_2")
else:
    print("var_list_3 object is NOT the same as var_list_2")
