import os
import sys
import json
import platform
from datetime import date
import argparse

if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"

def show_menu():
    print("----------Choose desired option----------")
    print("1. Add a point to record")
    print("2. Number of point during specific day")
    print("3. Number of points last week")
    print("4. Number of points last month")
    print("5. Number of points last year")
    print("6. Total number of points")
    print("7. Exit")
    return input("Enter the number of desired option(1-7):")

def create_record(filename):
    if not os.path.exists("records"):
        os.mkdir("records")
    if os.path.exists(f"records{slash}{filename}.json"):
        print(
            "Record file for this addiction already exists. Use \"open\" option to edit it or create another file"
        )
        return
    starter_date = date.today()
    header = {"Starting day": str(starter_date)}
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
        elif choice == "7":
            print("Finishing the application...")
            break
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
    