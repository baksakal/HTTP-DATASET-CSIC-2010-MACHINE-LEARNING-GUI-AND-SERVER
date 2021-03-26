from train import *
import PySimpleGUI as sg

sg.theme('Default 1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Status:' , key='Text1',size=(40,1) ,justification='center' )],
            [sg.Text('Enter HTTP Request:'), sg.Multiline(size=(40,8))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Malicious HTTP Request Detector', layout,element_justification='c')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    a = values[0]
    a = a.strip()
    a = a.replace(" ","")
    a = a.rstrip()
    a = a.replace("\r", "")
    solv = []

    if a == '':
        window.Element('Text1').Update("Empty")
        window.Element('Text1').Update(text_color='gray')
    else:
        solv.append(a)
        solv = calcFeatures(solv,2)
        result = model.predict(scaler.transform(solv))

        if result[0] == 0:
            window.Element('Text1').Update("Safe")
            window.Element('Text1').Update(text_color='green')
        else:
            window.Element('Text1').Update("Malicious")
            window.Element('Text1').Update(text_color='red')

    values[0] = []
    a = ""
    solv = []
    
window.close()