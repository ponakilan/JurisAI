import streamlit as st
import PyPDF2
from openai import OpenAI
import os

TEMPLATE_DIR="pages/templates"

client = OpenAI(
  api_key=st.secrets['OPENAI_API_KEY']
)

system_prompt = '''You are a legal document format validation AI. Your task is to compare a given legal document against a reference sample document and check if the format matches.

Instructions:
Identify Structural Differences:

Check if both documents have the same sections in the same order.
Ensure proper numbering, headings, and subheadings.
Verify formatting consistency (e.g., bolded section titles, paragraph spacing).
Check Content Consistency:

Ensure required clauses appear in the same sections as in the sample.
Identify any missing or extra sections.
Highlight inconsistent terminology or formatting errors.
Output Format:

Pass/Fail status for format adherence in h3 sizing.
List of differences, specifying missing, extra, or misformatted sections.
Suggested corrections(to be in bold) to align with the sample document.
Rules for Validation:
The provided legal document must closely follow the reference sample document’s structure.
Minor wording variations are acceptable unless they affect meaning or legality.
Clearly state any issues in a structured format.
'''

def read_pdf(file_path):
    """Extracts text from a given PDF file."""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def predefined_compare_document(template_name, user_document):
    """Retrieves the predefined template and compares it with the user document."""
    template_path = os.path.join(f"{TEMPLATE_DIR}/", f"{template_name}.pdf")
    
    if not os.path.exists(template_path):
        return "Template not found."

    template_text = read_pdf(template_path)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"sample-document:{template_text}, required-document:{user_document}"}
        ]
    )
    return completion.choices[0].message.content

def custom_compare_document(org_doc,chk_doc):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"sample-document:{chk_doc},required-document:{org_doc}"
        }
    ]
    )
    result_prompt = completion.choices[0].message.content
    return result_prompt

def main():
    st.set_page_config(page_title="Doc Formatting", layout="wide")
    
    st.title("Court-Ready Document Formatting")
    st.caption("Upload legal documents for format analysis or comparison.")
    
    tab1, tab2 = st.tabs(["Predefined Document Analysis", "Comparison Analysis"])
    
    with tab1:
        st.subheader("Predefined Document Analysis")
        predefined_docs = ["Business Service Agreement", "Affidavit for subsitution", "Agreement of License between Trade Mark Owner and a Manufacturer"
        "Anticipatory Bail Petition Format", "Confidential Information and Non-Disclosure Agreement NDA","Free privacy policy","Legal Notice for Recovery of Money","Licence to use Copyright","Partition Deed"]
        selected_doc = st.selectbox("Choose a predefined document", predefined_docs)
        uploaded_file = st.file_uploader("Upload your document", type=["txt", "pdf"], help="Supported formats: .txt, .pdf (max 10MB)")
        
        if uploaded_file:
            if st.button("Submit"):
                with st.spinner("Comparing document with chosen template..."):
                    document_text =""
                    if uploaded_file.type == "text/plain" :
                        document_text = uploaded_file1.getvalue().decode("utf-8")
                    elif uploaded_file.type == "application/pdf" :
                        readerfile = PyPDF2.PdfReader(uploaded_file)
                        document_text= "\n".join([page.extract_text() for page in readerfile.pages if page.extract_text()])
                    analysis = predefined_compare_document(selected_doc,document_text)
                    
                    st.markdown("#### Changes that should be made")
                    with st.container(border=True):
                            st.markdown(analysis)
        
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
                    document_text2 = uploaded_file2.getvalue().decode("utf-8")
                 elif uploaded_file1.type == "application/pdf" and uploaded_file2.type == "application/pdf":
                    reader1 = PyPDF2.PdfReader(uploaded_file1)
                    reader2 = PyPDF2.PdfReader(uploaded_file2)
                    document_text1 = "\n".join([page.extract_text() for page in reader1.pages if page.extract_text()])
                    document_text2 = "\n".join([page.extract_text() for page in reader2.pages if page.extract_text()])
                 with st.spinner("Comparing documents..."):
                    analysis=custom_compare_document(document_text1,document_text2)
                    st.markdown("#### Changes that are identified")
                    with st.container(border=True):
                        st.markdown("**Comparison Document:**")
                        st.markdown(analysis)

if __name__ == "__main__":
    main()