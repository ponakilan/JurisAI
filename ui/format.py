import streamlit as st

def analyze_document(document_text):
    return {
        "key_points": [
            "Position: Senior Developer with stock option vesting over 4 years",
            "Compensation: ₹21L base + 20% performance bonus potential",
            "Benefits: Full healthcare coverage and 5% 401(k) match",
            "Termination: 60-day employer notice vs 30-day employee notice"
        ],
        "risks": [
            ("Non-compete Clause", "high", "18-month restriction in tech industry - potentially unenforceable in some states"),
            ("Confidentiality", "high", "Lifetime obligation for trade secrets - exceeds typical 2-5 year standards"),
            ("IP Assignment", "medium", "All work products remain company property without exceptions"),
            ("Termination", "medium", "Discretionary termination for 'business needs' without clear parameters")
        ]
    }

def main():
    st.set_page_config(page_title="Doc Formatting", layout="centered")
    
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
                with st.spinner("Analyzing document..."):
                    document_text = "hello"
                    analysis = analyze_document(document_text)
                    
                    st.markdown("#### Wrong Formatting located in following places")
                    with st.container(border=True):
                        for point in analysis["key_points"]:
                            st.markdown(f"• {point}")
                    
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
                with st.spinner("Analyzing documents..."):
                    document_text1 = "hello"
                    document_text2 = "hello"
                    
                    analysis1 = analyze_document(document_text1)
                    analysis2 = analyze_document(document_text2)
                    
                    st.markdown("#### Changes that are identifiedS")
                    with st.container(border=True):
                        st.markdown("**First Document:**")
                        for point in analysis1["key_points"]:
                            st.markdown(f"• {point}")
                        
                        st.markdown("**Comparison Document:**")
                        for point in analysis2["key_points"]:
                            st.markdown(f"• {point}")
                    
                    st.markdown("#### Risk Assessment")
                    with st.container(border=True):
                        st.markdown("**First Document:**")
                        for risk in analysis1["risks"]:
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
                        
                        st.markdown("**Comparison Document:**")
                        for risk in analysis2["risks"]:
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

if __name__ == "__main__":
    main()