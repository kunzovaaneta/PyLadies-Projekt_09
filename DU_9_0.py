def vytvareni_slovniku_mocnin(zadane_cislo):
	"""Pro zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a
	jako hodnoty k nim jejich druhé mocnin"""

	slovnik_mocnin={}
	for cislo in range (1,zadane_cislo+1):
		vytvareni_slovniku_mocnin[cislo] = cislo**2
	
	return slovnik_mocnin

print (vytvareni_slovniku_mocnin(3))