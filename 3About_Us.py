import streamlit as st

def about_us():
    st.title('About Us')
    st.write('Welcome to Sustain Feed, a dedicated team committed to ending hunger and food insecurity in our community.')
    st.write('*Our Mission:*')
    st.write("At Sustain Feed, we are on a mission to tackle food waste and hunger simultaneously. We believe that every food item has value and potential to make a difference in someone's life. Our core mission is to predict the sales of supermarket food items a few days before expiry using advanced machine learning algorithms. By doing so, we aim to prevent surplus food from going to waste and ensure that it reaches those in need before it expires.")
    st.write('*Our Approach:*')
    st.write("Utilizing supervised machine learning techniques, we analyze various factors such as historical sales data, product attributes, and market trends to accurately forecast the demand for food items nearing their expiry date. By predicting sales in advance, we empower supermarkets and food suppliers to proactively manage their inventory, minimizing food waste while maximizing social impact.")
    st.write('*Join Us in Making a Difference:*')
    st.write("We invite you to join us in our mission to end food waste and hunger. Whether you're a supermarket looking to partner with us, a volunteer eager to lend a helping hand, or a supporter passionate about making a difference, there are many ways to get involved. Together, we can harness the power of technology, collaboration, and compassion to create a future where no one goes hungry and every meal counts.")
    st.write("*Together, Let's Turn Surplus into Sustenance:*")
    st.write('At Sustain Feed, we believe in the transformative power of food. Join us on our journey as we turn surplus into sustenance, one prediction, one distribution, and one meal at a time. Together, we can build a world where food waste is minimized, hunger is eradicated, and every individual has access to nutritious food and a brighter future.')
    st.write("Thank you for your support!")

# Main function
def main():
    #st.sidebar.title("Navigation")
    #page = st.radio("Go to", ["About Us"])
    # if page == "About Us":
        about_us()

if __name__ == '__main__':
    main()