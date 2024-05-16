import streamlit as st
import joblib
import numpy as np

st.markdown("<h1 style='text-align: center; color: Dark Blue;'>Predict Sales</h1>", unsafe_allow_html=True)

# Load the trained models for different options
models = {
    'Bread': joblib.load('Bread.pkl'),
    'Yogurt': joblib.load('Yogurt.pkl'),  
    'Pastry': joblib.load('Pastry.pkl'),
    'Paneer': joblib.load('Paneer.pkl'),
    'Milk': joblib.load('Milk.pkl'),
    'Egg': joblib.load('Egg.pkl'),
    'Packed Buttermilk': joblib.load('Packed Buttermilk.pkl')
}

# Create a function to predict
def predict(input_features, selected_option):
    model = models[selected_option]
    prediction = model.predict(input_features)
    return prediction

# Create the Streamlit web app
def main():
    
    # Dropdown list for selecting product
    selected_option = st.selectbox('Select Product', list(models.keys()))

    # Input field for stock
    quantity_remaining = st.number_input('Enter the quantity remaining :', value=0)

    # Input field for the day to predict sales
    days_to_predict = st.number_input('Enter the days to predict sales :', value=0)
    startpred = (90-days_to_predict)

    # Perform prediction when a button is clicked
    if st.button('Predict'):
        total_prediction = 0
        for i in range(startpred, 91):  # Changed 90 to 91 to include 90
            # Convert input features to a NumPy array
            input_features = np.array([[i]])
        
            # Call the predict function for the selected product
            prediction = predict(input_features, selected_option)
            total_prediction += prediction
        prediction1 = quantity_remaining - total_prediction

        st.write(f'Predicted sales of {selected_option} before Expiry Date is:', int(total_prediction))
        if prediction1 <= 0:
            st.write("The item will be stocked out before expiry.")
            st.write( "Hence, No wastage of food.. Hurray!!")  

        else:
            st.write(f'''Quantity to be purchased of {selected_option} by us is approximately {int(prediction1)} to reduce 
                     wastage of food and hunger issues.''')
        
        st.write("Click Here to place your sales order and join this noble cause.")

if __name__ == '__main__':
    main()
