import main
import homeworld
import numpy as np
import urllib.parse
import requests
import homeworld
import os.path
import datetime
import requests_cache

timestamps = []
timestampsfinal = np.array(0)


def search_for_people(name,world):

    ## initialization propably can be removed but helps to get the pagenum for the loop ahead
    exitvar = [0,0,0,0,0,0,0,0,0,0]
    haveYouFountAnything = 0
    value=name
    people,cached,time = get_page(1)
    pageNun = get_number_of_pages(people)


    ## starts loading pages of the swapi
    for j in range (1,pageNun):

        people,iscached,time = get_page(j)
        results = people['results']

        #looks in the entries of every page for a much is the given string
        for i in range (0,len(results)):
            if value.casefold() in results[i]['name'].casefold():


                ## if a mach is found starts building the output var

                exitvar[0] = ("Name: " + results[i]['name'])
                exitvar[1] = ("Height: " + results[i]['height'])
                exitvar[2] = ("Mass: " + results[i]['mass'])
                exitvar[3] = ("Birth Year: " + results[i]['birth_year'])
                exitvar[4] = ("------------")

                haveYouFountAnything = 1


                ## if the --world parameter is used or the world box is checked
                if (world):
                    exitvar[5],exitvar[6],exitvar[7] = homeworld.get(results,i)
                    exitvar[8] = ("------------")


                    ## if the page is taken from the cache
                    if (cached):
                        for i in range (0,len(time)):
                            if (time[i] == j):
                                exitvar[9] = ("Cached "+time[i-1])
                                break
                    else:
                        return exitvar



                else:
                    ## if the page is taken from the cache
                    if (cached):
                        for i in range(0, len(time)):
                            if (time[i] == j):
                                exitvar[5] = ("Cached "+time[i-1])
                                break
                            else:
                                exitvar[5] = ("Cached " + time[0])
                        exitvar[6] = ("------------")
                        return exitvar
                    else:
                        return exitvar
    ## case nothing is found print error message
    if (haveYouFountAnything==0):
       exitvar[0] = ("The force is not strong within you")

    return exitvar

def get_page(page_num):

    ## time parameter to be used as timestamps
    time = datetime.datetime.now()
    time = time.strftime("%y-%m-%d %X.%f")


    ## request and responce
    endpoint = "https://swapi.dev/api/people/?"
    type = 'json'
    url = endpoint + urllib.parse.urlencode({"format": type, "page": page_num})

    json_data = requests.get(url)
    cached=json_data.from_cache
    json_data = json_data.json()


    ### code for clearing the cache
    if (page_num==-100):
        timestamps.clear()
        return json_data, cached,timestamps

    else:
        timestamps.append(time)
        timestamps.append(page_num)

        # gets the first time a page was writen in the db
        for i in range (1,len(timestamps),2):
            for j in range (i+2,len(timestamps),2):
                if (timestamps[i]==timestamps[j]):
                    timestamps.pop( j-1 )
                    timestamps.pop( j-1 )

    return json_data, cached, timestamps




#calculates the number of pages for the people json
def get_number_of_pages(peoplejson):

    if peoplejson.get('count')%10>1:
        numberOfPages = round(peoplejson.get('count')/10)+1
    else:
        numberOfPages = round(peoplejson.get('count')/10)
    return (numberOfPages)






