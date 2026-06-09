# retail-store-location-analytics
Data-driven market optimization pipeline built with Python and Pandas to isolate high-yield, high-retention regional launch locations for physical retail expansion.

# AgroStar Retail Location Optimization Analysis

An data-driven exploratory analysis pipeline built with Python and Pandas to solve a strategic business intelligence problem: determining the optimal regional market launch for a physical agricultural retail presence.

## 📋 Case Scenario
Simulating a strategic decision checkpoint in **August 2018**, this pipeline evaluates multi-regional performance matrices across three states to isolate the highest-yield, highest-retention geographic sector for transitioning from an assisted-marketplace application framework to an offline brick-and-mortar operations model.

## 🛠️ Data Strategy & Pipeline Architecture
The analysis algorithm processes transactional log records up to the simulation boundary line via the following steps:
1. **Temporal Filtering:** Isolates dataset interactions strictly up to the August 31, 2018 data horizon.
2. **Data Cleansing:** Discards invalid transaction records by filtering out `CANCELLED` status profiles.
3. **Named Aggregations:** Groups distinct operations by distribution networks to calculate core localized consumer KPIs (`Total Revenue`, `Unique Customers`, and `Total Orders`).
4. **Loyalty Ratio Indexing:** Dynamically calculates an engineering frequency score (`Total Orders / Unique Customers`) to evaluate regional customer retention performance.

## 🚀 Getting Started
1. Clone this repository to your local directory.
2. Ensure you have Pandas installed via pip: `pip install pandas`
3. Place the source dataset `Task_1.csv` inside the primary directory root.
4. Execute the pipeline runtime script:
   ```bash
   python pandas_practice.py