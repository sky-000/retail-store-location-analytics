import pandas as pd
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

    print(top_locations.head(5).to_string(index=False))

