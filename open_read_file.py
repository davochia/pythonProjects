def read_file(file_name):
    # Reads in a file.

    new_file = open(file_name).read()
    print(new_file)
    return new_file


def read_file_into_list(file_name):
    # Reads in a file and stores each line as an element in a list

    with open(file_name, 'r') as file_read:
        return file_read.readlines()


def write_first_line_to_file(file_contents, output_filename):
    # Writes the first line of a string to a file.

    with open(output_filename, 'w') as nFile:
        return nFile.write(file_contents.split('\n')[0])


def read_even_numbered_lines(file_name):
    # Reads in the even numbered lines of a file

    with open(file_name, 'r') as file_read:
        f = file_read.readlines()
        even_list = []
        for index, values in enumerate(f):
            if (index + 1) % 2 == 0:
                even_list.append(values)
        return even_list


def read_file_in_reverse(file_name):
    # Reads a file and returns a list of the lines in reverse order

    with open(file_name, 'r') as file_read:
        f = file_read.readlines()
        return f[::-1]


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    print(file_contents.split('\n')[0])
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
