def mission_result(df):
    # Creating a new column and setting it's default as 1
    df['mission_result'] = 1
    
    # Slicing by the rows that contain a failure, then setting the result to 0
    df.loc[df.mission_status.str.contains('Failure'), 'mission_result'] = 0

    return df