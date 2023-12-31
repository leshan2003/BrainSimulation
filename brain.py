import numpy as np
from neuron import LIFNeuron

class brain:
    def __init__(self, network_shape=(10, 10, 10),threshold=30, decay=0.6, reset=-40, alpha=10, first_fire_neurons_num=400):
        self.network_shape = network_shape
        self.alpha = alpha
        self.first_fire_neurons_num = first_fire_neurons_num
        self.threshold = threshold
        self.decay = decay
        self.reset = reset

        self.neuron_network = np.empty(network_shape, dtype=object)
        for x in range(network_shape[0]):
            for y in range(network_shape[1]):
                for z in range(network_shape[2]):
                    position = (x, y, z)
                    self.neuron_network[x, y, z] = LIFNeuron(position=position)

    def calculate_input(self, position, last_fire_neurons):
        # 对position位置的神经元，计算上一个周期其他神经元放电对其产生的电流输入（电压增大）
        input_current = 0
        sum = 0
        for x in [position[0]-2, position[0]-1, position[0], position[0]+1, position[0]+2]:
            for y in [position[1]-2, position[1]-1, position[1], position[1]+1, position[1]+2]:
                for z in [position[2]-2, position[2]-1, position[2], position[2]+1, position[2]+2]:
                    if (x,y,z) != position and x >= 0 and x < self.network_shape[0] and y >= 0 and y < self.network_shape[1] and z >= 0 and z < self.network_shape[2]:
                        if (x,y,z) in last_fire_neurons:
                            sum += 1
                            distance = np.sqrt(np.sum(np.square(np.array(position) - np.array((x, y, z)))))
                            input_current += self.alpha / (distance**2) * np.random.uniform(0.5, 1.0)

        return input_current

    def simulate_once(self, last_fire_neurons):
        fire_neurons = []
        for x in range(self.network_shape[0]):
            for y in range(self.network_shape[1]):
                for z in range(self.network_shape[2]):
                    input_current = self.calculate_input(position=(x, y, z), last_fire_neurons=last_fire_neurons)
                    # if input_current > self.threshold - self.reset:
                    #     print(f"input_current at {x},{y},{z}",input_current)
                    self.neuron_network[x, y, z].V += input_current
                    if self.neuron_network[x, y, z].V >= self.threshold and self.neuron_network[x, y, z].ready == 1:
                        self.neuron_network[x, y, z].V = self.reset
                        fire_neurons.append((x,y,z))
                        self.neuron_network[x, y, z].ready = 0
                    else:
                        self.neuron_network[x, y, z].ready = 1
                        self.neuron_network[x, y, z].V = self.neuron_network[x, y, z].V - (self.neuron_network[x, y, z].V - self.reset) * self.decay

        return fire_neurons, len(fire_neurons)
    
    def simulate(self, time_step):
        # 仿真结果的记录
        fire_neurons_list = []
        fire_neurons_num = []

        # 随机生成若干个不同的初次放电神经元
        first_fire_neurons = []
        i = 0
        while(i < self.first_fire_neurons_num):
            x = np.random.randint(0, self.network_shape[0])
            y = np.random.randint(0, self.network_shape[1])
            z = np.random.randint(0, self.network_shape[2])
            if (x,y,z) not in first_fire_neurons:
                first_fire_neurons.append((x,y,z))
                i += 1
        fire_neurons_list.append(first_fire_neurons)
        fire_neurons_num.append(len(first_fire_neurons))

        simulate_time = 0
        while(simulate_time < time_step):
            # print(f"simulation time: {simulate_time}")
            simulate_time += 1
            # print(f"fire neurons: {(fire_neurons_list[-1])}")
            fire_neurons, num = self.simulate_once(fire_neurons_list[-1])
            fire_neurons_list.append(fire_neurons)
            fire_neurons_num.append(num)

        return fire_neurons_list,fire_neurons_num