import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def  _get_part_text(text, start, page_size):
    
    ends = [',', '.', '!', ':', ';', '?']
    res = text[start : start+page_size]
   
    
    def checker(res):
        
        if res[-1] in ends:
            if res[-2] not in ends:
                if text[start + len(res):]:
                    if text[start + len(res)][0] in ends:
                        return False
                return True
    
    while not checker(res):
        res = res[:-1]
    
    
    
    
    return res, len(res)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    
    with open(path) as f:
        counter = 1
        text = f.read()
        start = 0
        #pages = len(text) // PAGE_SIZE + 1

        while start < len(text):
            t , n = _get_part_text(text, start, PAGE_SIZE)
            book[counter] = t.lstrip()
            counter += 1
            start += n
            
    

final_path = os.path.join(sys.path[0], os.path.normpath(BOOK_PATH))#.replace('/services/', '/')

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(final_path)
#print(book)