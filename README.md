# Weather-Info-Grabber
**How to install**

## 1. Install Dependencies**
Firstly, make sure in whichever virtual environment you are using you install the following libraries.
You can install these libaries with the following pip commands.
```
pip install pandas
pip install splinter
```
*If you're getting the "module not found error" it's because your python doesn't have these libraries.*

## 2. Install chrome driver

Since my program uses Splinter instead of urllib2 or requests you need a driver to use the browser.
My program is tailored to use chrome so you need to install the chrome driver (here)[https://chromedriver.storage.googleapis.com/2.33/chromedriver_win32.zip].

If the above link doesn't work you can use this (one)[https://chromedriver.storage.googleapis.com/index.html?path=2.33/]

## 3. PUT THE chromedriver.exe IN THE SAME DIRECTORY

**Place the chromedriver.exe in the same directory as your Temp.py so that you won't get dumb errors!.**

*Or alternatively, you can put it in your path environmental variable if you're savvy enough to know how to do so.*

## 4. Usage

Now create a Temp.py with my github code or get the zip file and extract it in your working directory.
At this point you should be able to run the program via the commandline like so:
![Image here](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/Codeee.PNG)
**This example will collect Wheather data from New York every one hundred seconds and then put the data into a csv file.**
![Another Image](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/Working.PNG)
**If all is well your console might look something like this after a couple minutes.**

## COMMON ERRORS
