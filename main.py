
import sys
import requests_cache
import datetime
import grafics
import search

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



### main request called to get the json file and starts the caching



if __name__ == '__main__':




    requests_cache.install_cache('demo_cache')
    time = datetime.datetime.now()
    time = time.strftime("%y-%m-%d %X.%f")

    #print(len(sys.argv))
    if (len(sys.argv)==1 ):
        grafics.gui()
        requests_cache.clear()

    elif(len(sys.argv)==2):
        if(sys.argv[1]=='gui'):
            grafics.gui()
            requests_cache.clear()

        elif(sys.argv[1]=='-cc'):
            requests_cache.clear()
        else:
            print('Missing Arguments')


    else:
        if (len(sys.argv)==4 and sys.argv[3]=='--world') :
            consolog=search.search_for_people(sys.argv[2], True)
            for i in range(0,len(consolog)):
                if consolog[i]!=0:
                    print(consolog[i])


        else:
            consolog=search.search_for_people(sys.argv[2], False)
            for i in range(0, len(consolog)):
                if consolog[i] != 0:
                    print(consolog[i])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#number of pages in JSON feed


