#!/usr/bin/env python
# coding: utf-8

# ## News Summarizer

# ### Import Packages

# In[2]:


from bs4 import BeautifulSoup
from requests import get
import sys
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import yake
from nltk.stem import SnowballStemmer

if len(sys.argv) != 2:
    print("Usage: python news_summarizer.py <url>")
    sys.exit(1)

url = sys.argv[1]
# #### Creating a function to Extract only text form <p> Tags

# In[3]:


def get_only_text(url):
    '''
    return the title and the text of the article 
    at the specified url
    '''
    page = get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = " ".join(map(lambda p : p.text, soup.find_all("p")))
    title = " ".join(soup.title.stripped_strings)
    return title, text


# #### calling the function with the url

# In[4]:


text = get_only_text(url)


# In[5]:





# #### Number of words from text[1] which is the text

# In[6]:


len(str.split(text[1]))


# #### Summarization

# In[7]:




# In[8]:


parser = PlaintextParser.from_string(text[1], Tokenizer("italian"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 5)  
print("Title : ",text[0])
print("Summary : ")
for s in summary:
    print(s)


# ## Keywords

# In[33]:



stemmer = SnowballStemmer("italian")
kw_extractor = yake.KeywordExtractor(lan="it", n=1, top=10)  # top 10 keywords
keywords = kw_extractor.extract_keywords(text[1])
for word in keywords:
    print(word[0])


# In[ ]:





# In[ ]:




