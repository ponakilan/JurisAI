import streamlit as st
from openai import OpenAI
import re

client = OpenAI(
  api_key='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'
)

system_prompt = '''You are an AI legal assistant that provides guidance based on legal principles. 
Your responses should be neutral, informative, and help the user understand their legal options. 
You provide definitive legal conclusions. 
You do not provide general actions. You only provide legal advice and how to proceed judicially.
You do not provide advice to consult an attorney.
You provice decisive information.
Your response should contain three sections: 1.critical deadlines to file any complaint 2. required actions to be taken 3.legal protection acts that are applicable to the user's query'''



def get_guidance(prompt):
    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": prompt
        }
    ]
    )
    result_prompt = completion.choices[0].message.content
    #matches = re.split(r'\n\d+\.\s\*\*[^\*\*]\*\*:', result_prompt)
    final_response = result_prompt.replace('**','<h3>').replace('**:','</h3>')
    #print(final_response)
    return final_response
st.set_page_config(page_title="Legal Resolution Guide")
st.title("Legal Resolution Guide")
st.caption("Specialized support for your issues.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Describe your issue."
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your issue..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        response = get_guidance(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.warning("""
    **Important Reminders:**
    - Preserve all digital evidence immediately
    - Never sign termination agreements without legal review
    - Keep detailed timeline of events
    """)
