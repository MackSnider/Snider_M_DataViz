import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

years = [1994, 1998, 2002, 2006, 2010, 2014]

medals = [4, 1, 2, 2, 3, 3]

plt.bar(years, medals, color=(0/255, 100/255, 100/255), linewidth=6.0)

plt.ylabel("Medals Won")

plt.xlabel("Years")

plt.title("Medals Won per Winter Olympic Games", pad="20", **hfont)

plt.show()