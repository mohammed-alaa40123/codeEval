
import requests
import streamlit as st
import os
API = os.getenv["API"]
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": f"Bearer {API}"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


def evaluate_code(prompt):
    return query({"inputs": f"{prompt}"})


st.title("Code Evaluator")

# Collect task description and code from user
task_description = st.text_area("Task Description")
user_code = st.text_area("Code (Solution)")

# Build prompt
prompt = f"Evaluate the given Python code in percentage out of 100 in terms of task adherence, modularity, performance, clean code, and readability. If the task involves AI or data-related concepts, ensure key components like preprocessing, data splitting, model training, and testing are present.\n\n---\n\n**Task Description:**\n\n{task_description}\n\n---\n\n**Code (Solution):**\n\n```python\n{user_code}\n```\n\n---"
# Evaluate the code

eval = st.button("Evaluate😊")
evaluation_result = evaluate_code(prompt)[0]["generated_text"]

if eval:
# Display evaluation result
	st.subheader("Evaluation Result:")
	st.markdown(evaluation_result)
