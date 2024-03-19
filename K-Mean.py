import matplotlib.pyplot as plt
def lists_equal(lst1, lst2):
    return all(x == y for x, y in zip(lst1, lst2))
#zip : if list1[1,2,3]、list2[4,5,6]
#zip(list1,list2) = [(1,4),(2,5),(3,6)]

n = -1
point = [(2,5),(3,2),(3,3),(3,4),(4,3),(4,4),(6,3),(6,4),(6,6),(7,2),(7,5),(7,6),(7,7),(8,6),(8,7)]
X = [(2,2), (4,6), (6,5),(8,8)] #指定點
Q = 0   #計算疊代次數
global Loss
Loss =[]
while(Q<10) :
    Old_X = []  #儲存舊四點
    Dis = []    #儲存每個點離 指定四點 的各自距離
    M = []      #將距離存成4*15的矩陣
    x0 = []; x1 = []; x2 = []; x3 = []  #儲存每個點離哪個 指定點最近
    for i in point:
        n += 1
        for j in X:
            D = ((j[0]-i[0])**2+(j[1]-i[1])**2)**(0.5)  #算距離
            #D = math.dist(j,i)
            Dis.append(D)
        M.extend([Dis])
        Dis = []
    n = 0
    loss = 0
    for i in M:  
        loss += min(i)
    Loss.append(loss/15)    #紀錄距離變化

    for i in M:
        small = i.index(min(i))
        if small == 0 :
            x0.append(point[n])
        elif small == 1:
            x1.append(point[n])
        elif small == 2:
            x2.append(point[n])
        elif small == 3:
            x3.append(point[n])
        n += 1

    n = -1
    Old_X.extend(X)
    print("Old : ",Old_X)
    for i in [x0,x1,x2,x3]:
        n_x = 0
        n_y = 0
        n += 1 
        if len(i) == 0:
            continue
        for j in i:
            n_x += j[0]
            n_y += j[1]
        L = len(i)
        X[n] = (round(n_x / L, 2), round(n_y /L, 2))
    print("New : ", X,"\n")
    Q += 1
    if lists_equal(Old_X, X):
        print("不再變化，停止疊代。 總疊代 :", Q ,"次")
        break

#
print("疊代四點變化 ↑↑↑ / 最終結果 ↓↓↓")
print("最後四點 : \n",X)
print("\n個點分別屬於 ")
print("x0 : ",x0, "\nx1 : ",x1,"\nx2 : ",x2, "\nx3 : ",x3)
print("Loss :",Loss )

plt.plot(Loss, marker='o', linestyle='-')
plt.title('Loss Over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')

# 显示图例
plt.legend(['Loss'])

# 显示折线图
plt.grid(True)
plt.show()