import os
import pandas as pd
import requests
from urllib.request import urlretrieve


class FbData():

    token = 'BqJKkJ78a8PHaSq46ZA98CSfxbTJmNtSKl0wKKfDlFjF4Tof0ZCZBJBhdcLcZBgZCVbC7V3elpBDGjdAoPOPumNP7rjR7WZBqDpTQZDZD'

    def get_photos(self):

        """
        Function that uses the graph api to get the links of the pictures and save them in csv file
        :return: None
        """

        photos = 'https://graph.facebook.com/v3.2/me?fields=photos{picture}&access_token='+self.token  #url that gives photos, their ids and links
        result = requests.get(photos)
        result = result.json()  # Converted results to Dictionary format for extracting wanted data
        df = pd.DataFrame(result['photos']['data'])
        del df['id']
        df.columns = ['Links']
        df.to_csv('location_to_save/abc.csv', index=False)
        print('Done writing links')


    def get_created_time(self):

        """
        Uses the graph api to get the created time of pictures and save them in the csv file
        :return:None
        """

        location_of_csv_file = 'location'
        df = pd.read_csv(location_of_csv_file)
        list_of_created_time = []
        status = 'https://graph.facebook.com/v3.2/me?fields=photos{created_time}&access_token='+self.token
        result = requests.get(status)
        result = result.json()
        l = len(result['photos']['data'])
        for i in range(l):
            list_of_created_time.append(result['photos']['data'][i]['created_time'])
        df['Created Time'] = list_of_created_time
        df.to_csv(location_of_csv_file, index=False)
        print("Done writing created time of pics")


    def download_images(self):

        """
        Reads the csv file and downloads the images from stored links to specified folder
        :return:None
        """

        location_of_csv_file  = 'location'
        df = pd.read_csv(location_of_csv_file)
        path_to_save_pictures = 'location_of_folder'
        if os.path.exists(path_to_save_pictures):
            os.rmdir('photos')
        os.makedirs('photos')
        links = list((df['Picture Link']))
        i = 0
        for link in links:
            urlretrieve(link, path_to_save_pictures + '/image' + str(i) + '.jpg')
            i+=1

        os.chdir('/home/nineleaps/PycharmProjects/Projectts')
        print('Downloaded Images')

ob1 = FbData()
ob1.get_photos()
ob1.get_created_time()
ob1.download_images()
