some_sentence = input("Enter sentence: ").split( )

dict_1 = {i: some_sentence.count(i) for i in some_sentence}
print(dict_1)
