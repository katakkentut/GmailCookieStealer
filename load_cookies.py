import pickle
import undetected_chromedriver as uc
import time

if __name__ == '__main__':

    browser = uc.Chrome()
    browser.get(
        'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    cookies = pickle.load(open("cookies_Profile 1.pkl", "rb"))

    for cookie in cookies:
        cookie['domain'] = ".google.com"

        try:
            browser.add_cookie(cookie)

        except Exception as e:
            pass

    browser.get('https://mail.google.com/mail/u/0/#inbox')
    time.sleep(99999)

