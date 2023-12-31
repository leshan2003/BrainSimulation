class LIFNeuron:
    def __init__(self, position):
        self.position = position
        self.V = -60                  # 膜电位
        self.ready = 1