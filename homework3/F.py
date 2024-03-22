from collections import deque


def main():
    dictionary = set(input().strip().split())
    text = input().strip().split()

    shrinkedText = shrinkText(dictionary, text)
    print(shrinkedText)

def shrinkText(dictionary, text):
    replacedWords = deque()

    for word in text:
        isWordReplaced = False
        for i in range(len(word)):
            prefix = word[0 : i + 1]
            if prefix in dictionary:
                replacedWords.append(prefix)
                isWordReplaced = True
                break
        if not isWordReplaced:
            replacedWords.append(word)
    
    return " ".join(replacedWords)


if __name__ == '__main__':
    main()    