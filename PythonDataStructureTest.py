# List related functions
var_list_01 = ["aaa", "bbb", "ccc", "ddd", "eee"]

del var_list_01[0]
print(var_list_01)

# Tuple related functions
var_tuple_01 = "abc", 123, "def"
print(var_tuple_01[0])
var_tuple_02 = "raymond", var_tuple_01
print(var_tuple_02)

# Set related functions
var_set_01 = {"aaa", "bbb", "ccc", 123, 456, 123}
# index of set is not applicable
# print(var_set_01[0])
print(var_set_01)

var_vector_01 = ["a", "b", "c"]
var_vector_02 = ["a", "e", "f"]

var_set_02 = {x * 2 for x in var_vector_01 if x not in var_vector_02}

print(var_set_02)

# Dict related functions
var_dict_01 = {"raymond": "01", "vicky": "02"}
var_dict_01["amy"] = "03"
print(var_dict_01["raymond"])
print(var_dict_01)

var_dict_02 = {x: x + x for x in ("a", "b", "c")}
print(var_dict_02)

for i, j in var_dict_01.items():
    print(i, j)

# Dict magical iterative funtion call for multiple lists case?!
for i, j in zip(var_dict_01.items(), var_dict_02.items()):
    print("Test {0} Another Test {1}".format(i, j))
    # print(reversed("Test {0} Another Test {1}".format(i, j)))

var_vector_01.reverse()
print(var_vector_01)

for k in (reversed(var_vector_01)):
    print(k)
