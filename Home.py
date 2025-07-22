import streamlit as st
import time

title_text = "The LLM-Powered Assembly Assistant"
header_text = """
🛠️ Welcome to the LLM-Powered Assembly Documentation Tool.
Go to the 'Demo' Page to try it out!\n
Or go to the 'About' Page to find out more about this project!
"""

title = st.empty()
current = ""

for char in title_text:
    current += char
    title.title(current)
    time.sleep(0.1)

header = st.empty()
current = ""

for char in header_text:
    current += char
    header.header(current)
    time.sleep(0.02)
