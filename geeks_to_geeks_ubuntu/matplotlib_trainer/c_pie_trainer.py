# pie with program languages

import matplotlib.pyplot as plt

x = ['Python', 'Javascript', 'Java', 'C#', 'Outros']
y = [30,20,18,12,20]

plt.title("The most used programming language in the World!")
plt.pie(y, labels=x, autopct="%0.00f%%")
plt.show()