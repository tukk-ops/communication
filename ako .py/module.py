
import module2
module2.hello()

print("模組1__name__:"+ __name__ )

if __name__ == "__main__":
    print("模組1__name__==__main__>")

#運用不同檔案的內容的東西，要記得先存好在使用
#如果是在資料夾裡面的話，要用import pp.module2 as module2
