from bs4 import BeautifulSoup
import json

# name = "8.0-system"
name = "5.7-system"

# name = "8.0-rep"
# name = "5.7-rep"

# name = "8.0-innodb"
# name = "5.7-innodb"

with open(f"{name}.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

cnt = 0
all_params = []
for row in soup.ul.find_all('li', {'class': 'listitem'}):
    table = row.find('table', {"frame": "box"})
    if table:
        if len(row.find_all('tbody')) >= 1:
            tbody = row.find_all('tbody')[0]
            # print(tbody)
            # print('========')
            variables = False
            tmp = {}
            for tr in tbody.findChildren('tr', recursive=False):
                colname = tr.find('th').getText().strip()
                colvalue = tr.find('td').getText().strip()
                colname = colname.replace(
                    '\n                            ', ' ')
                tmp[colname] = colvalue
                if colname == 'System Variable':
                    variables = True
            if variables:
                all_params.append(tmp)
            cnt += 1

with open(f'{name}.json', 'w') as f:
    json.dump(all_params, f)
# print(all_params,cnt)
