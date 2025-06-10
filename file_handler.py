import csv
import os
from datetime import datetime

CSV_FOLDER = 'data'
FILE_NAME = 'health.csv'
CSV_FILE = os.path.join(CSV_FOLDER,FILE_NAME)

def initialize_file():
    # Folder exists? Nahi to banao
    if not os.path.exists(CSV_FOLDER):
        os.makedirs(CSV_FOLDER)

    # File exists and has content? Nahi to header likho
    if not os.path.exists(CSV_FILE) or os.path.getsize ==0:
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name","Date", "Weight(kg)","Age", "Sleep(hours)", "Water(L)", "Workout(minutes)", "Notes"])


def save_entry(entry):
    with open(CSV_FILE,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(entry)

def read_all_entries():
    with open(CSV_FILE,'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data