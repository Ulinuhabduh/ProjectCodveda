# Open file and handle exceptions
try:
    file = open("Word Counter\exampleText.txt", "r")

    text = file.read()
    words = text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    for word, count in word_counts.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("File not found.")