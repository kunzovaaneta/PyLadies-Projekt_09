slovnik = {1:1, 2:4, 4:16}

def soucet_hodnot_a_klicu (slovnik):
	"""Fuknce, která sečte a vypíše sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako
argument."""
	soucet_hodnot = 0
	soucet_klicu = 0
	for klic, hodnota in slovnik.items():
		soucet_klicu = klic + soucet_klicu
		soucet_hodnot = hodnota + soucet_hodnot
	print ("soucet kličů je {}".format(soucet_klicu))
	print ("součet hodnot je {}".format (soucet_hodnot))

soucet_hodnot_a_klicu(slovnik)