import webbrowser as wb
import os

def workauto():
    #code_path = 'C:\Program Files (x86)\\Dopamine\\dopamine.exe\\'
    #os.startfile(code_path)

    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = ("https://stackoverflow.com",
            "https://github.com/nabster1992",
            "https://google.com",
            "https://youtube.com")
    for url in URLS:
        wb.get(chrome_path).open_new_tab(url)


workauto()



