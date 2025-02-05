import os
import pathlib

parent = pathlib.Path(__file__).parent.resolve()


watchlist = []

def read_one(id):
    with open(f"watchlist/{id}.txt", 'r') as target:
        content = target.read().split("\n")
        content[2] = content[2].split(" ")[0]
        content[3] = content[3].split(" ")[0]
        content.append(id)
        return content

def readAll():
    targets = os.listdir(f"{parent}/watchlist")
    targets.remove("control.txt")

    if targets == None:
        return

    watchlist = []
    for t in targets:
        with open(f"watchlist/{t}", "r") as targetfile:
            content = targetfile.read().split("\n")
            watchlist.append(
                (
                    content[0],
                    content[1],
                    content[2].split(" ")[0],
                    content[3].split(" ")[0],
                    content[4],
                    t.split(".")[0]
                )
            )
    return watchlist