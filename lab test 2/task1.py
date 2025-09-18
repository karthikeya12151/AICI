def convert(amount, ccy, rate_fetcher=None):
    if rate_fetcher is None: rate_fetcher = default_rate_fetcher
    return amount * rate_fetcher(ccy)
def default_rate_fetcher(ccy):
    rates = {'USD': 83.0, 'EUR': 90.0, 'GBP': 105.0, 'JPY': 0.55, 'INR': 1.0, 'CAD': 60.0, 'AUD': 55.0, 'CHF': 95.0, 'CNY': 11.5, 'SGD': 61.0}
    return rates.get(ccy.upper(), 1.0)
def get_user_input():
    print("\n" + "="*50 + "\nCURRENCY CONVERTER\n" + "="*50)
    print("Available currencies: USD, EUR, GBP, JPY, INR, CAD, AUD, CHF, CNY, SGD")
    print("Enter 'quit' or 'exit' to stop the program\n" + "-"*50)
    while True:
        try:
            amount_input = input("Enter amount to convert: ").strip()
            if amount_input.lower() in ['quit', 'exit', 'q']: return None, None
            amount = float(amount_input)
            if amount < 0: print(" Amount cannot be negative. Please try again."); continue
        except ValueError: print(" Invalid amount. Please enter a valid number."); continue
        currency = input("Enter currency code (e.g., USD, EUR): ").strip().upper()
        if not currency: print(" Currency code cannot be empty. Please try again."); continue
        if currency.lower() in ['quit', 'exit', 'q']: return None, None
        return amount, currency
def display_conversion_result(amount, currency, converted_amount, rate):
    print("\n" + "="*50 + "\nCONVERSION RESULT\n" + "="*50)
    print(f"Amount: {amount:,.2f} {currency}\nExchange Rate: 1 {currency} = {rate:.2f} INR\nConverted Amount: {converted_amount:,.2f} INR\n" + "="*50)

def interactive_currency_converter():
    print("Welcome to the Currency Converter!\nThis tool converts various currencies to INR (Indian Rupees)")
    while True:
        try:
            amount, currency = get_user_input()
            if amount is None and currency is None: print("\n Thank you for using the Currency Converter!"); break
            rate = default_rate_fetcher(currency)
            converted_amount = convert(amount, currency)
            display_conversion_result(amount, currency, converted_amount, rate)
            while True:
                continue_choice = input("\nDo you want to convert another amount? (y/n): ").strip().lower()
                if continue_choice in ['y', 'yes']: break
                elif continue_choice in ['n', 'no']: print("\n Thank you for using the Currency Converter!"); return
                else: print("Please enter 'y' for yes or 'n' for no.")
        except KeyboardInterrupt: print("\n\n Program interrupted. Goodbye!"); break
        except Exception as e: print(f"\n An error occurred: {e}\nPlease try again.")
def run_tests():
    print("Running test cases...\n" + "="*50)
    test_rate_fetcher = lambda ccy: 83.0
    result = convert(10, 'USD', test_rate_fetcher)
    print(f"convert(10, 'USD') with rate 83.0 => {result}")
    result_default = convert(10, 'USD')
    print(f" convert(10, 'USD') with default fetcher => {result_default}")
    test_rates = {'USD': 83.0, 'EUR': 90.0, 'GBP': 105.0, 'JPY': 0.55}
    print("\nTesting different currencies:")
    for ccy, expected_rate in test_rates.items():
        test_fetcher = lambda ccy, rate=expected_rate: rate
        result = convert(10, ccy, test_fetcher)
        print(f" convert(10, '{ccy}') with rate {expected_rate} => {result}")
    print("\n" + "="*50)
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--test': run_tests()
    else: interactive_currency_converter()
