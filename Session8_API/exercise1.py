import requests
import pprint

# # API to get NASA's picture of the day.
# response = requests.get('https://api.nasa.gov/planetary/apod?hd=true&api_key=DEMO_KEY')
# print(response.status_code)
# # print(response.content)
# response_json = response.json()
# print(type(response_json))
# print(response_json)

# pprint.pprint(response_json)

inventory_response={"product_code":"le34",
                    "product_name":"Magic Bulb - Large",
                    "fitting_type":"e14",
                    "stock":2,
                    "unit_dimensions_cm":{"width":20,"height":40,"depth":20},
                    "upcoming_deliveries":[{"date":"01/02/2022","quantity":225},{"date":"01/03/2022","quantity":245}],
                    "unit_price":24.32,
                    "unit_currency":"EUR"}

#1a Get the product name of the item
print(inventory_response["product_name"])

#1b Find out how many deliveries are planned
print(len(inventory_response["upcoming_deliveries"]))

#1c Find out when the next delivery is
print(inventory_response["upcoming_deliveries"][0]["date"])

#1d Get the width of the bulb
print(inventory_response["unit_dimensions_cm"]["width"])

#1e Get the unit price of the bulb and the currency it's in.
print(inventory_response["unit_price"], inventory_response["unit_currency"])