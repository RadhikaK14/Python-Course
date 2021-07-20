import requests
import pprint

# query_params = {'api-key': '755d6e5b-ec68-4d2b-8509-2d380aab6e5d'} 
# response = requests.get("https://content.guardianapis.com/search", params=query_params)
# print(response.status_code)
# # print(response.content)
# pprint.pprint(response.json())

# Find a url to any article about clouds.
# query_params = {'api-key': '755d6e5b-ec68-4d2b-8509-2d380aab6e5d', 'q' : 'clouds'} 
# response = requests.get("https://content.guardianapis.com/search", params=query_params)
# # print(response.content)
# reponse_json = response.json()
# pprint.pprint(reponse_json['response']['results'][0]['webUrl'])

# # Find a url to any article 5 years or older about bitcoin.
# query_params = {'api-key': '755d6e5b-ec68-4d2b-8509-2d380aab6e5d', 'q' : 'bitcoin', 'to-date': '2016-01-01'} 
# response = requests.get("https://content.guardianapis.com/search", params=query_params)
# reponse_json = response.json()
# pprint.pprint(reponse_json['response']['results'][0]['webUrl'])

# # Count the number of articles written this year about 3D printing 
# # (hint: use the tag "technology/3d-printing" for The Guardian). 
# query_params = {'api-key': '755d6e5b-ec68-4d2b-8509-2d380aab6e5d', 'tag' : 'technology/3d-printing', 'from-date': '2021-01-01'} 
# response = requests.get("https://content.guardianapis.com/search", params=query_params)
# # reponse_json = response.json()['response']['results']
# # pprint.pprint(len(reponse_json))
# print(response.json()["response"]["total"])

# Find the first article written in the science section about the landing of the Mars Rover Perseverance. 
# The landing was on 18 Feb 2021. 
query_params = {'api-key': '755d6e5b-ec68-4d2b-8509-2d380aab6e5d', 'q' : 'Mars Rover', 'order-by':'oldest', 'from-date': '2021-02-18', 'section':'science'} 
response = requests.get("https://content.guardianapis.com/search", params=query_params)
pprint.pprint(response.json()['response']['results'][0]['webUrl'])

query_params = {'api-key': '755d6e5b-ec68-4d2b-8509-2d380aab6e5d', 'q':'perseverance', 'order-by':'oldest', 'from-date':'2021-02-18', 'to-date':'2021-02-20', 'section':'science'}
response = requests.get("https://content.guardianapis.com/search", params=query_params)
print(response.json()["response"]["results"][1]["webUrl"])