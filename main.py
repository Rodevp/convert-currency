from requests import get

BASE_URL = "https://free.currconv.com"
API_KEY = "YOUR API KEY"

def get_all_currencies() :

    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    data = get(BASE_URL + endpoint).json()

    return list( data["results"] ).sort()


def show_currencies(currencies) :

    for currency in currencies :
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")

        print("--------------------------------------")
        print(f"{_id} - {name} - {symbol}")

