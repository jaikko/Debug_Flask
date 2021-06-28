import json


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions

competitions = loadCompetitions()
   
foundCompetition = [c for c in competitions if c['name'] == "Spring Festival"][0]
print(foundCompetition['date'])
str = foundCompetition['date'].split(" ")[0].split("-")
# str = str.split(" ")[0].split("-")
# str = str[0].split("-")
print(str[0])