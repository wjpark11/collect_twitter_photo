import pandas as pd
import urllib.request
import os

df = pd.read_csv("tweet.csv", header=None)
df.columns = ['tweet', 'url']

df['name'] = df['tweet'].str.extract(r'(나나|카밀|디디|세라|사라|타타|제니|Camille|tah|Jenny|DD|D\sD|리나|Nana|새라|안나|Sara|밀러|디오|리사|nana|Dee.*dee|Dd|pony|Pony|Dior)')

df = df[~df['name'].isnull()]

df['name'].replace(['Camille'], '카밀', inplace=True)
df['name'].replace(['tah'], '타타', inplace=True)
df['name'].replace(['Jenny'], '제니', inplace=True)
df['name'].replace(['DD','D D','Dd', 'Deedee', 'Dee dee'], '디디', inplace=True)
df['name'].replace(['새라','Sara'], '세라', inplace=True)
df['name'].replace(['Dior'], '디오', inplace=True)
df['name'].replace(['Nana', 'nana'], '나나', inplace=True)
df['name'].replace(['pony', 'Pony'], '포니', inplace=True)

df = df.sort_values(by=['name'])

df['tweet'] = df['tweet'].str.extract(r'(?:RT\s@p9CKSFueA8q37pg:)?(.*)https')
df = df.reset_index()
df = df.drop('index', axis=1)

df['tweet'] = df['tweet'].str.replace('w/h', '', regex=True)
df['tweet'] = df['tweet'].str.replace('W/h', '', regex=True)

dirList = df['name'].unique()
iternum = df.shape[0]

for name in dirList:
    try:
        os.mkdir(name)
    except:
        pass

for i in range(iternum):
    try:
        urllib.request.urlretrieve(df['url'][i], f"{df['name'][i]}/{df['tweet'][i]}.jpg")
    except:
        print(df['tweet'][i])
