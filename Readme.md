# install on macos

clone the git repo to your Documents folder so you have ~/Documents/libgen/
install:

	`sh setup.sh`

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

## location
Once finished downloading your books will be stored in the ~/Documents/libgen/books folder. you can open it directly from the terminal with an alias.

	`libgen_dir`
