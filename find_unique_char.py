from collections import Counter


def find_unique_char(str):
    words_list = str.split(" ")
    chars_list = []

    for item in words_list:
        for ch in item:
            freq = Counter(item)
            if freq[ch] == 1:
                chars_list.append(ch)
            break

    for char in chars_list:
        freq_2 = Counter(chars_list)
        if freq_2[char] == 1:
            print(char)
            break


my_str = 'The Tao gave birth to machine language.  Machine language gave birth to the assembler. The assembler gave ' \
      'birth to the compiler.  Now there are ten thousand languages. Each language has its purpose, however humble.  ' \
      'Each language expresses the Yin and Yang of software.  Each language has its place within the Tao. But do not ' \
      'program in COBOL if you can avoid it. -- Geoffrey James, "The Tao of Programming"'

find_unique_char(my_str)
find_unique_char("C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, "
                 "it blows away your whole leg. (с) Bjarne Stroustrup")
