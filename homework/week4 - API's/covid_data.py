import requests
import pprint

# Use the UK government's COVID API to create a list of daily cases in the UK, 
# with each element in the list representing one day's cases.

# response = requests.get('https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=newCasesByPublishDate')
# # pprint.pprint(response.json())
# uk_cases = []
# for day in response.json()['body'][3]:
#     uk_cases.append(response.json()['body'][4])

# print(len(uk_cases))

uk_endpoint = 'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=overview&structure={"date":"date","newCases":"newCasesByPublishDate"}'
r = requests.get(uk_endpoint)
response = r.json()

uk_cases = []
for day in response["data"]:
    uk_cases.append((day["newCases"]))

# You could also use a list comprehension to create a list 
uk_cases = [day["newCases"] for day in response["data"]]

print(uk_cases)