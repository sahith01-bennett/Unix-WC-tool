import pathlib


def size_of_file(path:str):
    """
    Returns the size of the file at the given path in bytes.

    Parameters
    ----------
    path : str
        The path to the file.

    Returns
    -------
    int
        The size of the file in bytes if the file exists.
    None
        If the file does not exist, prints an error message and returns None.
    """
    file = pathlib.Path(path)
    if(file.is_file()==True): 
        return (file.stat().st_size) 
    else:
        print(f"No file exsists at {path}") 

def number_of_lines(path:str):
    """
    Returns the number of lines in the file at the given path.

    Parameters
    ----------
    path : str
        The path to the file.

    Returns
    -------
    int
        The number of lines in the file if the file exists.
    None
        If the file does not exist, prints an error message and returns None.
    """
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
    """
    Returns the number of words in the file at the given path.

    Parameters
    ----------
    path : str
        The path to the file.

    Returns
    -------
    int
        The number of words in the file if the file exists.
    None
        If the file does not exist, prints an error message and returns None.
    """
    file = pathlib.Path(path)
    if (file.is_file() == True):
        with file.open(mode='r',encoding="utf-8") as f:# file is opened in read mode and using UTF-8 for encoding and decoding of the file
            text = f.read().split() # f.read() returns a string and spliting tthe string when ever there is whitespace
        return(len(text))
    else:
        print(f"No such file exsists at {path}")

def number_of_chars(path:str):
    """
    Returns the number of characters in the file at the given path.

    Parameters
    ----------
    path : str
        The path to the file.

    Returns
    -------
    int
        The number of characters in the file if the file exists.
    None
        If the file does not exist, prints an error message and returns None.
    """
    file = pathlib.Path(path)
    n_chars = 0
    if (file.is_file() == True):
        with file.open(mode='r',encoding="utf-8") as f:
            for word in f:
              n_chars += len(word) 
        return(n_chars)
    else:
        print(f"No such file exsists at {path}")



    



