# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

# Import required libraries
import pandas as pd
import numpy as np

# Welcome message
print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

from io import StringIO

# Simulated CSV content
csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No
"""

# Create a StringIO object (simulates a file)
sales_data_csv = StringIO(csv_content)

# TODO 1: Load and Explore the Dataset

# 1.1 Load the dataset into a DataFrame called 'sales_df'
sales_df = pd.read_csv(sales_data_csv)

# 1.2 Display the first 5 rows
print("\nFirst 5 rows of the dataset:")
print(sales_df.head()) #the .head method automatically displays the first 5 rows, from 0 to 4

# 1.3 Display basic information about the DataFrame
print("\nDataFrame Info:")
sales_df.info() #the .info method shows the structure of the data, like the number of rows, the column names, and their data types 

# 1.4 Display the dimensions (rows, columns)
print(f"\nDataFrame Dimensions: {sales_df.shape[0]} rows x {sales_df.shape[1]} columns") #the .shape attribute will return a tuple consisting of rows and columns, we use index 0 and index 1 to indicate the starting points

# 1.5 Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(sales_df.describe()) #the .describe method shows math statistics about the data we give it, it returns operations like the mean, the count, and the standard deviation

# TODO 2: Column Selection and Basic Analysis

# 2.1 Select and display only 'Product', 'Units', and 'Total_Sales' columns
print("\nProduct, Units, and Total_Sales columns:")
print(sales_df[['Product', 'Units', 'Total_Sales']]) #this will select a smaller view of the table, only selecting the three columns with its data 

# 2.2 Calculate total units sold (skipna=True handles the one NaN in Units)
total_units = sales_df['Units'].sum() #the .sum method will add all the values inside the units column, and then we print it
print(f"\nTotal Units Sold: {total_units}") 

# 2.3 Calculate total sales revenue
total_revenue = sales_df['Total_Sales'].sum() #we do the same with the .sum method, but this time we select total sales instead of units, to get our revenue
print(f"Total Revenue: ${total_revenue:,.2f}")

# 2.4 Calculate average unit price 
avg_unit_price = sales_df['Unit_Price'].mean() #the .mean method will sum the values in unit price and divide them with the number of units, to get an average
print(f"Average Unit Price: ${avg_unit_price:.2f}")

# TODO 3: Row Selection and Filtering

# 3.1 Filter: North America region only
na_sales = sales_df[sales_df['Region'] == 'North America'] #the double equal sign will only return the rows that region equals north america, fitlering the data frame 
print(f"\nNorth America Sales ({len(na_sales)} records):")
print(na_sales)

# 3.2 Filter: Units sold > 20
high_volume_sales = sales_df[sales_df['Units'] > 20] #we will filter all the rows where units sold where higher than 20 
print(f"\nHigh Volume Sales - Units > 20 ({len(high_volume_sales)} records):")
print(high_volume_sales)

# 3.3 Filter: PhoneX products that were on promotion
phonex_promo = sales_df[(sales_df['Product'] == 'PhoneX') & (sales_df['Promotion'] == 'Yes')] #we will filter all the products where the promotion row was equal to yes, and only the phone x product, where the product equals to phone x
print(f"\nPhoneX On Promotion ({len(phonex_promo)} records):")
print(phonex_promo)

# 3.4 Filter: February 2024 sales using string method on Date column
feb_sales = sales_df[sales_df['Date'].str.startswith('2024-02')] #this will filter all the sales and return the ones that had a date starting with 2024-02
print(f"\nFebruary 2024 Sales ({len(feb_sales)} records):")
print(feb_sales)

# TODO 4: Advanced Filtering and Analysis

# 4.1 Find the product with the highest total sales
# Group by Product, sum Total_Sales, then find the idxmax
product_totals = sales_df.groupby('Product')['Total_Sales'].sum() #the groupby  method will divide the data fram into groups based on their column, add them, and bring them back together 
best_product = product_totals.idxmax() #the idmax method will look for the name of the highest value 
print(f"\nBest Product (Highest Total Sales): {best_product} (${product_totals[best_product]:,.2f})")

# 4.2 Total sales by region, sorted descending
sales_by_region = sales_df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False) #the .groupby method again, will split the data, sum it, and then will sort it from max value to the min value, because ascending was put to false
print("\nSales by Region (Descending):")
for region, val in sales_by_region.items():
   print(f"  {region} total sales = ${val:,.2f}")

# 4.3 Average units sold per category
avg_units_by_category = sales_df.groupby('Category')['Units'].mean() #the .mean method will sum all the units and divide them with the number of units to get an average, and then group it by category
print("\nAverage Units Sold per Category:")
print(avg_units_by_category)

# 4.4 Promotion effectiveness comparison
promo_df = sales_df[sales_df['Promotion'] == 'Yes'] #the double equal sign will set the variables and link them to yes and no strings, and we will compare them with the sales without promotion
no_promo_df = sales_df[sales_df['Promotion'] == 'No']

promo_comparison = {
    'promo_avg_sales': promo_df['Total_Sales'].mean(), 
    'no_promo_avg_sales': no_promo_df['Total_Sales'].mean(),
    'promo_total_revenue': promo_df['Total_Sales'].sum(),
    'no_promo_total_revenue': no_promo_df['Total_Sales'].sum()
}
print("\nPromotion Comparison:")
for key, val in promo_comparison.items():
    print(f"  {key}: ${val:,.2f}")


# TODO 5: Missing Value Detection and Reporting

# 5.1 Count missing values per column
missing_counts = sales_df.isnull().sum() #the .isnull method checks every cell and returns a true or false for each cell, and then we use sum to see how many of the values are missing 
print("\nMissing Value Counts per Column:")
print(missing_counts)

# 5.2 Percentage of missing values per column
missing_percentages = (sales_df.isnull().sum() / len(sales_df)) * 100 #we take the missing value counts, we sum them, and divide them by the number of rows. Lastly, we multiply them by 100 to get a percentage
print("\nMissing Value Percentages per Column:")
print(missing_percentages)

# TODO 6: Insights and Business Analysis

# 6.1 Top-performing category by total sales in each region
top_categories_by_region = (
    sales_df.groupby(['Region', 'Category'])['Total_Sales']
    .sum()
    .groupby(level='Region')
    .idxmax()
    .apply(lambda x: x[1])  # Extract just the Category name from the (Region, Category) tuple
)
print("\nTop-Performing Category by Region:")
print(top_categories_by_region)

# 6.2 Average unit price for each product category
avg_price_by_category = sales_df.groupby('Category')['Unit_Price'].mean()
print("\nAverage Unit Price by Category:")
print(avg_price_by_category)

# 6.3 Total revenue and percentage of overall sales per product
product_total_revenue = sales_df.groupby('Product')['Total_Sales'].sum()
product_revenue_analysis = pd.DataFrame({
    'total_revenue': product_total_revenue,
    'percentage': (product_total_revenue / total_revenue) * 100 #the pd.dataframe will create a new data frame with only the total revenue and what percentage it represents 
    })
print("\nProduct Revenue Analysis:")
print(product_revenue_analysis.sort_values('total_revenue', ascending=False))

# TODO 7: Generate Analysis Report

print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

# 7.1 Overall sales performance
avg_sale_value = total_revenue / len(sales_df)
print("\nOverall Performance:")
print(f"- Total Revenue: ${total_revenue:,.2f}")
print(f"- Total Units Sold: {int(total_units)}")
print(f"- Average Sale Value: ${avg_sale_value:.2f}") #we print the overall performance

# 7.2 Regional performance summary
print("\nRegional Performance:")
for region, sales in sales_by_region.items():
    print(f"{region}: ${sales:,.2f}") #we print the sales, but now by region

# 7.3 Product category performance
print("\nCategory Performance:")
for category in avg_units_by_category.index:
    avg_units = avg_units_by_category[category]
    avg_price = avg_price_by_category[category]
    print(f"{category}: Avg Units: {avg_units:.1f}, Avg Price: ${avg_price:.2f}") 

# 7.4 Promotion effectiveness
print("\nPromotion Effectiveness:")
print(f"- Promoted Items Avg Sale: ${promo_comparison['promo_avg_sales']:.2f}")
print(f"- Non-Promoted Items Avg Sale: ${promo_comparison['no_promo_avg_sales']:.2f}")
print(f"- Revenue from Promotions: ${promo_comparison['promo_total_revenue']:,.2f}")

# 7.5 Data quality report
columns_with_missing = missing_counts[missing_counts > 0].index.tolist()
total_missing = missing_counts.sum()
print("\nData Quality Report:")
print(f"- Missing Values Found: {columns_with_missing}")
print(f"- Total Missing Entries: {total_missing}")

# 7.6 Key business recommendations
print("\nKEY BUSINESS RECOMMENDATIONS:")

print("""
Recommendation 1. Invest more in the Computers category because computers have the highest average unit price at $966.66, meaning each sale generates significantly more revenue than any other category.
Recommendation 2. Increase SmartWatch promotions because SmartWatch is currently never on promotion yet consistently sells across multiple regions, meaning a targeted promotion could boost its steady sales volume.
Recommendation 3. Focus on growing PhoneX salesbecause PhoneX is the best performing product that gets a big part of the revenue at $35,099. 
 """)