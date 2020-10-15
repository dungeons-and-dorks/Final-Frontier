import pandas as pd


def get_space_data():
    # Pull in the data into a pandas data frame
    df = pd.read_csv("../data/Space_Corrected.csv")

    # drop excess columns generated by pandas
    df.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], inplace=True)

    # Rename the columns
    df.pipe(rename_columns)

    # Fix the values within the rocket_status column
    df.pipe(fix_rocket_status)
    
    # Fix the values/type within mission_cost
    df.pipe(fix_mission_cost)

    # Change the date column to a pandas datetime type
    df.date_time = pd.to_datetime(df.date_time)
    
    # Create the year column
    df['year'] = df.date_time.apply(lambda datetime: datetime.year)
    
    # Create the Month column
    df['month'] = df.date_time.apply(lambda datetime: datetime.month)

    # Set the index to be the datetime column, then drop it from the dataframe
    df.set_index(df.date_time, inplace=True)
    df.drop(columns="date_time", inplace=True)

    # Fill missing values with 0
    df.mission_cost.fillna(0, inplace=True)
    
    df.pipe(get_country_name)
    return df


def rename_columns(df):
    new_col_names = [
        "company_name",
        "location",
        "date_time",
        "rocket_type",
        "rocket_status",
        "mission_cost",
        "mission_status",
    ]
    df.columns = new_col_names
    return df


def fix_mission_cost(df):
    df.mission_cost = df.mission_cost.str.replace(' ', '')
    df.mission_cost = df.mission_cost.str.replace(',', '')
    df.mission_cost.astype(float)
    return df


def fix_rocket_status(df):
    df.loc[df.rocket_status == "StatusRetired", "rocket_status"] = "retired"
    df.loc[df.rocket_status == "StatusActive", "rocket_status"] = "active"
    return df

def get_country_name(df):
    """
    Takes in the a dataframe and return the Country name in 
    a new column
    """
    df['country'] = df['location'].str.split(', ').str[-1]
    df['country'].loc[df['country'] == 'Shahrud Missile Test Site'] = "Iran"
    df['country'].loc[df['country'] == 'New Mexico'] = 'United States of America'
    df['country'].loc[df['country'] == 'Yellow Sea'] = "China"
    df['country'].loc[df['country'] == 'Pacific Missile Range Facility'] = "United States of America"
    df['country'].loc[df['country'] == 'Pacific Ocean'] = "United States of America"
    df['country'].loc[df['country'] == 'Barents Sea'] = 'Russia'
    df['country'].loc[df['country'] == 'Gran Canaria'] = 'United States of America'
    df['country'].loc[df['country'] == 'USA'] = 'United States of America'
    return df
