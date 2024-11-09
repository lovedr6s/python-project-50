import argparse, json

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file', help="The first configuration file")
    parser.add_argument('second_file', help="The second configuration file")
    parser.add_argument('-f', '--format', default="plain")
    args = parser.parse_args()
    first_file = json.load(open("/Users/lovedr6s/Desktop/Programming/python-project-50/gendiff/scripts/" + args.first_file))
    second_file = json.load(open("/Users/lovedr6s/Desktop/Programming/python-project-50/gendiff/scripts/" + args.second_file))
    

if __name__ == '__main__':
    main()