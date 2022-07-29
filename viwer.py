# %%
from bs4 import BeautifulSoup
import csv

with open("data.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    head_list = soup.thead.tr.find_all("th")
    body_list = soup.tbody.find_all("tr")

# %%
th_list = []
for th in head_list:
    str = th.find("a").get_text().replace("▲▼","").strip()
    th_list.append(str)

# %%
tbody_t = []
for tr in body_list:
    tr_t = []
    for td in tr: 
        txt = td.get_text().strip()
        if len(txt) > 0 :
            tr_t.append(txt)
    tbody_t.append(tr_t)

# %%
with open('ccmt_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(th_list)
    # write multiple rows
    writer.writerows(tbody_t)

# %%



