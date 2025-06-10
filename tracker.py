from file_handler import save_entry, read_all_entries, CSV_FILE
from datetime import datetime
import csv


# 🟢 Function 1: Add new health entry
def add_new_entry():
    print("\n🔹 Enter your health data for today:")

    date = datetime.now().strftime("%d-%m-%y")
    name = input("🧑 Enter Your Name: ")
    weight = input("🏋️ Enter weight (kg): ")
    age = input("🏋️ Enter Your age: ")
    sleep = input("😴 Enter sleep hours: ")
    water = input("💧 Enter water intake (in liters): ")
    workout = input("🤸 Enter workout time (in minutes): ")
    notes = input("📝 Any notes (optional): ")

    entry = [name,date,weight,age,sleep,water,workout,notes]
    save_entry(entry)
    print("✅ Entry saved successfully!")

# 🔵 Function 2: View all entries
def view_all_entries():
    print("\n📋 Your Health Records:\n")

    data = read_all_entries()

    if len(data) <=1:
        print("⚠️ No data found.")
        return

    headers = data[0]
    rows = data[1:]

    # Column widths (adjust as needed)
    widths = [12,12,12,14,16,12,20,30] # 7 columns including "Name"

    # 🟩 Print header row
    for i, header in enumerate(headers):
        print(header.ljust(widths[i]), end=" | ")
    print()
    print("-" * (sum(widths) + len(widths) * 3))  # separator line

    # 🟦 Print each row

    for row in rows:
        for i, col in enumerate(row):
            print(col.ljust(widths[i]), end=' | ')
        print()

def search_by_date():
    print("\n🔎 Search Health Data by Date (format: DD-MM-YYYY)")
    search_date = input("📅 Enter date to search: ")

    data = read_all_entries()
    found = False

    for row in data[1:]: # skip headers.
        if row[0] == search_date:
            print("\n✅ Record found:")
        headers = data[0]
        for i in range(len(headers)):
            print(f"{headers[i]}:{row[i]}")
        found = True
        break
    if not found:
        print("❌ No record found for this date.")

def search_and_update():
    print("\n✏️ Update Entry")
    date = input("📅 Enter Date (e.g. 10-06-25): ")
    name = input("🧑 Enter Name: ")

    data = read_all_entries()
    headers = ["Name","Date", "Weight(kg)","Age", "Sleep(hours)", "Water(L)", "Workout(minutes)", "Notes"]
    widths = [12, 12, 12, 14, 16, 12, 20, 30]
    rows = data[1:]

    found = False

    for i, row in enumerate(rows):
        if row[0]==name and row[1]==date:
            print("\n✅ Record Found:")
            # for j in range(len(headers)):
            #     print(f"{headers[j]}:{row[j]}")
            print("\n✅ Record Found:")
            print("-" * (sum(widths) + 3 * len(widths)))
            for idx, cell in enumerate(row):
                print(headers[idx].ljust(widths[idx]), "|", cell)
            print("-" * (sum(widths) + 3 * len(widths)))

            # 🛠 Update options
            print("\n📝 Enter new values (press Enter to keep existing value):")

            for j in range(2,len(headers)): # skip Name and Date
                new_value = input(f"{headers[j]} {row[j]}: ")
                if new_value.strip() !="":
                    row[j] = new_value.strip()

            rows[i] = row
            found = True
            break

    if not found:
        print("❌ Record not found.")
        return
    # ✅ Rewrite the whole file with updated data

    with open(CSV_FILE,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(rows)

    print("✅ Record updated successfully.")




























