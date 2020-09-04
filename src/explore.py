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



def plot_rocket_type_and_status_by_company(df):
    """
    Takes in the space df and groups data into active and retired
    return 2 barplots:
    1. Number of Active Rocket Types for each Company
    2. Number of Retired Rocket Types for each Company    
    """
    
    #Group and split the data
    cmp = df.groupby(["company_name", "rocket_status"]).count()["rocket_type"].reset_index()
    active = cmp[cmp["rocket_status"] == "active"].sort_values("rocket_type")
    retired = cmp[cmp["rocket_status"] != "active"].sort_values("rocket_type")
    
    #Set the figure size for Active barplot
    plt.figure(figsize=(16,16))
    
    #Active Barplot
    chart = sns.barplot(x=active.company_name, y=active.rocket_type, color="green")
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.title("Number of Active Rocket Types for each Company", fontsize = 14)
    
    #Set the figure size for Retired barplot
    plt.figure(figsize=(16,16))
    
    #Retired Barplot
    chart1 = sns.barplot(x=retired.company_name, y=retired.rocket_type, color="red")
    chart1.set_xticklabels(chart1.get_xticklabels(), rotation=90)
    plt.title("Number of Retired Rocket Types for each Company", fontsize = 14)
    plt.show()
    
    
def plot_number_of_launches_per_company(df):
    """
    Takes in the space df and returns a
    bar plot thay shows the number of
    launches for each company in the data
    """
    
    #create a dataframe counting the number of times each company appears in a row
    company_numbers = df["company_name"].value_counts().reset_index()
    
    #rename the columns to mathc what they represent
    company_numbers.columns = ["company_name", "number_of_launches"]
    
    #create the barplot
    plt.figure(figsize=(16,24))
    sns.barplot(x = company_numbers.number_of_launches, y = company_numbers.company_name, color = "#39FF14")
    plt.title("Number of Launches per Company")
    plt.show()

    
def distribution_of_rocket_cost(df):
    """
    Takes in the space df and returns a distribution
    plot for mission costs. All values at zero have been 
    dropped as these did not have values to begin with.
    """
    #drop all values that are zero
    not_zero = df[df.mission_cost != 0]
    
    #make values into the millions
    not_zero.mission_cost = not_zero.mission_cost * 1000000
    
    #create the plot
    plt.figure(figsize = (16,16))
    sns.distplot(not_zero.mission_cost, kde = False, bins = 100, color = "#39FF14")
    plt.title("Distribution of Mission Cost - in Millions")
    plt.show()