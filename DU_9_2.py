
def z_retezce_vratit_slovnik():
	"""š funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé
znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci."""
	argument = list(input("Zadej řetězec, který chceš převést na slovnik:"))

	seznam_dvojic= []
	for pismeno in argument:
		pocet_vyskytu = argument.count(pismeno)
		seznam_dvojic.append((pismeno,pocet_vyskytu))
	
	slovnik = dict(seznam_dvojic)
	print(slovnik)

z_retezce_vratit_slovnik()