class LibraryItem:
    def  __init__(self,title, days):
        self.title = title
        self.days = int(days)
    def calculate_late_fee(self):
        t_basic = self.days*5
        return t_basic
class book (LibraryItem):
    def __init__(self, title, days):
        super().__init__(title, days)
    def calculate_late_fee(self):
        if int(self.days)<=7:
            return super().calculate_late_fee()
        else:
            t = 7*5
            n = self.days -7
            new_total = n*10
            total =t+new_total
            return total
class DVD(LibraryItem):
    def  __init__(self, title, days):
        super().__init__(title, days)
    def calculate_late_fee(self):
        return self.days*20
class Magazine(LibraryItem):
    def __init__(self, title, days):
        super().__init__(title,days)
    def calculate_late_fee(self):
        t_in_m = super().calculate_late_fee()
        if int(t_in_m)>50:
            return 50
        else:
            return super().calculate_late_fee()


test = int(input())
for i in range(test):
    data = input().split()
    level = data[0]
    title =data[1]
    days = data[2]
    if level == "Book":
        pp = book(title,days)
        print(f"{title} Fee: ${pp.calculate_late_fee()}")
    elif level =="DVD":
        pp = DVD(title,days)
        print(f"{title} Fee: ${pp.calculate_late_fee()}")
    else :
        pp = Magazine(title,days)
        print(f"{title} Fee: ${pp.calculate_late_fee()}")