import requests, json



#variables------------------------------------------------------
APIKey = "?api_key=RGAPI-fd40cb5b-0a42-44bb-97bf-96bcfd2c988b"
baseURL = "https://na1.api.riotgames.com/lol/"
summonerName = "I%20Touch%20Myself"



#Path Variables-------------------------------------------------
getSummonerByNamePath = "summoner/v4/summoners/by-name/"

#response = requests.get(baseURL + path + summonerName + APIKey)
#response = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/RiotSchmick?api_key=<key>'

#print(response.content)


#functions-------------------------------------------------------

#getSummonerID
#Returns id as a string
#doesn't use region yet -- maybe build it out alter
def getSummonerID(summonerName, region):
    summonerName = summonerName.replace(" ", "%20")
    req = requests.get(baseURL + getSummonerByNamePath + summonerName + APIKey)
    responseJSON = req.content
    responseDictionary = json.loads(responseJSON)
    summonerID = responseDictionary["id"]
    return summonerID

#getSummonerDictionary
#Returns summoner info as a dictionary
#doesn't use region yet -- maybe build it out alter
def getSummonerDictionary(summonerName, region):
    summonerName = summonerName.replace(" ", "%20")
    req = requests.get(baseURL + getSummonerByNamePath + summonerName + APIKey)
    responseJSON = req.content
    responseDictionary = json.loads(responseJSON)
    return responseDictionary





#tests-------------------------------------------------------------
#test getSummonerID - should return cM1HQxDnsLrWKFpELwDmChV8l-MUxgHenX6XQ32X7NUBsi8
summonerID = getSummonerID("I Touch Myself", "na")
if(summonerID == "cM1HQxDnsLrWKFpELwDmChV8l-MUxgHenX6XQ32X7NUBsi8"):
    print("getSummonerID() is working!")
else:
    print("getSummonerID() is failing!")

summonerDictionary = getSummonerDictionary("I Touch Myself", "na")
print(summonerDictionary)