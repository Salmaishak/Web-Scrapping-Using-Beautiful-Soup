import pandas as pd
fayoum = pd.read_csv('HotelsFayoum.csv')
alex = pd.read_csv('HotelsAlexandria.csv')
giza = pd.read_csv('HotelsGiza.csv')
luxor = pd.read_csv('HotelsLuxor.csv')
hurghada = pd.read_csv('HotelsHurgada2.csv')
sharm = pd.read_csv('HotelsSharm.csv')
cairo = pd.read_csv('Hotels.csv')
fayoum["City"] = "Al-Fayyum"
alex["City"] = "Alexandria"
giza["City"] = "Giza"
sharm["City"] = "Sharm El Sheikh"
hurghada["City"] = "Hurghada"
luxor["City"] = "Luxor"
cairo["City"] = "Cairo"
#fayoum.to_csv('Hotelsfayoum.csv',index=False, encoding="utf-8", mode='w')
#alex.to_csv('HotelsAlexandria.csv',index=False, encoding="utf-8", mode='w')
#luxor.to_csv('HotelsLuxor.csv',index=False, encoding="utf-8", mode='w')
#hurghada.to_csv('HotelsHurgada2.csv', index=False, encoding="utf-8", mode='w')
#sharm.to_csv('HotelsSharm.csv', index=False, encoding="utf-8", mode='w')
#giza.to_csv('HotelsGiza.csv', index=False, encoding="utf-8", mode='w')

#cairo.to_csv('Hotels.csv', index=False, encoding="utf-8", mode='w')
