import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import json

def scrape_faculty(browser):
    if(browser == 'Firefox'):
        driver = webdriver.Firefox()
    elif(browser == 'Chrome'):
        driver = webdriver.Chrome()
    elif(browser == 'Edge'):
        driver = webdriver.Edge()
    elif(browser == 'IE'):
        driver = webdriver.Ie()

    try:
        driver.get('https://engineering.tamu.edu/cse/profiles/index.html')
    except:
        print('Error: Browser is not supported')

    #page = requests.get('https://engineering.tamu.edu/cse/profiles/index.html')
    #driver.close()

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    faculty_directory = soup.find(class_='directory profile-list')
    faculty_profiles = faculty_directory.find_all('a')
    faculty_urls = {}

    faculty_root_dir = 'https://engineering.tamu.edu'

    for profile in faculty_profiles:
        #print('Profile: ',profile)
        span = profile.find_all('span')
        href = profile.get('href')
        #print('href: ', href)
        #print('Span: ',span)
        if(len(span) > 0):
            print('Name: ',span[0].contents[0])
            print('URL: ', faculty_root_dir + href)
            faculty_urls[span[0].contents[0]] = faculty_root_dir + href
        #print()

    #driver = webdriver.Firefox()

    faculty_data = {}

    for name in faculty_urls.keys():
        driver.get(faculty_urls[name])
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        education = soup.find('div', {'id': 'educationbackground'})
        research = soup.find('div', {'id': 'researchinterest'})
        awards = soup.find('div', {'id': 'awards'})
        publications = soup.find('div', {'id': 'publications'})

        items = [education, research, awards, publications]

        profile_str = name+'\n'

        for item in items:
            try:
                item_str = str(item.contents[3])[9:] #As to get rid of class tag
                #print(item_str)
                #item_str = re.sub(r'<?[/\\]?(br|p|ul|hl|li|="(no-bullets)?")>', '', item_str)
                item_str = re.sub(r'[</=]+[\w"\-_]+>', '', item_str)
                item_str = re.sub(r'amp;','',item_str)
                #print(item_str)
                profile_str += item_str.strip('\n')
            except:
                pass

        #print(profile_str)
        #print('--------------------------')
        faculty_data[name] = profile_str
        faculty_data[name+'_url'] = faculty_urls[name]


    driver.close()

    faculty_json = json.dumps(faculty_data)
    #print(type(faculty_json))
    #print(faculty_json)

    with open('faculty_data.json', 'w') as file:
        file.write(faculty_json)

if __name__ == '__main__':
    scrape_faculty('Firefox')