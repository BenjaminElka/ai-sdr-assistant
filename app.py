import os
from datetime import datetime

import streamlit as st
from openai import OpenAI


APP_TITLE = "AI SDR Assistant"
DEFAULT_PRODUCT_CONTEXT = (
    "A B2B software solution that helps sales teams research prospects, "
    "personalize outreach, qualify leads, and prepare follow-up sequences faster."
)

st.set_page_config(page_title=APP_TITLE, page_icon="🤖", layout="wide")

st.markdown(
    """
    <style>
    .main-header {font-size: 2.4rem; font-weight: 800; margin-bottom: 0.2rem;}
    .sub-header {font-size: 1.05rem; color: #666; margin-bottom: 1.5rem;}
    .metric-card {padding: 1rem; border: 1px solid #e6e6e6; border-radius: 14px; background: #fafafa;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(f'<div class="main-header">🤖 {APP_TITLE}</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">Create ethical, personalized sales outreach from prospect and company details.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Settings")
    model = st.selectbox("OpenAI model", ["gpt-4o-mini", "gpt-4.1-mini"], index=0)
    tone = st.selectbox("Outreach tone", ["Professional", "Friendly", "Direct", "Consultative"], index=0)
    buyer_stage = st.selectbox(
        "Buyer stage",
        ["Cold prospect", "Warm lead", "Re-engagement", "Post-demo follow-up"],
        index=0,
    )
    st.divider()
    st.caption("Set OPENAI_API_KEY in your environment or Streamlit secrets before running.")

left, right = st.columns([1, 1])

with left:
    st.subheader("Prospect details")
    company_name = st.text_input("Company name", placeholder="Example: Acme SaaS")
    company_website = st.text_input("Company website", placeholder="https://example.com")
    contact_name = st.text_input("Contact name", placeholder="Example: Dana Cohen")
    job_title = st.text_input("Contact job title", placeholder="Example: VP Sales")
    industry = st.text_input("Industry", placeholder="Example: B2B SaaS")

with right:
    st.subheader("Offer details")
    product_context = st.text_area("What are you selling?", value=DEFAULT_PRODUCT_CONTEXT, height=140)
    value_proposition = st.text_area(
        "Main value proposition",
        placeholder="Example: Reduce manual research time and improve reply rates with personalized messaging.",
        height=100,
    )
    call_to_action = st.text_input("Preferred CTA", value="Open to a quick 15-minute call next week?")


def build_prompt() -> str:
    return f"""
You are an ethical AI assistant for Sales Development Representatives.
Use only the information provided by the user. Do not invent facts, clients, funding, news, numbers, or case studies.

Prospect:
- Company: {company_name}
- Website: {company_website}
- Contact: {contact_name}
- Job title: {job_title}
- Industry: {industry}
- Buyer stage: {buyer_stage}

Offer:
- Product/service: {product_context}
- Value proposition: {value_proposition}
- Preferred CTA: {call_to_action}
- Tone: {tone}

Return the output in this exact structure:

## Prospect Snapshot
- One-sentence company summary based only on the provided information
- Why this prospect may be relevant
- Assumptions to verify before outreach

## Likely Pain Points
List 3 realistic pain points, clearly marked as hypotheses.

## Lead Qualification
Score the lead from 1-10 and explain the score in 2 bullets.

## Cold Email
Write one personalized email under 120 words.

## LinkedIn Message
Write one connection message under 300 characters.

## Cold Call Opener
Write a 20-second opener.

## Follow-Up Sequence
Write 3 follow-up emails under 90 words each.

## CRM Note
Write a concise CRM note for a sales rep.
"""

required_fields_complete = bool(company_name and contact_name and job_title and product_context)

st.divider()
col_a, col_b, col_c = st.columns(3)
col_a.markdown('<div class="metric-card"><b>Workflow</b><br>Research → Outreach → CRM</div>', unsafe_allow_html=True)
col_b.markdown('<div class="metric-card"><b>Output</b><br>Email, LinkedIn, call script, follow-ups</div>', unsafe_allow_html=True)
col_c.markdown('<div class="metric-card"><b>Focus</b><br>Ethical personalization, no fake claims</div>', unsafe_allow_html=True)

st.divider()

if st.button("Generate SDR package", type="primary", disabled=not required_fields_complete):
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", None)
    if not api_key:
        st.error("OPENAI_API_KEY is not set. Add it as an environment variable or Streamlit secret.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner("Generating SDR package..."):
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You write accurate, ethical, concise B2B sales outreach. Never invent facts.",
                        },
                        {"role": "user", "content": build_prompt()},
                    ],
                    temperature=0.65,
                )
            output = response.choices[0].message.content
            st.subheader("Generated SDR Package")
            st.markdown(output)
            st.download_button(
                "Download output as Markdown",
                data=output,
                file_name=f"sdr_output_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
                mime="text/markdown",
            )
        except Exception as exc:
            st.error(f"Something went wrong: {exc}")
else:
    if not required_fields_complete:
        st.info("Fill in company name, contact name, job title, and what you are selling to generate outreach.")

with st.expander("Example CV description"):
    st.write(
        "Built an AI-powered SDR assistant using Python, Streamlit, and the OpenAI API to generate prospect snapshots, "
        "lead qualification notes, personalized cold emails, LinkedIn messages, cold call openers, follow-up sequences, "
        "and CRM-ready summaries."
    )

st.caption("Portfolio project: AI-assisted sales prospecting and outreach workflow.")
