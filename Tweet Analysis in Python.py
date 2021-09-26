####################################
# Assignment: 2                    #
# Student Name: Shuangquan Zheng   #
####################################

def proper_capitalization(sentence):
    """
    Lower the cases of all the word in sentence with lower function
    and return that lowered case sentence.
    """
    lowered = sentence.lower()
    return lowered


def tokenization(sentence):
    """
    Return list of words by spliting the sentence by white single spaces
    using split function. It will return nothing if there is no word in
    sentence.
    """
    word_lst = sentence.split()
    return word_lst


def stop_word_removal(sentence, stop_words):
    """
    Removing stop words in sentences by lowering the cases of the words
    and then split them into list with split function. Once that's
    completed join the words in list with join function to return a sentence.
    """
    sentence_list = sentence.split()
    words_lst = stop_words.lower().split()
    temp_list = []
    for word in sentence_list:
        if word.lower() not in words_lst:
            temp_list.append(word)
    final_sentence = " ".join(temp_list)
    return final_sentence


def remove_punc(sentence, punctuation):
    """
    Removing punctuation as it only as trailing punctuation so removing
    only ones at the end of the word using strip function then add it to
    list thats stored under the variable name final which will then be
    joined through join function to make the final sentence and return that.
    """
    sentence_list = sentence.split()
    final = []
    for i in sentence_list:
        word = i.strip(punctuation)
        final.append(word)
    final_sentence = " ".join(final)
    return final_sentence


def remove_duplicate_words(sentence):
    """
    Remove duplciate words by using dictionary, if its not in dictionary
    then will append it to non_dup list which will then be sorted and join
    to make a sentence and return that.
    """
    sentence_list = sentence.split()
    dictionary = dict()
    non_dup = []
    for i in sentence_list:
        if i not in dictionary:
            dictionary[i] = 1
            non_dup.append(i)
    final_sentence = " ".join(sorted(non_dup))
    return final_sentence


def cleaning_noise(sentence):
    """
    For this function the removal take place in form of ignoring.
    If it doesnt have http, # and &amp but has @ it will first check
    if its and odd mention if it is then ignore and +1 to counter and
    proceed until no word left.
    """
    sentence_list = sentence.split()
    counter = 1
    new_sentence = []
    for element in sentence_list:
        if 'http' not in element and '#' not in element and '&amp' not in element:
            if '@' in element:
                if counter % 2 == 0:
                    new_sentence.append(element)
                    counter += 1
                else:
                    counter += 1
            else:
                new_sentence.append(element)
        if '&amp' in element:
            new_sentence.append(element.replace('&amp', '&'))
    final_sentence = " ".join(new_sentence)
    return final_sentence


def construct_ngrams(sentence, n):
    """
    Not using zip to make list of list of N-gram, Will return empty list
    if checker(length check) is less or equal to counter. If length of
    sentence is less than n then return empty list as can't create N-gram.
    While loop will stop once reaching end of list.
    """
    sentence_list = sentence.split()
    checker = len(sentence_list)
    counter = n
    new_list = []
    index_no = 0
    if n > checker or n <= 0:
        new_list = []
    else:
        while counter <= checker:
            new_list.append(sentence_list[index_no:counter])
            counter += 1
            index_no += 1
    return new_list


def pos(sentence):
    """
    While loop will continue and check word for vowels if have vowels then
    will continue to check for letter to remove if not then it will continue
    to next word if there is letter needed to be removed it will set
    condition_check to true and once done loop start again and move to next word
    once the sentences done looping it will continue while loop if condition_check
    is still True once thers nothing left then loop will stop as condition_check was
    set False at start of while loop and there were no change made to it as there's
    no letter to be removed hence no need to set the conditon_check to True.
    """
    sentence_list = sentence.split()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    indexes = 0
    condition_check = True
    while condition_check:
        indexes = 0
        condition_check = False
        for word in sentence_list:
            for letters in word:
                if letters in vowels and counter == 0:
                    counter += 1
            if word.endswith("'s") or word.endswith("s'") and counter == 1:
                condition_check = True
                counter = 0
                sentence_list[indexes] = word[0:-2]
                indexes += 1
            elif word.endswith('s'):
                if word.endswith("us") or word.endswith("ss"):
                    indexes += 1
                    counter = 0
                elif word.endswith('sses'):
                    condition_check = True
                    counter = 0
                    sentence_list[indexes] = word[0:-2]
                    indexes += 1
                elif word.endswith('ies') and (len(word)-2 > 2):
                    condition_check = True
                    counter = 0
                    sentence_list[indexes] = word[0:-2]
                    indexes += 1
                elif word.endswith('ies') and (len(word)-2 <= 2):
                    condition_check = True
                    counter = 0
                    sentence_list[indexes] = word[0:-1]
                    indexes += 1
                elif len(word) >= 2 and word[-2] in vowels:
                    indexes += 1
                    counter = 0
                elif counter == 0:
                    if len(word) == 1:
                        sentence_list[indexes] = word.strip('s')
                        condition_check = True
                        indexes += 1
                    else:
                        condition_check = False
                        indexes += 1
                else:
                    condition_check = True
                    counter = 0
                    sentence_list[indexes] = word[0:-1]
                    indexes += 1
            elif word.endswith('ed'):
                counter = 0
                if word.endswith('ied'):
                    if (len(word)-2 > 2):
                        condition_check = True
                        sentence_list[indexes] = word[0:-2]
                        indexes += 1
                    else:
                        sentence_list[indexes] = word[0:-1]
                        indexes += 1
                else:
                    condition_check = True
                    sentence_list[indexes] = word[0:-3]
                    indexes += 1
            elif word.endswith('er') or word.endswith('ing'):
                if word.endswith('ing'):
                    counter = 0
                    if (len(word)-2 > 3):
                        condition_check = True
                        sentence_list[indexes] = word[0:-3]
                        indexes += 1
                    else:
                        sentence_list[indexes] = word
                        indexes += 1
                else:
                    condition_check = True
                    counter = 0
                    sentence_list[indexes] = word[0:-2]
                    indexes += 1
            elif word.endswith('ly'):
                condition_check = True
                counter = 0
                sentence_list[indexes] = word[0:-2]
                indexes += 1
            else:
                indexes += 1
                counter = 0
    if sentence_list == []:
        final_sentence = ""
    else:
        final_sentence = " ".join(sentence_list)
    return final_sentence


def load_data(filename):
    """
    Read utf8 file through open function and encoding parameter set
    to utf-8 then use read function to read the file and use splitlines
    function to split each line in the text file follow by for loop to
    strip all the whitespace in the sentence.
    """
    file = open(filename, encoding='utf-8')
    new_lst = []
    for i in file.read().splitlines():
        new_lst.append(i.strip())
    file.close()
    return new_lst


def tweet_analysis():
    """
    Use input function to take strings from user than use open file
    with parameter mode of 'a' to allow append to previous line of text
    added to the file when I'm writing through loop which will stop
    writing to end of loop once it reach end of list in sentence_list
    and close the new file.
    """
    read_filename = input('Enter the name of the file to read: ')
    write_filename = input('Enter the name of the file to write: ')
    stop_word = input('Enter your stop words: ')
    punctuation = input('Enter your punctuations to remove: ')
    sentence_list = load_data(read_filename)
    new_list = []
    number_index = 0
    new_file = open(write_filename, "a")
    for sentence in sentence_list:
        processed_sentence = proper_capitalization(sentence)
        processed_sentence = stop_word_removal(processed_sentence, stop_word)
        processed_sentence = remove_punc(processed_sentence, punctuation)
        processed_sentence = remove_duplicate_words(processed_sentence)
        processed_sentence = cleaning_noise(processed_sentence)
        processed_sentence = pos(processed_sentence)
        new_list.append(processed_sentence)
        if number_index != len(sentence_list):
            sentence_with_n = processed_sentence + "\n"
            new_file.write(sentence_with_n)
            number_index += 1
        else:
            new_file.write(processed_sentence)
    new_file.close()
    return new_list


def word_ranking(corpus, n):
    """
    Ranking the occuarnce of the word first then use slicing to get the
    first n tuples and then sort them alphabetically by the words and
    return the ranked tuple.
    """
    count_dictionary = dict()
    tuple_lst = []
    for i in corpus:
        word_list = i.split()
        for word in word_list:
            if word not in count_dictionary:
                count_dictionary[word] = 1
            else:
                count_dictionary[word] += 1
    ordered_list = sorted(count_dictionary.values(), reverse=True)
    for num in ordered_list:
        for word in count_dictionary.keys():
            if count_dictionary[word] == num:
                tuple_lst.append(tuple([word, num]))
    ranked_tuple = sorted(tuple_lst[0:n])
    return ranked_tuple
