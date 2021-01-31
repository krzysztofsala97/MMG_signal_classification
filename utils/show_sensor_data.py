import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_sensor_data_3d(df, sensor_id, sensor_type):
    if sensor_type == 0:
        sensor_name = "Gyro_" + str(sensor_id)
    if sensor_type == 1:
        sensor_name = "Acc_" + str(sensor_id)
    if sensor_type == 2:
        sensor_name = "Mag_" + str(sensor_id)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.scatter(df[sensor_name + "_X"], df[sensor_name + "_Y"], df[sensor_name + "_Z"])
    plt.show()


def show_sensor_data_2d(df, sensor_id, sensor_type, axis1, axis2):
    if sensor_type == 0:
        sensor_name = "Gyro_" + str(sensor_id)
    if sensor_type == 1:
        sensor_name = "Acc_" + str(sensor_id)
    if sensor_type == 2:
        sensor_name = "Mag_" + str(sensor_id)

    fig, ax = plt.subplots()
    ax.set_xlabel(axis1)
    ax.set_ylabel(axis2)

    ax.plot(df[sensor_name+"_"+axis1], df[sensor_name+"_"+axis2], 'ro')

    plt.show()