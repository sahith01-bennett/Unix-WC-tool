import pathlib
import sys

def size_of_file(path:str):
    file = pathlib.Path(path)
    if(file.is_file()==True):
        print(file.stat().st_size)
    else:
        print(f"No file exsists at {path}")

def number_of_lines(path:str):
    file = pathlib.Path(path)
    no_of_lines = 0
    with file.open(mode='r' , encoding='utf-8') as f:
        for i in f.readlines():
            no_of_lines+=1
    print(no_of_lines)

def number_of_words(path:str):
    file = pathlib.Path(path)
    if (file.is_file() == True):
        with file.open(mode='r',encoding="utf-8") as f:
            text = f.read().split()
            print(len(text))
    else:
        print(f"No file exsists at {path}")

def number_of_char(path:str):
    file = pathlib.Path(path)
    chars = 0
    if (file.is_file() == True):
        with file.open(mode='r',encoding="utf-8") as f:
            for word in f:
              chars += len(word)
        print(chars)
    else:
        print(f"No file exsists at {path}")

def get_number_of_characters(file):
    try:
        f = open(file, 'r')
        data = f.read()
        f.close()
        number_of_characters = len(data)
        return number_of_characters
    except FileNotFoundError:
        print('There is no such file or directory')
        sys.exit()


#339292

    


if __name__== "__main__":
    #size_of_file("/Users/bunny/projects/My_Project_Portfolio/Unix_CL_tool/test.txt")
    #number_of_lines("/Users/bunny/projects/My_Project_Portfolio/Unix_CL_tool/test.txt")
    #number_of_words("/Users/bunny/projects/My_Project_Portfolio/Unix_CL_tool/test.txt")
    number_of_char("/Users/bunny/projects/My_Project_Portfolio/Unix_CL_tool/big.txt")
    #file = pathlib.Path("/Users/bunny/projects/My_Project_Portfolio/Unix_CL_tool/test.txt")
    #print(get_number_of_characters(file))

