import matplotlib.pyplot as plt

x = [35,25,20,20]
y = ['Python', 'Javascript', 'Java', 'C#']

plt.pie(x, labels=y, autopct='%0.00f%%')

plt.show()