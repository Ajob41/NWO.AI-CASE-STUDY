import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import itertools
import os

# main entry url to get the top 50 movies
url = 'https://www.imdb.com/feature/genre?ref_=fn_asr_ge'


req = requests.get(url)
content = BeautifulSoup(req.content, 'html.parser')
link_to_movie_genre = []
def get_movies_images(content):
    for image in content.find_all('img', {'class': 'pri_image'}):
        # get the parent node of the image element tag
        paren_of_image = image.parent
        # now get the href attribute of the parent node of image which is anchor tag
        href_anchor = paren_of_image.get('href')
        link_to_movie_genre.append(href_anchor)
get_movies_images(content)

# split the length of the link_to_movie_genre list into 3 parts

def split_list(link_to_movie_genre):
    split_list = []
    for i in range(0, len(link_to_movie_genre), 3):
        split_list.append(link_to_movie_genre[i:i+3])
    return split_list

split_list = split_list(link_to_movie_genre)


# iterate split_list and get the movie names by alt attribute of the image tag
first_movie_link = []
second_movie_link = []
third_movie_link = []
def get_movie_names(split_list):
    for i in split_list:
        first_movie_link.append(i[0])
        second_movie_link.append(i[1])
        third_movie_link.append(i[2])
get_movie_names(split_list)     

path = './Data/document.csv'

# iterate first_movie_link,second_movie_link,third_movie_link, in parallel 


for(a,b,c) in itertools.zip_longest(first_movie_link,second_movie_link,third_movie_link):
   url = a
   url2 = b
   url3 = c
   req = requests.get(url)
   req2 = requests.get(url2)
   req3 = requests.get(url3)
   content = BeautifulSoup(req.content, 'html.parser')
   content2 = BeautifulSoup(req2.content, 'html.parser')
   content3 = BeautifulSoup(req3.content, 'html.parser')
   for(i,j,k) in itertools.zip_longest(content.find_all('img', {'class': 'loadlate'}),content2.find_all('img', {'class': 'loadlate'}),content3.find_all('img', {'class': 'loadlate'})):
       # concatenate i j k 
         image_url = i.get('alt')
         image_url2 = j.get('alt')
         image_url3 = k.get('alt')
            # concatenate image_url,image_url2,image_url3
         image_url = image_url + ',' + image_url2 + ',' + image_url3
         # write image_url to csv file
         with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([image_url])
                