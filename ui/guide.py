import streamlit as st

EMPLOYMENT_KNOWLEDGE = {
    "wrongful_termination": {
        "description": "Unfair Dismissal After Safety Reporting",
        "critical_deadlines": [
            "- 3 months to file ACAS Early Conciliation",
            "- 6 months for Employment Tribunal claim",
            "- 2 years for personal injury claims"
        ],
        "steps": [
            "1. Secure employment contract and payslips",
            "2. Preserve all safety reports/emails (incl. metadata)",
            "3. File ACAS EC Form within 3 months [Mandatory]",
            "4. Request workplace arbitration if available",
            "5. Consider without-prejudice negotiations"
        ],
        "legal_basis": {
            "equality_act": "Protection against detriment (Section 44)",
            "era_1996": "Unfair dismissal rights (Section 94)",
            "whistleblowing": "Public Interest Disclosure Act 1998"
        },
        "template": """Subject: Formal Grievance - Unfair Dismissal
Dear HR Manager,

I am writing to formally challenge my termination dated [DATE]. 
As a protected whistleblower under Section 44 of the Equality Act 2010, 
my dismissal following safety reports on [ISSUE] constitutes unlawful retaliation.

I request:
1. Full reinstatement with back pay
2. Preservation of all relevant documents
3. Written response within 14 days

Please treat this as a formal grievance under Section 10 of the Employment Relations Act 1999."""
    }
}

def get_guidance(user_input):
    user_input = user_input.lower()
    triggers = [
        "wrongful termination", 
        "safety violation",
        "dismissed",
        "unfair dismissal",
        "whistleblower"
    ]
    return "employment"

st.set_page_config(page_title="Legal Resolution Guide")
st.title("Legal Resolution Guide")
st.caption("Specialized support for your issues.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Describe your issue."
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your issue..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        issue_type = get_guidance(prompt)
        response = ""
        if issue_type == "employment":
            data = EMPLOYMENT_KNOWLEDGE["wrongful_termination"]
            
            response = f"**Case Identified:** {data['description']}\n\n"
            response += "**Critical Deadlines:**\n" + "\n".join(data['critical_deadlines']) + "\n\n"
            response += "**Required Actions:**\n" + "\n".join(data['steps']) + "\n\n"
            response += "**Legal Protections:**\n"
            response += f"- Equality Act 2010: {data['legal_basis']['equality_act']}\n"
            response += f"- Employment Rights Act: {data['legal_basis']['era_1996']}\n"
            response += f"- Whistleblower Protection: {data['legal_basis']['whistleblowing']}\n\n"
            response += f"**Sample Grievance Letter:**\n```{data['template']}"
        else:
            response = "Please describe your employment issue in detail (e.g., dismissal timing, safety reports made)"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.warning("""
    **Important Reminders:**
    - Preserve all digital evidence immediately
    - Never sign termination agreements without legal review
    - Keep detailed timeline of events
    """)
