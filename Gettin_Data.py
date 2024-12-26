import yfinance as yf
import pandas as pd


def GetData(company_name, start_date, end_date): 
    data = yf.download(company_name, start=start_date, end=end_date)
    print("Data downloaded successfully!")
    print("Columns in Data:", data.columns)  # Check the columns
    data.reset_index(inplace=True)  # Reset index to make 'Date' a column
    return data

def showing_data_info(data):
    print("Initial data info:\n")
    print(pd.DataFrame(data.info()))
    print(data.isnull().sum())
    
def Clean_data(data):
    
    def Drop_missing_data(data , showmissing=False):
        data = data.dropna()
        if showmissing == True:
            print("Data after dropping null values:")
            print(data.info())
        return data  # Add return statement here

    def remove_outlines(data , showoutliners = False , showdata = False):
        # remove outliers using IQR method 
        Q1 = data['Close'].quantile(0.25)
        Q3 = data['Close'].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = data[(data["Close"] < lower_bound) | (data["Close"] > upper_bound)]
        data = data[(data["Close"] >= lower_bound) & (data["Close"] <= upper_bound)]
        
        if showoutliners == True:
            print(f"Number of outliers: {len(outliers)}")
            print(outliers)

        if showdata == True:
            print("Data after removing outliers:")
            print(data.info())
        return data  

    data = Drop_missing_data(data)
    data = remove_outlines(data)
    return data

def save_data (data ):
    data.to_csv("Cleaned_Data_Stocks.csv", index=True, date_format='%Y-%m-%d')
    print("Data saved successfully!")
    
# This code defines a series of functions to collect, preprocess, and visualize stock data for a specified company.
# It includes data downloading, handling missing values, removing outliers, plotting the cleaned data, and saving it to a CSV file.