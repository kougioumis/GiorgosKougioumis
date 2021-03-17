import main
import get_home_world
import numpy as np
import urllib.parse
import requests
import get_home_world
import os.path
import datetime
import requests_cache

timestamps = []
timestampsfinal = np.array(0)


def search_for_people(name,world):


    exitvar = [0,0,0,0,0,0,0,0,0,0]
    haveYouFountAnything = 0
    value=name
    people,iscached,time = get_page(1)
    pageNun = get_number_of_pages(people) #propably can be removed



    for j in range (1,pageNun):

        people,iscached,time = get_page(j)
        results = people['results']


        for i in range (0,len(results)):
            if value.casefold() in results[i]['name'].casefold():

                # print()
                # print("Name: " + results[i]['name'])
                # print("Height: " + results[i]['height'])
                # print("Mass: " + results[i]['mass'])
                # print("Birth Year: " + results[i]['birth_year'])


                exitvar[0] = ("Name: " + results[i]['name'])
                exitvar[1] = ("Height: " + results[i]['height'])
                exitvar[2] = ("Mass: " + results[i]['mass'])
                exitvar[3] = ("Birth Year: " + results[i]['birth_year'])
                exitvar[4] = ["------------"]
                #print(exitvar)

                #print("Birth Year: " + results[i]['created'])

                haveYouFountAnything = 1
                if (world):
                    exitvar[5],exitvar[6],exitvar[7] = get_home_world.get_home_world(results,i)
                    #print(exitvar)
                    if (iscached):
                        if(len(time)>1):
                            #
                            # print("------------")
                            # print("This entry is cached",time[0])
                            exitvar[8] = ("------------")
                            exitvar[9] = ("This entry is cached "+time[0])
                            return exitvar
                elif (iscached):

                    # print("------------")
                    # print("This entry is cached", time[0])


                    exitvar[5] = ("This entry is cached " + time[0])
                    return exitvar

    if (haveYouFountAnything==0):
       #print("The force is not strong in you")
       exitvar[0] = ("The force is not strong in you")


    return exitvar

def get_page(page_num):

    time = datetime.datetime.now()
    time = time.strftime("%c")

    endpoint = "https://swapi.dev/api/people/?"



    type = 'json'

    url = endpoint + urllib.parse.urlencode({"format": type, "page": page_num})


    #requests_cache.install_cache('demo_cache')


    json_data = requests.get(url)
    iscached =json_data.from_cache
    requests_cache.core
    json_data = json_data.json()
    if not (iscached):
        timestamps.append(time)

    else:
        #print(timestamps)
        timestamps.append(time)
        #print('1')



    return json_data, iscached,timestamps




#calculates the number of pages for the people json so we can know how deep we look and handle errors
def get_number_of_pages(peoplejson):

    if peoplejson.get('count')%10>1:
        numberOfPages = round(peoplejson.get('count')/10)+1
    else:
        numberOfPages = round(peoplejson.get('count')/10)
    return (numberOfPages)


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'demo_cache.sqlite3')


