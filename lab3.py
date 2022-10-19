import matplotlib.pyplot as plt
import numpy as np


"""
ODPOWIEDŹ CZEMU do zadania lab:
Z danych przedstawionych w zadaniu wynika, że ilość osób które utraciły węch w całym społeczeństwie jest mniejsze niż utrata węchu spowodowanych COVID-19
"""

class Covid19():
    def __init__(self, p_c, p_l, p_l_c) -> None:
        self.p_c = p_c
        self.p_l = p_l
        self.p_l_c = p_l_c
        self.p_c_l = self.count_pcl()

    def count_pcl(self) -> float:
        return  self.p_l_c*self.p_c/self.p_l



def plot_results(x_lst, y_lst, title, y_axis):
    plt.title(title)
    plt.xlabel('X RANGE') 
    plt.ylabel(y_axis)
    plt.plot(x_lst,y_lst)
    plt.show()

case1 = Covid19(0.0062,0.01,0.9)
print(case1.p_c_l)
case2 = Covid19(0.2,0.001,0.01)
print(case2.p_c_l)
# Change in P(C)
x_lst = np.linspace(0.0062,1,1000)
y_lst = []
for x in x_lst:
    case = Covid19(x,0.01,0.9)
    y_lst.append(case.p_c_l)

plot_results(x_lst,y_lst,"Change of P(C)",'P(C|L)') 

# Change in P(L)
x_lst = np.linspace(0.01,1,1000)
y_lst = []
for x in x_lst:
    case = Covid19(0.0062,x,0.9)
    y_lst.append(case.p_c_l)

plot_results(x_lst,y_lst,"Change of P(L)",'P(L)') 

# Change in P(L|C)
x_lst = np.linspace(0.1, 1, 1000)
y_lst = []
for x in x_lst:
    case = Covid19(0.0062,0.01,x)
    y_lst.append(case.p_c_l)

plot_results(x_lst,y_lst,"Change of P(L|C)",'P(C|L)') 

# case1 = Covid19(0.2,0.001,0.01)
# P(c) = 0.2,P(L)=0.001,P(L|C)=0.1

