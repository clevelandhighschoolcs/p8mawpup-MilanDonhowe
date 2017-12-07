from splinter import Browser
import sys, time

def main():

    if len(sys.argv) > 1:
        print "Welcome to bare minimum web page checking."
        url = sys.argv[1]
        if len(sys.argv) < 3:
            print "interval not stated please state now, default ten seconds."
            interval = 10
        elif len(sys.argv) == 3:
            interval = sys.argv[2]
        else:
            interval = sys.argv[2]
        check(url, interval)
    else:
        print "url and time was not given program defaulting to ten second interval, and cnn.com."
        interval = 10
        url = "http://www.cnn.com/"
        check(url, interval)
    
    
def check(url, interval):


    try:
        browser = Browser('chrome')
        browser.driver.set_window_size(1000,800)
        browser.visit(url)
        Original = len(browser.find_by_xpath('/html').text.encode('utf-8'))
        browser.quit()
        while True:
            print('To exit program ctrl+c')
            browser = Browser('chrome')
            browser.driver.set_window_size(1000,800)
            browser.visit(url)
            New = len(browser.find_by_xpath('/html').text.encode('utf-8'))
            if New != Original:
                print("PAGE CHANGED from %d bytes to %d bytes!" % (Original, New))
                Original = New
            else:
                print("No change detected")
            time.sleep(float(interval))
            browser.quit()
    except KeyboardInterrupt:
        print('Thank you for running this program exiting now.')
        sys.exit()

if __name__ == '__main__':
    main()
