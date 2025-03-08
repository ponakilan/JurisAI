import openai
import streamlit as st

from search import VectorDB

db = VectorDB()
OPEN_API_KEY = "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"
client = openai.OpenAI(api_key=OPEN_API_KEY)


def get_case_summary(text):
    case_details = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
              "content": """You are an entity extractor. Extract the following details from the given input and return it in this format:
              Case ID
              Parties 
              Issue 
              Decision
              Key points
              all the headings should be in h4"""},
              {"role": "user", "content": text}
        ]
    )
    return case_details.choices[0].message.content


def main():
    st.title("Precedent Case Analyzer")
    
    case_input = st.text_area("Describe your case:", 
                            height=150,
                            placeholder="Enter details about your case...")
    if st.button("Find Similar Cases"):
        similar_cases = db.search(case_input, 2)
        cases_text = " ".join([f"Case {i}" + case.page_content for i, case in enumerate(similar_cases)])
        key_points_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", 
                 "content": """ you are going to be precise about the result query you give.
                                give me key points not sentences
                                put them in bullet points.
                 Analyze the following cases and identify the key similarities among them. 
                                Consider factors such as underlying principles, patterns, causes, consequences, 
                                and any common themes or characteristics that connect them"""},
                {"role": "user", "content": "Original case: " + case_input + cases_text}
            ]
        ).choices[0].message.content
        st.subheader("Related Cases:")
        for i, case in enumerate(similar_cases):
            with st.expander(f"Case {i}"):
                st.markdown(get_case_summary(case.page_content), unsafe_allow_html=True)
                st.link_button("View Full Judgment", f"https://storage.googleapis.com/jurisai/{case.metadata['file_name']}")

        st.markdown("---")
        st.caption("**Similarities:**")
        st.markdown(key_points_response)

if __name__ == "__main__":
    main()
