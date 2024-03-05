import logging

# def calc(a: int, m: int):
#     return a*m
# print(calc(3, 5))
# Типизация
# Явная, Неявная, Динамическая
# int num = 1 | number=1 | number:int = 1
# def spammer(message: list)-> int:
#    return len(message)
# spammer(["Hello", "Friend", "MyHome"]) #3
# spammer23 = "Ошибка"
# def primer(a: str, b: str) -> list:
#   return [len(a), len(b)]
# print(primer(1,'privet'))


# m= 34
# spam = 'Hello'
# summa = None

# try:
# summa = m + spam
# except TypeError:
#   pass
# print(summa)


# spammer=(10, 12, 234)
# try:
#   gay = spammer.append(678)
# except AttributeError:
#    print("error")
logging.basicConfig(filename="Gay.log", format='%(name)s // %(asctime)s // %(process)d // %(levelname)s // %(message)s')


logging.warning('HelloWorld')
# logging.error('Hello World')
# logging.info('Hello World')
# logging.critical('Hello World')
# logging.debug('Hello World')
