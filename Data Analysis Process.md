# Data Analysis from A to Z
## Data Processing Pipeline
###### There are following stages:
1. obtaining data
2. cleaning, and transforming raw data
3. descriptive and exploratory data analysis, and
4. data modeling and prediction
## Project Report Structure
- Abstract (a brief and accessible description of the project)
- Introduction
- Methods that were used for data acquisition and processing
- Results that were obtained (do not include intermediate and insignificant
results in this section; rather, put them into an appendix)
- Conclusion
- Appendix. In addition to the non-essential results and graphics, the appendix contains
all reproducible code used to process the data: well-commented scripts that
can be executed without any command-line parameters and user interaction.
 A `README` file typically explains the provenance of the data and the format of
every attached data file.
## How to Assess and Manipulate Text Strings
### Case Conversion Functions:
`lower()` converts all characters to lowercase; 
`upper()` converts all characters to uppercase; and 
`capitalize()` converts the first character to uppercase and all other
characters to lowercase. 
### Predicate:
The predicate functions return `True` or `False`, depending on whether the string
belongs to the appropriate class: 
 `islower()` checks if all alphabetic characters are
in lowercase; `isupper()` checks if all alphabetic characters are in uppercase; `isspace()`
checks if all characters are spaces; `isdigit()` checks if all characters are decimal
digits in the range 0–9; and `isalpha()` checks if all characters are alphabetic
characters in the ranges a–z or A–Z.
### Decoding:
The decoding functions convert a binary array to a character
string and back: `bin.decode()` converts a binary array to a string, and `s.encode()`
converts a string to a binary array. Many Python functions expect that binary data is converted to strings until it is further processed.
### Steps of String Processing:
1.  Getting rid of unwanted whitespaces (including new lines and tabs). The functions `lstrip()` (left strip), `rstrip()` (right
strip), and `strip()` remove all whitespaces at the beginning, at the end, or all
around the string. (They don’t remove the inner spaces.) 
2. The function `split(delim='')` splits the string s into a list of substrings, using delim as the delimiter. If the delimiter isn’t specified,
Python splits the string by all whitespaces and lumps all contiguous whitespaces together.
3. The sister function `join(ls)` joins a list of strings ls into one string, using the object string as the glue.
4. The function `find(needle)` returns the index of the first occurrence of the substring needle in the object string or -1 if the substring is not present. 
5. The function `count(needle)` returns the number of non-overlapping occurrences of the substring needle in the object string. 

## Choosing the Right Data Structure
- _Lists_ as arrays. They have linear search time, which makes them impractical for storing large amounts of searchable data.
- _Tuples_ are immutable lists. Once created, they cannot be changed. They still have linear search time. 
- _Sets_ are not sequences: set items don’t have indexes. Sets can store at most one copy of an item and have sublinear O(log(N)) search
time. They are excellent for membership look-ups and eliminating duplicates (if you convert a list with duplicates to a set, the duplicates are gone):
`myList = list(set(myList))` _#Remove duplicates from myList_
- _Dictionaries_ map keys to values. An object of any hashable data type (number, Boolean, string, tuple) can be a key, and different keys in the same dictionary
can belong to different data types. There is no restriction on the data types of dictionary values. Dictionaries have sublinear O(log(N)) search time. They
are excellent for key-value look-ups.

## Comprehending Lists Through List Comprehension
List comprehension is an expression that transforms a collection (not necessarily a list) into a list. It is used to apply the same operation to all or some
list elements, such as converting all elements to uppercase or raising them all to a power.
**The transformation process looks like this:**
1. The expression iterates over the collection and visits the items from the
collection.
2. An optional Boolean expression (default `True`) is evaluated for each item.
3. If the Boolean expression is `True`, the loop expression is evaluated for the current item, and its value is appended to the result list.
4. If the Boolean expression is `False`, the item is ignored.

## Counting with Counters
A counter is a dictionary-style collection for tallying items in another collection. It is defined in the module collections. You can pass the collection to be tallied
to the constructor `Counter` and then use the function `most_common(n)` to get a list of `n` most frequent items and their frequencies (if you don’t provide `n`, the
function will return a list of all items).
















