import streamlit as st

st.set_page_config(page_title="JurisAI", layout="wide")

st.markdown(
    """
    <style>
        a {
            text-decoration: none !important;
            color: black !important;
        }
        .main {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            padding: 20px;
            align-items:center;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
            width: 550px;
            height:250px;
            text-align: center;
            margin-left:auto;
            margin-right:auto;
            # background-image: url("https://cdn-icons-png.flaticon.com/512/888/888108.png");
            # background-repeat: no-repeat;
            # background-position: right;

        }
        .card:hover {
            
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
        .card button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        .card button:hover {
            background-color: #45a049;
        }
        .material-symbols-outlined {
        font-variation-settings:
        'FILL' 0,
        'wght' 400,
        'GRAD' 0,
        'opsz' 48
        }
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("<h1 style='text-align: center;'>JurisAI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; opacity:40%;'>Your AI-powered legal assistant for quick and effective legal solutions.</h4>",unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<a href="http://13.201.51.57/format"><div class="card"> <h2>Court-Ready Document Formatting</h2><p>Generate legally compliant documents tailored to your needs, formatted and structured professionally for court submission.</p>', unsafe_allow_html=True)
    st.markdown('</div></a>', unsafe_allow_html=True)


    st.markdown('<a href="http://13.201.51.57/doc"><div class="card"> <h2>Legal Document Simplification</h2> <p>Break down complex legal jargon into clear, understandable language so you can grasp your legal rights and obligations effortlessly.</p>', unsafe_allow_html=True)

    st.markdown('</div></a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="http://13.201.51.57/guide"><div class="card"> <h2>Inexpensive Legal Advice</h2> <p>Get quick, cost-effective legal guidance from AI-assisted research and recommendations tailored to your situation.</p>', unsafe_allow_html=True)

    st.markdown('</div></a>', unsafe_allow_html=True)

    st.markdown('<a href="http://13.201.51.57/similar-cases"><div class="card"> <h2>Cases Library</h2> <p>Explore a comprehensive collection of past legal cases, decisions, and references to support your case research.</p>', unsafe_allow_html=True)

    st.markdown('</div></a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)