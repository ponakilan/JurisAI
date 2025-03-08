import streamlit as st
import PyPDF2
def predefined_compare_document(chosen_temp, document_text):
    changes=""
    return changes
def custom_compare_document(org_doc,chk_doc):
    changes=""
    return changes

def main():
    st.set_page_config(page_title="Doc Formatting", layout="wide")
    
    st.title("Court-Ready Document Formatting")
    st.caption("Upload legal documents for format analysis or comparison.")
    
    tab1, tab2 = st.tabs(["Predefined Document Analysis", "Comparison Analysis"])
    
    with tab1:
        st.subheader("Predefined Document Analysis")
        predefined_docs = ["Employment Agreement", "Non-Disclosure Agreement (NDA)", "Service Contract", "Lease Agreement"]
        selected_doc = st.selectbox("Choose a predefined document", predefined_docs)
        uploaded_file = st.file_uploader("Upload your document", type=["txt", "pdf"], help="Supported formats: .txt, .pdf (max 10MB)")
        
        if uploaded_file:
            if st.button("Submit"):
                with st.spinner("Comparing document with chosen template..."):
                    document_text = "hello"
                    analysis = predefined_compare_document(selected_doc,document_text)
                    
                    st.markdown("#### Wrong Formatting located in following places")
                    with st.container(border=True):
                        for point in analysis["key_points"]:
                            st.markdown(point)
                    
                    st.markdown("#### Changes that should be made")
                    with st.container(border=True):
                        for risk in analysis["risks"]:
                            label, severity, details = risk
                            color = {
                                "high": "#ef476f",
                                "medium": "#ffd166",
                                "low": "#06d6a0"
                            }.get(severity, "#666666")
                            
                            st.markdown(
                                f"<div style='padding: 0.5rem; border-left: 4px solid {color}; margin: 0.5rem 0;'>"
                                f"<b>{label}</b><br>"
                                f"<span style='color: {color}; font-size: 0.9em'>{details}</span>"
                                "</div>", 
                                unsafe_allow_html=True
                            )
        
    with tab2:
        st.subheader("Comparison Analysis")
        uploaded_file1 = st.file_uploader("Choose sample format document", type=["txt", "pdf"], help="Supported formats: .txt, .pdf (max 10MB)")
        uploaded_file2 = st.file_uploader("Choose document for comaparison", type=["txt", "pdf"], help="Supported formats: .txt, .pdf (max 10MB)")
        
        if uploaded_file1 and uploaded_file2:
            if st.button("Submit Comparison"):
                 document_text1 = ""
                 document_text2 = ""
                 if uploaded_file1.type == "text/plain" and uploaded_file2.type == "text/plain":
                    document_text1 = uploaded_file1.getvalue().decode("utf-8")
                 elif uploaded_file1.type == "application/pdf" and uploaded_file2.type == "application/pdf":
                    reader1 = PyPDF2.PdfReader(uploaded_file1)
                    reader2 = PyPDF2.PdfReader(uploaded_file2)
                    document_text1 = "\n".join([page.extract_text() for page in reader1.pages if page.extract_text()])
                    document_text2 = "\n".join([page.extract_text() for page in reader2.pages if page.extract_text()])
                 with st.spinner("Comparing documents..."):
                    analysis=custom_compare_document(document_text1,document_text2)
                    st.markdown("#### Changes that are identifiedS")
                    with st.container(border=True):
                        st.markdown("**Comparison Document:**")
                        for point in analysis["key_points"]:
                            st.markdown(point)

if __name__ == "__main__":
    main()