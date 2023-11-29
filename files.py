files = ['1.txt', '2.txt', '3.txt']

texts = {}
for file in files:
    with open(file, 'r', encoding='utf-8') as one_file:
        text = one_file.read()
        one_file.seek(0)
        length = len(one_file.readlines())
        texts[file] = {'text': text, 'length': length}

sorted_texts = sorted(texts.keys(), key=lambda x: (texts[x]['length']))

with open('all_texts.txt', 'a', encoding='utf-8') as all_texts:
    for text in sorted_texts:
        all_texts.write(text + '\n')
        all_texts.write(str(texts[text]['length']) + '\n')
        all_texts.write(texts[text]['text'] + '\n')