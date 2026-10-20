'''
Aryona Lewis
filtering banned words from the sentence "The Quick Brown Fox Jumps."
'''
def text_filter(message):
    banned_words = ["turkey", "dog", "fox", "cat", "chicken"]
    words = message.split()
    filtered = []
    for word in words:
        if word.lower() not in banned_words:
            filtered.append(word)
    return " ".join(filtered)


def main():
    message = input(" ")
    print("Input Message:", message)
    print("Output Message:", text_filter(message))


main()


