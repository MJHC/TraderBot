import json
import random
import os
import urllib.request
from time import sleep

money = 50000
holding = 0
lowest = 0
sellPrice = 0
tPrice = 0

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def getPrice():
   req = urllib.request.Request("https://api.nomics.com/v1/currencies/ticker?key=69c0eef305f3ec8c70dd75282b55633cb91e492b&ids=BTC")
   with urllib.request.urlopen(req) as response:
      data = json.loads(response.read())
      print("Coin " + data[0]['currency'] + " Current price: " + data[0]['price'])
      return float(data[0]['price'])

def buyCrypto(low, procent, coinPrice, profitMargin):
    global holding; global money; global sellPrice
    if money > 5000:
        power = money * procent
        if low >= coinPrice:
            holding += power / coinPrice
            money = money - power
            sellPrice = coinPrice * profitMargin

def testPrice():
    price = random.randint(45000, 52000)
    print("Coin: BTC Current price: " + str(price))
    return price


def sellCrypto(coinPrice):
    global sellPrice; global money; global holding
    if coinPrice >= sellPrice:
        money += coinPrice * holding
        holding = 0



runtime = 500
update = 1

#buyCrypto(49000, 0.5, testPrice(), 1.002)
#sleep(1)

for i in range(runtime):
    clearConsole()
    tPrice =  testPrice()
    buyCrypto(47000, 0.5, tPrice, 1.002)
    sellCrypto(tPrice)
    print("money: "+str(money) + "\nholdings: "+str(holding))
    sleep(update)