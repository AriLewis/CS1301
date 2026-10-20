course = {
                        'code': 4320,
                        'name': 'Operating System',
                        'dept': 'Computer Science',
                        'building': 'Langdale Hall',
                        'room': 218,
                        'sections': [2]

}
def text_filter(message):
    banned_words = ["turkey", "dog", "fox", "cat", "chicken"]
    words = message.split()
    filtered = []
    for word in words:
        if word.lower() not in banned_words:
            filtered.append(word)
    return " ".join(filtered)


def main():
    message = input(">: ")
    print("Input Message:", message)
    print("Output Message:", text_filter(message))


main()