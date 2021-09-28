from bs4 import BeautifulSoup
import requests
import lxml
import mechanize
import datetime
import re

BITCOIN_INCEPTION_DATE = datetime.date(2009, 1, 3)

url = 'https://www.amazon.de/'
usr = 'dominiklimbach@rocketmail.com'
pwd = 'Q25.Free-XA'


