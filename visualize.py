import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def visualize(fire_neurons_list,mode):
    for i in range(len(fire_neurons_list)):
        x = [position[0] for position in fire_neurons_list[i]]
        y = [position[1] for position in fire_neurons_list[i]]
        z = [position[2] for position in fire_neurons_list[i]]

        # 创建一个三维子图
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # 绘制三维散点图
        ax.scatter(x, y, z, c='r', marker='o')

        # ax.text(-2, 1, 5, f'N = {len(fire_neurons_list[i])}', color='green', fontsize=15, transform=ax.transAxes)

        # 设置图表标题和坐标轴标签
        ax.set_title(f'timestep : {i}, {len(fire_neurons_list[i])} firing neurons')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')

        # 显示或存储图表
        plt.savefig(f"system/figures/{mode}/{i:0>2d}.png")
        # plt.show()
