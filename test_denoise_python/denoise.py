'''Form a list of strings from HTML text-content and structure

Functional style solution to simplify the HTML
DOM tree of any chunk of HTML. Higher-order Functions,
Lambdas, Closure, and List Comprehensions are used.

This algorithm focuses on extracting text content
while retaining basic structural relationships
from the HTML as semantic structural units
of natural language.

IN:  HTML Chunk or Whole document
OUT: List of HTML lines destructured
'''
from bs4 import BeautifulSoup
import pprint

def get(file):
    '''Get HTML file from path
    
    PARAM: str - Path to file
    RETURNS: html/txt file as Python List of lines
    '''
    with open(file, 'r') as html_file:
        return html_file.readlines()

def soup_lines(lines):
    '''Make beautiful soup object instances from HTML lines

    PARAM: List of html lines in a list
    RETURNS: List of beautifulsoup instances'''
    for l in lines:
        return (BeautifulSoup(l, 'html.parser') for l in lines)

# List comprehensions getting parts from the beautifulsoup object instances
read_tags = lambda soup: [tag.name for tag in soup.find_all()]
read_attrs = lambda soup: [tag.attrs for tag in soup.find_all()]
read_text = lambda soup: [tag.text for tag in soup.find_all()]

def remove_char(rm_char, line_string):
    line = ''
    for char in line_string:
        if char == rm_char:
            line += ''
        else:
            line += char
    return line

def join_parts(tag, attr, text):
    return f'{", ".join(tag)}, {attr}, {"".join(text)}'
                
# This is done by another class in the codebase but here it is expecting
# to receive the body only or just the div that holds the product info.
def destructure_noisy_html(html_lines):
    # Split noisy HTML chunk into lines keeping natural order
    # And hold as Beautiful Soup object instances (1 per line)
    # Important: KEEPS HTML DOCUMENT ORDER
    # Do a series of List Comprehensions:
    # Remove tabs
    lines = [remove_char('\t', line) for line in html_lines]
    # Create list: HTML_TAGS
    tags = [read_tags(soup) for soup in soup_lines(lines)]
    # Create list: HTML_ATTRIBUTES as dictionary-like
    attrs = [read_attrs(soup) for soup in soup_lines(lines)]
    # Create list: TEXT string from HTML content
    text = [read_text(soup) for soup in soup_lines(lines)]
    # Create quiet list: STRINGS of 3 above lists
    quiet_lines = (list(map(join_parts, tags, attrs, text)))

    return quiet_lines

if __name__ == ('__main__'):
    noisy_html = get('specs-chunk.html')
    quiet_html = destructure_noisy_html(noisy_html)
    
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(quiet_html)
