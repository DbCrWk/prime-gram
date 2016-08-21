import warnings

'''
main anagram method that takes in two parameters:
list of words for which to anagrams
filename (optional)
'''
def anagram( *args ):
    # check number of parameters
    if len( args ) == 1:
        # use default name 'words.txt' for list of words
        filename = 'words.txt'
        warnings.warn( 'no word list specified, looking for words.txt', UserWarning)
    else:
        # load words from file from second argument
        filename = args[1]

    # load word map from file
    word_map = load_word_list_with_map( filename )

    # list of words is the first argument
    test_words = args[0]

    # initialize empty list of anagram lists
    anagram_list = []

    # iterate through input words to find their anagrams
    for word in test_words:
        # quick check to see if the input word is even in our possible anagram words
        if word not in word_map.keys():
            warnings.warn( 'input word not in list of words', UserWarning )

        # add anagrams to the anagram list
        anagram_list.append( search_for_anagram( word, word_map ) )

    return anagram_list

# prime number mapping for each letter
letter_map = {
'a' : 2,
'b' : 3,
'c' : 5,
'd' : 7,
'e' : 11,
'f' : 13,
'g' : 17,
'h' : 19,
'i' : 23,
'j' : 29,
'k' : 31,
'l' : 37,
'm' : 41,
'n' : 43,
'o' : 47,
'p' : 53,
'q' : 59,
'r' : 61,
's' : 67,
't' : 71,
'u' : 73,
'v' : 79,
'w' : 83,
'x' : 89,
'y' : 97,
'z' : 101,
'-' : 103
}

# compute the unique number assigned to a combination of letters
def word_to_number( word ):
    # make sure that the word is lowercase
    word = word.lower()

    # initialize our unique number to 1
    word_number = 1
    for letter in word:
        try:
            # compute the running product of prime numbers
            word_number = word_number * letter_map[ letter ]
        except KeyError:
            warnings.warn( 'word contains invalid characters', UserWarning )
            word_number = 0

    return word_number

def create_word_map( content ):
    word_map = { word : word_to_number( word ) for word in content }
    return word_map

# load a list of words from a file and return a map of words to their numbers
def load_word_list_with_map( filename ):
    try:
        # load the each of the file into a list
        with open( filename ) as word_file:
            content = word_file.read().splitlines()
        # create the map from words to their numbers
        word_map = create_word_map( content )
    except Exception:
        # return empty dictionary if file not found
        warnings.warn( 'file not found', UserWarning )
        word_map = {}

    return word_map

# search for a word's anagrams in a word map
def search_for_anagram ( word, word_map ):
    # generate the value of the word
    word_value = word_to_number( word )

    # intiialize empty list of anagrams
    anagram_list = []

    # iterate through word map to find words with same number
    for entry, value in word_map.iteritems():
        '''
        add the word to the list of anagrams if and only if
        it has same value and it is not the word itself
        '''
        if value == word_value and entry != word:
            anagram_list.append( entry )

    return anagram_list
