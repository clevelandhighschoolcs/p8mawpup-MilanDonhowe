# Minimum.py - Detect changes in a website.
***(This was a high school assignment.)***

# Getting started
## .exe or .py
There are two methods of using my program, using chromedriver.exe and Minimum.exe or using the Minimum.py and chrome.exe with dependencies.

# Minimum.exe

## 1. Setup (.exe)

![Image of what to download](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/ExeDrive.PNG)

Download both the minimum executable and chromedriver executable.

![Image of what it should look like](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/ExeDirect.PNG)

Place them both into the same directory.

## 2. Usage (.exe)

```Minimum.exe [url] [seconds]```

Make sure to run the executable through the command line to pass it arguments.  
The first parameter will tell the program which url to monitor while the second parameter will set the interval (time between checks) for the program to operate on.

**Example**

![Example image here](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/UsageExe.PNG)



# Minimum.py

## 1. Setup (.py)
```pip install splinter```

Download the .py file **and** the chromedriver.exe.  (may require unzipping a file or two)

![Visual aid](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/PyDrive.PNG)

**Make sure to place both files into the same directory.**

![Visual aid](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/PypDrive.png)

## 2. Usage (.py)

The usage for the .py version is mostly identical to the .exe.

```Minimum.py [url] [seconds]```

Make sure to run the .py file through the command line to pass it arguments.  
The first parameter will tell the program which url to monitor while the second parameter will set the interval (time between checks) for the program to operate on.

![Visual aid](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/PypDrive.png)

# Built with
* [Python 2.7.14](https://www.python.org/downloads/)
* [Splinter 0.7.7](https://splinter.readthedocs.io/en/latest/)
* [chromedriver.exe 2.33](https://sites.google.com/a/chromium.org/chromedriver/)
* [Pyinstaller](http://www.pyinstaller.org/)

# Acknowledgements
A lot of this code which my program uses is derived from the wonderful article, ["Mastering Python Web Scraping: Get Your Data Back"](https://hackernoon.com/mastering-python-web-scraping-get-your-data-back-e9a5cc653d88) by the talented [Lauren Glass](https://hackernoon.com/@laurenjglass9).


