# This is a sample Python script.
import json

import requests

import requests
import requests_cache
import urllib.parse
import datetime
import re
import numpy as np
import get_home_world
import timedelta
import os
import sqlite3
import sys  #############################################################

import sqlite3
from sqlite3 import Error

import tkinter as tk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

timestamps = []
timestampsfinal = np.array(0)


def cachetrack(pagenum,level):



    time = datetime.datetime.now()
    time = int(time.strftime("%f"))

    timestamps.append(time)
    timestamps.append(pagenum)
    timestamps.append(level)

def get_time():
    time = datetime.datetime.now()
    time = time.strftime("%c")
    #print(time)
    return time






### main request called to get the json file and starts the caching

def get_page(page_num):

    time = datetime.datetime.now()
    time = time.strftime("%c")

    endpoint = "https://swapi.dev/api/people/?"



    type = 'json'

    url = endpoint + urllib.parse.urlencode({"format": type, "page": page_num})


    #requests_cache.install_cache('demo_cache')


    json_data = requests.get(url)
    iscached =json_data.from_cache
    #
    json_data = json_data.json()
    # if not (iscached):
    #     timestamps.append(time)
    #
    # else:
    #     #print(timestamps)
    #     print('1')



    return json_data, iscached,timestamps




#calculates the number of pages for the people json so we can know how deep we look and handle errors
def get_number_of_pages(peoplejson):

    if peoplejson.get('count')%10>1:
        numberOfPages = round(peoplejson.get('count')/10)+1
    else:
        numberOfPages = round(peoplejson.get('count')/10)
    return (numberOfPages)


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'demo_cache.sqlite3')





###
def search_for_people():

    haveYouFountAnything = 0
    world=True ######
    value = input("What are you looking for Jedi:")
    people,iscached,time = get_page(1)
    pageNun = get_number_of_pages(people) #propably can be removed



    for j in range (1,pageNun):

        people,iscached,time = get_page(j)
        results = people['results']


        for i in range (0,len(results)):
            if value.casefold() in results[i]['name'].casefold():
                print()
                print("Name: " + results[i]['name'])
                print("Height: " + results[i]['height'])
                print("Mass: " + results[i]['mass'])
                print("Birth Year: " + results[i]['birth_year'])
                #print("Birth Year: " + results[i]['created'])

                haveYouFountAnything = 1
                if (world==True):
                    get_home_world.get_home_world(results,i)
                    if (iscached):
                        if(len(time)>1):
                            print(time[0])
                            print("------------")
                            print("This entry is cached",time)
                elif (iscached):

                    print("------------")
                    print("This entry is cached", time)

    if (haveYouFountAnything==0):
       print("The force is not strong in you")



if __name__ == '__main__':

    requests_cache.install_cache('demo_cache')
    time = datetime.datetime.now()
    time = time.strftime("%c")

    while(1):
        search_for_people()

        #requests_cache.clear()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#number of pages in JSON feed


