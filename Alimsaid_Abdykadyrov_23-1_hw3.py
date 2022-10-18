class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return (self.cpu + self.memory) / 2

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __str__(self):
        return f'Cpu: {self.cpu}, Memory: {self.memory}'


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(
            f'Идет звонок на номер {call_to_number}, с сим-карты {sim_card_number}'
            f'{self.__sim_cards_list[sim_card_number]})'
        )

    def __str__(self):
        return f'Sim-Card: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        print(f'Маршрут построен до {location}')

    def __str__(self):
        return Computer.__str__(self) + f' Sim-Cards {self.sim_cards_list}'


comp_1 = Computer(9, 599)

phone_1 = Phone(['O!'])

smart_1 = SmartPhone(12, 128, ['MegaCom', 'MegaLine', 'Beeline'])
smart_2 = SmartPhone(10, 64, ['O!', 'MegaCom'])

print(comp_1)
print(phone_1)
print(smart_1)
print(smart_2)

print('Computation:', comp_1.make_computations())

smart_1.call(1, "+996708167997")
smart_2.use_gps('LA')

print('Сравнение:')
print(comp_1 > smart_1)
print(smart_2 < smart_1)
print(smart_1 == comp_1)
print(comp_1 != smart_2)
print(comp_1 >= smart_2)
print(smart_1 <= comp_1)
