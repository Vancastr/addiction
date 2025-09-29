import os
import sys
import json
import datetime
import argparse


def create():
    print("Create")
    return

def open():
    print("Open")
    return

def delete():
    print("Delete")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--create", 
        dest="create", 
        help="Create new file about your addiction"
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
        create()
    elif args.open:
        open()
    elif args.delete:
        delete()
    return

if __name__ == "__main__":
    main()
    