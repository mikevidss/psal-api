import requests
import json

def cookies():
    r = requests.get('https://psal.org/profiles/school-profile.aspx#22527')
    cookies_dic = r.cookies.get_dict()
    cs = []
    cookie_header = ''
    for c in cookies_dic:
        a = cookies_dic.get(c)
        b = f"{c}={a};"
        cs.append(b)
        
    return cookie_header.join(cs)

def monthsGames(month,year):
    url = f"https://www.psal.org/SportDisplay.svc/GetStudentGrade?schoolId=%2722527%27%20&nmonth={month}&nyear={year}&orderBY='DATE-desc'";
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Host':'www.psal.org',
        'Referer':'https://www.psal.org/profiles/school-profile.aspx',
        'Cookie':cookies(),
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Accept-Language':'en-US,en;q=0.9',
        'Sec-Fetch-Dest':'empty',
        'X-Requested-With':'XMLHttpRequest'
    }
    d = requests.get(url,headers=headers)
    return d.text

def seasonGames(year):
    url = f"https://www.psal.org/SportDisplay.svc/vw_School_Profile?$filter=cschool eq'22527' and (season eq '{year}')&$orderby=Expr8 asc";
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Host':'www.psal.org',
        'Referer':'https://www.psal.org/profiles/school-profile.aspx',
        'Cookie':cookies(),
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Accept-Language':'en-US,en;q=0.9',
        'Sec-Fetch-Dest':'empty',
        'X-Requested-With':'XMLHttpRequest'
    }
    d = requests.get(url,headers=headers)
    return d.text

def sportProfile(year, sportId):
    url = f"https://www.psal.org/SportDisplay.svc/getTeamScheduleAny?csports='{sportId}'&season={year} &schoolid='22527'&format=' '";
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Host':'www.psal.org',
        'Referer':'https://www.psal.org/profiles/team-profile.aspx',
        'Cookie':cookies(),
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Accept-Language':'en-US,en;q=0.9',
        'Sec-Fetch-Dest':'empty',
        'X-Requested-With':'XMLHttpRequest'
    }
    d = requests.get(url,headers=headers)
    return d.text

def game(gameId, sportId):
    url = f"https://www.psal.org/SportDisplay.svc/Get_DisplayGameInfo?gameid={gameId}&csport='{sportId}'";
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Host':'www.psal.org',
        'Referer':'https://www.psal.org/games/game-detail.aspx',
        'Cookie':cookies(),
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Accept-Language':'en-US,en;q=0.9',
        'Sec-Fetch-Dest':'empty',
        'X-Requested-With':'XMLHttpRequest'
    }
    d = requests.get(url,headers=headers)
    return d.text

def roster(year, sportId):
    url = "https://www.psal.org/SportDisplay.svc/getTeamRosters?season={}&csports='{}' &schoolid='22527'&activeInactive='Y'".format(year, sportId)
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Host':'www.psal.org',
        'Referer':'https://www.psal.org/profiles/team-profile.aspx',
        'Cookie':cookies(),
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Accept-Language':'en-US,en;q=0.9',
        'Sec-Fetch-Dest':'empty',
        'X-Requested-With':'XMLHttpRequest'
    }
    d = requests.get(url,headers=headers)
    return d.text
