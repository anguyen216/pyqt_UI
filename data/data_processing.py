import os
import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

#################### data processing standard process #########################
path = os.getcwd() #os.path.abspath(__file__)
ds_path = path+'/S2019.csv'
ds = pd.read_csv(ds_path)
ds.columns = ds.columns.str.strip()  # remove leading and trailing space
# # extract language numbears and popular language size
pop_lang = ['Python','JavaScript','Java','TypeScript','Go','C++','Ruby','PHP','C#','C']
langs = ['AlanguageInfo','BlanguageInfo','ClanguageInfo','DlanguageInfo']
for index, row in ds.iterrows():
    for item in langs:
        col1 = item + 'count'
        col2 = item + 'size'
        ls = str(ds.at[index,item])
        lcount = set()
        lsize = 0
        if ls != 'nan':
            ls = ls.split(';')
            for l in ls:
                lname,lsize = l.split(':')
                lname = lname.strip()
                lsize = int(lsize.strip())
                lcount.add(lname)
                if lname in pop_lang:
                    lsize+=lsize
        ds.at[index,col2] = lsize
        ds.at[index,col1] = len(lcount)

dataframe = ds[['GitHub']].copy(deep=True)

# # lifespan
dataframe['lifespan'] = ds['lifeSpan']

# RestrictedContributionsCount + CommitContributions = A
commits = ['RestrictedContributionsCount','CommitContributions'] 
dataframe['A']=ds[commits].sum(axis=1)

# commitComments + issueComments + gistComments + repositoryDiscussionComments + repositoryDiscussions = B
comments = ['commitComments','issueComments','gistComments','repositoryDiscussionComments','repositoryDiscussions']
dataframe['B']=ds[comments].sum(axis=1)

# PullRequestReviewContributions + pullRequests = C
PR = ['PullRequestReviewContributions','pullRequests']
dataframe['C']=ds[PR].sum(axis=1)

# Issues + gists + projects = D
issues = ['issues','gists','projects']
dataframe['D']=ds[issues].sum(axis=1)

# A lang numbers + C langs numbers = E
lang_AC_num = ['AlanguageInfocount', 'ClanguageInfocount']
dataframe['E']=ds[lang_AC_num].sum(axis=1)

# A lang size + C lang size = F
lang_AC_size = ['AlanguageInfosize', 'ClanguageInfosize']
dataframe['F']=ds[lang_AC_size].sum(axis=1)

# B lang numbers + D langs numbers = G
lang_BD_num = ['BlanguageInfocount', 'DlanguageInfocount']
dataframe['G']=ds[lang_BD_num].sum(axis=1)

# B lang size + D lang size = H
lang_BD_size = ['BlanguageInfosize', 'DlanguageInfosize']
dataframe['H']=ds[lang_BD_size].sum(axis=1)

# A + B + C + D count = I
ABCD_count = ['repoACount', 'repoBCount', 'repoCCount', 'repoDCount']
dataframe['I']=ds[ABCD_count].sum(axis=1)

# A fork,star,watch + C fork,star,watch = J
AC_fsw = ['forkACount', 'stargazerACount', 'Awatchers',
          'forkCCount', 'stargazerCCount', 'Cwatchers']
dataframe['J']=ds[AC_fsw].sum(axis=1)

# B fork,star,watch + D fork,star,watch = K
BD_fsw = ['forkBCount', 'stargazerBCount', 'Bwatchers',
          'forkDCount', 'stargazerDCount', 'Dwatchers']
dataframe['K']=ds[BD_fsw].sum(axis=1)

# A size + C size = L
AC_size = ['repoASize', 'repoCSize']
dataframe['L']=ds[AC_size].sum(axis=1)

# B size  + D size = M
BD_size = ['repoBSize', 'repoDSize']
dataframe['M']=ds[BD_size].sum(axis=1)












