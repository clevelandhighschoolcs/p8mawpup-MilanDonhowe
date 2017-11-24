# Weather-Info-Grabber installation tutorial

## 1. Install Dependencies
Firstly, boot up whichever virtual environment you are using and install the following libraries via the following pip commands:
```
pip install pandas
pip install splinter
```

## 2. Download chromedriver.exe

Since my program uses Splinter instead of urllib2 or requests you need a driver to use the browser.
My program is tailored to use chrome so you need to install the chrome driver [here](https://chromedriver.storage.googleapis.com/2.33/chromedriver_win32.zip).

If the above link doesn't work you can use this [one](https://chromedriver.storage.googleapis.com/index.html?path=2.33/) (get the win32 zip).

## 3. EXTRACT FROM ZIP AND PLACE THE chromedriver.exe IN THE SAME DIRECTORY

**Place the chromedriver.exe in the same directory as your Temp.py so that you won't get dumb errors!**

![Here should be a image](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/samedirectroy.png)

*Or alternatively, you can put it in your path environmental variable if you're savvy enough to know how to do so.*

## 4. Usage

Now create a Temp.py with my github code or get the zip file and extract it in your working directory.

The program can be run like so: 
```
Temp.py "Location here" [Seconds before running again]
```

At this point you should be able to run the program via the commandline like so:
![Image here](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/Codeee.PNG)

**This example will collect Weather data (windspeed, temperature, etc) from New York every one hundred seconds and then put the data into a csv file.**

**If all is well your console might look something like this after a couple minutes.**
![Another Image](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/Working.PNG)



***If you want to stop the program press ctrl+c.***

**To open/view the CSV file contents you will have to use something like Microsoft excel or Openoffice Calc.**

If you manage to pry open the csv file the contents should look something like this: 

![Csv contents image here](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/Coolio.PNG)

## COMMON ERRORS

**Module not found**:

If your module isn't getting picked up it's more than likely due to the fact you're not specifying your virtual environment specific version of python.  You can fix this just by adding "python " to the beginning of your command line argument like so:
![Image of commandline argument with python at beginning](https://github.com/MilanDonhowe/Weather-Info-Grabber/blob/master/Images/Sweettt.PNG)
If you continue having errors try re-running the pip commands.
 
**Permission for CSV not granted**:

I've run into this weird bug where I can't alter an existing csv file occasionally.  You can fix this just by deleting the csv file and the program will remake the csv file again and function properly.
 



