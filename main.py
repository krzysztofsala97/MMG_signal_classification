import pandas as pd
import numpy as np
from utils.show_sensor_data import show_sensor_data_3d, show_sensor_data_2d
from utils.calculate_offset import calculate_offset
from utils.ellipsoid import elipsoid
from scipy.optimize import fmin_bfgs
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
# ----------------------------------------------------------------------------------------------------------------------
# Calculating gyroscope and accelerometer offset and ellipsoid parameters
saved_data = {}
for i in range(0, 8):
    print("-"*15)
    g_x = calculate_offset(df_mmg_calib_Xu, df_mmg_calib_Xd, i, 0, "X")
    g_y = calculate_offset(df_mmg_calib_Yu, df_mmg_calib_Yd, i, 0, "Y")
    g_z = calculate_offset(df_mmg_calib_Zu, df_mmg_calib_Zd, i, 0, "Z")
    a_x = calculate_offset(df_mmg_calib_Xu, df_mmg_calib_Xd, i, 1, "X")
    a_y = calculate_offset(df_mmg_calib_Yu, df_mmg_calib_Yd, i, 1, "Y")
    a_z = calculate_offset(df_mmg_calib_Zu, df_mmg_calib_Zd, i, 1, "Z")
    res = fmin_bfgs(elipsoid, np.array([1, 1, 1, 0, 0, 0]), args=(df_mmg_calib[["Mag_" + str(i) + "_X",
                                                                                "Mag_" + str(i) + "_Y",
                                                                                "Mag_" + str(i) + "_Z"]],))
    print(f'Gyroscope offset for axis X of sensor {i} is {g_x}')
    print(f'Gyroscope offset for axis Y of sensor {i} is {g_y}')
    print(f'Gyroscope offset for axis Z of sensor {i} is {g_z}')
    print(f'Accelerometer offset for axis X of sensor {i} is {a_x}')
    print(f'Accelerometer offset for axis Y of sensor {i} is {a_y}')
    print(f'Accelerometer offset for axis Z of sensor {i} is {a_z}')
    print(f'Ellipsoid parameters for sensor{i}: a={res[0]}; b={res[1]}; c={res[2]}; x0={res[3]}, y0={res[4]}; z0={res[5]}')

    saved_data[i] = {}
    saved_data[i]["gyro"] = {}
    saved_data[i]["acc"] = {}
    saved_data[i]["mag"] = {}
    saved_data[i]["gyro"]["X"] = g_x
    saved_data[i]["gyro"]["Y"] = g_y
    saved_data[i]["gyro"]["Z"] = g_z
    saved_data[i]["acc"]["X"] = a_x
    saved_data[i]["acc"]["Y"] = a_y
    saved_data[i]["acc"]["Z"] = a_z
    saved_data[i]["mag"]["a"] = res[0]
    saved_data[i]["mag"]["b"] = res[1]
    saved_data[i]["mag"]["c"] = res[2]
    saved_data[i]["mag"]["x0"] = res[3]
    saved_data[i]["mag"]["y0"] = res[4]
    saved_data[i]["mag"]["z0"] = res[5]


# ----------------------------------------------------------------------------------------------------------------------
# TODO: Use calculated parameters to calibrate sensors data
# print("-"*15)
# print(saved_data)
