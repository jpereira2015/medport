def count_lines_in_file(file_path):
    line_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for _ in file:
            line_count += 1
    return line_count

# Replace '/path/to/your/file.xml' with the actual path to your XML file
file_path = '/Users/josephpereira/medport/ptwiki-20240401-pages-articles-multistream.xml'
line_count = count_lines_in_file(file_path)

print(f"The file {file_path} contains {line_count} lines.")
