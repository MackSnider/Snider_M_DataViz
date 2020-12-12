import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [5, 10]
colors = ['#FAE500', '#2E00AD']
labels = ["Skating", "Skiing"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)


plt.show()
