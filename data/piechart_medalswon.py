import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

values = [4, 1, 2, 2, 3, 3]
colors = ['#99F6FA', '#58ABAD', '#B5FDFF', '#AD6F47', '#FABE98', '#0047FA']
labels = [1994, 1998, 2002, 2006, 2010, 2014]


plt.pie(values, labels=labels, colors=colors)


plt.show()
