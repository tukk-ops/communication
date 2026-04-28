#推倒式，縮減行數，美化
grade =[90,90,89,27,78,56]
pass_pe = [x for x in grade if x >=60]
print(*pass_pe)


#字典推倒式
#{key: expression for key, value in iterable}

city ={"la":190,"tw":90,"jp":20,"china":100}
city_value ={key:(value*0.99-32 )for key , value in city.items()}
print(city_value)#這裡的攻勢沒有意義，練習用


city2 ={"la":"rain","tw":"sun","jp":"no sun ","china":"sun"}
city_weather = {key:value for key, value in city2.items()if value =="sun"}
print(city_weather)

#條件 + 函釋

city3 = {"la":190,"tw":90,"jp":20,"china":100}

def check_temp (value):
    if value >= 70:
        return "熱"
    elif value >= 40:
        return"溫暖"
    else:
        return"冷"

city_tempure ={key: check_temp(value) for key,value in city3.items()}
print(city_tempure)
#結合含式，函帶入函數裡面，去產生新的字典