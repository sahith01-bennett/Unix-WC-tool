import pathlib
# model.py contains the functions to calculate - 
# 1) size of the file - returns the size of file
# 2) number of lines in file - returns number of lines in the file
# 3) number_of words - retruns number of words in the file
# 4) number of chars - returns number of chars in the file
# All the function take the path of the file as an argument and print the respective results
# file is opened using Pathlib library

def size_of_file(path:str):
    file = pathlib.Path(path)
    if(file.is_file()==True): # checking if files exists or not
        return (file.stat().st_size) # st_size attribute give the size of the file in bytes, using end =" " wil makes sure things are printed in one line
    else:
        print(f"No file exsists at {path}") 

def number_of_lines(path:str):
    file = pathlib.Path(path)
    no_of_lines = 0
    if(file.is_file()==True):
        with file.open(mode='r' , encoding='utf-8') as f: # file is opened in read mode and using UTF-8 for encoding and decoding of the file
            for i in f.readlines(): #f.readlines() returns a list of lines in the file 
                no_of_lines+=1
        return(no_of_lines)
    else:
         print(f"No such file exsists at {path}")

def number_of_words(path:str):
    file = pathlib.Path(path)
    if (file.is_file() == True):
        with file.open(mode='r',encoding="utf-8") as f:# file is opened in read mode and using UTF-8 for encoding and decoding of the file
            text = f.read().split() # f.read() returns a string and spliting tthe string when ever there is whitespace
        return(len(text))
    else:
        print(f"No such file exsists at {path}")

def number_of_chars(path:str):
    file = pathlib.Path(path)
    n_chars = 0
    if (file.is_file() == True):
        with file.open(mode='r',encoding="utf-8") as f:
            for word in f:
              n_chars += len(word) # we calculate length of each word and add it to the n_chars variable
        return(n_chars)
    else:
        print(f"No such file exsists at {path}")



    



