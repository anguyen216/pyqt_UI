### Author: Jialin Cui 
### Refactored by Anh Nguyen
import os
import pandas as pd
import numpy as np 
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

class Metrics():
    def __init__(self, path_to_file):
        self._ds = pd.read_csv(path_to_file)
        # remove leading and trailing space in column names
        self._ds.columns = self._ds.columns.str.strip()
        self._pop_lang = set(['Python','JavaScript','Java','TypeScript','Go','C++','Ruby','PHP','C#','C'])
        self._langs = ['AlanguageInfo','BlanguageInfo','ClanguageInfo','DlanguageInfo']

    def get_datatable(self):
        return self.dataframe

    ## extract language numbears and popular language size
    def _getLanguageNumberAndSize(self):
        for index, row in self._ds.iterrows():
            for item in self._langs:
                col1 = item + 'count'
                col2 = item + 'size'
                ls = str(self._ds.at[index, item])
                lcount = set()
                lsize = 0
                if ls != 'nan':
                    ls = ls.split(';')
                    for l in ls:
                        lname, lsize = l.split(':')
                        lname = lname.strip()
                        lsize = int(lsize.strip())
                        lcount.add(lname)
                        if lname in self._pop_lang:
                            lsize += lsize
                self._ds.at[index, col2] = lsize
                self._ds.at[index, col1] = len(lcount)

    def constructMetricsTable(self):
        self._getLanguageNumberAndSize()
        self.dataframe = self._ds[['GitHub']].copy(deep=True)
        # # lifespan
        self.dataframe['lifespan'] = self._ds['lifeSpan']

        # RestrictedContributionsCount + CommitContributions = A
        commits = ['RestrictedContributionsCount','CommitContributions'] 
        self.dataframe['A'] = self._ds[commits].sum(axis=1)

        # commitComments + issueComments + gistComments + repositoryDiscussionComments + repositoryDiscussions = B
        comments = ['commitComments','issueComments','gistComments','repositoryDiscussionComments','repositoryDiscussions']
        self.dataframe['B'] = self._ds[comments].sum(axis=1)

        # PullRequestReviewContributions + pullRequests = C
        PR = ['PullRequestReviewContributions','pullRequests']
        self.dataframe['C'] = self._ds[PR].sum(axis=1)

        # Issues + gists + projects = D
        issues = ['issues','gists','projects']
        self.dataframe['D'] = self._ds[issues].sum(axis=1)

        # A lang numbers + C langs numbers = E
        lang_AC_num = ['AlanguageInfocount', 'ClanguageInfocount']
        self.dataframe['E'] = self._ds[lang_AC_num].sum(axis=1)

        # A lang size + C lang size = F
        lang_AC_size = ['AlanguageInfosize', 'ClanguageInfosize']
        self.dataframe['F'] = self._ds[lang_AC_size].sum(axis=1)

        # B lang numbers + D langs numbers = G
        lang_BD_num = ['BlanguageInfocount', 'DlanguageInfocount']
        self.dataframe['G'] = self._ds[lang_BD_num].sum(axis=1)

        # B lang size + D lang size = H
        lang_BD_size = ['BlanguageInfosize', 'DlanguageInfosize']
        self.dataframe['H'] = self._ds[lang_BD_size].sum(axis=1)

        # A + B + C + D count = I
        ABCD_count = ['repoACount', 'repoBCount', 'repoCCount', 'repoDCount']
        self.dataframe['I'] = self._ds[ABCD_count].sum(axis=1)

        # A fork,star,watch + C fork,star,watch = J
        AC_fsw = ['forkACount', 'stargazerACount', 'Awatchers',
                'forkCCount', 'stargazerCCount', 'Cwatchers']
        self.dataframe['J'] = self._ds[AC_fsw].sum(axis=1)

        # B fork,star,watch + D fork,star,watch = K
        BD_fsw = ['forkBCount', 'stargazerBCount', 'Bwatchers',
                'forkDCount', 'stargazerDCount', 'Dwatchers']
        self.dataframe['K'] = self._ds[BD_fsw].sum(axis=1)

        # A size + C size = L
        AC_size = ['repoASize', 'repoCSize']
        self.dataframe['L'] = self._ds[AC_size].sum(axis=1)

        # B size  + D size = M
        BD_size = ['repoBSize', 'repoDSize']
        self.dataframe['M'] = self._ds[BD_size].sum(axis=1)

    
