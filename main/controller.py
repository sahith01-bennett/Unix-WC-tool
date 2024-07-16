import model
import argparse
import sys


def ccwc():
    """
    This function parses command-line arguments to determine which properties
    of the file to count and print. It supports counting the number of lines,
    words, characters, and bytes in a file. If no specific property is requested,
    it prints the number of lines, words, and characters by default.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        help="take path of the file"
    )    

    parser.add_argument(
        "-c",
        "--byte",
        action="store_true",
        help="print the byte counts"
    )

    parser.add_argument(
        "-l",
        "--line",
        action="store_true",
        help="prints number of lines"
    )

    parser.add_argument(
        "-w",
        "--word",
        action="store_true",
        help="prints number of words"
    )

    parser.add_argument(
        "-m",
        "--char",
        action="store_true",
        help="prints number of characters"
    )


    args = parser.parse_args()

    path = args.path

   
    if (path.isspace()):
        print("please enter the path of the file")
        sys.exit()


    if (path == None):
        text = sys.stdin.read()
        ## still have to write code for the case where text of the file is given in input

    else:
        if not args.byte and not args.line and not args.word and not args.char:
            print(model.number_of_lines(path), end=" ")
            print(model.number_of_words(path), end=" ")
            print(model.number_of_chars(path), end=" ")
        else:
            if(args.byte):
                print(model.size_of_file(path), end=" ")

            if(args.line):
                print(model.number_of_lines(path), end=" ")

            if(args.word):
                print(model.number_of_words(path), end=" ")

            if(args.char):
                print(model.number_of_chars(path), end=" ")

        print(args.path)

        

if __name__ == "__main__":
    ccwc()
