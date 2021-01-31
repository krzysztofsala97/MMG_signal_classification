import pandas as pd

from utils.show_sensor_data import show_sensor_data_3d, show_sensor_data_2d
from utils.calculate_offset import calculate_offset
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

# show_sensor_data_3d(df_mmg_calib, 1, 2)
# show_sensor_data_2d(pd.concat([df_mmg_calib_Xu, df_mmg_calib_Xd], ignore_index=True), 0, 0, "X", "Y")
# show_sensor_data_2d(pd.concat([df_mmg_calib_Yu, df_mmg_calib_Yd], ignore_index=True), 0, 0, "Y", "Z")
# show_sensor_data_2d(pd.concat([df_mmg_calib_Zu, df_mmg_calib_Zd], ignore_index=True), 0, 0, "Z", "X")
# print(f'Accelerometer offset for axis X of sensor 0 is {calculate_offset(df_mmg_calib_Xu, df_mmg_calib_Xd,0,1,"X")}')
# print(f'Accelerometer offset for axis Y of sensor 0 is {calculate_offset(df_mmg_calib_Yu, df_mmg_calib_Yd,0,1,"Y")}')
# print(f'Accelerometer offset for axis Z of sensor 0 is {calculate_offset(df_mmg_calib_Zu, df_mmg_calib_Zd,0,1,"Z")}')

for i in range(0, 8):
    print("-"*15)
    print(f'Gyroscope offset for axis X of sensor {i} is {calculate_offset(df_mmg_calib_Xu, df_mmg_calib_Xd, i, 0, "X")}')
    print(f'Gyroscope offset for axis Y of sensor {i} is {calculate_offset(df_mmg_calib_Yu, df_mmg_calib_Yd, i, 0, "Y")}')
    print(f'Gyroscope offset for axis Z of sensor {i} is {calculate_offset(df_mmg_calib_Zu, df_mmg_calib_Zd, i, 0, "Z")}')
    print(f'Accelerometer offset for axis X of sensor {i} is {calculate_offset(df_mmg_calib_Xu, df_mmg_calib_Xd, i, 1, "X")}')
    print(f'Accelerometer offset for axis Y of sensor {i} is {calculate_offset(df_mmg_calib_Yu, df_mmg_calib_Yd, i, 1, "Y")}')
    print(f'Accelerometer offset for axis Z of sensor {i} is {calculate_offset(df_mmg_calib_Zu, df_mmg_calib_Zd, i, 1, "Z")}')

# TODO: Magnetometer calibration procedure
