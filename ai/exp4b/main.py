from urllib.request import urljoin 
from bs4 import BeautifulSoup 
import requests 
from urllib.request import urlparse 
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", default="https://www.geeksforgeeks.org/machine-learning/", help="URL to crawl")
ap.add_argument("-d", "--depth", default=1, help="Depth of crawling")
ap.add_argument("-m", "--method", default="dfs", help="Method of crawling")

args = vars(ap.parse_args())
# Set for storing urls with same domain 
links_intern = set() 
input_url = args["url"]
depth = int(args["depth"])

# Set for storing urls with different domain 
links_extern = set() 


# Method for crawling a url at next level 
def level_crawler(input_url): 
	temp_urls = set() 
	current_url_domain = urlparse(input_url).netloc 

	# Creates beautiful soup object to extract html tags 
	beautiful_soup_object = BeautifulSoup( 
		requests.get(input_url).content, "lxml") 

	# Access all anchor tags from input 
	# url page and divide them into internal 
	# and external categories 
	for anchor in beautiful_soup_object.findAll("a"): 
		href = anchor.attrs.get("href") 
		if(href != "" or href != None): 
			href = urljoin(input_url, href) 
			href_parsed = urlparse(href) 
			href = href_parsed.scheme 
			href += "://"
			href += href_parsed.netloc 
			href += href_parsed.path 
			final_parsed_href = urlparse(href) 
			is_valid = bool(final_parsed_href.scheme) and bool( 
				final_parsed_href.netloc) 
			if is_valid: 
				if current_url_domain not in href and href not in links_extern: 
					print("Extern - {}".format(href)) 
					links_extern.add(href) 
				if current_url_domain in href and href not in links_intern: 
					print("Intern - {}".format(href)) 
					links_intern.add(href) 
					temp_urls.add(href) 
	return temp_urls 

def bfs_crawler(input_url, depth):
	# We have used a BFS approach 
	# considering the structure as 
	# a tree. It uses a queue based 
	# approach to traverse 
	# links upto a particular depth. 
	queue = [] 
	queue.append(input_url) 
	for j in range(depth): 
		for count in range(len(queue)): 
			url = queue.pop(0) 
			urls = level_crawler(url) 
			for i in urls: 
				queue.append(i) 

def dfs_crawler(input_url, depth):
    # We have used a DFS approach 
    # considering the structure as 
    # a tree. It uses a stack based 
    # approach to traverse 
    # links upto a particular depth. 
    stack = [] 
    stack.append(input_url) 
    visited = set()

    while stack and depth >= 0:
        url = stack.pop() 
        if url not in visited:
            visited.add(url)
            urls = level_crawler(url) 
            for i in urls: 
                stack.append(i) 
        depth -= 1

print("Using {} method".format(args["method"]))

if(depth == 0): 
	print("Intern - {}".format(input_url)) 

elif(depth == 1): 
	level_crawler(input_url) 

else: 
	# If the depth is more than 1 
	# then a BFS is performed to reach 
	# the desired depth. 
	if args["method"] == "bfs":
		bfs_crawler(input_url, depth)
	else:
		dfs_crawler(input_url, depth)


