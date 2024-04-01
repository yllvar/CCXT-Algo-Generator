import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize OpenAI instance
myOpenAPiKey = ""
llm = OpenAI(openai_api_key=myOpenAPiKey)

# Define prompt template with reference to CCXT
prompt_template = PromptTemplate(
    template="As an expert in cryptocurrency trading using the CCXT library, develop Python code that utilizes CCXT to fetch market data, place orders, and implement trading strategies. Explain each line of code meticulously, elucidating its role in the overall strategy and ensuring optimal performance in cryptocurrency markets.",
    input_variables=["language", "task"]
)

# Define LLM chain with the prompt template
ccxt_chain = LLMChain(
    prompt=prompt_template,
    llm=llm,
    output_key="code"
)

# Title of the Streamlit app
st.title("Cryptocurrency Trading Algorithm Generator")

# Description of the app
st.write("This app generates Python code for cryptocurrency trading algorithms using the CCXT library.")

# Initial conversation prompt
continue_conversation = st.text_area("Start the conversation with the model:")

# Continue conversation loop
while True:
    # Prompt user for input
    user_input = st.text_area("Your response to the model:", value=continue_conversation, height=200)

    # Generate response from the model
    response = llm.generate(prompt=[user_input], max_tokens=50)  # Prompt should be a list

    # Display model's response
    st.subheader("Model's Response:")
    st.write(response.choices[0].text.strip())

    # Prompt user to continue the conversation
    continue_conversation = st.text_area("Continue the conversation with the model:", value=response.choices[0].text.strip())

    # Check if user wants to end the conversation
    if st.button("End Conversation"):
        st.write("Conversation ended.")
        break  # Exit the loop to end the conversation
