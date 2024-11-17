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
change data path at main function 
default path ("C:\Work\EarthlyE\data.xlsx")
e.g.
```
if __name__ == '__main__':
    dashboard = StoreDashboard('C:/Work/EarthlyE/data.xlsx') # replace your data path here
    dashboard.run_dashboard()
```
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

 ### 🔗Contact Me
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white&link=mailto:mahmoudnasraly@gmail.com)](mailto:mahmoudnasraly@gmail.com)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
)](https://www.linkedin.com/in/mahmoud-nasr-832627201/)
[![CodePen.io](https://img.shields.io/badge/Codepen-000000?style=for-the-badge&logo=codepen&logoColor=white)](https://codepen.io/MahmoudNasrAly)
[![Whatsapp](https://img.shields.io/badge/-Whatsapp-075e54?style=for-the-badge&logo=Whatsapp&logoColor=white)](https://api.whatsapp.com/send?phone=01552416449)
