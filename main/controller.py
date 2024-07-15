import model
import argparse
import sys


def ccwc():
    parser = argparse.ArgumentParser()

    parser.add_argument("path",nargs="?")

    parser.add_argument("-c",action="store_true")

    parser.add_argument("-l",action="store_true")

    parser.add_argument("-w",action="store_true")

    parser.add_argument("-m",action="store_true")


    args = parser.parse_args()

    path = args.path

    if(not path):
        print("please enter the path of the file")
        sys.exit()
    elif (path.isspace()):
        print("please enter the path of the file")
        sys.exit()


    if (path == None):
        text = sys.stdin.read()
        ## still have to write code for the file is give in input

    else:
        if(not args.c and not args.l and not args.w and not args.m):
            print(model.number_of_lines(path), end=" ")
            print(model.number_of_words(path), end=" ")
            print(model.number_of_chars(path), end=" ")
        else:
            if(args.c):
                print(model.size_of_file(path), end=" ")

            if(args.l):
                print(model.number_of_lines(path), end=" ")

            if(args.w):
                print(model.number_of_words(path), end=" ")

            if(args.m):
                print(model.number_of_chars(path), end=" ")

        print(args.path)
        

if __name__ == "__main__":
    ccwc()
