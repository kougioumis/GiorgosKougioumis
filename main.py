

import requests_cache

import datetime


import grafics


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



### main request called to get the json file and starts the caching



if __name__ == '__main__':

    requests_cache.install_cache('demo_cache')
    time = datetime.datetime.now()
    time = time.strftime("%c")
    grafics.gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#number of pages in JSON feed


