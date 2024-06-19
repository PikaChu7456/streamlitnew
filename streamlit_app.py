import streamlit as st
import cohere

# Initialize the Cohere client
co = cohere.Client('TcZjPcNuntkBpDbSsH5M5X8N9vlSs6Mq11KoL3rd')

# Initialize the chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Create a Streamlit text input for user input
user_input = st.text_input("Enter your message:")

# Create a Streamlit button to trigger the response generation
generate_response = st.button("Get Response")

# Create a Streamlit text area to display the chat history
chat_history_area_placeholder = st.empty()
chat_history_area = chat_history_area_placeholder.text_area("Chat History:", height=300, value="")

if generate_response:
    # Get the user input
    message = user_input

    # Generate a response with the current chat history
    response = co.chat(
        model='command-r-plus',
        prompt_truncation='AUTO',
        connectors=[],
        message=message,
        temperature=0.8,
        chat_history=st.session_state.chat_history,
        preamble='Humorous, witty, and playful. Think comedy writer.'
    )
    answer = response.text

    # Update the chat history
    user_message = {"role": "USER", "text": message}
    bot_message = {"role": "CHATBOT", "text": answer}

    st.session_state.chat_history.append(user_message)
    st.session_state.chat_history.append(bot_message)

    # Update the chat history area
    chat_history_text = ""
    for message in st.session_state.chat_history:
        if message["role"] == "USER":
            chat_history_text += "**You:** " + message["text"] + "\n"
        else:
            chat_history_text += "**Bot:** " + message["text"] + "\n"
    chat_history_area_placeholder.text_area("Chat History:", height=300, value=chat_history_text)
