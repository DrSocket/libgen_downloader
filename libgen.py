from xml.etree.ElementInclude import include
from lib.libgen_search import LibgenSearch
import subprocess
import os
import sys
import time

not_found = []
skipped = []
manual = False

def search_author(s, res, line):
	author = input("Enter the author name: ")
	links = []
	auth = author.split()
	for r in res:
		if len(auth) > 1 and auth[0] in r['Author'] and auth[1] in r['Author']:
			links.append(r)
		elif auth[0].lower() in r['Author'].lower():
			links.append(r)
	if len(links) == 0:
		line = line + " " + author
		res = s.search_auto(line)
		return res
	else:
		return links

def search_extension(res, ext):
	links = []
	for r in res:
		if r['Extension'] == ext:
			links.append(r)
	if len(links) == 0:
		print ("Extension not found in results")
	else:
		return links

def prompt():
	ret = input("""
Enter the index of the book you want to download, 
multiple books can be separated by comma:

`x` : to skip					`a`: add author to search
`s`: sort by most recent			`b` : unsort
`more` : show more book results			`f` : search by extension
`manual` : enter a book manually		`exit` : to exit

-> """).strip()
	return ret

def download_books(choice, res):
	success = False
	if choice.isdigit():
		choice = int(choice)
		if res[choice]:
			links = s.resolve_download_links(res[choice])
			url = links['GET']
			# output_path = f"books/{res[choice]['Title']}.{res[choice]['Extension']}"
			subprocess.Popen(f"wget -b -q {url} -P ./books/",shell=True, stdout=subprocess.DEVNULL)
			# subprocess.Popen(['wget', '-b', '-q', url, '-P', output_path])
			success = True
	else:
		choice = choice.split(', ')
		for c in choice:
			if c.isdigit():
				c = int(c)
				if res[c]:
					links = s.resolve_download_links(res[c])
					url = links['GET']
					# output_path = f"books/{res[c]['Title']}.{res[c]['Extension']}"
					subprocess.Popen(f"wget -b -q {url} -P ./books/",shell=True)
					# subprocess.Popen(['wget', '-b', '-q', url, '-P', output_path], bufsize=0)
					success = True
	if success:
		print("Download started")
	else:
		print("Download failed")
	return success

def format_res(s: LibgenSearch, res: list, line: str, more: int = 5):
	os.system('cls' if os.name == 'nt' else 'clear')
	if res:
		print (f'{line}\n')
		for i, r in enumerate(res):
			if i > more:
				break
			print(f"{i}: {r['Title']} | {r['Year']}\n\t{r['Author']} | {r['Size']} | {r['Extension']} \n")
		while True:
			try:
				choice = prompt()
				if choice == 'x':
					skipped.append(line)
					break
				if choice == 'a':
					links = search_author(s, res, line)
					if links:
						format_res(s, links, line)
					break
				if choice == 's':
					links = sorted(res, key=lambda k: k['Year'], reverse=True)
					ret = format_res(s, links, line)
					if ret == 'b':
						format_res(s, res, line)
					break
				if choice == 'f':
					ext = input("Enter the extension: ")
					links = search_extension(res, ext)
					if links:
						format_res(s, links, line)
					break
				if choice == 'b':
					return 'b'
				if choice == 'exit':
					return -1
				if choice == 'more':
					more = int(input("Enter the number of results you want to see: "))
					if more > 25 and len(res) > 25:
						res = s.search_auto(line)
					format_res(s, res, line, more)
				download_books(choice, res)
				return
			except ValueError:
				print("Invalid choice")
				continue
	else:
		not_found.append(line)
		return "Title not found"

def make_list():
	books = []
	with open("list.txt") as f:
		for line in f:
			books.append(line.strip())
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("Book List: \n" + " | ".join(books))
	print ('\n')
	f.close()
	return books

if __name__ == "__main__":
	s = LibgenSearch()
	if len(sys.argv) > 1:
		manual = True
		print (f"Searching for {sys.argv[1]}")
		res = s.search_title(sys.argv[1])
		status = format_res(s, res, sys.argv[1], True)
	else:
		books = make_list()
		for i, book in enumerate(books):
			res = s.search_title(book)
			status = format_res(s, res, book, i == len(books) - 1)
			if status == -1:
				break
	print ('\nSkipped books: \n')
	for book in skipped:
		print (book)
	print ('\nBooks not found: \n')
	for book in not_found:
		print (book)
