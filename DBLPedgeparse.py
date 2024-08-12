def extract_marked_lines(file_path):
    index_lines = []
    perc_lines = []

    tempindex = ""

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith("#index"):
                    tempindex = (line[len("#index"):].strip())
                elif line.startswith("#%"):
                    index_lines.append(tempindex)
                    perc_lines.append(line[len("#%"):].strip())
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file at {file_path}.")
    except UnicodeDecodeError:
        print(f"Error: The file at {file_path} contains characters that cannot be decoded with 'utf-8' encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return index_lines, perc_lines

def write_to_output_file(output_file_path, index_lines, perc_lines):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for index, title in zip(index_lines, perc_lines):
                file.write(f"{index}\t{title}\n")
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")

# Usage
input_file_path = 'D:\\kcore_dataset\\outputacm.txt'
# output_file_path = 'D:\\parsingProject\\newdatasetparsed.txt'
output_file_path = 'D:\\parsingProject\\newdatasetedges.txt'
index_lines, perc_lines = extract_marked_lines(input_file_path)

write_to_output_file(output_file_path, index_lines, perc_lines)