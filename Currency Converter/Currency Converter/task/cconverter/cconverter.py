# RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
# ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
# HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
# AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
# MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.

# rates = {
#     "RUB": 2.98,
#     "ARS": 0.82,
#     "HNL": 0.17,
#     "AUD": 1.9622,
#     "MAD": 0.208
# }
#
# try:
#     # conis = float(input("Please, enter the number of conicoins you have:\n"))
#     # rate = float(input("Please, enter the exchange rate:"))
#     conis = float(input())
# except OSError as os:
#     print("OSError", os)
# except Exception as e:
#     print("Exception", e)
# finally:
#     for key in rates:
#         formatted_float = "{:.2f}".format(conis * rates[key])
#         print(f"I will get {formatted_float} {key} from the sale of {conis} conicoins.")

import requests
import json


def read_currency_to_exchange():
    try:
        return input().lower()

    except Exception as e_read_currency_to_exchange:
        print(f"{read_currency_to_exchange.__name__} error: {e_read_currency_to_exchange}")


def read_currency_code_receive():
    try:
        return input().lower()

    except Exception as e_read_currency_code_receive:
        print(f"{read_currency_code_receive.__name__} error: {e_read_currency_code_receive}")


def retrieve_data_from_float_rates(code_have):
    try:
        url = f'http://www.floatrates.com/daily/{code_have}.json'
        response = requests.get(url)
        if response.status_code == 200:
            return requests.get(url)
        else:
            # print("Response failed")
            return False

    except Exception as e_retrieve_data_from_floatRates:
        print(str(e_retrieve_data_from_floatRates))
        print(f"{retrieve_data_from_float_rates.__name__} error: {e_retrieve_data_from_floatRates}")


def init_exchange_rates(ex_dict, p_currency_code_have):
    default_ex_rates = ["usd", "eur"]
    try:
        if p_currency_code_have == default_ex_rates[0]:
            # EUR
            init_cache_dict = {default_ex_rates[1]: ex_dict[default_ex_rates[1]]["rate"]}
        else:
            # USD
            init_cache_dict = {default_ex_rates[0]: ex_dict[default_ex_rates[0]]["rate"]}

        return init_cache_dict
    except Exception as exc_init_cache:
        print(f"{init_exchange_rates.__name__} error: {exc_init_cache}")


def save_exchange_rates(p_cache_dict, ex_dict, p_exchange_dict):
    try:
        # 5. Take a look at the cache. Maybe you already have what tyou need?
        rate = "rate"  # "inverseRate"  # "rate"
        if ex_dict in p_cache_dict:
            # 6. If you have the currency in your cache, calculate the amount.
            print("Oh! It is in the cache!")
        else:
            # 7. If not, get it from the site, and calculate the amount.
            print("Sorry, but it is not in the cache!")
            p_cache_dict[ex_dict] = p_exchange_dict[ex_dict]["rate"]

        return p_cache_dict

    except Exception as e_save_exchange_rates:
        print(f"{save_exchange_rates.__name__} error: {e_save_exchange_rates}")


def init_exchange_rates_dict(ex_dict, p_currency_code_have):
    default_ex_rates = ["usd", "eur"]
    try:
        if p_currency_code_have == default_ex_rates[0]:
            # EUR
            init_cache_dict = {default_ex_rates[1]: ex_dict[default_ex_rates[1]]["rate"]}
        else:
            # USD
            init_cache_dict = {default_ex_rates[0]: ex_dict[default_ex_rates[0]]["rate"]}

        return init_cache_dict
    except Exception as exc_init_cache:
        print(f"{init_exchange_rates.__name__} error: {exc_init_cache}")


def start_cache():
    currencies = ["usd", "eur"]
    cache_init = {}
    try:
        exchange_currency_default = retrieve_data_from_float_rates(currencies[0])
        if exchange_currency_default:
            exchange_json_default = exchange_currency_default.text
            exchange_dict_default = json.loads(exchange_json_default)
            # cache_init = init_exchange_rates_dict(exchange_dict_default, currencies[0])
            # EUR
            cache_init = {currencies[1]: exchange_dict_default[currencies[1]]["rate"]}

        exchange_currency_default = retrieve_data_from_float_rates(currencies[1])
        if exchange_currency_default:
            exchange_json_default = exchange_currency_default.text
            exchange_dict_default = json.loads(exchange_json_default)
            # USD
            # cache_init = {currencies[0]: exchange_dict_default[currencies[0]]["rate"]}
            cache_init[currencies[0]] = exchange_dict_default[currencies[0]]["rate"]

        return cache_init
    except Exception as e_start_cache:
        print(f"{start_cache.__name__} error: {e_start_cache}")


def main():

    try:

        # 0a. init USD
        cache_dict = start_cache()

        # 1. Take the currency code and
        currency_code_have = read_currency_to_exchange()

        # 2. Retrieve the data
        exchange_currency = retrieve_data_from_float_rates(currency_code_have)

        if exchange_currency:
            exchange_json = exchange_currency.text
            exchange_dict = json.loads(exchange_json)

            # 10. Repeat steps 4-9 until there is no currency left to process.
            while True:
                # 4a. Read the currency to exchange
                currency_code_receive = read_currency_code_receive()

                if currency_code_receive in cache_dict:
                    cache_dict.update()
                    dummy = {currency_code_receive:exchange_dict[currency_code_receive]["rate"]}
                    cache_dict.update(dummy)

                # 4b.
                if currency_code_receive == '':
                    break

                # 4d. Read amount
                conis = float(input())

                # 5. Checking the cache...
                print("Checking the cache...")
                # 4c. once again
                cache_dict = save_exchange_rates(cache_dict, currency_code_receive, exchange_dict)

                amount_fmt_float = "{:.2f}".format(conis * cache_dict[currency_code_receive])  # [rate]
                print(f'You received {amount_fmt_float} {currency_code_receive.upper()}.')
        else:
            print("An error occurred while trying to get json")
    except Exception as e_main:
        print(f"{main.__name__} error: {e_main}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e_start:
        print(f"{__name__} error: {e_start}")
