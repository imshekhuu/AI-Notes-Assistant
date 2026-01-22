from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# -------------------- MODEL --------------------
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# -------------------- SUMMARY --------------------
summary_prompt = PromptTemplate(
    template="""
Summarize the following notes into clear, concise bullet points.
Keep it short and exam-oriented.

Notes:
{notes}

Summary:
""",
    input_variables=["notes"]
)

summary_chain = summary_prompt | model | parser

def summarize_notes(notes):
    return summary_chain.invoke({"notes": notes})


# -------------------- QUESTIONS --------------------
question_prompt = PromptTemplate(
    template="""
From the following notes, generate:
1. 5 conceptual questions
2. 5 short-answer questions

Do NOT include explanations.
Just list questions clearly.

Notes:
{notes}

Questions:
""",
    input_variables=["notes"]
)

question_chain = question_prompt | model | parser

def generate_questions(notes):
    return question_chain.invoke({"notes": notes})


# -------------------- BASICS --------------------
basics_prompt = PromptTemplate(
    template="""
Extract the BASIC concepts from the notes.
For each concept:
- Give a short definition (1–2 lines)
- Keep it simple and foundational

Notes:
{notes}

Basics:
""",
    input_variables=["notes"]
)

basics_chain = basics_prompt | model | parser

def extract_basics(notes):
    return basics_chain.invoke({"notes": notes})



# -------------------- EXPLANATION --------------------
explain_prompt = PromptTemplate(
    input_variables=["notes"],
    template="""
Explain the following notes in very simple language.
Use step-by-step explanation.
Assume the reader is a beginner.

Notes:
{notes}

Explanation:
"""
)

explain_chain = explain_prompt | model | parser


def explain_notes(notes):
    return explain_chain.invoke({"notes": notes})
