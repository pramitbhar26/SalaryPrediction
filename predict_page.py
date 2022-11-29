import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor_loaded = data["model"]
le_Country = data["le_Country"]
le_edu = data["le_edu"]


def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")


    countries = {
          "United States of America",                                                                 
           "Germany",          
        "United Kingdom of Great Britain and Northern Ireland",
         "India",
          "Canada",                                                 
         "France",                                                           
        "Brazil",                                                  
        "Spain",                                                   
        "Poland",                                                   
        "Netherlands",                                              
        "Australia",                                                
        "Italy",                                                    
        "Sweden",                                                   
        "Russian Federation",                                       
        "Switzerland",                                              
        "Turkey",                                                   
        "Austria",                                                  
        "Israel",                                                   
        "Czech Republic",                                           
        "Belgium",                                                  
        "Portugal",                                                 
        "Denmark",                                                  
        "Mexico",                                                   
        "Norway",                                                   
        "Romania",                                                  
        "Greece",                                                   
        "Pakistan",                                                 
        "New Zealand",                                              
        "Finland",                                                  
        "Argentina",                                                
        "South Africa",                                             
        "Ukraine",                                                 
        "Hungary",                                                  
        "Bangladesh",                                               
        "China",                                                    
        "Indonesia",                                                
        "Nigeria",                                                  
        "Egypt"    
    }
    education={
        "Master’s degree", "Bachelor’s degree", "Less than a Bachelors",
       "Post grad"
    }
    country = st.selectbox("Country",countries)
    education = st.selectbox("Education Level",education)
    experience = st.slider("Years of Experience",0,30,3)
    ok = st.button("Calculate Salary")
    if ok:
        z=np.array([[country,education,experience]])
        z[:, 0] = le_Country.transform(z[:,0])
        z[:, 1] = le_edu.transform(z[:,1])
        z = z.astype(float)

        salary = regressor_loaded.predict(z)
        st.subheader(f"The estimated Salary is ${salary[0]:.2f}")

