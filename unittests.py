import unittest
import pandas as pd


def mean(arr):
    return sum(arr)/len(arr)

def clean(df):
    return df.fillna(0)

def join_df(df1,df2):
    return pd.concat([df1,df2])

class MyTest(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1,2,3]),2)
    def test_clean_df(self):
        df = pd.DataFrame([[1,2],[3,4]], columns=['col1','col2'])
        self.assertTrue(clean(df).columns.tolist() == df.columns.tolist())
    def test_df(self):
        df1 = pd.DataFrame([[1,2],[3,4]], columns=['col1','col2'])
        df2 = pd.DataFrame([[1,3],[1,5]], columns=['col1','col2'])
        self.assertTrue((join_df(df1,df2).isnull().mean() <0.2).all())
