import matplotlib.pyplot as plt

x = [36,24,22,18]
y = ['Python', 'Javascript', 'Java', 'C#']

plt.pie(x, labels=y, autopct='%0.00f%%')
plt.title("The most used languages around the World!")

plt.show()