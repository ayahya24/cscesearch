import json
import re
import copy
import FacultyScraper
from selenium.common.exceptions import NoSuchWindowException

data = ''
with open('faculty_data.json', 'r') as file:
    data = file.read()

data = json.loads(data)
#print(data['Tanzir Ahmed'], data['Tanzir Ahmed_url'])

search_keywords = ['machine', 'learning']
case_sensitive = False

#use len(re.findall))

def search_matches(search_keywords, case_sensitive):
    matches = {}
    for name in data.keys():
        if name[-4:] == '_url':
            continue
        matches[name] = 0
        for kw in search_keywords:
            num_matches = len(re.findall(kw, data[name]))
            if(not case_sensitive):
                num_matches = len(re.findall(kw, data[name], flags=re.IGNORECASE))
            matches[name] += num_matches
        #print(name, matches[name])
    return matches

matches = search_matches(search_keywords, case_sensitive)

keys = list(matches.keys())
keys = sorted(keys, key=lambda name: matches[name], reverse=True)

#print(keys)

inputs = ''

while not inputs=='_exit':
    inputs = input('>>>')
    args = re.split(' ', inputs)
    cmd = args[0]
    name = ' '.join(args[1:])
    if(cmd=='url'):
        try:
            print(data[name+'_url'])
        except KeyError:
            print('Error: Name not found')
    if(cmd=='data'):
        try:
            print(data[name])
        except KeyError:
            print('Error: Name not found')
    if (cmd == 'matches'):
        try:
            print(matches[name])
        except KeyError:
            print('Error: Name not found')
    if(cmd == 'search'):
        search_keywords = args[1:]
        matches = search_matches(search_keywords, case_sensitive)
        keys = list(matches.keys())
        keys = sorted(keys, key=lambda name: matches[name], reverse=True)
        print(keys)
        if(matches[keys[0]] == 0):
            print('Warning: No matches were found for any search keywords')
    if(cmd=='scrape'):
        browser = args[1]
        try:
            FacultyScraper.scrape_faculty(browser)
            print('Updated data scraped from webpages')
        except NoSuchWindowException:
            print('Error: Window closed before scraping could finish')
        except IndexError:
            FacultyScraper.scrape_faculty('Firefox')