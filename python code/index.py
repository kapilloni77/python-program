list1 = [5, 2, 9, 1, 7, 8, 4, 2]
list2 = [18, 0, 9, 11, 17, 28, 9]
def func (list1,list2):
    li = list1 + list2
    max_numbers = max(li)
    print(f"Maximum number: {max_numbers}")
    
    li_1= list(set(list1))
    li_2= list(set(list2))
    print(f"remove duplicates: {li_1}")
    print(f"remove duplicates: {li_2}")
    
    
    lis_sor= sorted(list1, reverse=True)
    lis_sor= sorted(list2, reverse=True)
    print(f"unorder: {lis_sor}")
    print(f"unorder: {lis_sor}")
    
    if len(list1) > 5:
        list1.pop(5)
    if len(list2) > 5:
        list2.pop(5)
    print(f"element removing at index 5: {list1}")
    print(f"element removing at index 5: {list2}")
    
    combi= sorted(set(li), reverse=True)
    sec_hei = combi[1] if len(combi) > 1 else None
    print(f"Sec highest number: {sec_hei}")

func (list1, list2)
print("****************")
# 2
input_data = [
    {'datetime': '11-02-2023 3:00', 'generation': 180, 'revenue': 15},
    {'datetime': '11-02-2023 3:05', 'generation': 107, 'revenue': 16},
    {'datetime': '12-02-2023 3:00', 'generation': 170, 'revenue': 17},
    {'datetime': '12-02-2023 3:05', 'generation': 145, 'revenue': 18},
    {'datetime': '13-02-2023 3:00', 'generation': 160, 'revenue': 19}
]

data = filter(lambda a: a['generation'] > 160, input_data)
data_1 = list(data)
print(data_1)
print("************************")
#5
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
co = {}

for i in weekdays:
    co[i] = co.get(i, 0) + 1

print(co)
print("**************************")
#4
input_data = [
    {"Krishna": [87, 92, 58]},
    {"Arjun": [55, 39, 46, 72]},
    {"Malika": [49, 72, 52, 78]},
]
def cal_per(input_data):
    resu = []
    for stu in input_data:
        for name, marks in stu.items():
            per = round(sum(marks) / (len(marks) * 100) * 100, 2)
            resu.append({name: per})
            
    return resu
ou = cal_per(input_data)
print(ou)