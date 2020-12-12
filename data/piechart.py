import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [8, 7]
colors = ['#99F6FA', '#AD6F47']
labels = ["Men", "women"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)


plt.show()
