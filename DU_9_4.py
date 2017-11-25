"""Hra kdo? S kým? Co dělali??"""
import random
seznam_kdo=[]
seznam_s_kym=[]
seznam_co_delali=[]
seznam_kde=[]
seznam_kdy=[]
seznam_proc=[]

	
def utvareni_seznamu_na_kdo():
	while True:
		kdo=input("Kdo?")
		seznam_kdo.append(kdo)
		pokracovani=input("chceš přidat další odpověd? ano x ne ")
		if pokracovani == "ne" or pokracovani == "Ne":
			break
def utvareni_seznamu_na_s_kym():
	while True:
		s_kym=input("S kým?")
		seznam_s_kym.append(s_kym)
		pokracovani=input("chceš přidat další odpověd? ano x ne ")
		if pokracovani == "ne" or pokracovani == "Ne":
			break
def utvareni_seznamu_na_co_delali():
	while True:
		co_delali=input("Co dělali")
		seznam_co_delali.append(co_delali)
		pokracovani=input("chceš přidat další odpověd? ano x ne ")
		if pokracovani == "ne" or pokracovani == "Ne":
			break
def utvareni_seznamu_na_kde():
	while True:
		kde=input("Kde to dělali")
		seznam_kde.append(kde)
		pokracovani=input("chceš přidat další odpověd? ano x ne ")
		if pokracovani == "ne" or pokracovani == "Ne":
			break

def utvareni_seznamu_na_kdy():	
	while True:
		kdy=input("Kdy?")
		seznam_kdy.append(kdy)
		pokracovani=input("chceš přidat další odpověd? ano x ne ")
		if pokracovani == "ne" or pokracovani == "Ne":
			break

def utvareni_seznamu_na_proc():	
	while True:
		proc=input("Proč?")
		seznam_proc.append(proc)
		pokracovani=input("chceš přidat další odpověd? ano x ne ")
		if pokracovani == "ne" or pokracovani == "Ne":
			break
utvareni_seznamu_na_kdo()
utvareni_seznamu_na_s_kym()
utvareni_seznamu_na_co_delali()
utvareni_seznamu_na_kde()
utvareni_seznamu_na_kdy()
utvareni_seznamu_na_proc()

kdo = random.choice(seznam_kdo)
s_kym = random.choice(seznam_s_kym)
co_delali = random.choice(seznam_co_delali)
kde = random.choice(seznam_kde)
kdy = random.choice(seznam_kdy)
proc = random.choice(seznam_proc)

print(kdo,s_kym,co_delali,kde, kdy, proc)