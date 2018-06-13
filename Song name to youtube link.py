from bs4 import BeautifulSoup
import requests
import urllib


def milo(): #Milo is the name of my dog :P

       User_input = input("Title of Youtube vid - ")

       words = User_input.split()

       lst = []    #Couldnt figure out a way to "add" words together, so worked my way around.
 
       lst.append('+'.join(words))
       print("https://www.youtube.com/results?search_query=" + lst[0])


       url = "https://www.youtube.com/results?search_query=" + lst[0]

       source_code = requests.get(url)
       plain_text = source_code.text
       soup = BeautifulSoup(plain_text, 'html.parser')
     
       for link in soup.findAll('a', {'class': 'yt-uix-tile-link'}): #Had troubles finding the classname.
           lst.append('https://www.youtube.com' + link.get('href'))
       print(lst[1]) # Probably much better ways to do this, but this was my work around.






milo()

