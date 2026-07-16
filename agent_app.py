import streamlit as st
from langgraph.graph import StateGraph, END
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated
import operator
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Research Assistant Agent")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

@tool
def calculator(expression: str) -> str:
    """Evaluates a basic math expression, e.g. '5 + 3' or '10 * 2'."""
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid expression"

@tool
def get_word_definition(word: str) -> str:
    """Returns a simple definition for a small set of known words."""
    definitions = {
        "rag": "Retrieval-Augmented Generation — combining document retrieval with LLM generation.",
        "agent": "An AI system that can decide which actions or tools to use to complete a task.",
        "embedding": "A numerical representation of text that captures its meaning."
    }
    return definitions.get(word.lower(), "Definition not found.")

tools = [calculator, get_word_definition]
tools_by_name = {t.name: t for t in tools}
llm_with_tools = llm.bind_tools(tools)

class GraphState(TypedDict):
    messages: Annotated[list, operator.add]

def call_model(state: GraphState) -> GraphState:
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

def call_tool(state: GraphState) -> GraphState:
    last_message = state["messages"][-1]
    call = last_message.tool_calls[0]
    tool_fn = tools_by_name[call["name"]]
    result = tool_fn.invoke(call["args"])
    tool_message = ToolMessage(content=str(result), tool_call_id=call["id"])
    return {"messages": [tool_message]}

def should_continue(state: GraphState) -> str:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "use_tool"
    return "end"

graph = StateGraph(GraphState)
graph.add_node("call_model", call_model)
graph.add_node("call_tool", call_tool)
graph.set_entry_point("call_model")
graph.add_conditional_edges("call_model", should_continue, {"use_tool": "call_tool", "end": END})
graph.add_edge("call_tool", "call_model")

app = graph.compile()

# TYPE THIS PART — the new concept: Streamlit UI wrapping the agent
user_question = st.text_input("Ask me something (math or word definitions):")

if user_question:
    with st.spinner("Thinking..."):
        result = app.invoke({"messages": [HumanMessage(content=user_question)]})
        final_answer = result["messages"][-1].content
        st.write("**Answer:**", final_answer)

        with st.expander("See agent's steps"):
            for msg in result["messages"]:
                st.write(f"**{type(msg).__name__}:** {msg.content}")