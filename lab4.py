import matplotlib.pyplot as plt
import numpy as np


class Burglary:
    def __init__(self, pi, pa, pb, pai, pbi) -> None:
        self.dog_alarm = None
        self.silent_alarm = None
        self.p_i = pi
        self.p_a = pa
        self.p_b = pb
        self.p_a_i = pai
        self.p_b_i = pbi

    def update_dog_alarm(self, status):
        self.dog_alarm = status

    def update_silent_alarm(self, status):
        self.silent_alarm = status

    def probability(self):
        if self.silent_alarm is None and self.dog_alarm:
            return (self.p_b_i * self.p_i) / self.p_b

        if self.dog_alarm is None and self.silent_alarm:
            return (self.p_a_i * self.p_i) / self.p_a

        if self.dog_alarm and self.silent_alarm:
            return (self.p_b_i / self.p_b) * ((self.p_a_i * self.p_i) / self.p_a)

        if self.silent_alarm and not self.dog_alarm:
            return ((1 - self.p_b_i) / (1 - self.p_b)) * ((self.p_a_i * self.p_i) / self.p_a)

        if self.dog_alarm and not self.silent_alarm:
            return (1 - self.p_a_i) / (1 - self.p_a) * ((self.p_b_i * self.p_i) / self.p_b)


def plot_results(x_lst, y_lst, title, y_axis):
    plt.title(title)
    plt.xlabel('X RANGE')
    plt.ylabel(y_axis)
    plt.plot(x_lst, y_lst)
    plt.show()


burglary = Burglary(0.002, 0.01, 0.5, 0.8, 0.98)
print(f'Reason from multiple evidence, burglary:')
print('=========================================')
burglary.update_silent_alarm(True)
burglary.update_dog_alarm(True)
print(
    f'Silent Alarm: True, Dog: True, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(True)
burglary.update_dog_alarm(False)
print(
    f'Silent Alarm: True, Dog: False, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(True)
burglary.update_dog_alarm(None)
print(
    f'Silent Alarm: True, Dog: None, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(None)
burglary.update_dog_alarm(True)
print(
    f'Silent Alarm: None, Dog: True, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(False)
burglary.update_dog_alarm(True)
print(
    f'Silent Alarm: False, Dog: True, Probability: {burglary.probability():.2%}')

burglary = Burglary(0.002, 0.01, 0.5, 0.98, 0.70)
print(f'Old dog, Good Alarm:')
print('=========================================')
burglary.update_silent_alarm(True)
burglary.update_dog_alarm(True)
print(
    f'Silent Alarm: True, Dog: True, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(True)
burglary.update_dog_alarm(False)
print(
    f'Silent Alarm: True, Dog: False, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(True)
burglary.update_dog_alarm(None)
print(
    f'Silent Alarm: True, Dog: None, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(None)
burglary.update_dog_alarm(True)
print(
    f'Silent Alarm: None, Dog: True, Probability: {burglary.probability():.2%}')
burglary.update_silent_alarm(False)
burglary.update_dog_alarm(True)
print(
    f'Silent Alarm: False, Dog: True, Probability: {burglary.probability():.2%}')


# change in dog
x = np.linspace(0, 1, 100)
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, 0.98, i)
    burglary.update_silent_alarm(True)
    burglary.update_dog_alarm(True)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: True, DOG: False', 'dog sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, 0.98, i)
    burglary.update_silent_alarm(True)
    burglary.update_dog_alarm(False)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: True, DOG: None', 'dog sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, 0.98, i)
    burglary.update_silent_alarm(True)
    burglary.update_dog_alarm(None)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: None, DOG: True', 'dog sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, 0.98, i)
    burglary.update_silent_alarm(None)
    burglary.update_dog_alarm(True)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: False, DOG: True', 'dog sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, 0.98, i)
    burglary.update_silent_alarm(False)
    burglary.update_dog_alarm(True)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: True, DOG: True', 'dog sens')

# change in alarm
x = np.linspace(0, 1, 100)
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, i, 0.98)
    burglary.update_silent_alarm(True)
    burglary.update_dog_alarm(True)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: True, DOG: False', 'alarm sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, i, 0.98)
    burglary.update_silent_alarm(True)
    burglary.update_dog_alarm(False)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: True, DOG: None', 'alarm sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, i, 0.98)
    burglary.update_silent_alarm(True)
    burglary.update_dog_alarm(None)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: None, DOG: True', 'alarm sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, i, 0.98)
    burglary.update_silent_alarm(None)
    burglary.update_dog_alarm(True)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: False, DOG: True', 'alarm sens')
probability_lst = []
for i in x:
    burglary = Burglary(0.002, 0.01, 0.5, i, 0.98)
    burglary.update_silent_alarm(False)
    burglary.update_dog_alarm(True)
    probability_lst.append(burglary.probability())

plot_results(x, probability_lst, 'Alarm: True, DOG: True', 'alarm sens')
