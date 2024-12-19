from gendiff import generate_diff
from gendiff.frame import parsearguments


def main():
    '''generates diff from two files.'''
    args = parsearguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
