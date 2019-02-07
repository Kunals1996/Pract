import csv
import requests
from urllib.request import urlretrieve
import os
import pandas as pd

'''
The Graph API is the primary way to get data into and out of the Facebook platform. 
It's an HTTP-based API that apps can use to programmatically query data, post new stories, 
manage ads, upload photos, and perform a wide variety of other tasks.
'''

'''
An Access Token is a credential that can be used by an application to access an API. 
Access Tokens can be either an opaque string or a JSON web token.
 Access Tokens should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API.
'''

token = 'EAAg3lQGIA8UBAKZCIEwrxv1uydygtlVwSK9ipOdaZCq37OdGw1co80r3tszE5B5luJFGUbjER38TJiXRCiqQ0ZAzYEOOL8enTWeKZBIjKDNboDTG57OMI6XwliWmWDZAafefbBenJd0X55ncHwWBNFd9SSyX5mxx79YaOJ5ZBemOMeUtNkQFwsqZCjuy2pfA7jSEdJ1xTieQQZDZD'


class FbData():
    global token


    def get_photos(self):
        csv_file = open('fbpics.csv', 'w')  # opens csv file in write mode
        csv_writer = csv.writer(csv_file)  # a writer object to write on csv file
        csv_writer.writerow(['Picture Link'])
        photos = 'https://graph.facebook.com/v3.2/me?fields=photos{picture}&access_token='+token  #url that gives photos, their ids and links
        RESULT = requests.get(photos)
        RESULT = RESULT.json()  # Converted results to Dictionary format for extracting wanted data
        length_of_list_wanted = len(RESULT['photos']['data'])  # Length of list in dict that containg links
        for i in range(length_of_list_wanted):
            csv_writer.writerow([RESULT['photos']['data'][i]['picture']])  # Writing links to csv file
        csv_file.close()
        print('Done writing links')

    def get_created_time(self):
        location_of_csv_file = '/home/nineleaps/PycharmProjects/Projectts/fbpics.csv'
        df = pd.read_csv(location_of_csv_file)  # Reading csv file using pandas and creating data frame
        list_of_created_time = []
        status = 'https://graph.facebook.com/v3.2/me?fields=photos{created_time}&access_token='+token  # Url that gives created time of pics
        RESULT = requests.get(status)
        RESULT = RESULT.json()
        l = len(RESULT['photos']['data'])
        for i in range(l):
            list_of_created_time.append(RESULT['photos']['data'][i]['created_time'])
        df['Created Time'] = list_of_created_time
        df.to_csv(location_of_csv_file, index=False)  # Converting data frame to csv on wanted location
        print("Done writing created time of pics")

    def download_images(self):
        location_of_csv_file  = '/home/nineleaps/PycharmProjects/Projectts/fbpics.csv'
        df = pd.read_csv(location_of_csv_file)
        path_to_save_pictures = '/home/nineleaps/PycharmProjects/Projectts/photos'
        if os.path.exists(path_to_save_pictures): # If a folder for saving pic already exists, deletes it
            os.rmdir('photos')
        os.makedirs('photos')  # Makes a folder with name 'photos' to save pictues
        links = list((df['Picture Link']))
        i = 0
        for link in links:
            urlretrieve(link, path_to_save_pictures + '/image' + str(i) + '.jpg')  # Retrieving images from urls
            i+=1

        os.chdir('/home/nineleaps/PycharmProjects/Projectts')  #Going back from folder of saved pics (this step is not necessary)
        print('Downloaded Images')

ob1 = FbData()
ob1.get_photos()
ob1.get_created_time()
ob1.download_images()