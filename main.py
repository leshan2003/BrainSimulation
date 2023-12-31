import numpy as np
import matplotlib.pyplot as plt
from visualize import visualize
from neuron import LIFNeuron
from brain import brain
from params import params
# np.random.seed(7)

def main():
    # par = params(mode='normal')
    par = params(mode='abnormal_decay')
    # par = params(mode='abnormal_threshold')
    # par = params(mode='abnormal_reset')

    mybrain = brain(threshold=par.threshold, decay=par.decay, reset=par.reset, alpha=par.alpha, first_fire_neurons_num=par.first_fire_neurons_num)
    fire_neurons_list, fire_neurons_num = mybrain.simulate(time_step=10)
    
    # print(fire_neurons_list)
    print(fire_neurons_num)
    visualize(fire_neurons_list,mode=par.mode)
    
def simulate_n_times(n):
    normal_num_average = []
    abnormal_decay_num_average = []
    abnormal_threshold_num_average = []
    abnormal_reset_num_average = []
    for i in range(n):
        print(f"epoch {i}")
        for mode in ['normal','abnormal_decay','abnormal_threshold','abnormal_reset']:
            par = params(mode=mode)
            mybrain = brain(threshold=par.threshold, decay=par.decay, reset=par.reset, alpha=par.alpha, first_fire_neurons_num=par.first_fire_neurons_num)
            fire_neurons_list, fire_neurons_num = mybrain.simulate(time_step=10)
            if mode == 'normal':
                normal_num_average.append(np.array(fire_neurons_num))
            elif mode == 'abnormal_decay':
                abnormal_decay_num_average.append(np.array(fire_neurons_num))
            elif mode == 'abnormal_threshold':
                abnormal_threshold_num_average.append(np.array(fire_neurons_num))
            elif mode == 'abnormal_reset':
                abnormal_reset_num_average.append(np.array(fire_neurons_num))
        
    normal_num_average = np.array(normal_num_average).mean(axis=0)
    abnormal_decay_num_average = np.array(abnormal_decay_num_average).mean(axis=0)
    abnormal_threshold_num_average = np.array(abnormal_threshold_num_average).mean(axis=0)
    abnormal_reset_num_average = np.array(abnormal_reset_num_average).mean(axis=0)
    # 将四个np.array合并，保存到txt文件中
    np.savetxt('figures/num_average.txt', np.array([normal_num_average,abnormal_decay_num_average,abnormal_threshold_num_average,abnormal_reset_num_average]), fmt='%d')

    # 柱状图
    plt.figure()
    # figure size
    plt.figure(figsize=(10, 5))
    plt.title('average firing neurons number')
    plt.xlabel('time step')
    plt.ylabel('firing neurons number')
    # x轴坐标从0到10，间隔为1
    plt.xticks(np.arange(11))
    # 错开一点显示
    x = np.arange(11)
    width = 0.2
    plt.bar(x, normal_num_average, width=width, label='normal',color='blue')
    plt.bar(x+width, abnormal_decay_num_average, width=width, label='abnormal_decay',color='orange')
    plt.bar(x+2*width, abnormal_threshold_num_average, width=width, label='abnormal_threshold',color='green')
    plt.bar(x+3*width, abnormal_reset_num_average, width=width, label='abnormal_reset',color='red')
    plt.legend()
    plt.savefig(f"figures/num_average.png",dpi=600)
    # plt.show()

if __name__ == "__main__":
    main()