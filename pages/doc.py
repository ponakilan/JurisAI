import streamlit as st
import openai
import PyPDF2

client = openai.OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

def analyze_document(document_text):
    if not document_text.strip():
        return {"key_points": ["No content found in the document."], "risks": []}

    # Request key points from OpenAI
    key_points_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Extract key points from the following legal document and provide short explanation."},
            {"role": "user", "content": document_text}
        ]
    )
    key_points = key_points_response.choices[0].message.content.strip().split("\n")

    # Request risks from OpenAI
    risks_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Analyze the legal document and extract potential risks. "
                    "List each risk with severity (High/Medium/Low) and a short explanation in this format strictly and dont number the points:\n"
                    "Risk Name - Severity - Explanation"},
            {"role": "user", "content": document_text}
        ]
    )
    risks = risks_response.choices[0].message.content.strip().split("\n")

    risks_data = [tuple(risk.split(" - ")) for risk in risks if " - " in risk]  # Extracting risk label, severity, and details
    
    # Sort risks by severity order: High > Medium > Low
    severity_order = {"high": 1, "medium": 2, "low": 3}
    risks_data.sort(key=lambda x: severity_order.get(x[1].lower(), 4))

    return {"key_points": key_points, "risks": risks_data}

def main():
    st.set_page_config(page_title="LegalDoc Analyzer", layout="centered")

    st.title("📜 Legal Document Analyzer")
    st.caption("Upload your legal document for automated risk analysis and summary")

    uploaded_file = st.file_uploader("Choose a document", type=["txt", "pdf"], help="Supported formats: .txt, .pdf (max 10MB)")

    # Submit button
    analyze_button = st.button("Analyze Document", type="primary")

    if uploaded_file and analyze_button:
        document_text = ""

        if uploaded_file.type == "text/plain":
            document_text = uploaded_file.getvalue().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            document_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

        with st.spinner("🔍 Analyzing document..."):
            analysis = analyze_document(document_text)

            st.subheader("📌 Analysis Results")

            st.markdown("### ✅ Key Provisions")
            with st.container():
                for point in analysis["key_points"]:
                    st.markdown(point)

            st.markdown("### ⚠️ Risk Assessment")
            if not analysis["risks"]:
                st.markdown("No risks identified.")
            else:
                severity_colors = {"high": "#ef476f",
                    "medium": "#ffd166",
                    "low": "#06d6a0"}

                with st.container():
                    for label, severity, details in analysis["risks"]:
                        color = severity_colors.get(severity.lower(), "#666666")

                        st.markdown(
                            f"<div style='padding: 0.5rem; border-left: 4px solid {color}; margin: 0.5rem 0;'>"
                            f"<b>{label}</b><br>"
                            f"<span style='color: {color}; font-size: 0.9em'>{details}</span>"
                            "</div>", 
                            unsafe_allow_html=True
                        )

if __name__ == "__main__":
    main()
