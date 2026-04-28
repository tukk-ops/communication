data = input()
n = int(input())
word =""
if len(data) <= 100:
    for char in data:
        if "A" <= char <= "Z":                                                 #  先轉unicode 減去自首後加上轉移的數字，之後家回去
            news = chr((ord(char) -ord("A")+ n)%26 + ord("A"))                 #   %26是防止跑出26個字母迴圈外，
            word += news

        elif "a" <= char <= "z":
             news = chr((ord(char) -ord("a")+ n)%26+ ord("a"))
             word += news  
        elif "0" <= char <= "9":
                word += chr((ord(char) - ord("0") + n) % 10 + ord("0"))
        else:
             word += char
    print(word)

#ord文字轉uniode
# chr unicode 轉文字