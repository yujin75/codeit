out_file = open('new_file.txt', 'w')

while True:
    word_en = input("영어 단어를 입력하세요: ")
    if(word_en == 'q'):
        break
    word_ko  = input("한국어 뜻을 입력하세요: ")
    out_file.write("%s: %s\n" % (word_en, word_ko))

out_file.close()