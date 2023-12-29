def count_most_common_word(lines):
    words = lines.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common_word = max(word_count, key=word_count.get)
    return most_common_word, word_count[most_common_word]


input_file = input("Введите имя входного файла: ")
output_file = input("Введите имя выходного файла: ")

with open(input_file, 'r') as file:
    with open(output_file, 'w') as output:
        for line in file:
            line = line.strip()
            if line:
                common_word, count = count_most_common_word(line)
                output.write(f"{common_word} - {count}\n")
