

def reverse_string():
    sentence = input('Write a sentence to reverse: ').split()
    r_sentence = ''
    for i in range(-1, -(len(sentence) + 1), -1):
        r_sentence += sentence[i] + ' '
    return r_sentence





def main():
    print(reverse_string())

if __name__ == "__main__":
    main()