import argparse, json

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file', help="The first configuration file")
    parser.add_argument('second_file', help="The second configuration file")
    parser.add_argument('-f', '--format', default="plain")
    args = parser.parse_args()
    first_file = json.load(open("/Users/lovedr6s/Desktop/Programming/python-project-50/gendiff/scripts/" + args.first_file))
    second_file = json.load(open("/Users/lovedr6s/Desktop/Programming/python-project-50/gendiff/scripts/" + args.second_file))
    print(generate_diff(first_file, second_file))
    

def generate_diff(first_file, second_file):
    all_keys = sorted(set(first_file.keys()).union(second_file.keys()))
    result_of_difference = []
    for key in all_keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                result_of_difference.append(f"   {key}: {first_file[key]}")
            else:
                result_of_difference.append(f" - {key}: {first_file[key]}")
                result_of_difference.append(f" + {key}: {second_file[key]}")
        elif key in first_file:
            result_of_difference.append(f" - {key}: {first_file[key]}")
        elif key in second_file:
            result_of_difference.append(f" - {key}: {second_file[key]}")
    return result_of_difference
    


if __name__ == '__main__':
    main()