#LEGB，順序由上而下
#local
#enclosed
#gobal
#built in ，，你不需要定義就能直接使用，例如 print(), len(), int(), list() 等。

fe= 10 #痊癒變數，在同一個檔案內的任何地方都可以讀取它
def function1():
    a=1
    print("a:",a)
    def function2():
        b=2
        print("b:",b)
        print("b:",b)
        print(fe)
    function2()

function1()
#function2()裡面的a會往外找，找到外面function1的 a=1
#對於function2()來說， a=1是一個#enclosed、b=2是區域 

#round是四捨五入