# pip install BeautifulSoup4

from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_doc, 'html.parser')

all_params = []


with open("web-5.7.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for row in soup.tbody.find_all('tr'):
    par_category = row.find('th').find('a').get('href').split('#')[0].split('.html')[0]
    par_link = row.find('th').find('a').get('href')
    par_name = row.find('th').find('a').get_text()
    par_atr1= row.select('td')[0].get_text()
    par_atr1 = par_atr1 if len(par_atr1)>=1 else "non"
    par_atr2 = row.select('td')[1].get_text()
    par_atr2 = par_atr2 if len(par_atr2)>=1 else "non"
    par_atr3 = row.select('td')[2].get_text()
    par_atr3 = par_atr3 if len(par_atr3)>=1 else "non"

    par_atr4 = row.select('td')[3].get_text()
    par_atr4 = par_atr4 if len(par_atr4)>=1 else "non"

    par_atr5 = row.select('td')[4].get_text()
    par_atr5 = par_atr5 if len(par_atr5)>=1 else "non"

    _p = {'Category':par_category,'Name':par_name, 'Cmd-Line'	: par_atr1,'Option File':par_atr2,	'System Var':par_atr3,	'Var Scope':par_atr4,	'Dynamic':par_atr5,
    'Link':f"https://dev.mysql.com/doc/refman/8.0/en/{par_link}"}
    all_params.append(_p)
    # print(par_category,par_name,par_atr1,par_atr2,par_atr3,par_atr4,par_atr5)
    # print("=====")
import json

with open('parameters.json','w') as f:
    # f.write(all_params,json.dump)
    json.dump(all_params, f)
# print(all_params)