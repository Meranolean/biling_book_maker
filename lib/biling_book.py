from blb_helpers import print_book
from blb_func import parse_study_english_words

BEGIN = '''\
<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
  <description>
    <title-info>
        <genre>antique</genre>
        <author><first-name></first-name><last-name>{}</last-name></author>
        <book-title>{}</book-title>
        <!-- <coverpage><image l:href="#img_0"/></coverpage> -->
        <lang>es</lang>
    </title-info>
  </description>
<body>'''


END = '''
</body>
</FictionBook>
'''

import json
def make_book(name: str, author: str, url: str, npage: int) -> None:
    book = parse_study_english_words(url, npage)
    book = json.load(open('../../../books_to_print'))[1]
    book_output = print_book(book, name, BEGIN.format(author, name), END)
    with open(name.lower().replace(' ', '_') + '.fb2', 'w') as fout:
        fout.write(book_output)
