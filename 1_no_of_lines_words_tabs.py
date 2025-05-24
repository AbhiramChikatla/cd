def count_file_contents(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print(content)
    num_chars = len(content)
    num_words = len(content.split())
    num_lines = content.count('\n')
    num_spaces = content.count(' ')
    num_tabs = content.count('\t')

    print(f"Number of Characters: {num_chars}")
    print(f"Number of Words: {num_words}")
    print(f"Number of Lines: {num_lines}")
    print(f"Number of Spaces: {num_spaces}")
    print(f"Number of Tabs: {num_tabs}")

# Provide the file path here
file_path = "sample.txt"  # Change this to your file name
count_file_contents(file_path)
