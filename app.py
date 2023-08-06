import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

# Load the Mart Sales dataset
@st.cache
def load_data():
    df =  pd.read_csv('Order.tsv',sep='\t',header=0)
df.head()

def main():
    st.title("Mart Sales Data Analysis")
    
    # Load the dataset
    df = load_data()
    
    st.write("## Mart Sales Dataset")
    st.write(df.head())  # Display the first few rows of the dataset
    
    # Basic statistics
    st.write("## Basic Statistics")
    st.write(df.describe())
    
    # Interactive components
    st.write("## Interactive Components")
    
    # Sidebar filters
    st.sidebar.title("Filters")
    category = st.sidebar.selectbox("Select Category", df['Category'].unique())
    filtered_data = data[data['Category'] == category]
    
    # Display filtered data
    st.write(f"Displaying data for Category: {category}")
    st.write(filtered_df)
    
    # Data visualization
    st.write("## Data Visualization")
    
    # You can add plots and charts here using the data
    
if __name__ == "__main__":
    main()
