# Unix WC Tool

## Overview

This tool is designed to provide various statistics about a file, such as the number of lines, words, characters, and the size of the file. It's a command-line utility that makes it easy to get quick insights into your files.

## Features

- **Count Lines**: Get the total number of lines in a file.
- **Count Words**: Calculate the total number of words in a file.
- **Count Characters**: Determine the total number of characters in a file.
- **File Size**: Check the size of the file.

## Installation

To use this tool, you need to have Python installed on your system. Clone this repository to your local machine using:

```bash
git clone https://github.com/sahith01-bennett/Unix-WC-tool.git
```
## Usage
To use the tool, run the controller.py(in main folder) script from your terminal with the desired options:
```bash
python controller.py [options] path_to_file
```

### Options
-m, --char : Prints the number of characters in the file.
-c, --byte : Prints the size of the file.
-l, --line : Prints the number of lines in the file.
-w, --word : Prints the number of words in the file.
If no options are provided, the tool will print the number of lines, words, and characters by default.


### Examples
Count the number of words in a file:

```bash
python controller.py -w path_to_your_file
```

Get the size of the file:
```bash
python controller.py -c path_to_your_file
```
