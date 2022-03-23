import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for item in kwargs.items():
            for i in range(item[1]):
                self.contents.append(item[0])
    def draw(self, n):
        drawn = []
        if n <= len(self.contents):
            for i in range(n):
                i_delete = random.randrange(len(self.contents))
                drawn.append(self.contents[i_delete])
                self.contents.pop(i_delete)
        else:
            drawn = copy.deepcopy(self.contents)
            for i in range(len(self.contents)):
                self.contents.pop()
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        m = 0
        for i in range(num_experiments):
            hat_copy = copy.deepcopy(hat)
            drawn = hat_copy.draw(num_balls_drawn)
          
            increase_m = True
            for item in expected_balls.items():
                if drawn.count(item[0]) < item[1]:
                    increase_m = False
            if increase_m: m += 1
            hat_copy = copy.copy(hat)
        return m/num_experiments






