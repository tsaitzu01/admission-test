def count(input):

    dic = {}

    for i in input:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

def group_by_key(input):

    dic = {}
    for i in input:
        ele = i['key']
        if ele not in dic:
            dic[ele] = 0
        dic[ele] += i['value']
    return dic

input2 = [
    {'key': 'a', 'value': 3}, 
    {'key': 'b', 'value': 1}, 
    {'key': 'c', 'value': 2}, 
    {'key': 'a', 'value': 3}, 
    {'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}