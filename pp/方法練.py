class car :
    def turn_on(self):
        print("你啟動了引擎")
        return self

    def drive(self):
        print("你開車了")
        return self
    
    def brake(self):
        print("妳踩了煞車")
        return self
    
    def trun_off(self):
        print("以熄火")
        return self

car0 = car()
car0.turn_on().drive()

#如果沒有寫 return，Python 預設會回傳 None。
#如果接著寫 .drive()，就變成了 None.drive()，程式會直接崩潰報錯。
#return self， 它會把「這台車子自己 (self)」重新丟回給你。
#執行 car0.turn_on()，印出啟動引擎 ， 回傳 car 本體。