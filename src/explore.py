# Imports

#for data manipulation
import pandas as pd

#data visualization
import seaborn as sns
import matplotlib.pyplot as plt



def distro_plot_for_single_column(dataframe, column_name):
    """Taked in a dataframe name and column name
    and return a distrobution plot for that column"""
    
    #Set figure size for all plots
    plt.rc("figure", figsize = (16,16))

    #Set fontsize for titles
    plt.rc("font", size=14)
    
    #Set color for distro plot
    c = "#5B0A91"
    plt.title(f"Distribution plot for {column_name}")
    sns.distplot(dataframe[column_name], color = c)


def ditro_plot_for_entire_df(df):
    """
    Takes in a numerical only dataframe such as a crosstab
    and returns Distribution plots for each column in the
    dataframe.
    """
    for i, col in enumerate(df.columns):
        plt.figure(i)
        distro_plot_for_single_column(df, col)
        

def mission_status_distro_plot(df):
    """
    Takes i the sapce dataframe and returns a
    barplot for the number of launches for 
    each Status mission
    """
    #ccreate a df that counts the missions for each status
    df_1 = df["mission_status"].value_counts().reset_index()
    
    plt.figure("figure", figsize = (16,16))
    sns.barplot(df_1["index"], df_1["mission_status"], color="#39FF14")
    plt.title("Number of missions by Mission Status", fontsize = 14)
        

        
def success_percent_by_country(df):
    """
    Takes in the space df and returns a table with the following by Country:
    Failure
    Partial Failure
    Prelaunch Failure
    Success
    Succes in percent
    """
    table = pd.pivot_table(df, values='year', index='country',
                    columns='mission_status', aggfunc='count', fill_value=0)
    table['Success (in prc)'] = table['Success'] / table.sum(axis=1)
    return table.style.format({'Success (in prc)' : '{:.2%}'})\
               .background_gradient(cmap='Reds')\
               .background_gradient(cmap='Greens',subset=["Success"])\
               .background_gradient(cmap='Greens',subset=["Success (in prc)"])