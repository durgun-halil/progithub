import random

def get_next_card():
    kartlar = ['Maça', 'Kupa', 'Sinek', 'Elmas']
    siralamalar = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    rastgele_kart = random.choice(kartlar)
    rastgele_siralama = random.choice(siralamalar)
    return (rastgele_kart, rastgele_siralama)

def get_card_value(kart):
    if kart[1] in ['J', 'Q', 'K']:
        return 10
    elif kart[1] == 'A':
        return 11
    elif kart[1] == 'K' and kart[0] in ['Maça', 'Sinek']:
        return 1
    else:
        return int(kart[1])

pot = int(input("Bilgenin parası: "))
num_games = int(input("Oyun sayısı: "))

for game in range(1, num_games + 1):
    print("Oyun", game)
    kral_cards = []
    kral_total_value = 0
    for i in range(2):
        card = get_next_card()
        kral_cards.append(card)
        if i == 0:
            print("(*)", card[0], card[1])
        else:
            print(card[0], card[1])
            kral_total_value += get_card_value(card)
    bilge_cards = []
    bilge_total_value = 0
    for i in range(2):
        card = get_next_card()
        bilge_cards.append(card)
        print(card[0], card[1])
        bilge_total_value += get_card_value(card)
    print("Toplam değer:", bilge_total_value)
    while bilge_total_value < 21:
        choice = input("Vurmak mı istiyorsun yoksa durmak mı istiyorsun? [V/D]: ")
        if choice.upper() == 'V':
            card = get_next_card()
            bilge_cards.append(card)
            bilge_total_value += get_card_value(card)
            print(card[0], card[1])
            print("Toplam değer:", bilge_total_value)
        elif choice.upper() == 'D':
            break
    if bilge_total_value == 21:
        pot += 50
        print("It is Blackking! Bilge kazandı.")
    elif bilge_total_value > 21:
        pot -= 50
        print("Bastın, kaybettin.")
    else:
        kral_total_value += get_card_value(kral_cards[0])
        while kral_total_value < 17:
            card = get_next_card()
            kral_cards.append(card)
            kral_total_value += get_card_value(card)
        print("Kralın toplam değeri:", kral_total_value)
        if kral_total_value > 21 or bilge_total_value > kral_total_value:
            pot += 50
            print("Bilge kazandı.")
        elif bilge_total_value == kral_total_value:
            print("Berabere kaldılar.")
        else:
            pot -= 50
            print("Bilge kaybetti.")
    print("Pot:", pot)
    print("")
