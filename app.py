import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain




st.set_page_config(page_title="AlgebrAI: Your Math Chatbot", page_icon="🧮")
st.title("🧮 Text to Math Problem Solver (Groq + LangChain)")

st.markdown(
    """
    <div style='display:flex; align-items:center; gap:10px; margin-bottom:10px;'>
        <img src='https://img.icons8.com/ios-filled/50/000000/brain.png' width='30'>
        <span style='font-weight:bold;'>Model in Use: llama-3.3-70b-versatile</span>
    </div>
    """,
    unsafe_allow_html=True
)

groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
if not groq_api_key:
    st.info("Please enter your Groq API key.")
    st.stop()

st.success("Hey 👋 Stuck with a math problem!")    

show_steps = st.sidebar.checkbox("Show step-by-step explanation", value=True)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0
)

if show_steps:
    prompt_text = """
You are a math tutor.

Solve the problem carefully.
Show all calculations step by step.
Number each step clearly.
End with a final answer line.

Problem:
{question}

Format your response exactly like this:

Step 1: ...
Step 2: ...
Step 3: ...

Final Answer: ...
"""
else:
    prompt_text = """
Solve the problem and give ONLY the final numerical answer.

Problem:
{question}
"""

prompt = PromptTemplate(input_variables=["question"], template=prompt_text)
chain = LLMChain(llm=llm, prompt=prompt)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Math chatbot. Ask me any math question."}
    ]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Enter your math problem here...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.spinner("Solving..."):
        result = chain.run(user_input)

    st.session_state["messages"].append({"role": "assistant", "content": result})
    st.chat_message("assistant").write(result)
    st.caption("✅ Completed")
