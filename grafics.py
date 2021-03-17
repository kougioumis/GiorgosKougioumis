
import requests_cache
import PySimpleGUI as sg
import search
import main

def gui():
    file_list_column = [
        [
            sg.Text("Looking for someone?"),
            sg.In(size=(25, 1), enable_events=True, key="parameter1"),
            sg.CBox('World', key='cb1'),
            sg.Button('Search', button_color=('white', 'Blue'), key='Search'),
            sg.Button('Clear Cache', button_color=('white', 'Red'), key='ClearCache'),

        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(80, 20), key="output"
            )
        ],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column)
        ]
    ]

    window = sg.Window("SWAPI", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()

        if event == "Search":
            # print(values["parameter1"],values["cb1"], event)
            # const = values["cb1"]

            values = search.search_for_people(values["parameter1"], values["cb1"])
            # remove not used fields
            for i in range(len(values) - 1, 0, -1):
                if (values[i] == 0):
                    values.pop(i)

            window["output"].update(values)

        if event == "ClearCache":
            requests_cache.clear()
            values["parameter1"] = ['Cache clear', 'The force is with you']
            values = values["parameter1"]
            window["output"].update(values)

        if event == sg.WIN_CLOSED:
            break

        # Folder name was filled in, make a list of files in the folder
        # if event == "parameter1":
        #     folder = values["parameter1"]
        #     try:
        #         # Get list of files in folder
        #         file_list = os.listdir(folder)
        #     except:
        #         file_list = []
        #
        #     fnames = [
        #         f
        #         for f in file_list
        #         if os.path.isfile(os.path.join(folder, f))
        #            and f.lower().endswith((".png", ".gif"))
        #     ]
        #     window["-FILE LIST-"].update(fnames)
        # elif event == "-FILE LIST-":  # A file was chosen from the listbox
        #     try:
        #         filename = os.path.join(
        #             values["-FOLDER-"], values["-FILE LIST-"][0]
        #         )
        #         window["-TOUT-"].update(filename)
        #         window["-IMAGE-"].update(filename=filename)
        #
        #     except:
        #         pass

    window.close()