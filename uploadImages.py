from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.keys import Keys

from datetime import datetime

import os
import time
import pandas as pd

class Upload:

    def __init__(self, filename, column_name, img_format, admin_upload_url, master_user, master_pass, path_to_geckodriver,
    path_to_redo_button):

        self.filename = filename
        self.column = column_name
        self.img_format = img_format
        self.url = admin_upload_url
        self.user = master_user
        self.password = master_pass
        self.driver_path = path_to_geckodriver
        self.file_format = filename.split('.')[-1]
        self.redo_path = path_to_redo_button

        self.go()

    def go(self):

        if 'csv' in self.file_format:
            df = pd.read_csv(self.filename, sep=';', encoding='utf-8')

        else:
            df = pd.read_excel(self.filename) 

        driver = webdriver.Firefox(executable_path = self.driver_path)
        driver.get(self.url)
        
        date = str(datetime.now())[:-7].replace(':', '-')
        final_date = date[:10] + '_' + date[11:]

        fails_file = 'fails' + final_date + '.csv'
        wins_file = 'wins' + final_date + '.csv'

        f = open(fails_file, 'w', encoding='utf-8')
        g = open(wins_file, 'w', encoding='utf-8')

        username = driver.find_element_by_id('id_username')
        username.send_keys(self.user)

        password = driver.find_element_by_id('id_password')
        password.send_keys(self.password)

        login_button = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input')
        login_button.click()

        print('LOGGED IN')

        path = os.getcwd() + '\\images\\'

        for ind in df.index:
            try:
                id = df[self.column_name][ind]
                filepath = path + str(id) + self.img_format

                file_selector = driver.find_element_by_id('id_file')

                file_selector.send_keys(filepath)

                title = driver.find_element_by_id('id_title')

                title.send_keys(id)

                objectid = driver.find_element_by_id('id_objectid')
                    
                objectid.send_keys(id)

                print(ind+1, 'DONE')
                g.write(id+'\n')
            
            except (TimeoutException, NoSuchElementException, InvalidArgumentException) as e:
                print(ind+1, e)
                f.write(id+'\n')
            
            finally:
                redo = driver.find_element_by_xpath(self.redo_path).click()
                driver.implicitly_wait(10)
        
        f.close()
        g.close()
        driver.quit()

Upload('exemple.xls', 'objectid', 'jpg', 'http://127.0.0.1:8000/administrator/upload/upload/add/', 
'admin', 'admin_pass', 'C:\\Users\\Dylan\\Documents\\python\\geckodriver-v0.26.0-win64\\geckodriver.exe', 
'/html/body/div/div[3]/div/form/div/div/input[2]')