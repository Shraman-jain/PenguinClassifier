import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

def app():
    
    st.write("""
          # Data Prediction
          """
          )
    st.subheader(""" 
    You can either upload a csv file with one row or can give the data using the input feature.
    """)
    st.sidebar.header('User Input Features')

    st.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
    """)

    # Collects user input features into dataframe
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
    else:
        def user_input_features():
            island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
            sex = st.sidebar.selectbox('Sex',('male','female'))
            bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
            bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
            flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
            body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
            data = {'island': island,
                    'bill_length_mm': bill_length_mm,
                    'bill_depth_mm': bill_depth_mm,
                    'flipper_length_mm': flipper_length_mm,
                    'body_mass_g': body_mass_g,
                    'sex': sex}
            features = pd.DataFrame(data, index=[0])
            return features
        input_df = user_input_features()

    # Combines user input features with entire penguins dataset
    # This will be useful for the encoding phase
    penguins_raw = pd.read_csv('C:/Users/DELL/Desktop/shraman/project/penguin_classification/penguin_cleaned.csv')
    penguins = penguins_raw.drop(columns=['species'])
    df = pd.concat([input_df,penguins],axis=0)

    # Encoding of ordinal features
    # https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
    encode = ['sex','island']
    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df,dummy], axis=1)
        del df[col]
    df = df[:1] # Selects only the first row (the user input data)
    df1=df[1:]
    # Displays the user input features
    st.subheader('User Input features')

    if uploaded_file is not None:
        st.write(df)
        st.write(df1)
    else:
        st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
        st.write(df)

    # Reads in saved classification model
    load_clf = pickle.load(open('C:/Users/DELL/Desktop/shraman/project/penguin_classification/penguins_clf.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)


    penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])

    #st.subheader('Prediction Probability')
    #st.write('Adelie: 0' , 
    #            'Chinstrap : 1',
    #            'Gentoo : 2 ')
    #st.write(prediction_proba[0])
    
    '''st.write("Probability of ",penguins_species[0],"species is",
    prediction_proba[0][0])
    st.write("Probability of ",penguins_species[1],"species is",
    prediction_proba[0][1])
    st.write("Probability of ",penguins_species[2],"species is",
    prediction_proba[0][2])
    '''
    st.subheader('Prediction')


    if (str(penguins_species[prediction][0])=='Adelie'):
        image = Image.open('C:/Users/DELL/Desktop/shraman/project/penguin_classification/adile_img.jpg')
        
    elif (str(penguins_species[prediction][0])=='Chinstrap'):
        image = Image.open('C:/Users/DELL/Desktop/shraman/project/penguin_classification/chinstrap_img.jpg')
       
    elif (str(penguins_species[prediction][0])=='Gentoo'):
        image = Image.open('C:/Users/DELL/Desktop/shraman/project/penguin_classification/gentoo_img.jpg')
        



    #image = Image.open('shraman.jpg')
    st.image(image, caption="{} species".format(penguins_species[prediction][0]))
    maximum_probability=max(prediction_proba[0][2],prediction_proba[0][0],prediction_proba[0][1])
    result="There are **{:.2f} %** chances that this might be a **{} species**""".format(100 *float(maximum_probability) ,penguins_species[prediction][0])
    
    if (100 * float(maximum_probability))>50:
        st.success(result)
    else:
        st.warning(result)    

    
    
    st.write("""
    ### In case you need some data to play with !!!
    """)
    # initialize list of lists
    data = [['Adelie','Torgersen',39.1,18.7,181,3750,'male'],['Gentoo','Biscoe',46.1,13.2,211,4500,'female'],
    ['Chinstrap','Dream',46.5,17.9,192,3500,'female']]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['species','island','bill_length','bill_depth','flipper_length','body_mass','sex'])

    # print dataframe.
    st.dataframe(df)

    st.write("""
    ## Created By
    Shraman Jain :
    https://www.linkedin.com/in/shraman-jain/
    """)


