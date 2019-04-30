from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import csv
import time


steamUrls = ['https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers',
             'https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers&page=2',
             'https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers&page=3',
             'https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers&page=4']


csvfile = open("bigSteamProject1", 'w', newline='', encoding='utf-8')
# make a new variable, c, for Python's CSV writer object -
c = csv.writer(csvfile)
c.writerow(['urls', 'price', 'title', 'details', 'genre'])



def doEverything():

    gameUrls = []
    temp_row= []

    for urls in steamUrls:
        cookies = { 'birthtime': '283993201', 'mature_content': '1' }
        r = requests.get(urls, cookies=cookies).text
        #This solution was found here: https://stackoverflow.com/questions/33603416/python-beautiful-soup-getting-past-steams-age-check
        html = urlopen(urls)
        soup = BeautifulSoup(r, 'html.parser')
        mainUrl = soup.find('div', {'id':'search_result_container'})
        theUrl = mainUrl.find_all('a', {'class': 'search_result_row'})
        for a in theUrl:
            gameUrls.append(a.get('href'))
            temp_row.append(a.get('href'))
        #for gameUrl in gameUrls:
            #html = urlopen(gameUrl)
            #soup = BeautifulSoup(html, 'html.parser')


    for price in gameUrls:
        cookies = { 'birthtime': '283993201', 'mature_content': '1' }
        r = requests.get(price, cookies=cookies).text
        html = urlopen(price)
        soup = BeautifulSoup(r, 'html.parser')
        try:
            mainPage = soup.find('div',{"class":"responsive_page_content"})
            moreContent = mainPage.find('div',{"class":"page_content_ctn"})
            #print(moreContent)
            #orgBunPrice = mainPage.find('div',{'class':'discount_original_price'})
            discBunPrice = mainPage.find('div',{'class':'discount_final_price'})
            #temp_row.append(orgBunPrice.get_text())
            temp_row.append(discBunPrice.get_text())
        except:
            pass
        try:
            mainPage = soup.find('div',{"class":"game_purchase_action"})
            #orgPrice = mainPage.find('div',{'class':'discount_original_price'})
            discPrice = mainPage.find('div',{'class':'discount_final_price'})
            #temp_row.append(orgPrice.get_text())
            temp_row.append(discPrice.get_text())
        except:
            pass
        try:
            mainPage = soup.find('div',{"class":"game_purchase_action"})
            price = mainPage.find('div',{'class':'game_purchase_price'})
            temp_row.append(price.get_text())
        except:
            pass

        time.sleep(1)

    for title in gameUrls:
        cookies = { 'birthtime': '283993201', 'mature_content': '1' }
        r = requests.get(title, cookies=cookies).text
        html = urlopen(title)
        soup = BeautifulSoup(r, 'html.parser')
        try:
            mainPage = soup.find('div', {"class": 'page_content'})
            for titles2 in mainPage.find('h2', {"class": 'pageheader'}):
                temp_row.append(titles2.get_text())
                #this code above is needed for getting the titles of bundles. For some reason they aren't the same tags.
        except:
            pass
        try:
            mainPage = soup.find('div',{"class":"responsive_page_content"})
            for title in mainPage.find_all("div", {"class":"apphub_AppName"}):
                temp_row.append(title.get_text())
        except:
            pass

    for deets in gameUrls:
        cookies = { 'birthtime': '283993201', 'mature_content': '1' }
        r = requests.get(deets, cookies=cookies).text
        gameDeets = []
        html = urlopen(deets)
        soup = BeautifulSoup(r, 'html.parser')
        mainPage = soup.find('div',{"class":"responsive_page_content"})
        for player in mainPage.find_all('div', {'class': 'game_area_details_specs'}):
            gameDeets.append(player.get_text())
        temp_row.append(gameDeets)


    for gameGenre in gameUrls:
        try:
            cookies = { 'birthtime': '283993201', 'mature_content': '1' }
            r = requests.get(gameGenre, cookies=cookies).text

            soup = BeautifulSoup(r, 'html.parser')
            mainPage = soup.find('div',{"class":"responsive_page_content"})
            genreBlock = mainPage.find('div', {'class': 'details_block'})
            genre = genreBlock.find('a').get_text()


            aList = [genre]
            genreNext = genreBlock.find('a')
            while True:
                if genreNext.next_sibling.next_sibling.name == 'a':
                    aList.append(genreNext.next_sibling.next_sibling.get_text())
                    genreNext = genreNext.next_sibling.next_sibling
                else:
                    break
            temp_row.append(aList)
        except:
            pass

    c.writerow(temp_row)
    time.sleep(1)
doEverything()
csvfile.close()
