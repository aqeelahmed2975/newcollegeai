import streamlit as st
from google import genai
Robo=genai.Client(api_key="AIzaSyDUzxme5hzw082d1PcIfjoe3IMoIpQCLYo")
st.title("My Own GPT")
question=st.text_input("Ask Anything")
if st.button("send"):
    response = Robo.models.generate_content(
        model = "gemini-2.5-flash",
        contents = question
        )
    st.write("Ans:"+response.text)
