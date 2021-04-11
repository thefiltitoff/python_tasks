import logging


def main(func):
    f = open('myapp.log','a')
    f.write(str(type(func)))
    f.write(str(func))
    f.write('\n')
    f.close()
   # raise Exception("Zero!")


def run_with_log(a):

    try:
        return 1/a
    except ZeroDivisionError as e:
        main(e)
        logging.basicConfig(level=logging.DEBUG, filename='myapp.log')
        logging.exception("Oops:")


run_with_log(0)


