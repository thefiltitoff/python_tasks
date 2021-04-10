import logging

def main():
    raise Exception("Hey!")
    run_with_log(main)

def run_with_log(main):
    logging.basicConfig(level=logging.DEBUG, filename='myapp.log')
    try:
        main()
    except:
        logging.exception("Oops:")


print(main())


"""
def main():
    raise Exception("Hey!")

logging.basicConfig(level=logging.DEBUG, filename='myapp.log')

try:
    main()
except:
    logging.exception("Oops:")
"""


