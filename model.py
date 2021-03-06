#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:49:31 2018

@author: nehabhomia
"""


import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0
counter = -1

def init():
    global entries, next_id, counter
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        counter = int(entries[-1]['MAX_ID'])
        next_id = counter + 1
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id, counter
    now = datetime.now()
    next_id = counter + 1
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "post_id": str(next_id)}
    counter = counter + 1
    entries.insert(0, entry) ## add to front of list
    
    try:
        entries[-1]['MAX_ID'] = str(next_id)
    except:
        entries.insert({'MAX_ID': str(next_id)})
    
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
        
def delete_entry(post_id):
    global entries
    for each_entry in entries:
        try:
            if each_entry['id'] == post_id:
                entries.remove(each_entry)
                break
        except:
            pass