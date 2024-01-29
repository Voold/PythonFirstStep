import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
            print("Это текст после функции")
        else: print("URL IS WRONG")
    return wrapper
@validator #ПО СУТИ ФУНКЦИЯ ДЛЯ ФУНКЦИЙ. ОПТИМИЗАЦИЯ ЕБАЙШАЯ. можно несколько
def open_url(url):
    webbrowser.open(url)

open_url("https://voold.online")