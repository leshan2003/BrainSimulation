import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import imageio
import os
from glob import glob
from PIL import Image 


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

def gen_GIF():
    for mode in ['normal','abnormal_decay','abnormal_threshold','abnormal_reset']:
        images = []
        file_path = os.path.join('./figures/'+ mode+'/')
        # 用glob找到file_path下所有后缀为png的文件，且不分大小写
        for filename in sorted(glob(file_path + '*.png', recursive=True), key=os.path.getmtime):
            images.append(Image.open(filename))

        images[0].save("./figures/"+mode+"/demo.gif", format='GIF',save_all=True, append_images=images[1:], loop=5,duration=500)



if __name__ == '__main__':
    gen_GIF()