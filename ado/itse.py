n = int(input())

for i in range(n):

    t,m,k = map(int,input().split())

    k_value = map(int,input().split())
    #split()的清單無法直接被使用，要從新加入到新的list李
    k_list = []
    for  k in k_value:
          k_list.append(int(k))
    k_list.sort()
    #題目要求說不能重複又要加總，所以將他從小排到大，依序加起來最好

    total = sum(k_list[:m])
    #依照員工數量做切面，有三個員工，所以要012個商品加總，所以會切:m(m-1個數)

    if total <= t:
        print(total)
    else:
        print("Impossible")