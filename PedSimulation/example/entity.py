from PedSimulation.entity import *
from PedSimulation.shape2d import *

class Pedestrian(Agent):
    def __init__(self, shape):
        super(Pedestrian, self).__init__(shape)
        self.mass = 80

class Wall(Movable):
    def __init__(self,shape):
        super(Wall, self).__init__(shape)

    def affected(self, affection):
        pass

class RecordPed(Pedestrian):
    def __init__(self, shape, data_list=None):
        super(Pedestrian, self).__init__(shape)
        self.data_list = data_list

    def affected(self, affection):
        if affection.a_type == "Csv":
            self.position = affection.value

class EllipseCsvPed(RotateAgent):
    def __init__(self,data_list = None):
        super(EllipseCsvPed, self).__init__(Ellipse2D)
        self.data_list = data_list

    def affected(self, affection):
        if affection.a_type == "":
            pass

class SafetyRegion(Goal):
    pass

class RotatePedestrian(RotateAgent):
    def __init__(self, shape):
        super(RotatePedestrian, self).__init__(shape)
        self.mass = 80
        self.inertia = 4
