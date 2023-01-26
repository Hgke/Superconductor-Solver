from Objects.ComplexObjectBase import ComplexObjectBase


class NDRO(ComplexObjectBase):
    """
    NDRO (Non Destructive Read Out) cell
    Inputs:
    1 – data signal 
    2 – readout signal
    3 – dumping signal
    4  – N/C
    5 – data output signal
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 5)
        self.N = 11

        self.name = 'NDRO'
        self.description = 'NDRO cell'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=0.5, loc=[sk[5]])
        self.add_ib(name='Ib2', val=0.5, loc=[sk[9]])

        self.add_JJ(name='J1', c=1.504,  A=1.504, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J2', c=1,  A=1, B=0, loc=[sk[6], sk[10]])
        self.add_JJ(name='J3', c=2,  A=2, B=0, loc=[sk[9], 0])
        self.add_JJ(name='J4', c=1,  A=1, B=0, loc=[sk[10], 0])
        self.add_JJ(name='J5', c=1.504,  A=1.504, B=0, loc=[sk[6], sk[8]])
        self.add_JJ(name='J6', c=1.504,  A=1.504, B=0, loc=[sk[7], sk[10]])
        
        self.add_MutualInductance(name='L1_and_L4',L1=4.54, L2=1.298,k=0.5, loc=[5,6,1,7])

        self.add_L(name='L0',val=1, loc=[sk[0], sk[5]])
        self.add_L(name='L2', val=2.53, loc=[sk[6], sk[9]])
        self.add_L(name='L3', val=1.298, loc=[sk[2], sk[8]])
        self.add_L(name='L_out1',val=1,loc=[sk[9],sk[3]])
        self.add_L(name='L_out2',val=1,loc=[sk[10],sk[4]])

