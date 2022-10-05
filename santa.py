import os
import pandas as pd

def get_persons_dataframe():
    """read persons.csv and convert the data in a DataFrame"""
    file_path = f'{os.path.dirname(__file__)}\\persons.csv'
    df = pd.read_csv(file_path)
    df.columns = [col.upper() for col in df.columns]
    df = df.convert_dtypes()
    if 'ID' in df and df['ID'].is_unique:
        if "NOT MATCHING" in df:
            df['NOT MATCHING'] = df['NOT MATCHING'].fillna("").map(
                lambda x: x.split(' '))
        return df
    else:
        return False


def main():
    df = get_persons_dataframe()
    print(df)

if __name__ == "__main__":
    main()