import pandas as pd

smsLocation="../data/SMSSpamCollection"
listNames=['label', 'sms_message']
df=pd.read_table(smsLocation, sep="\t", names=listNames)
print (df.head())
df['label']=df.label.map({'ham':0, 'spam':1})
print(df.head())

import textProcessing as tp
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = tp.lowerCase(documents)
print(lower_case_documents)

sans_punct_documents=tp.sansPunct(lower_case_documents)
print(sans_punct_documents)

