import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_exp(x):
    if x=='Less than 1 year':
        return 0.5
    if x=='More than 50 years':
        return 50.0
    return float(x)


def clean_edu_level(x):
    if x=='Master’s degree (M.A., M.S., M.Eng., MBA, etc.)':
        return 'Master’s degree'
    if x=='Bachelor’s degree (B.A., B.S., B.Eng., etc.)':
        return 'Bachelor’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    
    return 'Less than a Bachelors'
@st.cache
def load_data():
    df=pd.read_csv('survey_results_public.csv')
    x=df
    x=x[["Country","EdLevel","YearsCode","YearsCodePro","Employment","ConvertedCompYearly"]]
    x=x.rename({"ConvertedCompYearly" : "Salary"}, axis=1)
    x=x[x["Salary"].notnull()]
    x=x.dropna()
    x.drop("Employment",axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    x['Country'] = x['Country'].map(country_map)
    x=x[x['Salary'] <= 250000]
    x=x[x['Salary']>=10000]
    x=x[x['Country']!='Other']
    x['EdLevel'] = x['EdLevel'].apply(clean_edu_level)
    x['YearsCodePro']=x['YearsCodePro'].apply(clean_exp)
    return x
df = load_data()    
def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    st.write(
        """
        ### Stack Overflow Developer Survey 2022
        """
    )
    data =df['Country'].value_counts()
    explode=[5]
    fig1,ax1 = plt.subplots()
    ax1.pie(data,labels=data.index, autopct="%1.1f%%",shadow=True,startangle=90,radius=1800)
    ax1.axis("equal")
    st.write("""#### Number of Data from different Countries""")
    st.pyplot(fig1)
    

