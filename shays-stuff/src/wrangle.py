import pandas as pd

def get_space_data():
    # Pull in the data into a pandas data frame
    df = pd.read_csv('../data/Space_Corrected.csv')
    
    # drop excess columns generated by pandas
    df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'], inplace = True)
    
    # Rename the columns
    df.pipe(rename_columns)
    
    # Change the date column to a pandas datetime type
    df.date_time = pd.to_datetime(df.date_time)
    
    # Set the index to be the datetime column, then drop it from the dataframe
    df.set_index(df.date_time, inplace=True)
    df.drop(columns='date_time', inplace=True)
    
    # Fill missing values with 0
    df.mission_cost.fillna(0, inplace=True)
    
    return df

def rename_columns(df):
    new_col_names = ['company_name', 'location', 'date_time',
       'rocket_type', 'rocket_status', 'mission_cost', 'mission_status']
    
    df.columns = new_col_names
    
    return df