import streamlit as st
import urllib.request
from PIL import Image

def app():
    st.write("# Penguin Prediction App")
    
    st.write("""
    ### This web application predicts the **Palmer Penguin** species in which you can classify penguin in two ways- either by using an **IMAGE** of a penguin or by adding specific **DATA** of a penguin i.e. their (bill_length,bill_depth,flipper_length etc.).
    """)
    st.write("""
    Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins)in R  by **Allison Horst**.
    """)
    st.write("""
    This webapp is a modification of a project which was made by **Chanin Nantasenamat** a.k.a. **DataProfessor**
    https://www.youtube.com/dataprofessor 
    """)

    st.write("""
    ## Meet the Palmer penguins

    They are of 3 species **CHISTRAP** ,**GENTOO** AND **ADELIE**.
    """)
    
    urllib.request.urlretrieve(
    'https://s3.amazonaws.com/download.zyoga.in/culmen_depth.png',
    "bill_length.png")

    image = Image.open("bill_length.png")

    st.image(image, caption="{} species".format('Palmer penguins'))
    st.write("""
    ## Bill dimensions""")

    st.write("""
            The culmen is the upper ridge of a bird’s bill. In the simplified penguins data, culmen length and depth are renamed as 
            variables bill_length_mm and bill_depth_mm to be more intuitive.
            For this penguin data, the culmen (bill) length and depth are measured as shown below 
            (thanks Kristen Gorman for clarifying!):""")


    image1 = Image.open('https://s3.amazonaws.com/download.zyoga.in/culmen_depth.png')

    st.image(image, caption="{}".format('Bill dimensions'))

    st.write("""
    ## Artwork
    You can download palmerpenguins art (useful for teaching with the data) in vignette("art"). If you use this artwork, please cite with: “Artwork by @allison_horst”.
    ## License
    Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
    ## Created By
    Shraman Jain :
    https://www.linkedin.com/in/shraman-jain/
    
    """)