# cscesearch
A web scraper to search in the faculty directory in the CSCE department at Texas A&amp;M using selenium and BeautifulSoup.

# Usage
To use, run FacultySearcher.py from a terminal. Required dependencies are selenium and BeautifulSoup.
Commands and arguments are as follow:

scrape [browser name]
Begins to scrape data using the browser installed on your machine specified. Supported browsers are Internet Explorer, Chrome, Microsoft Edge and Firefox. Run this before any other command.

url [name]:
Outputs the link to the webpage of a faculty member of name [name].

data[name]:
Outputs the raw text of the webpage of the faculty member of name [name].

search [keywords...]
Searches the entire directory of faculty and their webpages from scraped data to find matches of keywords and outputs a list of faculty in descending order of number of matches.

matches [name]:
Outputs the number of matches found in the webpage of the faculty member of name [name].

