import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load(r"E:\chatbot\backend\personality_project\model\naive_bayes.pkl")

# Define the personality traits
traits = ["Openness", "Neuroticism", "Conscientiousness", "Agreeableness", "Extraversion"]

# Function to predict personality
def predict_personality(gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion):
    input_features = [gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion]
    prediction = model.predict([input_features])
    return prediction[0]

# Streamlit app
def main():
    st.title("Welcome to Human Personality Prediction Web Application")
    st.image("https://media.licdn.com/dms/image/C5112AQE1gd7jQK8rZA/article-cover_image-shrink_720_1280/0/1566049171907?e=2147483647&v=beta&t=xEYv549P55_lU3dKxHO1bd85onvnDrvLoYfyRVhotek")

    st.caption("You can predict human personality by providing following factors. Try once!")
    # Input fields
    gender = st.number_input("Gender Male-0 / Female-1" , min_value=0 , max_value=1)
    age = st.number_input("Age", min_value=18, max_value=34)
    openness = st.slider("Openness", 1, 9)
    neuroticism = st.slider("Neuroticism", 1, 9)
    conscientiousness = st.slider("Conscientiousness", 1, 9)
    agreeableness = st.slider("Agreeableness", 1, 9)
    extraversion = st.slider("Extraversion", 1, 9)

    # Predict button
    if st.button("Predict"):
        prediction = predict_personality(gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion)
        st.success(f"Predicted Personality :-- ' {prediction} ' ")
    st.caption("Developed by ADNAN BAIG")

if __name__ == "__main__":
    main()