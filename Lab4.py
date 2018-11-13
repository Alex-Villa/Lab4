# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert_(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search_(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            print("A total of", item_index, "comparisons were made to find the anagram:")
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove_(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)


# This method is the file reader that opens the text documents and extracts the hash value of all users and saves them to a 2D array
def file_reader_(data_total_):
    htable = ChainingHashTable(data_total_)
    try:
        with open("words.txt", "r") as text_file:
            i = 1
            for line in text_file:
                line = line.lower()
                #print(line)
                htable.insert_(line.strip())
                i+=1
    except FileNotFoundError:
        print("I'm sorry, but the file cannot be found.")
        print("Please place the file in the folder with the program and label it 'words' with .txt extension and start the program again.")
        quit()
    return htable

# This method is the file reader that opens the text documents and extracts the hash value of all users and saves them to a 2D array
def data_in_file_counter():
    try:
        with open("words.txt", "r") as text_file:
            i = 1
            for line in text_file:
                i+=1
        data_total_ = i+10
    except FileNotFoundError:
        print("I'm sorry, but the file cannot be found.")
        print("Please place the file in the folder with the program and label it 'words' with .txt extension and start the program again.")
        quit()
    return data_total_

def load_factor_(data_total_):
    load_factor = data_total_ / data_total_ + 10
    print("The load factor for file 'words.txt' with a total of", data_total_, "data entries and a table size of", data_total_ + 10, "to reduce collisions is: ", load_factor)

def print_anagrams_(word, hashTable, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if hashTable.search_(str) != None:
            print( prefix + word, "\n__________________________________________________________\n")
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                print_anagrams_(before + after, hashTable, prefix + cur)
def main():
    ht1 = file_reader_(data_in_file_counter())
    load_factor_(data_in_file_counter())
    word = input("Please enter a word to find its anagram: ")
    print("__________________________________________________________\n")
    word = word.lower()
    print_anagrams_(word, ht1)


main()