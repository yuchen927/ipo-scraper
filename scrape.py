import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def fetch():
    url = 'https://www.iposcoop.com/ipo-calendar/'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.select('table tr')
    data = []
    for tr in rows[1:]:
        cols = [td.get_text(strip=True) for td in tr.find_all('td')]
        if cols:
            data.append(cols)
    headers = [th.get_text(strip=True) for th in soup.select('table tr th')]
    df = pd.DataFrame(data, columns=headers)
    fname = f"ipos_{datetime.utcnow().strftime('%Y%m%d')}.csv"
    df.to_csv(fname, index=False)
    print(f"Exported {fname}")

if __name__=="__main__":
    fetch()
