# get necessary components to actually run interactive tester
from anagram import anagram

# take in a filename for the list of words
filename = raw_input( 'enter filename of list of words or leave blank to use words.txt\n>> ' )

# if blank, default to words.txt
if filename == '':
    filename = 'words.txt'

# take in command (quit or otherwise)
command = raw_input( 'enter quit to quit or hit enter to start testing\n>> ' )

# keep taking commands until quit is entered
while ( command != 'quit' ):
    words = raw_input( 'enter words to test as comma separated list (no spaces)\n>> ' )
    word_list = words.split(',')
    print 'anagram list:'
    print anagram( word_list, filename )
    command = raw_input( 'enter anything to start testing or quit to quit\n>> ' )

print 'interactive tester done'
