import streamlit as st

#Set the application title
st.title("GPT-3.5 Text Summarizer")

#Provide the input area for text to be summarized
input_text = st.text_area("Enter the text you want to summarize:", height=200)

#Initiate three columns for section to be side-by-side
col1, col2, col3 = st.columns(3)

#Slider to control the model hyperparameter
with col1:
    token = st.slider("Token", min_value=0.0, max_value=200.0, value=50.0, step=1.0)
    temp = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    top_p = st.slider("Nucleus Sampling", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    f_pen = st.slider("Frequency Penalty", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)

#Selection box to select the summarization style
with col2:
    option = st.selectbox(
        "How do you like to be explained?",
        (
            "Second-Grader",
            "Professional Data Scientist",
            "Housewives",
            "Retired",
            "University Student",
        ),
    )

#Showing the current parameter used for the model 
with col3:
    with st.expander("Current Parameter"):
        st.write("Current Token :", token)
        st.write("Current Temperature :", temp)
        st.write("Current Nucleus Sampling :", top_p)
        st.write("Current Frequency Penalty :", f_pen)

#Creating button for execute the text summarization
if st.button("Summarize"):
    st.write(generate_summarizer(token, temp, top_p, f_pen, input_text, option))