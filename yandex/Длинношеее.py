def print_long_words(text):
    vowels = 'аоэиуыеёюяaeiouy'
    syllable = 0
    count = 0
    count_ = 0
    for i in text.lower():
        if i.isalpha():
            if i in vowels:
                syllable += 1
        else:
            if syllable >= 4:
                print(text[count_ + 1:count].lower())
            count_ = count
            syllable = 0
        count += 1
