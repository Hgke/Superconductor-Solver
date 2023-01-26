from Objects.ComplexObjectBase import ComplexObjectBase


class DC_SFQ_1(ComplexObjectBase):
    """
    A converter from DC pulses to SFQ pulses

    Inputs:
    1 - DC pulse input
    2 - SFQ pulse output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 13

        self.name = 'DC_SFQ'
        self.description = 'DC to SFQ converter'

    def create_elements(self, sk):

        #self.add_ib(name='Ib1', val=4.28, loc=[sk[10]])
        
        
        k = 0.08 * 1/0.05
        k_i = 12.5 /12.5
        k_c = 0.055 * 15
        
        self.add_ib(name='Ib1', val=k_i*3.2, loc=[sk[10]])

        self.add_JJ(name='J1', c=k_c*1,  A=k_i*1.18, B=0, loc=[sk[3], sk[4]])
        self.add_JJ(name='J2', c=k_c*1,  A=k_i*1.37, B=0, loc=[sk[7], sk[8]])
        self.add_JJ(name='J3', c=k_c*1,  A=k_i*1.37, B=0, loc=[sk[5], sk[6]])
        self.add_JJ(name='J4', c=k_c*1,  A=k_i*1.96, B=0, loc=[sk[11], sk[12]])

        self.add_L(name='L2', val=k*1.27, loc=[sk[0], sk[2]])
        self.add_L(name='L8', val=k*1.36, loc=[sk[5], 0])
        self.add_L(name='L4', val=k*0.49, loc=[sk[2], sk[3]])
        self.add_L(name='Lp3', val=k*0.26, loc=[sk[6], sk[7]])
        self.add_L(name='L5', val=k*0.49, loc=[sk[2], sk[5]])
        self.add_L(name='Lp2', val=k*0.07, loc=[sk[8], 0])
        self.add_L(name='L10', val=k*0.08, loc=[sk[4], sk[7]])
        self.add_L(name='L6', val=k*0.43, loc=[sk[4], sk[9]])
        self.add_L(name='Lp11', val=k*0.03, loc=[sk[10], sk[9]])
        self.add_L(name='L13', val=k*0.66, loc=[sk[9], sk[11]])
        self.add_L(name='Lp4', val=k*0.001, loc=[sk[12], 0])
        self.add_L(name='L15', val=k*0.001, loc=[sk[11], sk[1]])

