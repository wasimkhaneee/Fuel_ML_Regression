
import pickle
import streamlit as st

from zipfile import ZipFile


# loading the temp.zip and creating a zip object
with ZipFile("regression_walmart_rf.pkl.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall()

# loading the trained model
pickle_in = open('regression_walmart_rf.pkl', 'rb')
regressor = pickle.load(pickle_in)

@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs
def prediction(Store, Holiday, Temperature, Fuel_Price, CPI, Unemployment, Day, Week,Month,Year):
    if Holiday_Flag == "Holiday":
      Holiday_Flag = 1
    else:
      Holiday_Flag = 0
    # Making predictions
    prediction = regressor.predict(
        [[Store, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment, Day, Week,Month,Year]])

    return prediction


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;"> Pragyan AI Walmart Sale Prediction ML App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    Store = st.number_input("EnterNumber of Store Number",min_value=1, max_value=50)
    Holiday = st.selectbox('Holiday Status',("Holiday","Not Holiday"))
    Temperature = st.number_input("Enter The Temperature value", min_value=1.0, max_value=75.0)
    Fuel_Price = st.number_input("Enter The Fuel_Price value", min_value=1.0, max_value=75.0)
    CPI = st.number_input("Enter The CPI value", min_value=100.0, max_value=250.0)
    Unemployment = st.number_input("Enter Unemployment Rate", min_value=1.0, max_value=20.0)
    Day = st.number_input("Enter The Day of Week",min_value=0, max_value=6)
    Week = st.number_input("Enter The Week of the Year",min_value=1, max_value=53)
    Month = st.number_input("Enter The Month of the Year",min_value=1, max_value=12)
    Year =  st.number_input('Enter The Year',min_value=2010, max_value=2023)
    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Store, Holiday, Temperature, Fuel_Price, CPI, Unemployment, Day, Week,Month,Year)
        st.success('Your Walmart Sale Prediction is {}'.format(result))
        print(result)

if __name__=='__main__':
    main()
