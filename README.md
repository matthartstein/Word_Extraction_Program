This program analyzes a text file (books, articles, journals, etc.), then analyzes another text file that contains words to "skip", or remove, from the first text file. For example, if you include the letter 'I' in the skip-words.txt file, all instances of the letter 'I' will be removed from the first file you give to the program (i.e. "emperor3.txt"). Using multiple letters to skip is also permitted. Lastly, the program will show the top 5 word pair instances that occurs in the story file after finding and removing the letters to skip/remove. Feel free to experiment with this program by including your own books as text files and then creating your own custom skip-words.txt list.

My program will only run if you give it three command-line arguments in the following order:

"python assignment9.py emperor3.txt skip-words.txt".
