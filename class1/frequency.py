myfile= open("para.txt","r")

list_of_lines = myfile.readlines()

frequency ={}

for line in list_of_lines:
    tmp = line.strip()
    word_list =[]
    word_list = tmp.split(" ")
    print(word_list)
    for word in word_list:
        tmp_word = word.strip()
        #frequncu ogi goeas here
        if temp word in frequency:
            val = frequency[temp_word]
            val = val +1
            frequency[temp_word] = val
        else:
            frequency[temp_word] =1
                 #print(tmp)
    print(list_of_lines)
    print(frequency)