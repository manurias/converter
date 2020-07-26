def conversor(tipo_pesos, valore_dolar):
    pesos = input("Quanti pesos " + tipo_pesos + " hai?: ")
    pesos = float(pesos)
    dollari = pesos / valore_dollaro
    dollari = round(dollari, 2)
    dollari = str(dollari)
    print("Hai $" + dollari + " dollari")


menu = """
Benvenuto al convertitore di monete 💰

1 - Pesos colombiani
2 - Pesos argentini
3 - Pesos messicani

Scegli una opzione: """

opzione = int(input(menu))

if opzione == 1:
    conversor("colombiani", 3875)
elif opzione == 2:
    conversor("argentini", 65)
elif opzione == 3:
    conversor("messicani", 24)
else:
    print('Inserisci un opzione corretta per favore')
