import time
#print(time.ctime(0))初始時間
#print(time.time())初始到現在的時間
#local_time = time.localtime()
#print("time",time.strftime("%Y - %M - %d",local_time))
#通常是：時間物件.strftime("格式代碼")
#Python 看到 % 開頭的字，就會自動換成對應的數字
#%Y	Year (四位數年份)	2026
#%m	month (月份 01-12)	01
#%d	day (日期 01-31)	27
#%H	Hour (24小時制的小時)	16
#%M	Minute (分鐘)	30
#%S	Second (秒)	05


#給時間轉回來
import time

# 這是你的文字資料
time_str = "2021-12-31 23:20:10"
time_obj = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")

print("轉換後的物件：", time_obj)
