import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import os
import requests
from dateutil import rrule, relativedelta
from datetime import datetime, timedelta
import json

def json_dump(df, filename):
    # headers = ['Date(UTC)', 'Value']
    # json = {x: [], y: []}
    d = {'x': df.iloc[:,0].tolist(), 'y': df.iloc[:,1].tolist()}
    with open(f"{filename}.json", 'w') as f:
        f.write(f"{filename} = '{json.dumps(d)}'")

def plot_ethereum():
    # https://etherscan.io/chart/tx
    os.system('curl "https://etherscan.io/chart/tx?output=csv" > ethereum.csv')
    headers = ['Date(UTC)', 'Value']
    df = pd.read_csv('ethereum.csv', usecols=headers)
    def reFormat(dt):
        return datetime.strptime(dt, '%m/%d/%Y').strftime('%Y-%m-%d')
    dates = df.iloc[:,0].tolist()
    dates = list(map(reFormat, dates))
    df['Date(UTC)'] = dates

    df.set_index('Date(UTC)').plot()
    json_dump(df, 'ethereum')
    plt.show()

def plot_bitcoin():
    # https://www.blockchain.com/charts/n-transactions
    os.system('curl "https://api.blockchain.info/charts/n-transactions?timespan=all&sampled=true&metadata=false&cors=true&format=csv" > bitcoin.csv')
    headers = ['Date(UTC)', 'Value']
    df = pd.read_csv('bitcoin.csv', names=headers)
    # process time format
    def reFormat(dt):
        return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    dates = df.iloc[:,0].tolist()
    dates = list(map(reFormat, dates))
    df['Date(UTC)'] = dates
    
    json_dump(df, 'bitcoin')
    df.set_index('Date(UTC)').plot()
    plt.show()

def plot_tezos():
    # https://api.tzkt.io/#operation/Operations_GetTransactionsCount
    df = pd.read_csv('tezos.csv')
    if df.shape[0] == 0:
        record = False
        start = datetime(2019, 2, 1)
        last = 0
    else:
        record = True
        start = datetime.strptime(df['Date(UTC)'][df.shape[0]-1], '%Y-%m-%d') + relativedelta.relativedelta(months=2)
        last_date = datetime.strptime(df['Date(UTC)'][df.shape[0]-1], '%Y-%m-%d') + relativedelta.relativedelta(months=1)
        print(last_date)
        api = f'https://api.tzkt.io/v1/operations/transactions/count?timestamp.lt={last_date.strftime("%Y-%m-%d")}T00:00:00Z'
        response = requests.get(api)
        print(response.status_code)
        last = int(response.text)

    now = datetime.now()
    l = []
    for dt in rrule.rrule(rrule.MONTHLY, dtstart=start, until=now):
        api = f'https://api.tzkt.io/v1/operations/transactions/count?timestamp.lt={dt.strftime("%Y-%m-%d")}T00:00:00Z'
        response = requests.get(api)
        print(response.status_code)
        cnt = int(response.text)
        if(record):
            l.append([(dt - relativedelta.relativedelta(months=1)).strftime('%Y-%m-%d'), (cnt - last) / (dt - last_date).days])
        else:
            record = True
        last = cnt
        last_date = dt
    df2 = pd.DataFrame(l, columns=['Date(UTC)', 'Value'])
    df = pd.concat([df, df2], ignore_index=True)
    df.to_csv('tezos.csv', index=False)
    json_dump(df, 'tezos')

    df.set_index('Date(UTC)').plot()
    plt.show()

def plot_polygon():
    # https://polygonscan.com/chart/tx
    os.system('curl "https://polygonscan.com/chart/tx?output=csv" > polygon.csv')
    headers = ['Date(UTC)', 'Value']
    df = pd.read_csv('polygon.csv', usecols=headers)
    def reFormat(dt):
        return datetime.strptime(dt, '%m/%d/%Y').strftime('%Y-%m-%d')
    dates = df.iloc[:,0].tolist()
    dates = list(map(reFormat, dates))
    df['Date(UTC)'] = dates

    json_dump(df, 'polygon')
    df.set_index('Date(UTC)').plot()
    plt.show()


def main():
    plot_ethereum()
    plot_bitcoin()
    plot_tezos()
    plot_polygon()


if __name__ == '__main__':
    main()
