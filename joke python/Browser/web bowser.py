import webbrowser
import os

with open('engine.txt') as setting:
    if 
    engine = input('Search engine preference: ')
def browse(inp):
    inp = input("Search--URL--Mail recepient--File-file_name--update-info-updatedinfo: ")
    inp = inp.lower()
    while inp != "":
        if "https://" in inp or "www." in inp or "file://" in inp:
            webbrowser.open_new_tab(inp)
        elif "https://" not in inp and "mail" not in inp and "www." not in inp and "update-info" not in inp and "file-open-" not in inp and "launch-" not in inp:
            webbrowser.open_new_tab(f"https://www.google.com/search?q={inp}")
        elif "-mail-" in inp.split()[0] and "-update-info-" not in inp:
            inp = inp.split("-")
            webbrowser.open_new_tab(f"mailto:{inp[1]}")
        elif "-update-info-" in inp:
            inpset = {inp}
            inplist = inp.split("-")
            print(inp[2])
        elif "file-open-" in inp:
            inp = inp.split("-")
            webbrowser.open_new_tab(f"file://{inp[2]}")
        elif "launch-" in inp:
            inp = inp.split("-")
            open(inp[1])
        else:
            print("AN UNKNOWN ERROR OCCURED")
        print("EXECUTED")
browse(inp)