import matplotlib.pyplot as plt 

hfont = {'fontname':'codec cold' }

countries = ['AUS', 'CRO']


color = ('#99F6FA', '#00FA67')


medals = [15, 11]

plt.barh(countries, medals, color=color, linewidth=6.0)

plt.ylabel("Medals Won")

plt.xlabel("Countries")

plt.title("Croati VS Australia", pad="20", **hfont)

plt.show()