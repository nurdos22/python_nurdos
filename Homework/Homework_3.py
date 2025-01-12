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
        return f"CPU + Memory = {self.__cpu + self.__memory}"

    def __str__(self):
        return f"Computer(CPU: {self.__cpu}, Memory: {self.__memory})"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Calling {call_to_number} from SIM-{sim_card_number} ({sim_card})")
        else:
            print("Invalid SIM card number.")

    def __str__(self):
        return f"Phone(SIM Cards: {', '.join(self.__sim_cards_list)})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Building route to {location}...")


    def __str__(self):
        return f"SmartPhone(CPU: {self.cpu}, Memory: {self.memory}, SIM Cards: {', '.join(self.sim_cards_list)})"



computer = Computer(3.2, 16)
phone = Phone(["Beeline", "Megacom"])
smartphone1 = SmartPhone(2.5, 8, ["O!", "Beeline"])
smartphone2 = SmartPhone(3.0, 32, ["Megacom"])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print(computer.make_computations())

phone.call(1, "+996777998811")
phone.call(3, "+996999112233")

smartphone1.use_gps("Bishkek")
print(smartphone1.make_computations())
smartphone1.call(2, "+996550001122")

# Comparing objects
print(computer == smartphone1)
print(computer > smartphone1)
print(smartphone1 < smartphone2)




