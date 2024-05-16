import streamlit as st
st.set_page_config(page_title ="multiple", page_icon="sunglass"
)


st.markdown("<h1 style='text-align: center; color: Dark Green;'>Sustain Feed </h1>", unsafe_allow_html=True)

# st.sidebar.success("select pages")
# st.sidebar.success("Select a page above.")

# Create a dictionary to store username and password (for demonstration purposes)
user_credentials = {
    "username": "admin",
    "password": "password123"
}

def main( ):
    #st.title( "Login Page" )
    st.markdown("<h3 style='text-align: center; color: Dark Green;'>Login Page</h3>", unsafe_allow_html=True)

    #Create input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Create a login button
    if st.button("Login"):
        if username == user_credentials["username"] and password == user_credentials["password"]:
            st.success("Logged in as {}".format(username))
        else:
            st.error("Invalid credentials. Please try again.")

if __name__ == "__main__":
    main()
