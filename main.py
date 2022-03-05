from script import Stock_Price
from script import Today
import secret
import tweepy


#Setting variables:
selected_stocks = ['GOLL4.SA', 'PETR4.SA', 'ITUB4.SA', 'MGLU3.SA', 'VALE3.SA', 'WEGE3.SA', 'ABEV3.SA', 'BBDC4.SA', 'BOVA11.SA']

day = Today()

#Searching for stocks price
stock_price = Stock_Price(selected_stocks, day, day)

#Open tweepy
client = tweepy.Client(consumer_key=secret.api_key, 
                       consumer_secret=secret.api_key_secret,
                       access_token=secret.acess_token,
                       access_token_secret=secret.acess_token_secret)

#Tweeting
for n in range(0, len(selected_stocks)):
    txt = f'{selected_stocks[n]}: Cotação do dia {day}: {stock_price[n]:.2f}'
    respo = client.create_tweet(text=txt)
    print(respo)
   