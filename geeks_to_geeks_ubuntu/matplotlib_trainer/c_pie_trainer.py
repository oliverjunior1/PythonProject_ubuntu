import matplotlib.pyplot as plt

x = ['Python', 'Javascript', 'Java', 'C#', 'Outros']
y = [30,20,15,10,25]

plt.pie(y, labels=x, autopct='%0.00f%%')
plt.show()