import typing as tp

d0 = '\n'
d1 = '\n  '
d2 = '\n    '
d3 = '\n      '

def normalize(string: str) -> str:
    string = string.replace('\r', '').replace('\n', '')
    while string[0] == ' ':
        string = string[1: ]
    while string[-1] == ' ':
        string = string[: -1]
    return string


def find_chapters(book: tp.List[tp.Tuple[str, str]], begin: int, end: int) -> tp.List[int]:
    chapters_id = []
    for i, (eng, rus) in enumerate(book[begin: end]):
        norm_eng = normalize(eng)
        if norm_eng.startswith('CHAPTER') or ('CHAPTER' in norm_eng):
            chapters_id.append(begin + i)
    chapters_id.append(end)
    return chapters_id

def find_parts(book: tp.List[tp.Tuple[str, str]]) -> tp.List[int]:
    part_id = []
    for i, (eng, rus) in enumerate(book):
        norm_eng = normalize(eng)
        if norm_eng.startswith('Part'):
            part_id.append(i)
    part_id.append(len(book))
    return part_id


def print_chapter_table(book: tp.List[tp.Tuple[str, str]], begin: int, end: int, string: str) -> str:
    string += d0 + '<table>'
    for j in range(begin, end):
        eng, rus = book[j]
        string += d1 + '<tr>'
        string += d2 + '<td>' + normalize(eng) + '</td>'
        string += d2 + '<td>' + normalize(rus) + '</td>'
        string += d1 + '</tr>'
    string += d0 + '</table>'
    return string


def print_chapter(book: tp.List[tp.Tuple[str, str]], begin: int, end: int, string: str) -> str:
    for j in range(begin, end):
        eng, rus = book[j]
        string += d1 + '<p>' + normalize(eng) + '</p>'
        string += d1 + '<p>' + normalize(rus) + '</p>'
        string += d1 + '=' * 10
    return string


def print_part(book: tp.List[tp.Tuple[str, str]], begin: int, end: int, string: str) -> str:
    chapter_to_write = find_chapters(book, begin, end)
    for chapter_begin, chapter_end in zip(chapter_to_write[: -1], chapter_to_write[1:]):
        string += d0 + '<section>' + d1 + '<title>' + d2 + '<p>' + \
                  normalize(book[chapter_begin][0]) + '</p>' + \
                  d1 + '</title>' + d1 + '<empty-line/>'
        print(normalize(book[chapter_begin][0]))
        string = print_chapter(book, chapter_begin + 1, chapter_end, string)
        string += d0 + '</section>'
    return string


def print_book(book: tp.List[tp.Tuple[str, str]], book_name: str, BEGIN: str, END: str) -> str:
    string = BEGIN
    string += d1 + '<title>' + d2 + '<p><strong>' + book_name + '</strong></p>' + d1 + '</title>'
    
    parts_to_write = find_parts(book)
    for part_begin, part_end in zip(parts_to_write[: -1], parts_to_write[1:]):
        string += d0 + '<section>' + d1 + '<title>' + d2 + '<p><strong>' + \
                  normalize(book[part_begin][0]) + '</strong></p>' + \
                  d1 + '</title>'
        string = print_part(book, part_begin + 1, part_end, string)
        string += d0 + '</section>'
    string += END
    return string
