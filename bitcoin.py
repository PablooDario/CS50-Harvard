import sys
import requests

def main():
    # if user did not input a value in command line
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        #if user did not input a float value
        n = float(sys.argv[1])
        try:
            # get the current value of bitcoin
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            bitcoinValue = response["bpi"]["USD"]["rate_float"]
            # get the value of n bitcoins
            amount = bitcoinValue * n
            print(f"${amount:,.4f}")
        except requests.RequestException:
            sys.exit("Request Error")
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()