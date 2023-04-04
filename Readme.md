# install on macos

clone the git repo to your Documents folder so you have ~/Documents/libgen/
install:

	`sh setup.sh`
	
The installation through setup.sh doesn't necessarily work. Best to navigate to the project directory and run `libgen.py <book name>` or fill list.text with the books you'd like to download and run `libgen.py` in your terminal

# usage

## download list
If you want to download from list of books add `list.txt` to the libgen folder with the list of book names, one book per line. 

eg. list.txt\
\
A brief history of black holes\
Existential physics\
...
\
\
then run from terminal

	`libgen`

## download manual
If you want to download book titles manually run from terminal

	`libgen <name of the book>`

A menu will guide you through the process.

![Alt text](images/main%20menu.png)

## location
Once finished downloading your books will be stored in the ~/Documents/libgen/books folder. you can open it directly from the terminal with an alias.

	`libgen_dir`
