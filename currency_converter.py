
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    print("DEBUG URL:", url)  
    response = requests.get(url)
    data = response.json()
    if "result" in data and data["result"] is not None:
        return data['result']
    else:
        print("❌ Error: Couldn't fetch conversion rate.")
        return None


def main():
    print("💱 Currency Converter using Live Exchange Rates")
    try:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("From currency (e.g. USD): ").upper()
        to_currency = input("To currency (e.g. INR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)

        if result is not None:
            print(f"\n✅ {amount} {from_currency} = {float(result):.2f} {to_currency}")


    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
