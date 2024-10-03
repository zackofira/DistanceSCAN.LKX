# Step 1: Read the file with numbers row by row
def read_number_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip().split() for line in f.readlines()]

# Step 2: Create a dictionary mapping numbers to titles
def create_title_map(file_path):
    title_map = {}
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            # Split by the tab character to separate the number from the title
            num, title = line.split("\t", 1)
            title_map[num] = title.strip()  # Avoid stripping the number
    return title_map

# Step 3: Replace numbers in the original data with their corresponding titles (and preserve the number)
def replace_numbers_with_titles(numbers_data, title_map):
    replaced_data = []
    for row in numbers_data:
        titles_row = [f"{num}: {title_map.get(num, f'Title not found for {num}')}" for num in row]
        replaced_data.append('\n'.join(titles_row))  # Separate titles by newline
    return replaced_data

# Step 4: Output the result with two newlines separating rows
def print_titles(replaced_data):
    for row in replaced_data:
        print(row)
        print("\n")  # Two newlines between rows

numbers_file = 'C:\\clusters\\New\\08-5050-parsed.txt'  # Replace with your file path
titles_file = 'C:\\coolfiles\\crazy.txt'    # Replace with your file path

numbers_data = read_number_file(numbers_file)
title_map = create_title_map(titles_file)
replaced_data = replace_numbers_with_titles(numbers_data, title_map)

print_titles(replaced_data)

