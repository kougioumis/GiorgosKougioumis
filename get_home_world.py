import requests
import requests_cache
import urllib.parse
import datetime
import re
import main
##if the --world param is used we call this
def get_home_world(results,i):


    url = results[i]['homeworld']
    print("------------")
    print("Homeworld")
    print("------------")

    pagenum = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", url) #gives the page number

    homeworlRequestcahce = requests.get(url)
    homeworlRequest = homeworlRequestcahce.json()

    main.cachetrack(int(pagenum[0]), 2)                                      #request - cachingtraking



    print("Name: " + homeworlRequest['name'])
    print("Population: " + homeworlRequest['population'])


    if (homeworlRequest['orbital_period']!='unknown'):
        years = int(homeworlRequest['orbital_period']) / 365            #here for error exception
        years = round(years, 2)

        if (homeworlRequest['rotation_period']!='unknown'):
            days = int(homeworlRequest['rotation_period']) / 24
            days = round(days, 2)                                        #here for error exception

            print(f"On " + homeworlRequest['name'] + ", 1 year on Earth is ", years, "years and 1 day", days, "days")

    else:
        print(f"This system Unkown to me is")   #the exception





