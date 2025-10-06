import os
import sys
import json
from datetime import date
import argparse


def create_record(filename):
    if not os.path.exists("records"):
        os.mkdir("records")
    if os.path.exists(f"records/{filename}.json"):
        print(
            "Record file for this addiction already exists. Use \"open\" option to edit it or create another file"
        )
        return
    starter_date = date.today()
    header = {"Starting day": str(starter_date)}
    with open(f"records/{filename}.json", "w") as f:
        json.dump(header, f)
    return

def open_record():
    print("Open")
    return

def delete_record(filename):
    if os.path.exists(f"records/{filename}.json"):
        os.remove(f"records/{filename}.json")
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
        open_record()
    elif args.delete:
        delete_record(args.delete)
    return

if __name__ == "__main__":
    main()
    