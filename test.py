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

text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

start = 0
page_size = 54
res = text[start : start+page_size]

#print(text[start + len(res):])

print(*_get_part_text(text, 0, 54), sep='\n')