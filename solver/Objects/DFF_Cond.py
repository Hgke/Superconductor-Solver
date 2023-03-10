from Objects.ComplexObjectBase import ComplexObjectBase


class DFF_Cond(ComplexObjectBase):
    """
    D Flip-Flop element

    Inputs:
    1 - input signal
    2 - clock
    3 - output signal
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 7

        self.name = 'DFF with Condensator'
        self.description = 'D trigger with Read-Out line'

    def create_elements(self, sk):
        self.add_JJ(name='J0', c=1, A=1.96, B=0, loc=[sk[3], sk[4]])
        self.add_JJ(name='J1', c=1, A=1.96, B=0, loc=[sk[4], 0])
        self.add_JJ(name='J2', c=1, A=2.96, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J3', c=1, A=2.16, B=0, loc=[sk[5], sk[6]])
        
        self.add_L(name='L0', val=1.048, loc=[sk[0], sk[3]])
        self.add_L(name='L1', val=3.21, loc=[sk[4], sk[5]])
        
        self.add_C(name='C1', c=30, loc=[sk[5], sk[2]])
        self.add_L(name='L3', val=0.6, loc=[sk[1], sk[6]])

        self.add_ib(name='Ib1', val=1.38, loc=[sk[4]])
