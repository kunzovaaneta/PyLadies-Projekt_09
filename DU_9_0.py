def vytvareni_a_vraceni_slovniku():
	"""Pro zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a
	jako hodnoty k nim jejich druhé mocnin"""

	zadane_cislo = int(input("zadej číslo větší než 1 -"))
	jednotlivé_argumenty_slovniku = []
	for cislo in range (1,zadane_cislo+1):
		jednotlivé_argumenty_slovniku = [(cislo, cislo**2)] + jednotlivé_argumenty_slovniku

	slovnik_argumentu = dict(jednotlivé_argumenty_slovniku)
	print(slovnik_argumentu)

vytvareni_a_vraceni_slovniku()