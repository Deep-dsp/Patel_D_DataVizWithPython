import matplotlib.pyplot as plt

hours = [4, 8, 2]
activities = ['sleep', 'work', 'play']
color = ['gold', 'silver', 'red']
plt.pie(hours, labels=activities, colors=color, startangle=90, autopct='%.1f%%')
plt.show()