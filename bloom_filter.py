import mmh3
##install mmh3 :- pip3 install mmh3
words_to_add = ["geeks", "date", "cat"]
words_to_check = ["geeks", "date" ,"not"]
mbit_arr_size = 20
no_of_hashes = 3
mbit_arr = [0 for i in range(mbit_arr_size)]


def get_hash(index, value, size):
    return mmh3.hash(value, index) % size


def setBitArray(words):
    for i in range(len(words)):
        for j in range(no_of_hashes):
            hash_val = get_hash(j, words[i], mbit_arr_size)
            mbit_arr[hash_val] = 1

def check(word):
    for j in range(no_of_hashes):
        hash_val = get_hash(j, word, mbit_arr_size)
        if mbit_arr[hash_val] ==  0: return False
    return True


#set mbit_arr
setBitArray(words_to_add)

#check elements
for word in words_to_check:
    if check(word):print(f"Word {word} may be present")
    else:print(f"Word {word} surely not present")

