import logging


def main(func):
    f = open('myapp.log','a')
    f.write(str(type(func)))
    f.write(str(func))
    f.write('\n')
    f.close()
   # raise Exception("Zero!")


def run_with_log(func):

    try:
        func()
    except ZeroDivisionError as e:
        main(e)
        logging.basicConfig(level=logging.DEBUG, filename='myapp.log')
        logging.exception("Oops:")


def test():
    return 1/0

run_with_log(test)


