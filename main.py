import requests



#variables------------------------------------------------------
APIKey = "?api_key=RGAPI-ee6d4575-3807-4cb6-9d17-b4fd8723d75b"
baseURL = "https://na1.api.riotgames.com/lol/"
path = "summoner/v4/summoners/by-name/"
summonerName = "I%20Touch%20Myself"

response = requests.get(baseURL + path + summonerName + APIKey)
#response = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/RiotSchmick?api_key=<key>'

print(response.content)