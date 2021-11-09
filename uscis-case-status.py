'''
DISCLAIMER: 
Created for personal purposes to check statuses for limited number of cases.
When you run this code, you assume all the responsibility!
Dont abuse government systems! God knows the architecture it is running on..
'''

import requests
from bs4 import BeautifulSoup

DATA_DIR = './data'
USCIS_URL = 'https://egov.uscis.gov/casestatus/mycasestatus.do'

def read_input_file(filename: str) -> list:
    pass

def parse_uscis_page(url: str, casenum: str = None, neighbor: int = 0) -> str:
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup
    

def send_email(emails: list) -> bool:
    pass

def send_text(mobiles: list) -> bool:
    pass

def archive_results(filepath: str) -> bool:
    pass

# Program Starts here
data = parse_uscis_page(USCIS_URL)
print(data)