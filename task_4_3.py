dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_key = list(dict_1.keys())
index = 0
while index <= len(list_key)-1:
    b = len(list_key[index])
    dict_1[list_key[index] + str(b)] = dict_1.pop(list_key[index])
    index += 1
print(dict_1)

dict_2 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_key_2 = list(dict_2.keys())
for i in range(len(list_key_2)):
    d = len(list_key_2[i])
    dict_2[list_key_2[i] + str(d)] = dict_2.pop(list_key_2[i])
print(dict_2)