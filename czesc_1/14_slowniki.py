slownik = {
    "klucz1": "wartosc",
    "klucz2": "wartosc2",
    "klucz3": "wartosc",
    "klucz4": "wartosc"
}
print(slownik["klucz1"])

for klucz in slownik:
    print(klucz, slownik[klucz])

for wartosc in slownik.values():
    print(wartosc)

for klucz, wartosc in slownik.items():
    print(klucz, wartosc)
