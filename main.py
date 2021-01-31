import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ----------------------------------------------------------------------------------------------------------------------
# Loading data
column_names = []
for i in range(0,74):
    if i < 2:
        if i == 0:
            column_names.append("ID")
        else:
            column_names.append("Timestamp")
    else:
        if (i - 2) % 9 == 0:
            column_names.append("Gyro_"+str((i-2)//9)+"_X")
        if (i - 2) % 9 == 1:
            column_names.append("Gyro_" + str((i-2)//9) + "_Y")
        if (i - 2) % 9 == 2:
            column_names.append("Gyro_" + str((i-2)//9) + "_Z")
        if (i - 2) % 9 == 3:
            column_names.append("Acc_" + str((i-2)//9) + "_X")
        if (i - 2) % 9 == 4:
            column_names.append("Acc_" + str((i-2)//9) + "_Y")
        if (i - 2) % 9 == 5:
            column_names.append("Acc_" + str((i-2)//9) + "_Z")
        if (i - 2) % 9 == 6:
            column_names.append("Mag_" + str((i-2)//9) + "_X")
        if (i - 2) % 9 == 7:
            column_names.append("Mag_" + str((i-2)//9) + "_Y")
        if (i - 2) % 9 == 8:
            column_names.append("Mag_" + str((i-2)//9) + "_Z")

df_mmg_calib = pd.read_csv("data/MMG_calib_1.csv", names=column_names)
df_mmg_calib = df_mmg_calib[df_mmg_calib["ID"] == 0]
for i in range(2, 6):
    df_temp = pd.read_csv("data/MMG_calib_"+str(i)+".csv", names=column_names)
    df_temp = df_temp[df_temp["ID"] == 0]
    df_mmg_calib = pd.concat([df_mmg_calib, df_temp], ignore_index=True)

df_mmg_calib_Xu = pd.read_csv("data/MMG_calib_X_up.csv", names=column_names)
df_mmg_calib_Xu = df_mmg_calib_Xu[df_mmg_calib_Xu["ID"] == 0]

df_mmg_calib_Xd = pd.read_csv("data/MMG_calib_X_down.csv", names=column_names)
df_mmg_calib_Xd = df_mmg_calib_Xd[df_mmg_calib_Xd["ID"] == 0]

df_mmg_calib_Yu = pd.read_csv("data/MMG_calib_Y_up.csv", names=column_names)
df_mmg_calib_Yu = df_mmg_calib_Yu[df_mmg_calib_Yu["ID"] == 0]

df_mmg_calib_Yd = pd.read_csv("data/MMG_calib_Y_down.csv", names=column_names)
df_mmg_calib_Yd = df_mmg_calib_Yd[df_mmg_calib_Yd["ID"] == 0]

df_mmg_calib_Zu = pd.read_csv("data/MMG_calib_Z_up.csv", names=column_names)
df_mmg_calib_Zu = df_mmg_calib_Zu[df_mmg_calib_Zu["ID"] == 0]

df_mmg_calib_Zd = pd.read_csv("data/MMG_calib_Z_down.csv", names=column_names)
df_mmg_calib_Zd = df_mmg_calib_Zd[df_mmg_calib_Zd["ID"] == 0]
