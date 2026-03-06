import os
import sys
import json
import platform
from datetime import date, timedelta
import argparse

if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"

def show_menu():
    print("----------Choose desired option----------")
    print("1. Add a point to record")
    print("2. Number of point during specific day")
    print("3. Number of points this week")
    print("4. Number of points this month")
    print("5. Number of points this year")
    print("6. Total number of points and starting day")
    print("7. Exit")
    return input("Enter the number of desired option(1-7):")

def string_to_date(orig: str):
    date_list = orig.split("-")
    for i in range(len(date_list)):
        date_list[i] = int(date_list[i])
    return date(date_list[0], date_list[1], date_list[2])

def create_record(filename):
    if not os.path.exists("records"):
        os.mkdir("records")
    if os.path.exists(f"records{slash}{filename}.json"):
        print(
            "Record file for this addiction already exists. Use \"open\" option to edit it or create another file"
        )
        return
    starter_date = date.today()
    header = {str(starter_date): 0}
    with open(f"records{slash}{filename}.json", "w") as f:
        json.dump(header, f)
    return

def open_record(record):
    while True:
        choice = show_menu()
        if choice == "1":
            with open(f"records{slash}{record}.json", "r") as f:
                info = json.load(f)
            current_date = date.today()
            if info.get(str(current_date)) is None:
                info[str(current_date)] = 1
            else:
                info[str(current_date)] += 1
            with open(f"records{slash}{record}.json", "w") as f:
                json.dump(info, f)
        elif choice == "2":
            with open(f"records{slash}{record}.json", "r") as f:
                info = json.load(f)
            needed_date = input("Enter your wanted date using next format: \"1970-12-31\"   ")
            date_info = info.get(needed_date)
            if date_info is None:
                print("Records do not contain such date. You either won that day or made a mistake right now. Try again just to be sure")
            else:
                print(f"Number of defeats during {needed_date}: {info[needed_date]}")
            print("-----------------------------------------------")
        elif choice == "3":
            with open(f"records{slash}{record}.json", "r") as f:
                info = json.load(f)
            current_date = date.today()
            start_of_week = current_date - timedelta(7)
            defeats = 0
            for key in info.keys():
                day = string_to_date(key)
                if day > start_of_week and day <= current_date:
                    defeats += info[key]
            print(f"Number of defeats this week: {defeats}")
            print("-----------------------------------------------")
        elif choice == "4":
            with open(f"records{slash}{record}.json", "r") as f:
                info = json.load(f)
            current_date = date.today()
            start_of_month = date(current_date.year, current_date.month, 1)
            defeats = 0
            for key in info.keys():
                day = string_to_date(key)
                if day > start_of_month and day <= current_date:
                    defeats += info[key]
            print(f"Number of defeats this month: {defeats}")
            print("-----------------------------------------------")
        elif choice == "5":
            with open(f"records{slash}{record}.json", "r") as f:
                info = json.load(f)
            current_date = date.today()
            start_of_year = date(current_date.year, 1, 1)
            defeats = 0
            for key in info.keys():
                day = string_to_date(key)
                if day > start_of_year and day <= current_date:
                    defeats += info[key]
            print(f"Number of defeats this year: {defeats}")
            print("-----------------------------------------------")
        elif choice == "6":
            with open(f"records{slash}{record}.json", "r") as f:
                info = json.load(f)
            defeats = 0
            days = list(info.keys())
            start_day = min(days)
            for key in info.keys():
                defeats += info[key]
            print(f"Total number of defeats: {defeats}")
            print(f"Starting day: {start_day}")
            print("-----------------------------------------------")
        elif choice == "7":
            print("Finishing the application...")
            break
        else:
            print("You've entered wrong number or symbol. Please choose again.")
            print("-----------------------------------------------")
    return

def delete_record(filename):
    if os.path.exists(f"records{slash}{filename}.json"):
        os.remove(f"records{slash}{filename}.json")
        print("Record has been deleted successfully")
    else:
        print("Such record does not exist")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--create", 
        dest="create", 
        help="Create new addiction record"
        )
    parser.add_argument(
        "-o", "--open", 
        dest="open", 
        help="Edit or read info about your current addiction"
        )
    parser.add_argument(
        "-d", "--delete", 
        dest="delete",
        help="Delete file about your addiction"
        )
    args = parser.parse_args()

    if len(sys.argv) <= 2:
        print("Please choose option for working with file")
        print("Type --help argument if you want to know about available options")
        return
    elif len(sys.argv) > 4:
        print("Please choose only one option to work with")
        return
    
    if args.create:
        create_record(args.create)
    elif args.open:
        open_record(args.open)
    elif args.delete:
        delete_record(args.delete)
    return

if __name__ == "__main__":
    main()
    