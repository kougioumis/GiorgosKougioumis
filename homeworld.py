import requests
import re


def get(results,i):


    url = results[i]['homeworld']
    homeworlRequestcahce = requests.get(url)
    homeworlRequest = homeworlRequestcahce.json()

    # here for error exception
    if (homeworlRequest['orbital_period']!='unknown'):
        years = int(homeworlRequest['orbital_period']) / 365
        years = round(years, 2)
        # here for error exception
        if (homeworlRequest['rotation_period']!='unknown'):
            days = int(homeworlRequest['rotation_period']) / 24
            days = round(days, 2)

            return ("Name: " + homeworlRequest['name']),("Population: " + homeworlRequest['population']),('On ' + homeworlRequest['name'] + ', 1 year on Earth is '+ str(years)+ " years and 1 day "+ str(days)+ "days")
    else:
        return (f"This system Unkown to me is"),0,0




