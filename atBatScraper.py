import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.baseballpress.com/lineups/2023-04-14"

def get_names(item):
    try:
        player_name = item.get('data-razz').split("/")[-2].replace("+"," ")
    except IndexError:
        player_name = ""
    return player_name

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

a,b = 0,10

for i in range(7):

    try:
        first_lineup = [get_names(item) for item in soup.select(".col--min:nth-of-type(1) > a.player-link, [class$='col--min']:nth-of-type(1) .player > a.player-link")]
        first_lineup = first_lineup[a:b] + [''] * (9 - len(first_lineup))
    except:
        first_lineup = [''] * 9

    try:
        second_lineup = [get_names(item) for item in soup.select(".col--min:nth-of-type(2) > a.player-link, [class$='col--min']:nth-of-type(2) .player > a.player-link")]
        second_lineup = second_lineup[a:b] + [''] * (9 - len(second_lineup))
    except:
        second_lineup = [''] * 9

    df = pd.DataFrame({"first_lineup": first_lineup, "second_lineup": second_lineup})
    df.to_csv("baseballpress.csv", encoding='utf-8', index=False)
    print(df)

    a+=10
    b+=10

    print ("--------------------------------------------")