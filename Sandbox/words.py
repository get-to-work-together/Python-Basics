
text = """
Eindhoven (Geluidsfragment uitspraak (info / uitleg)) is een stad en gemeente in de Kempen, in het zuidoosten van de Nederlandse provincie Noord-Brabant. Het is naar inwonertal al sinds 1961 de vijfde gemeente van Nederland. Ze telt 238.478 inwoners (31 januari 2022) op een grondgebied van 88,84 km². Ze omvat naast de gelijknamige stad Eindhoven tevens het dorp Acht en de uitbreidingslocatie Meerhoven.

De gemeente Eindhoven maakte in de eerste helft en het midden van de twintigste eeuw een explosieve groei door. In 1920 annexeerde de stad — aan het begin van de eeuw een klein Kempisch stadje — vijf omliggende gemeenten, waardoor de gemeente ineens enorm vergroot werd, zowel qua oppervlakte (van 75 tot 6300 ha) als qua inwoneraantal (van 6.500 naar 46.000).[1] Op 1 januari 1940 had Eindhoven al 113.126 inwoners.[1] Het schaarde zich daarmee al hoog op de ranglijst van grootste gemeentes in Nederland. In de volgende 75 jaar werd dit inwonertal verdubbeld. Allesbepalend voor deze ontwikkeling was de groei van het Philips-concern, van gloeilampenfabriek tot multinational en wereldspeler op het gebied van de elektronica.

De gemeente verwelkomde haar 225.000e inwoner[2] op 24 november 2015. De stad groeit nog steeds: de prognose is dat het aantal inwoners van de gemeente in 2040 zal zijn gestegen naar 248.000.[3] De gemeente is de hoofdplaats van de Metropoolregio Eindhoven (MRE) en maakt deel uit van het stedelijk netwerk BrabantStad. De agglomeratie Eindhoven (niet te verwarren met de metropoolregio), bestaande uit onder andere de gemeenten Eindhoven, Veldhoven, Best, Nuenen en Geldrop-Mierlo, telt bijna 420.000 inwoners op een oppervlakte van ongeveer 540 km². In de MRE wonen ongeveer 750.000 mensen.
"""

text = text.lower()

text = text.translate(str.maketrans('', '', '.,()[]0123456789?!/'))

words = text.split()

print(words)

unique_words = set(words)

print(unique_words)

d = dict()
for word in sorted(unique_words):
    d[word] = words.count(word)

for word, n in sorted(d.items(), key = lambda item: item[1], reverse = True):
    print('%-30s : %4d' % (word, n))
