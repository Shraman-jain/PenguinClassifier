import streamlit as st
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
    
    image = Image.open('https://lh3.googleusercontent.com/fife/AAWUweV346xy21p7e0vQzJQPTEB2Qs6qPgJ5cDMYMLOAnwliQU6Y39sZq3aouFZ0oB5vCD95QRykuDyWK5HHkg73sGt-tbOslq0X8AHhy_cT4GAV7BvucIEy6MpJaFPnR8wEs2YML4zjYEklleTJnjm6W4M96S72VeU8sJQDmQn6O2wUjrKKxMp_rRGmbm9GCjFrOj8FncQj15eISpHoQD2QM3qz2YfUfNV-n_5vMQKlBACShjuMPDQIITWXTsnFBmilFrrT2QuDWKXiqPbxJGRlu2WXLYwcRe_Ewt59eDyK_s0MaKs9g5g3NjurXye2xSTSFwwxC8fhRqvbpTnaUJA5DkEJ5rYTCdVAUGtO7P9vuUtAGkFPx42_iLqYjBTI-mAxSopnFXZn3_iDDjpe4DVUUTyo3AYZesdmK_ezrl3gu13kgNC8x9T3AVjXhfHiB22zox-V10_UjskVNzKfrCuG3MLixNnv7rX69xHxMsX26wD24XeJBDkcVupzUaS04kZmtpxWhVNfxACLOkDEkfzgj4wqGLb3qvuPYidA0GKy4_X2T--tv5wJUM6DshJ6YyEygOYxYEtLulltF6RkZbiQKzBfG3ENUJ0oV4109tf2ly99FayjBG4r0tAZatVbcRtCXj_vSzfIYesV-Cj5xZODPoPpG4se9VdjVOiWaHC97b5hcwrRybMDVUfOyCNvliyO693cYsoq3pM5m_f6i2ySmG9lfPWQR7Q=w1366-h606-ft')

    st.image(image, caption="{} species".format('Palmer penguins'))

    st.write("""
    ## Bill dimensions""")

    st.write("""
            The culmen is the upper ridge of a bird’s bill. In the simplified penguins data, culmen length and depth are renamed as 
            variables bill_length_mm and bill_depth_mm to be more intuitive.
            For this penguin data, the culmen (bill) length and depth are measured as shown below 
            (thanks Kristen Gorman for clarifying!):""")


    image1 = Image.open('https://s3.amazonaws.com/download.zyoga.in/culmen_depth.png')

    st.image(image1, caption="{}".format('Bill dimensions'))

    st.write("""
    ## Artwork
    You can download palmerpenguins art (useful for teaching with the data) in vignette("art"). If you use this artwork, please cite with: “Artwork by @allison_horst”.
    ## License
    Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
    ## Created By
    Shraman Jain :
    https://www.linkedin.com/in/shraman-jain/
    
    """)