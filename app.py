import streamlit as st
import pandas as pd

# Load the Mart Sales dataset
@st.cache
def load_data():
    data = pd.read_csv("mart_sales_dataset.csv")
    return data

def main():
    st.title("Mart Sales Data Analysis")
    
    # Load the dataset
    data = load_data()
    
    st.write("## Mart Sales Dataset")
    st.write(data.head())  # Display the first few rows of the dataset
    
    # Basic statistics
    st.write("## Basic Statistics")
    st.write(data.describe())
    
    # Interactive components
    st.write("## Interactive Components")
    
    # Sidebar filters
    st.sidebar.title("Filters")
    category = st.sidebar.selectbox("Select Category", data['Category'].unique())
    filtered_data = data[data['Category'] == category]
    
    # Display filtered data
    st.write(f"Displaying data for Category: {category}")
    st.write(filtered_data)
    
    # Data visualization
    st.write("## Data Visualization")
    
    # You can add plots and charts here using the data
    
if __name__ == "__main__":
    main()
