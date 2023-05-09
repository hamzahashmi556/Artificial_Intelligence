from Lab_4 import Environment
from Lab_4 import Room
from Lab_4 import Agent


# TASK # 2 & 3 N NUMBER OF ROOM CLEANER AGENT + STOP THE AGENT WHEN COMPLETED
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

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            action = self.agent.act()
            self.action = action

            if action == 'clean':
                self.currentRoom.status = "clean"
            elif action == "next":
                # Move to Next Room
                self.currentRoomNumber += 1
                if self.currentRoomNumber != len(self.rooms):
                    self.currentRoom = self.rooms[self.currentRoomNumber]
                # self.currentRoom = self.rooms[self.currentRoomNumber + 1]
                # self.currentRoomNumber += 1

            self.displayAction()
            self.step += 1

    def displayPerception(self):
        print(f"Perception at step {self.step} is [{self.currentRoom.status},{self.currentRoom.location}]")

    def displayAction(self):
        if self.action == "exit":
            print("All Rooms has been cleaned :)")
        else:
            print("------- Action taken at step %d is [%s]" % (self.step, self.action))


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
