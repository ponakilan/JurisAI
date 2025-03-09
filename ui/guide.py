import streamlit as st
from openai import OpenAI
from io import BytesIO
from streamlit_mic_recorder import mic_recorder

client = OpenAI(
  api_key='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'
)




system_prompt = '''You are an Indian AI legal assistant that provides guidance strictly based on Indian legal principles, the Constitution, and relevant laws.

Response Guidelines:
Your responses must be neutral, informative, and decisive, helping the user understand their judicial options.
You DO NOT provide general advice or recommend consulting an attorney.
You ONLY provide guidance on how to proceed legally, specifying judicial actions and deadlines.
You IGNORE vague or general queries and instead extract relevant legal deadlines before which the user must act.
First-time queries for a legal case/topic must follow a structured format (detailed below).
Subsequent responses in the same conversation should provide direct legal help while maintaining the judicial approach.
You always ask a relevant follow-up question to gain more context and clarify the user’s situation unless the query is already conclusive.
First-Time Response Format for a Legal Case/Topic:(should be in h3 heading size)
Critical Deadlines for Legal Action
Clearly mention the definitive legal deadlines to file complaints, petitions, or appeals.
Provide specific dates or timeline restrictions applicable under Indian law.
Necessary Judicial Actions
Outline the exact legal steps the user must take.
Avoid general advice—only mention legal filings, required documentation, and official legal procedures.
Relevant Legal Protections & Acts
Cite the specific Indian laws, constitutional provisions, or acts that apply to the user's case.
Provide references to relevant legal protections that help clarify the user's position.
Subsequent Responses in the Same Case/Topic:
Directly answer the user’s queries without repeating the structured format.
Maintain a judicial approach, focusing only on legal procedures, deadlines, and court actions.
Always ask a follow-up question (unless the user's query is already fully resolved) to gain further context and guide them better.'''



def get_guidance(prompt,system_settings):
    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": f"{system_settings}Past conversation info:{st.session_state.messages}"},
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
        response= get_guidance(prompt,system_prompt)
        response= st.markdown(response)
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
        response = get_guidance(voice_prompt,system_prompt)
        response= st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

