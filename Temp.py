# YOU NEED CHROME DRIVER IN YOUR PATH ENVIRONMENT VARIABLE FOR THIS PROGRAM TO WORK
# Find what the tempature is
# Usage: temp.py "location" seconds
# Example: temp.y "Portland Oregon" 40
#  > Would get weather data for Portland Oregon every 40 seconds.

import pandas as pd
from splinter import Browser
import sys, time, datetime

def GetData(url, Location):
    browser = Browser('chrome')
    browser.driver.set_window_size(1000,800)
    browser.visit(url)
    
    #Temps
    Fahrenheit = '//*[@id="wob_tm"]'
    Celsius = '//*[@id="wob_ttm"]'
    
    Temperature_data = []
    
    # Get fahrenheit temperature
    Fahrenheit_data = browser.find_by_xpath(Fahrenheit).text.encode('utf8')
    
    # Get celsius temperature
    ClickIt = browser.find_by_xpath('//*[@id="wob_d"]/div/div[1]/div/div[2]/a[2]/span')
    ClickIt.click()
    Celsius_data = browser.find_by_xpath(Celsius).text.encode('utf8')
    
    # When I am collecting the data
    When = datetime.datetime.now().strftime("%x %I:%M %p") #%x Locale's date, %I hour format in 12s, %M is minutes and %p tells me PM or AM
    
    # Get other details
    Percipitation_data = browser.find_by_xpath('//*[@id="wob_pp"]').text.encode('utf8')
    Humidity_data = browser.find_by_xpath('//*[@id="wob_hm"]').text.encode('utf8')
    # Windspeed_data = browser.find_by_xpath('//*[@id="wob_ws"]').text.encode('utf8') Right now windspeed element won't load..
    Description_data = browser.find_by_xpath('//*[@id="wob_dc"]').text.encode('utf8')
    
    Temperature_data.append((Location, When, Fahrenheit_data, Celsius_data, Percipitation_data, Humidity_data, Description_data))
    
    # Get the data in Pandas format
    df = pd.DataFrame(data=Temperature_data, columns=["Location" ,"Time" ,"Fahrenheit", "Celsius", "Percipitation %", "Humidity" , "Description"])
    
    # Add to file
    df.to_csv("temperature.csv", mode='a', header=False)
    browser.quit()

def main():
    Location = ""
    delay = 10000
    
    if(len(sys.argv) > 1):
        url = "https://www.google.com/search?safe=strict&ei=21kPWruVLdiojwOm1IL4Dg&q=" + str(sys.argv[1]) + " temperature"
        Location = str(sys.argv[1])
        if(len(sys.argv) > 2):
            delay = int(sys.argv[2])
    else:
        url = "https://www.google.com/search?safe=strict&ei=21kPWruVLdiojwOm1IL4Dg&q=temperature"
        Location = "Local"
    
    print("Running program every %s seconds,  To stop the program press control+c" % (str(delay)))
    
    try:
    
        while True:
        
            GetData(url, Location)
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("Thank you for running this program, exiting now")
    
    # Exit out of program
    exit()



main()
