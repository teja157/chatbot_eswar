import streamlit as st
import openai
import os

# Set your OpenAI API key
api_key = os.environ.get("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")

if api_key is None:
    st.error("OpenAI API key is missing. Set the OPENAI_API_KEY environment variable.")
    st.stop()

openai.api_key = api_key

def display_chat_history(messages):
    for message in messages:
        st.write(f"{message['role'].capitalize()}: {message['content']}")

def get_assistant_response(messages):
    try:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        )
        response = r['choices'][0]['message']['content']
        return response
    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API Error: {e}")
        st.stop()

def main():
    st.title("OpenAI GPT-3.5 Turbo Chatbot")

    messages = [{"role": "assistant", "content": "How can I help?"}]

    while True:
        display_chat_history(messages)

        user_input = st.text_input("User:")
        messages.append({"role": "user", "content": user_input})

        assistant_response = get_assistant_response(messages)
        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()

