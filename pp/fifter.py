#過濾器 fifter

#可以用來過濾可跌帶的資料結構(list)

friend =[
    ("john",29),
    ("eod",90),
    ("iuoo",9)

]
age_can = lambda data: data[1] >=18

can_people =list(filter(age_can,friend))

for friend in can_people:
    print(friend[0])
    print(friend[1])


