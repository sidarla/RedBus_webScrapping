import streamlit as st
import pandas as pd


data =pd.read_csv(r"C:/Users/Dell/OneDrive/Desktop/streamlit/telanagana_buses.csv")
df = pd.DataFrame(data)

# Custom CSS to change font size of the title
st.markdown(
    """
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
        color: #fff; 
        font-family:'bree serif';
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Using custom class in markdown to change title font size
st.sidebar.markdown('<p class="big-font">Welcome to Red Bus</p>', unsafe_allow_html=True)



st.markdown(
    """
    <style>
    .big-font {
        font-size:25px !important;
        font-weight: bolder;
        color: #fff; 
        font-family:'Monoton';
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Using custom class in markdown to change title font size


st.sidebar.markdown('<p class="big-font">Home</p>', unsafe_allow_html=True)
Select_state=st.sidebar.selectbox("# Select the State",["Telangana","Andhra Pradesh","Kerala","Tamil nadu","Punjab",""],index=5)
if st.sidebar.button("Submit State"):
    st.write(f"You selected the Bus is: {Select_state}")
    

st.markdown(
    """
    <style>
    /* Change background color of the sidebar */
    [data-testid="stSidebar"] {
        background-color:#e3093c;
        color:#fff;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


# Main Page


st.markdown(
    """
    <style>
    .custom-title {
        color: #e3093c;  /* Red color */
        font-size: 40px;
        font-family: 'playfair display';
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f'<h1 class="custom-title">{Select_state} Bus Booking System</h1>', unsafe_allow_html=True)


 
route=st.selectbox("Select the Route",['Khammam to Hyderabad','Hyderabad to Vijayawada','Hyderabad to Vijayawada','Vijayawada to Hyderabad','Kakinada to Visakhapatnam','Bangalore to Tirupati','Tirupati to Bangalore'])
#unique_routes = df['route_name'].unique()

#route = st.selectbox("Select the Route", unique_routes)





# Select Seat Type
seat_type = st.selectbox("Select the Seat Type", ["Sleeper", "Seater"])

# Select AC Type
ac_type = st.selectbox("Select the AC Type", ["A/C", "Non A/C"])

# Select Ratings
rating_filter = st.selectbox("Select the Ratings", ["2 to 3","3 to 4", "4 to 5"])

# Starting Time Filter
time_filter = st.selectbox("Starting time", ["22:00 - 23:00", "23:00 - 00:00"])

# Bus Fare Range
fare_range = st.selectbox("Bus Fare Range", ["others", "300-500", "500-1000"])






# Inject custom CSS for button styling
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #e0073a; /* Green background */
        color: white;             /* White text */
        padding: 10px 24px;       /* Add padding */
        text-align: center;       /* Center the text */
        text-decoration: none;    /* Remove underline */
        display: inline-block;    /* Make it inline */
        font-size: 16px;          /* Font size */
        margin: 4px 2px;          /* Add some margin */
        cursor: pointer;          /* Cursor on hover */
        border-radius: 12px;
        border-width:2px;
        border-color:#fff;      /* Rounded corners */
    }

    div.stButton > button:hover {
        background-color: #fff;
        color:#000; /* Darker shade of green on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Create the button
if st.button('Click Me'):
    filtered_df = df[df['route_name'] == route]
    #filtered_df = filtered_df[filtered_df['bustype'] == seat_type]
    filtered_df = filtered_df[filtered_df['star_rating'].between(float(rating_filter.split(' ')[0]), float(rating_filter.split(' ')[2]))]
    #filtered_df = filtered_df[filtered_df['Price'].between(int(fare_range.split('-')[0]), int(fare_range.split('-')[1]))] if fare_range != 'others' else filtered_df
    if(Select_state=="Telangana"):
        if not filtered_df.empty:
            st.write("### Available Buses................")
            st.dataframe(filtered_df[['route_name', 'route_link', 'busname', 'bustype', 'duparting_time', 'duration', 'reaching_time', 'star_rating', 'Price', 'Seats_Available']])
    elif(Select_state=="Andhra Pradesh"):
        st.write("### Available Buses......................")
        st.dataframe(filtered_df[['route_name', 'route_link', 'busname', 'bustype', 'duparting_time', 'duration', 'reaching_time', 'star_rating', 'Price', 'Seats_Available']])
    
