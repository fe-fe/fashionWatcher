from watch import enjoei
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pathlib

parent = pathlib.Path(__file__).parent.resolve()

options = Options()
options.add_argument("--headless=new")

def update_one(title, target, id):

    path = f"{parent}\\watchlist\\{id}.txt"
    with open(path, "r") as tfile:
        content = tfile.read().split("\n")
    
    with open(path, "w") as tfile:
        tfile.write(f"{content[0]}\n{title}\n{content[2]}\n{target} TARGET\n{content[4]}")
        

def update_all():
    
    targets = os.listdir(f"{parent}/watchlist")
    targets.remove("control.txt")
    results = []
    browser = webdriver.Chrome(options=options)
    for t in targets:
        with open(f"watchlist/{t}", "r") as targetfile:
            content = targetfile.readlines()
        
        current = enjoei(content[0], browser, False)
        content[2] = f"{current[0]} CURRENT\n"

        with open(f"watchlist/{t}", "w") as targetfile:
            for c in content:
                targetfile.write(c)
        content[2] = content[2].split(" ")[0]
        content[3] = content[3].split(" ")[0]
        results.append(content)
    return results