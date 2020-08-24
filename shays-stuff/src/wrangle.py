import pandas as pd

def get_space_data():
    # Pull in the data into a pandas data frame
    df = pd.read_csv('../data/Space_Corrected.csv')
    return df