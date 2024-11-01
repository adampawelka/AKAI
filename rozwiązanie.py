import json

with open("zbiór_wejściowy.json", "r", encoding="utf-8") as file:
    zbior_wejsciowy = json.load(file)

with open("kategorie.json", "r", encoding="utf-8") as file:
    kategorie = json.load(file)

def masa_na_uncje(masa):
    if "ct" in masa:
        masa = float(masa.replace("ct", "").replace(",", "."))
        return masa * 0.007054792
    elif "g" in masa:
        masa = float(masa.replace("g", "").replace(",", "."))
        return masa * 0.0352739619

typ_czystosc_wartosc = {}
for item in kategorie:
    typ_czystosc_wartosc[(item["Typ"], item["Czystość"])] = item["Wartość za uncję (USD)"]


obiekty_z_wartosciami = []


for obiekt in zbior_wejsciowy:
    masa = masa_na_uncje(obiekt["Masa"])
    if (obiekt["Typ"], obiekt["Czystość"]) in typ_czystosc_wartosc:
        wartosc_za_uncje = typ_czystosc_wartosc[(obiekt["Typ"], obiekt["Czystość"])]
        wartosc_wlasciciela = round(masa * wartosc_za_uncje, 2)
        obiekty_z_wartosciami.append((obiekt, wartosc_za_uncje, wartosc_wlasciciela))    

obiekty_z_wartosciami.sort(key=lambda x: x[1], reverse=True)
najlepsze = obiekty_z_wartosciami[:5]

print("5 danych o największej wartości na jednostkę:\n")
for i, element in enumerate(najlepsze, start=1):
    obiekt = element[0]
    wartosc_za_uncje = element[1]
    wartosc_wlasciciela = element[2]
    print(f"{i}. Typ: {obiekt['Typ']}")
    print(f"Czystość: {obiekt['Czystość']}")
    print(f"Masa: {obiekt['Masa']}, Barwa: {obiekt['Barwa']}")
    print(f"Pochodzenie: {obiekt['Pochodzenie']}")
    print(f"Wartość za jednostkę (uncję): {wartosc_za_uncje} USD")
    print(f"Właściciel: {obiekt['Właściciel']}")
    print(f"Wartość posiadana przez właściciela: {wartosc_wlasciciela} USD")
    print("----------------------\n")
