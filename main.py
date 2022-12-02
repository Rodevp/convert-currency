from requests import get

BASE_URL = "https://free.currconv.com"
API_KEY = "YOUR API KEY"

def get_all_currencies() :

    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    data = get(BASE_URL + endpoint).json()

    return list( data["results"] ).sort()


def show_currencies(currencies) :

    for _, currency in currencies :
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")

        print("--------------------------------------")
        print(f"{_id} - {name} - {symbol}")



def currencie_rate(currency_one, currency_two) :
    endpoint = f"api/v7/convert?q={currency_one}_{currency_two}&compact=ultra&apiKey={API_KEY}"

    response = get(BASE_URL + endpoint).json()

    if len(response) == 0 :
        print("invalid currencies")
        return


    rate = list( response.values() )[0]

    print(f"{currency_one} -> {currency_two} = {rate}")

    return rate


def convert_currency(currency_one, currency_two, amount) :

    rate = currencie_rate(currency_one, currency_two)

    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return

    converted = rate * amount
    print(f"{amount} {currency_one} is to equal {converted} {currency_two}")    

    return converted

