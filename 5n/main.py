import sys
from process_data import ProcessDataClass

def main():
    c = ProcessDataClass(csv_path='duraliminiy.csv')
    c.print_raw()
    c.preprocess()
    c.print_preprocessed()

if __name__ == "__main__":
    sys.exit(main())

