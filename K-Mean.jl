# 可與 D:\Python Program\ML\K-Mean (有注解)一起看
using Plots
function lists_equal(lst1, lst2)
    return all(x == y for (x, y) in zip(lst1, lst2))
end

point = [(2,5),(3,2),(3,3),(3,4),(4,3),(4,4),(6,3),(6,4),(6,6),(7,2),(7,5),(7,6),(7,7),(8,6),(8,7)]
X = [(2.0,2.0), (4.0,6.0), (6.0,5.0),(8.0,8.0)] #指定點
Q = 0   #計算疊代次數
global Loss = []
while Q < 10
    global x0,x1,x2,x3
    Old_X = []  #儲存舊四點
    Dis = []    #儲存每個點離 指定四點 的各自距離
    M = []      #將距離存成4*15的矩陣
    x0 = []; x1 = []; x2 = []; x3 = []  #儲存每個點離哪個 指定點最近
    
    for i in point
        for j in X
            D = sqrt((j[1]-i[1])^2 + (j[2]-i[2])^2)  #算距離
            push!(Dis, D)
        end
        push!(M, Dis)
        Dis = []
    end

    global n = 1
    loss = 0
    for i in M  
        loss += minimum(i)
    end
    push!(Loss, loss/15)    #紀錄距離變化

    for i in M
        small = argmin(i)
        if small == 1
            push!(x0, point[n])
        elseif small == 2
            push!(x1, point[n])
        elseif small == 3
            push!(x2, point[n])
        elseif small == 4
            push!(x3, point[n])
        end
        n += 1
    end

    Old_X = copy(X)
    println("Old : ", Old_X)
    n = 1
    for i in [x0, x1, x2, x3]
        n_x = 0.0
        n_y = 0.0
        for j in i
            n_x += j[1]
            n_y += j[2]
        end
        L = length(i)
        X[n] = ((n_x / L), (n_y / L))
        n += 1
    end
    println("New : ", X, "\n")
    global Q += 1
    if lists_equal(Old_X, X)
        println("不再變化，停止疊代。 總疊代 :", Q ,"次")
        break
    end
end
println("最後四點 : \n", X)
println("\n個點分別屬於 ")
println("x0 : ", x0, "\nx1 : ", x1, "\nx2 : ", x2, "\nx3 : ", x3)
println("Loss :", Loss)
plot(Loss, 
    xlabel = "Iteration", 
    ylabel = "Loss", 
    title = "Loss Over Iterations", 
    label = "Loss", 
    lw = 2,
    legend = :bottomright
)