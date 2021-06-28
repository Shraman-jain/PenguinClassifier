import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
import base64
import urllib.request


def app():
  @st.cache(allow_output_mutation=True)
  def load_model():
    model=tf.keras.models.load_model('Penguin_classifier_model.hdf5')
    return model
  with st.spinner('Model is being loaded..'):
    model=load_model()

  st.write("""
          # Image Classification
          """
          )

  file = st.file_uploader("Please upload a file", type=["jpg", "png","jpeg"])
  def get_image_download_link(img):
    """Generates a link allowing the PIL image to be downloaded
	  in:  PIL image
	  out: href string
	  """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}">Left click on me !!!</a>'
    return href
  
  
  st.set_option('deprecation.showfileUploaderEncoding', False)
  class_names=['Adélie_penguin', 'Chinstrap_penguin', 'Gentoo_penguin']
  def import_and_predict(image_data, model):
    
          size = (180,180)    
          image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
          image = np.asarray(image)
          img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
          #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
          img_reshape = img[np.newaxis,...]
    
          prediction = model.predict(img_reshape)
        
          return prediction
  if file is None:
      st.write("""
      #### Please upload an image file""")
  else:
      image = Image.open(file)
      image.thumbnail((1800,1074))
      st.image(image, use_column_width=True)
      predictions = import_and_predict(image, model)
      score = tf.nn.softmax(predictions[0])
    # st.write(predictions)
    # st.write(score)
      #result=""" This penguin is most likely to be a **{}** with a **{:.2f}** percent confidence.""".format(, )
      result="""There are **{:.2f} %** chances that this might be a **{}** """.format(100 * np.max(score),class_names[np.argmax(score)])
      if (100 * np.max(score))>50:
          st.success(result)
      else:
          st.warning(result)
  
  st.write("""
      ### In case you need some Images to play with !!!
      """)
  st.write("""(**Note**:to download images left click on the link and then save as file with .png or .jpg format)
  """)
  
  urllib.request.urlretrieve(
  'https://s3.amazonaws.com/download.zyoga.in/Chinstrap+penguin_1.jpeg',
  "Chinstrap.png")
  chim = Image.open("Chinstrap.png")
  ch = np.asarray(chim)
  ch_result = Image.fromarray(ch)
  
  urllib.request.urlretrieve(
  'https://s3.amazonaws.com/download.zyoga.in/Gentoo+penguin_1.jpeg',
  "Gentoo.png") 
  gent = Image.open("Gentoo.png")
  gento = np.asarray(gent)
  gent_result = Image.fromarray(gento)
  
  urllib.request.urlretrieve(
  'https://s3.amazonaws.com/download.zyoga.in/Ad%C3%A9lie+penguin_6.jpeg',
  "Adelie.png")
  ade = Image.open("Adelie.png")
  adelie = np.asarray(ade)
  ad_result = Image.fromarray(adelie)
  
  #st.text('Chinstrap photo')
  chinstrap=get_image_download_link(ch_result)
  st.markdown(chinstrap, unsafe_allow_html=True)
  
  #st.text('Adelie photo')
  Adelie=get_image_download_link(ad_result)
  st.markdown(Adelie, unsafe_allow_html=True)
  
  #st.text('Gentoo photo')
  Gentoo=get_image_download_link(gent_result)
  st.markdown(Gentoo, unsafe_allow_html=True)



  st.write("""
    ## Created By
    Shraman Jain :
    https://www.linkedin.com/in/shraman-jain/
    """)

      

