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
    st.set_page_config(page_title="LegalDoc Analyzer", layout="centered")
    
    st.title("Legal Document Analyzer")
    st.caption("Upload your legal document for automated risk analysis and summary")
    
    uploaded_file = st.file_uploader("Choose a document", 
                                   type=["txt", "pdf"],
                                   label_visibility="collapsed",
                                   help="Supported formats: .txt, .pdf (max 10MB)")
    
    doc_container = st.empty()
    analysis_container = st.empty()
    
    if not uploaded_file:
        return
    
    with st.spinner("Analyzing document..."):
        document_text = "hello"
        analysis = analyze_document(document_text)
        
        doc_container.empty()
        analysis_container.empty()
        
        st.subheader("Analysis Results")
        
        st.markdown("#### Key Provisions")
        with st.container(border=True):
            for point in analysis["key_points"]:
                st.markdown(f"• {point}")
        
        st.markdown("#### Risk Assessment")
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

if __name__ == "__main__":
    main()
