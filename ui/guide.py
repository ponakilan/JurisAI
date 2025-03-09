import streamlit as st
from openai import OpenAI
from io import BytesIO
from streamlit_mic_recorder import mic_recorder

client = OpenAI(
  api_key='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'
)




system_prompt_deadlines = '''You are an AI legal assistant that provides guidance based on legal principles. 
Your responses should be neutral, informative, and help the user understand their legal options. 
You provide definitive legal conclusions. 
Ignore the general query of the user.
Only pick up the context and give the necessary deadlines before which the user has to take any action.
You do not provide general actions. You only provide legal advice and how to proceed judicially.
You do not provide advice to consult an attorney.
You provide decisive information.
Your response should show only critical deadlines to file any complaints according to the query.
Provide definite dates and timeline restrictions before which necessary actions can be taken'''

system_prompt_actions = '''You are an AI legal assistant that provides guidance based on legal principles. 
Your responses should be neutral, informative, and help the user understand their legal options. 
You provide definitive legal conclusions. 
You do not provide general actions. You only provide legal advice and how to proceed judicially.
You do not provide advice to consult an attorney.
You provice decisive information.
Your response should mention only the required actions to be taken'''


system_prompt_acts = '''You are an AI legal assistant that provides guidance based on legal principles. 
Your responses should be neutral, informative, and help the user understand their legal options. 
You provide definitive legal conclusions. 
You do not provide general actions.
Ignore the general query and pick up the context alone and mention the laws and legal protection acts that can work in favour of the user.
List the legal acts and laws as list with minimal explanation of each.
You do not provide advice to consult an attorney.
You provice decisive information.
Your response should provide the legal protection acts of those in relevance to the user's query '''


def get_guidance(prompt,system_settings):
    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_settings},
        {
            "role": "user",
            "content": prompt
        }
    ]
    )
    result_prompt = completion.choices[0].message.content
    return result_prompt

st.set_page_config(page_title="Legal Resolution Guide")
st.title("Legal Resolution Guide")
st.caption("Specialized support for your issues.")
st.markdown('<style>h3{margin-top:0;padding-top:0 !important;}</style>',unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Describe your issue in you regional language."
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def callback():
    if st.session_state.my_recorder_output:
        audio_bytes = st.session_state.my_recorder_output['bytes']
        

response_headings = ["Critical Deadlines to File Any Complaint:","Required Actions to Be Taken:","Legal Protection Acts That Are Applicable:"]

button,prompt = st.columns(2,vertical_alignment="bottom")

prompt = st.chat_input("Enter your issue...")
#button = st.button("Voice")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        response_deadlines = get_guidance(prompt,system_prompt_deadlines)
        response_actions = get_guidance(prompt,system_prompt_actions)
        response_acts = get_guidance(prompt,system_prompt_acts)
        response = response_deadlines+response_actions+response_deadlines
        response_deadlines = st.markdown(f'<h3>{response_headings[0]}</h3><p>{response_deadlines}</p>',unsafe_allow_html=True)
        response_actions = st.markdown(f'<h3>{response_headings[1]}</h3><p>{response_actions}</p>',unsafe_allow_html=True)
        response_acts = st.markdown(f'<h3>{response_headings[2]}</h3><p>{response_acts}</p>',unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
with st.sidebar:
    st.markdown("""
    <style>
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        background-color: #ffc133;
        padding: 10px;
        border-radius: 10px;
    }
    .sidebar-content {
        font-size: 15px;
        color: #ffffff;
        padding: 10px;
    }
    </style>
    <div class="sidebar-title">Voice Recorder</div>
    <div class="sidebar-content">
        - Speak in your Regional Language<br>
    </div>
    """, unsafe_allow_html=True)
    recording = mic_recorder(key='my_recorder', callback=callback)

if recording:
    recording_bytes = recording["bytes"]
    with open("voice.mp3","wb") as file:
        file.write(BytesIO(recording_bytes).read())
    audio_file= open("./voice.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )
    voice_prompt = transcription.text
    with st.chat_message("user"):
        st.markdown(voice_prompt)
    st.session_state.messages.append({"role": "user", "content": voice_prompt})
    with st.chat_message("assistant"):
        response_deadlines = get_guidance(voice_prompt,system_prompt_deadlines)
        response_actions = get_guidance(voice_prompt,system_prompt_actions)
        response_acts = get_guidance(voice_prompt,system_prompt_acts)
        response = response_deadlines+response_actions+response_deadlines
        response_deadlines = st.markdown(f'<h3>{response_headings[0]}</h3><p>{response_deadlines}</p>',unsafe_allow_html=True)
        response_actions = st.markdown(f'<h3>{response_headings[1]}</h3><p>{response_actions}</p>',unsafe_allow_html=True)
        response_acts = st.markdown(f'<h3>{response_headings[2]}</h3><p>{response_acts}</p>',unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})

