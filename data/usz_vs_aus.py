import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [5, 167]
colors = ['#99F6FA', '#FA1001']
labels = ["AUS", "USA"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)


plt.show()
