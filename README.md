# Store Management Dashboard  

This project provides a robust **Store Management Dashboard** built with Python, Dash, and Plotly. It allows for efficient visualization and analysis of store inventory data, tracking missing items, staff performance, and time-based trends.  

---

## Features  

1. **Interactive Dashboard**  
   - Key Performance Indicators (KPIs): Total Missing Items, Highest Missing Quantities, etc.  
   - Filters for Date Range, Staff, and Category.  
   - Visualizations:  
     - Missing Items Trend Over Time.  
     - Missing Items by Category, Staff, and Time of Day.  

2. **Quick Data Visualization**  
   - A standalone function (`visualize_data`) for quick dataset insights.  

3. **Dynamic Filtering**  
   - Data dynamically updates when filters are applied.  

---

## Installation  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/MahmoudNasrAly/EarthyE/store-management-dashboard.git  
   cd store-management-dashboard

2.Install Dependencies
Ensure Python 3.8+ is installed, then install the required libraries:
  ```bash 
pip install pandas plotly dash openpyxl
```
3.set up your data 
change data path 
defalut path ("C:\Work\EarthlyE\data.xlsx")

4.Run the Dashboard

Update the data_path in the script to point to your data file (e.g., C:/Work/EarthlyE/data.xlsx).

Execute
```
python dashboard.py
```
Dash will be running on http://127.0.0.1:8050/

Usage
Dashboard Mode
Run the dashboard to explore:

Missing items trends.
Staff and category analysis.
Daily performance insights.
Quick Data Visualization
To visualize data directly without launching the dashboard:

Update the data_path in the script with your file path.
Call visualize_data(data_path) in a Python environment.

store-management-dashboard/  
│  
├── dashboard.py               # Main application file.  
├── data.xlsx             # Your inventory dataset (add your file here).  
└── README.md             # Documentation.  

Contribution
Contributions are welcome! Open an issue or submit a pull request.

