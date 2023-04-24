import re 

text2 = """COM    Computers
205 MAT   Mathematics 189"""

regex_num = re.compile('\d+')
s = regex_num.search(text2)

print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print(text2[s.start():s.end()])

text = """101   COM \t  Computers
205   MAT \t  Mathematics
189   ENG  \t  English"""  
print(text)

regex = re.compile('\s+')
print(regex.sub(' ', text))

# or
print(re.sub('\s+', ' ', text))

# get rid of all extra spaces except newline
regex = re.compile('((?!\n)\s+)')
print(regex.sub(' ', text))

text = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""  

re.findall('[0-9]+', text)

re.findall('[A-Z]{3}', text)

re.findall('[A-Za-z]{4,}', text)

# define the course text pattern groups and extract
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
re.findall(course_pattern, text)

text = "< body>Regex Greedy Matching Example < /body>"
re.findall('<.*>', text)

re.findall('<.*', text)

re.search('<.*?>', text).group()

text = 'machinelearningplus.com'
print(re.findall('.', text))  # .   Any character except for a new line
print(re.findall('...', text))

text = 'machinelearningplus.com'
print(re.findall('\.', text))  # matches a period
print(re.findall('[^\.]', text))

text = '01, Jan 2015'
print(re.findall('\d+', text))

text = '01, Jan 2015'
print(re.findall('\D+', text)) 

text = '01, Jan 2015'
print(re.findall('\w+', text)) 

text = '01, Jan 2015'
print(re.findall('\W+', text))

text = '01, Jan 2015'
print(re.findall('[a-zA-Z]+', text))

text = '01, Jan 2015'
print(re.findall('\d{4}', text))  # {n} Matches repeat n times.
print(re.findall('\d{2,4}', text))

print(re.findall(r'Co+l', 'So Cooool Coool cool coool col')) 

print(re.findall(r'Pi*lani', 'Pilani dfbdfb fgfgf'))

print(re.findall(r'colou?r', 'color'))

re.findall(r'\btoy\b', 'play toy broke toys')

emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
re.findall(pattern, emails, flags=re.IGNORECASE)

#Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.""" 

import re
re.findall(r'\bB\w+', text, flags=re.IGNORECASE)

#Split the following irregular sentence into words
sentence = """A, very   very; irregular_sentence"""

import re
" ".join(re.split('[;,\s_]+', sentence))

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

import re

def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
    tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    tweet = re.sub('@\S+', '', tweet)  # remove mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    return tweet
print(clean_tweet(tweet))