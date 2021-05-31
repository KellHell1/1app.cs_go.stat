import requests
import sys
#api_steam = A8F344C924ADF251D79C33006F51ABF0
#id_my = 76561198264607321
requests_main = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=A8F344C924ADF251D79C33006F51ABF0&steamid=76561198264607321')
requests_stats = requests_main.json()
a=[]
stat = requests_stats['playerstats']['stats']

kd = round(stat[0]['value'] / stat[1]['value'],2)
total_kills_knife = stat[9]['value']


total_matches_played = stat[128]['value']
total_matches_won = stat[127]['value']
winrate_procent = str(round(stat[127]['value']/stat[128]['value'],2))[2:]
total_planted_bombs = stat[3]['value']
total_defused_bombs = stat[4]['value']

print(winrate_procent)






