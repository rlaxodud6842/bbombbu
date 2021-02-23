from bs4 import BeautifulSoup
import urllib
import asyncio
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

app = commands.Bot(command_prefix='뽐')

token = "ODA2ODkzODMzNzA3MDYxMjc4.YBwEcQ.QBIkAn9IvOi4sWOal-cnesD--xc"
calcResult = 0


@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("뽐검색")
    await app.change_presence(status=discord.Status.online, activity=game)


@app.command(name="검색")
async def _search_blog(ctx, *, go,):
    URL = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1&divpage=65'
    driver = webdriver.Chrome(executable_path='C:\chromedrive\chromedriver.exe')
    driver.get(url=URL)

    driver.implicitly_wait(time_to_wait=5)
    driver.find_element_by_css_selector('.input').send_keys(go)
    driver.find_element_by_css_selector('.input').send_keys(Keys.ENTER)
    ef = driver.current_url
    mooyaho = requests.get(ef)
    html = mooyaho.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('font', 'list_title')
    won = []
    del title[0]
    cnt = 0
    for i in title:
        won.append(i.get_text())

        for c in won:
            if cnt ==5:
                return

            await ctx.send(won)
            won = []
            cnt += 1
    driver.close()





app.run(token)
