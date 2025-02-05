from watch import enjoei
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless=new")

def add_to_wl(link: str, title: str, target: str):
    browser = webdriver.Chrome(options=options)
    price = enjoei(link, browser, True)

    with open(f"watchlist/control.txt", "r") as control:
        content = control.read().split("\n")
        index = content[0]
        index = int(index) + 1

    content[0] = str(index)
    content.append(f"{index}: {title}")

    with open(f"watchlist/control.txt", "w") as control:
        for l in content:
            control.write(l+"\n")

    with open(f"watchlist/{index}.txt", "w") as newfile:
        newfile.write(f"{link}\n{title}\n{price[0]} CURRENT\n{target} TARGET\n{price[1]}")
    
    browser.close()
    return (link, title, price[0], target, price[1])