
import requests_cache
import PySimpleGUI as sg
import search
import datetime
import main

def gui():

    valuesnew = []
    valuesnewnames = []
    sg.theme('DarkAmber')
    file_list_column = [
        [
            sg.Text("Looking for someone?",),
            sg.In(size=(25, 1), enable_events=True, key="parameter1"),
            sg.CBox('World', key='cb1'),
            sg.Button('Search',  key='Search',bind_return_key=True),
            sg.Button('Search History',  key='SearchHistory'),
            sg.Button('Results History',  key='ResultsHistory'),
            sg.Button('Clear Cache', key='ClearCache')],

        [sg.Listbox(values=[], enable_events=True, size=(100, 20), key="output")],
        [sg.Text("May the force be with you!")]
    ]

    layout = [[sg.Column(file_list_column,element_justification='c')]]
    window = sg.Window("SWAPI",layout, icon='images/swapi.ico')


    # Run the Event Loop
    while True:
        event, values = window.read()

        if event == "Search":

            timeofsearch = datetime.datetime.now()
            timetimeofsearch = ("You did that search at: " + timeofsearch.strftime("%y-%m-%d %X.%f"))
            divisionstr = ("------------")
            valuesnewnames.append(values["parameter1"])
            values = search.search_for_people(values["parameter1"], values["cb1"])

            # remove not used fields
            for i in range(len(values)-1, 0, -1):
                if (values[i] == 0):
                    values.pop(i)

            # implements an append to a list so that we can keep track of the history
            for i in range( 0,len(values)):
                valuesnew.append(values[i])

            #keeps the names features in the searches a timestamp for every search and a division string to be used later

            #valuesnewnames.append(values[0])
            valuesnew.append(timetimeofsearch)
            valuesnew.append(divisionstr)
            #values.append(timetimeofsearch)
            #values.append(divisionstr)

            window["output"].update(values)

        if event == "ResultsHistory":
            window["output"].update(valuesnew)


        if event == "SearchHistory":
            window["output"].update(valuesnewnames)


        if event == "ClearCache":

            ##clear cache precedure makes zero all tables and gives an output


            requests_cache.clear()
            values["parameter1"] = ['Cache cleared', 'With you the force is']
            values = values["parameter1"]
            valuesnew = []
            valuesnewnames = []

            ## get_page(-100) is a unique entry for get_page to initialize values of timestamps table that is used for caching
            search.get_page(-100)
            window["output"].update(values)

        if event == sg.WIN_CLOSED:
            requests_cache.clear()
            break

    window.close()