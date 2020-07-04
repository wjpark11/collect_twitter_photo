import pandas as pd
import urllib.request
import os

df = pd.read_csv("tweet.csv", header=None)
df.columns = ['tweet', 'num', 'url']

df['name'] = df['tweet'].str.extract(r'(수영|에바|퐁요|미아|에스마|썸머|엘리|아나|Ana|하이디|세희|새희|유나|Yuna|핑크|제니|Jenny|Aille|제시카|리나|Lina|디디|DD|타티|타니아|타타|해나|나나|nana|세라|새라|리사|카밀)')

df = df.fillna('기타')

df['name'].replace(['Camille'], '카밀', inplace=True)
df['name'].replace(['tah','타티','타니아'], '타타', inplace=True)
df['name'].replace(['Jenny'], '제니', inplace=True)
df['name'].replace(['DD','D D','Dd', 'Deedee', 'Dee dee','dd'], '디디', inplace=True)
df['name'].replace(['새라','Sara', '사라'], '세라', inplace=True)
df['name'].replace(['Dior'], '디오', inplace=True)
df['name'].replace(['Nana', 'nana'], '나나', inplace=True)
df['name'].replace(['pony', 'Pony'], '포니', inplace=True)
df['name'].replace(['로젠', '로제'], '로제린', inplace=True)
df['name'].replace(['아나', 'Ana'], '안나', inplace=True)
df['name'].replace(['세희', '새희'], '하이디', inplace=True)
df['name'].replace(['Yuna'], '유나', inplace=True)
df['name'].replace(['Lina'], '리나', inplace=True)

df['num'].replace(0,'',inplace=True)

df = df.sort_values(by=['name'])

df['tweet'] = df['tweet'].str.extract(r'(?:RT\s[^\s]*\s)?(.*)https')

df['tweet'] = df['tweet'].str.replace('w/h', '', regex=True)
df['tweet'] = df['tweet'].str.replace('W/h', '', regex=True)
df['tweet'] = df['tweet'].str.replace(r'/', '', regex=True)
df['tweet'] = df['tweet'].str.strip()
df['tweet'] = df['tweet'].str.replace(r'\s\s+','', regex=True)

df["num"]= df["num"].astype('str') 
new = df['num'].copy()

df["tweet"]= df["tweet"].str.cat(new, sep ="") 

df = df.drop_duplicates(subset='url', keep='first')

df = df.reset_index()
df = df.drop('index', axis=1)

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
