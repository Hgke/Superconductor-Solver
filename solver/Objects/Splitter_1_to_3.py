from Objects.ComplexObjectBase import ComplexObjectBase


class Splitter_1_to_3(ComplexObjectBase):
    """
    SFQ pulse splitter

    Inputs:
    1 - input signal
    2 - output signal 1
    3 - output signal 2
    4 - output signal 3
    """

    def __init__(self, loc):
        super().__init__(loc=loc)
        #self.check_loc(loc, 3)
        self.N = 5

        self.name = 'Splitter_1_to_3'
        self.description = 'Splitter_1_to_3'

    def create_elements(self, sk):
        self.add_ib(name='ibJin', val=0.75, loc=[sk[4]])
        self.add_ib(name='ibJout1', val=0.75, loc=[sk[1]])
        self.add_ib(name='ibJout2', val=0.75, loc=[sk[2]])
        self.add_ib(name='ibJout3', val=0.75, loc=[sk[3]])

        self.add_JJ(name='Jin', c=1, A=1, B=0, loc=[sk[4], 0])
        self.add_JJ(name='Jout1', c=1, A=1, B=0, loc=[sk[1], 0])
        self.add_JJ(name='Jout2', c=1, A=1, B=0, loc=[sk[2], 0])
        self.add_JJ(name='Jout3', c=1, A=1, B=0, loc=[sk[3], 0])

        self.add_L(name='Lin', val=1, loc=[sk[0], sk[4]])
        self.add_L(name='Lout1', val=1, loc=[sk[4], sk[1]])
        self.add_L(name='Lout2', val=1, loc=[sk[4], sk[2]])
        self.add_L(name='Lout3', val=1, loc=[sk[4], sk[3]])
