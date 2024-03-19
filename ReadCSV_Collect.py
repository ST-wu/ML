import pandas as pd

DF = pd.read_csv("D:\\Julia Program\\data_with_classes.csv")


M1 = []
M2 = []
M3 = []

# 遍历每一行数据
for index, row in DF.iterrows():
    class_ = row['Class']
    if class_ == 1:
        M1.append(row[:5])
    elif class_ == 2:
        M2.append(row[:5])
    elif class_ == 3:
        M3.append(row[:5])

# print("M1大小:", len(M1))
# print(pd.DataFrame(M1))
# print("")
# print("M2大小:", len(M2))
# print(pd.DataFrame(M2))
# print("")
# print("M3大小:", len(M3))
# print(pd.DataFrame(M3))
import numpy as np

M1_np = np.array(M1)
M2_np = np.array(M2)
M3_np = np.array(M3)

print("M1形状:", M1_np.shape)
print(M1_np)

print("M2形状:", M2_np.shape)
print(M2_np)

print("M3形状:", M3_np.shape)
print(M3_np)
