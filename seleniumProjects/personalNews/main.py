from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 


website = "https://www.reddit.com/r/CoDCompetitive/"

options = Options()
options.add_experimental_option('detach',True) # keeps the browser from automatically closing.

# the driver can be downloaded from https://chromedriver.chromium.org/downloads
path_to_driver = '/Users/aman/Downloads/chromedriver' 
service  = Service(executable_path=path_to_driver)
driver = webdriver.Chrome(service = service,options=options)

driver.get(website)
