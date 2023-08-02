class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configs are ::", self.cpu, self.ram)


com1 = Computer("i5", "16gb")
com2 = Computer("IOS", "64gb")

com1.config()
com2.config()
