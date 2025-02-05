import os
import pathlib

parent = pathlib.Path(__file__).parent.resolve()

def delete(id: str):
    name = id+".txt"
    os.remove(f"{parent}/watchlist/{name}")