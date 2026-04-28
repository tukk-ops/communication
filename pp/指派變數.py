def hello():
    print("ppppppppp")

#hi = hello()變數 hi 現在裡面裝的是 None，無法被執行
hi = hello  # 注意！這裡沒有括號，這叫「指向變數」
hi()
#記憶體位置相同
def shout():
    print("哇啊啊啊！")

def run_later(action):#你定義了一個「執行官」，他的工作是接收一個任務（叫做 action），然後執行它。
    print("等待 3 秒...")
    # 這裡才執行傳進來的動作
    action()

# 我們傳入 shout（不加括號），代表把這個動作「交給」run_later
run_later(shout)#把**「尖叫這項技術的說明書」**交給了，讓其使用