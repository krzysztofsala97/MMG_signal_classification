import pandas as pd
import numpy as np


def calculate_offset(df_up, df_down, sensor_id, sensor_type, axis):
    if sensor_type == 0:
        sensor_name = "Gyro_" + str(sensor_id) + "_" + axis
    if sensor_type == 1:
        sensor_name = "Acc_" + str(sensor_id) + "_" + axis
    if sensor_type == 2:
        sensor_name = "Mag_" + str(sensor_id) + "_" + axis

    df = pd.concat([df_up, df_down], ignore_index=True)
    data_sum = df[sensor_name].sum()
    num_idx = len(df.index.values)

    return data_sum/num_idx
