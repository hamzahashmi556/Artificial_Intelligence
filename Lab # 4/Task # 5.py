from Lab_4 import Environment
from Lab_4 import Room
from Lab_4 import Agent


# TASK # 5: REMOVE SENSES OF AGENT (FUNCTIONS/METHODS), AGENT WON'T BE ABLE TO EXECUTE ANY METHODS, THROW ERROR,
# MALFUNCTION ETC
class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, no_of_rooms):
        self.n = no_of_rooms
        self.agent = agent
        self.rooms = []
        for i in range(self.n):
            self.rooms.append(Room(i + 1, 'dirty'))
        self.currentRoom = self.rooms[0]
        self.currentRoomNumber = 0
        self.delay = 1000
        self.step = 1
        self.action = ""

class VaccumAgent(Agent):
    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location < self.environment.n:
            return 'next'
        return 'exit'


if __name__ == '__main__':
    number_of_rooms = int(input("Enter Number of Room: "))
    number_of_steps = number_of_rooms * 2
    vcagent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(vcagent, number_of_rooms)
    env.executeStep(number_of_steps)
