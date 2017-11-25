slovnik = {1:"jedna", 2:"dvě",3:"tři"}

def vypis_obsahu_slovniku(slovnik):
	"""funkce vypíše obsah slovníku (klíče a k nim náležící hodnoty) na jednotlivé řádky."""
	for klic, hodnota in slovnik.items():
		klic_hodnota=(klic,hodnota)
		print(klic_hodnota)

vypis_obsahu_slovniku(slovnik)