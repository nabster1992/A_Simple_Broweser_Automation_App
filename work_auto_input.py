import webbrowser as wb
import os

def workauto():

    Chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    url = input('Enter name of the website to open: -')
    wb.get(Chrome_path).open(url)


workauto()



