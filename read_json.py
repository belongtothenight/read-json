import json

total_data = []
total_data_cnt = 0
data_block_cnt = []

f = open('即時動態1.json', 'r', encoding='utf-8')
data = json.load(f)
data = data['datas']
f.close()

# print all data
print(data)

for x in data:
    key = x.keys()
    #print(key)# print individual key by data
    values = x.values()
    #print(values)# print individual data
    
    key = list(key)
    values = list(values)
    total_data.append(values)

print(key)
print(total_data)

# get total data count
total_data_cnt = (len(total_data))
for data_block in total_data:
    data_block_cnt.append(len(data_block))
        
print(total_data_cnt)
print(data_block_cnt)

# print individual data
for i in range(total_data_cnt):
    for j in range(data_block_cnt[i-1]):
        total_data[i][j] = str(total_data[i][j])
        print(key[j] + ": " + total_data[i][j])

#print(key[0] + ": " + total_data[0][0])