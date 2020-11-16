# retrieve data from the internet 

import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    print("result code: "+ str(weburl.getcode()))

    data = weburl.read()
    print(data) #html data for google.com home page

if __name__ == "__main__":
    main()