import streamlit as st
from langchain.chat_models import init_chat_model

from core.search import VectorDB

CASE_DATA = {
    "ENV-1988-001": {
        "pdf_url": "https://storage.googleapis.com/kagglesdsdata/datasets/2734042/10312496/pdfs/-0___jonew__judis__10557.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250227%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250227T194202Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=676760f25132178d41724e2e1523d9517542587ab790b2aab3f50b715046b90c3ad38eee09e9e2ddec24d87e888835a0325f455eaf51287bf92f8e3031f7822b4bb1f838df9cf12cd3a6f949dfd8eb31534b311db0e6ef8ac5b9106535fcff14ba467df31c66fb53ecace41960c9473295cc77a3d332368a2f46cdbca019c8251d206dc40e363e4a7671c16c373b2b40904ddb122099bfe716713775f60fee7f80885b22d0a93ceff71d9186d89365f04c68d2a379a38ecdad413575e9ee42b7e840487734610838d9bae898cb9b56adec32031c1d44da5f959409c259921bd9a0fb986eb2b6fd0213d0a1f95ad8f4afc80559e471d46a6f2e0e18bdc2657de5",
        "summary": {
            "Parties": "M.C. Mehta vs Union of India",
            "Issue": "Industrial pollution in Ganga River from tanneries",
            "Decision": "Closure of polluting industries near Ganga",
            "Key Points": [
                "Landmark environmental PIL case",
                "Established 'Polluter Pays' principle",
                "Ordered relocation of hazardous industries"
            ]
        }
    },
    "ENV-1997-002": {
        "pdf_url": "https://storage.googleapis.com/kagglesdsdata/datasets/2734042/10312496/pdfs/-0___jonew__judis__10557.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250227%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250227T194202Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=676760f25132178d41724e2e1523d9517542587ab790b2aab3f50b715046b90c3ad38eee09e9e2ddec24d87e888835a0325f455eaf51287bf92f8e3031f7822b4bb1f838df9cf12cd3a6f949dfd8eb31534b311db0e6ef8ac5b9106535fcff14ba467df31c66fb53ecace41960c9473295cc77a3d332368a2f46cdbca019c8251d206dc40e363e4a7671c16c373b2b40904ddb122099bfe716713775f60fee7f80885b22d0a93ceff71d9186d89365f04c68d2a379a38ecdad413575e9ee42b7e840487734610838d9bae898cb9b56adec32031c1d44da5f959409c259921bd9a0fb986eb2b6fd0213d0a1f95ad8f4afc80559e471d46a6f2e0e18bdc2657de5",
        "summary": {
            "Parties": "M.C. Mehta vs Union of India",
            "Issue": "Air pollution damaging Taj Mahal",
            "Decision": "Implementation of protective zone measures",
            "Key Points": [
                "PIL for cultural heritage preservation",
                "Mandated cleaner fuels in Taj Trapezium Zone",
                "Established monitoring committee"
            ]
        }
    }
}

db = VectorDB()
model = init_chat_model(
    "gpt-4o",
    model_provider="openai"
)

def get_case_summary(case_id):
    summary = CASE_DATA[case_id]["summary"]
    return f"""
    **Parties**: {summary['Parties']}  
    **Legal Issue**: {summary['Issue']}  
    **Court Decision**: {summary['Decision']}  

    **Key Aspects**:  
    {''.join(f'- {point}' for point in summary['Key Points'])}
    """

def main():
    st.title("Precedent Case Analyzer")
    
    case_input = st.text_area("Describe your case:", 
                            height=150,
                            placeholder="Enter details about your case...")

    similar_cases = db.search(case_input, 2)


    if st.button("Find Similar Cases"):
        st.subheader("Related Cases:")
        
        with st.expander("Case ENV-1988-001: Ganga Pollution Case"):
            case_data = CASE_DATA["ENV-1988-001"]
            st.markdown(get_case_summary("ENV-1988-001"))
            if st.link_button("View Full Judgment", case_data["pdf_url"]):
                pass

        with st.expander("Case ENV-1997-002: Taj Mahal Protection"):
            case_data = CASE_DATA["ENV-1997-002"]
            st.markdown(get_case_summary("ENV-1997-002"))
            if st.link_button("View Full Judgment", case_data["pdf_url"]):
                pass

        st.markdown("---")
        st.caption("**Summary:**")
        st.markdown("""
        - Both landmark environmental PIL cases
        - Involve protection of national heritage/resources
        - Established significant environmental jurisprudence
        """)

if __name__ == "__main__":
    main()
