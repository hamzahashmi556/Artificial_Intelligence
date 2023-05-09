from Lab_4 import Environment
from Lab_4 import Room
from Lab_4 import Agent


# 3 ROOM CLEANER AGENT
class ThreeRoomVaccumCleanerEnvironment(Environment):

    def __init__(self, agent):
        self.r1 = Room("A", "dirty")
        self.r2 = Room("B", "dirty")
        self.r3 = Room("c", "dirty")
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.currentRoom.status = "clean"
            elif res == "right":
                self.currentRoom = self.r2
            elif res == "down":
                self.currentRoom = self.r3
            else:
                self.currentRoom = self.r1
                break

            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print(f"Perception at step {self.step} is [{self.currentRoom.status},{self.currentRoom.location}]")

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

    def delay(self, n=100):
        self.delay = n


class VaccumAgent(Agent):
    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        elif self.environment.currentRoom.location == 'A':
            return 'right'
        elif self.environment.currentRoom.location == 'B':
            return 'down'
        else:
            return 'left'


if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = ThreeRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(6)
