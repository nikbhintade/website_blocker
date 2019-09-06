import time
from datetime import datetime as dt


host_path = r"C:\windows\system32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('working hours...')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if str(redirect + " " + website) in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0, 0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("you can use it")

    time.sleep(5)
