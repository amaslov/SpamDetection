import numpy as np

## lowerCase(list[] documents).
## outputs the list of documents converted to lower case
def lowerCase(documents):
    lowerCaseDocuments=[]
    for i in documents:
        lowerCaseDocuments.append(i.lower())
    return(lowerCaseDocuments)
import re, string

## sansPunct(list[] documents)
## outputs the list of documents with string.punctuation removed
def sansPunct(documents):
    sansPunctDocuments=[]
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    for i in documents:
        sansPunctDocuments.append(regex.sub('',i))
    return(sansPunctDocuments)

