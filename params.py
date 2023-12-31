class params:
    def __init__(self,mode="normal") -> None:
        self.mode = mode
        self.first_fire_neurons_num = 400
        self.alpha = 10

        if self.mode == 'normal':
            self.threshold = 30
            self.decay = 0.6
            self.reset = -40

        elif self.mode == 'abnormal_decay':
            self.threshold = 30
            self.decay = 0.2
            self.reset = -40

        elif self.mode == 'abnormal_threshold':
            self.threshold = 10
            self.decay = 0.6
            self.reset = -40
        
        elif self.mode == 'abnormal_reset':
            self.threshold = 30
            self.decay = 0.6
            self.reset = -20