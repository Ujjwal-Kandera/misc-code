# Q - WAP to check the frequency of elements in a list

data_list = [2,6,7,9,5,6,6,9,10]
freq = {}
for item in data_list:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
        
print(freq)