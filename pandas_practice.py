import pandas as pd
import matplotlib.pyplot as plt  #pyplot is a collection of function that make matplotlib work as MATLAB
import os

def analyze_agrostar_data(file_path='Task_1.csv'):
    # Safety check to see if the user actually has the file
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' was not found.")
        print("Please download 'Task_1.csv' from the AgroStar case study and place it in this directory.")
        return
    
    df = pd.read_csv(file_path)

    df['Order Date & Time'] = pd.to_datetime(df['Order Date & Time'] ,format='mixed' , errors='coerce')

    df_filtered =df[df['Order Date & Time'] <= '2018-08-31' ]



    df_filtered = df_filtered[df_filtered['Order Status'].str.lower() != 'cancelled']



    location_ranking = df_filtered.groupby(['Shipping City','Corrected City']).agg(
       Total_Revenue = ('Order Value','sum'),
       Unique_Customer = ('Customer ID','nunique'),
       Total_order =('Order ID','count')
    ).reset_index()

    location_ranking['order_per_farmer'] = location_ranking['Total_order'] / location_ranking['Unique_Customer']

    top_locations = location_ranking.sort_values(by='Total_Revenue' , ascending=False)

    top5 = top_locations.head(5).copy()
    print(top5)
    
    # Chart 1 - Revenue by City
    plt.figure(figsize=(8, 5))
    plt.bar(top5['Corrected City'], top5['Total_Revenue'], color='steelblue')
    plt.title('Top 5 Cities by Revenue')
    plt.xlabel('City')
    plt.ylabel('Revenue')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('revenue_by_city.png')
    plt.show()

    # Chart 2 - Orders per Farmer by City
    plt.figure(figsize=(8, 5))
    plt.barh(top5['Corrected City'], top5['order_per_farmer'], color='coral')
    plt.title('Orders per Farmer — Top 5 Cities')
    plt.xlabel('Orders per Farmer')
    plt.ylabel('City')
    plt.tight_layout()
    plt.savefig('orders_per_farmer.png')
    plt.show()

    # Chart 3 - Unique Customers vs Revenue
    plt.figure(figsize=(10, 6))
    plt.scatter(location_ranking['Unique_Customer'], 
                location_ranking['Total_Revenue'], 
                color='green', s=100, alpha=0.6)

    # Label only top 5 cities
    for i, row in top5.iterrows():
        plt.annotate(row['Corrected City'], 
                    (row['Unique_Customer'], row['Total_Revenue']),
                    textcoords='offset points', xytext=(8, 4), fontsize=9, color='red')

    plt.title('Unique Customers vs Total Revenue — All Cities')
    plt.xlabel('Unique Customers')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.savefig('customers_vs_revenue.png')
    plt.show()

analyze_agrostar_data()
