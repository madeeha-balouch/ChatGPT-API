import openai 
import streamlit as st
import constants

openai.api_key = constants.APIKEY
modelEngine = "text-davinci-003" #Refer to the openai documentation for the avaialble models. 

st.title("ChatGPT API") #Title of the page
st.divider() #adds a horizontal line

# Text field for users to type in their query
query = st.text_input('Please type in your query', 'what is generative AI?')

completion = openai.Completion.create(
  model=modelEngine,
  prompt=query,
  max_tokens=1024,  
  temperature= 0.5, 
  n=1,
  stop=None
)

response = completion.choices[0].text
st.text_area("The response to your query is:", response.strip() , 400)

