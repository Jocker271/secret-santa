"""
Created on 2022-11-01
by Johanes Wehden (Jocker271)
"""

import os, random
import pandas as pd

def get_santa_dataframe():
    """read persons.csv and convert the data in a DataFrame"""
    file_path = f'{os.path.dirname(__file__)}\\persons.csv'
    santa_df = pd.read_csv(file_path).convert_dtypes()
    santa_df.columns = [col.upper() for col in santa_df.columns]
    if 'ID' in santa_df and santa_df['ID'].is_unique:
        santa_df.set_index(['ID'], inplace=True)
        if "NOT MATCHING" in santa_df:
            santa_df['NOT MATCHING'] = santa_df['NOT MATCHING'].fillna("").map(
                lambda ids: ids.split(' '))
        return santa_df
    else:
        return False

def create_santa_matches(santa_df):
    for santa in len(santa_df):
        get_match()
    return True

def get_match(santa_df):
    return True

def main():
    santa_df = get_santa_dataframe()
    test = create_santa_matches(santa_df)
    print(santa_df)

if __name__ == "__main__":
    main()
