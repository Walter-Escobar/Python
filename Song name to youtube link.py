from bs4 import BeautifulSoup
import requests
import urllib


def milo():

       User_input = input("Title of Youtube vid - ")

       words = User_input.split()

       lst = []

       lst.append('+'.join(words))
       print("https://www.youtube.com/results?search_query=" + lst[0])


       url = "https://www.youtube.com/results?search_query=" + lst[0]

       source_code = requests.get(url)
       plain_text = source_code.text
       soup = BeautifulSoup(plain_text, 'html.parser')

       for link in soup.findAll('a', {'class': 'yt-uix-tile-link'}):
           lst.append('https://www.youtube.com' + link.get('href'))
       print(lst[1])


# the commented part wouldnt work
      # for link in soup.findAll('a',"video-title"):
           # song = link.get('href')
          # lst.append('https://www.youtube.com' + song)
          # print(lst[])



milo()

