import streamlit as st
import plotly.graph_objects as go
import random
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(layout="wide", page_title="Bayes' Theorem Explorer", page_icon="🧮")

# Custom CSS (unchanged, omitted for brevity)
st.markdown("""
<style>
    # ... (keep the existing CSS)
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>🧮 Bayes' Theorem Explorer 🧮</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the Bayes' Theorem Explorer!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's explore Bayes' Theorem and its applications in various scenarios.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What is Bayes' Theorem?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
Bayes' Theorem is a fundamental principle in probability theory that describes the probability of an event based on prior knowledge of conditions that might be related to the event. It is expressed as:

<span class='highlight'>P(A|B) = (P(B|A) * P(A)) / P(B)</span>

Where:
- P(A|B) is the posterior probability of A given B
- P(B|A) is the likelihood of B given A
- P(A) is the prior probability of A
- P(B) is the marginal probability of B
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["📊 Example", "🧮 Interactive Calculator", "🏥 Medical Diagnosis", "🧠 Quiz"])

with tab1:
    st.markdown("<p class='medium-font'>Example: Email Spam Filter</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's consider an email spam filter:
        • 1% of all emails are spam
        • 95% of spam emails contain the word "free"
        • 10% of non-spam emails contain the word "free"

        What is the probability that an email is spam, given that it contains the word "free"?
        </p>
        """, unsafe_allow_html=True)
        
        # Calculations
        p_spam = 0.01
        p_free_given_spam = 0.95
        p_free_given_not_spam = 0.10

        p_free = p_spam * p_free_given_spam + (1 - p_spam) * p_free_given_not_spam
        p_spam_given_free = (p_free_given_spam * p_spam) / p_free

        st.markdown(f"""
        <p class='small-font'>
        P(Spam | Free) = (P(Free | Spam) * P(Spam)) / P(Free)<br>
        = ({p_free_given_spam:.4f} * {p_spam:.4f}) / {p_free:.4f}<br>
        = {p_spam_given_free:.4f}
        </p>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <p class='small-font'>
        Therefore, the probability that an email is spam, given that it contains the word "free", is about {p_spam_given_free:.2%}.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        # Visualization
        fig, ax = plt.subplots()
        ax.bar(['P(Spam)', 'P(Free)', 'P(Spam|Free)'], [p_spam, p_free, p_spam_given_free], color=['#3498DB', '#E74C3C', '#F1C40F'])
        ax.set_ylabel('Probability')
        ax.set_title('Probabilities in Spam Filter Example')
        st.pyplot(fig)

with tab2:
    st.markdown("<p class='medium-font'>Interactive Bayes' Theorem Calculator</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        p_a = st.slider("P(A) - Prior probability", 0.0, 1.0, 0.5, 0.01)
        p_b_given_a = st.slider("P(B|A) - Likelihood", 0.0, 1.0, 0.8, 0.01)
        p_b = st.slider("P(B) - Marginal probability", 0.0, 1.0, 0.3, 0.01)

        p_a_given_b = (p_b_given_a * p_a) / p_b if p_b != 0 else 0

        st.markdown(f"""
        <p class='medium-font'>Results:</p>
        <p class='small-font'>
        P(A|B) = {p_a_given_b:.4f}
        </p>
        """, unsafe_allow_html=True)

    with col2:
        # Visualization
        fig = go.Figure(data=[go.Bar(x=['P(A)', 'P(B|A)', 'P(B)', 'P(A|B)'], 
                                     y=[p_a, p_b_given_a, p_b, p_a_given_b],
                                     marker_color=['#3498DB', '#E74C3C', '#F1C40F', '#2ECC71'])])
        fig.update_layout(title="Visualization of Bayes' Theorem",
                          xaxis_title="Probabilities",
                          yaxis_title="Value",
                          plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig)

    st.markdown("<p class='small-font'>Try adjusting the sliders to see how the posterior probability changes!</p>", unsafe_allow_html=True)

with tab3:
    st.markdown("<p class='medium-font'>Medical Diagnosis: Bayes' Theorem in Action</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's apply Bayes' Theorem to a medical diagnosis scenario. We'll calculate the probability of a patient having a disease given a positive test result.
        </p>
        """, unsafe_allow_html=True)

        prevalence = st.slider("Disease prevalence", 0.0, 0.1, 0.01, 0.001)
        sensitivity = st.slider("Test sensitivity", 0.8, 1.0, 0.95, 0.01)
        specificity = st.slider("Test specificity", 0.8, 1.0, 0.90, 0.01)

        p_positive = prevalence * sensitivity + (1 - prevalence) * (1 - specificity)
        p_disease_given_positive = (sensitivity * prevalence) / p_positive

        st.markdown(f"""
        <p class='small-font'>
        P(Disease | Positive) = (P(Positive | Disease) * P(Disease)) / P(Positive)<br>
        = ({sensitivity:.4f} * {prevalence:.4f}) / {p_positive:.4f}<br>
        = {p_disease_given_positive:.4f}
        </p>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <p class='small-font'>
        The probability of having the disease, given a positive test result, is {p_disease_given_positive:.2%}.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        # Visualization
        fig, ax = plt.subplots()
        ax.bar(['P(Disease)', 'P(Positive)', 'P(Disease|Positive)'], 
               [prevalence, p_positive, p_disease_given_positive], 
               color=['#3498DB', '#E74C3C', '#F1C40F'])
        ax.set_ylabel('Probability')
        ax.set_title('Probabilities in Medical Diagnosis')
        st.pyplot(fig)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "In Bayes' Theorem, what does P(A|B) represent?",
            "options": ["Prior probability", "Likelihood", "Posterior probability", "Marginal probability"],
            "correct": 2,
            "explanation": "P(A|B) represents the posterior probability, which is the probability of event A occurring given that B has occurred."
        },
        {
            "question": "If P(A) = 0.4, P(B|A) = 0.3, and P(B) = 0.2, what is P(A|B) according to Bayes' Theorem?",
            "options": ["0.5", "0.6", "0.7", "0.8"],
            "correct": 1,
            "explanation": """Using Bayes' Theorem: P(A|B) = (P(B|A) * P(A)) / P(B)
            = (0.3 * 0.4) / 0.2 = 0.12 / 0.2 = 0.6"""
        },
        {
            "question": "What is the main advantage of using Bayes' Theorem in real-world applications?",
            "options": ["It's always faster than other methods", "It incorporates prior knowledge into probability calculations", "It only works with large datasets", "It eliminates the need for data collection"],
            "correct": 1,
            "explanation": "Bayes' Theorem allows us to incorporate prior knowledge (P(A)) into our probability calculations, making it particularly useful in real-world scenarios where we have some prior information or beliefs."
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"<p class='small-font'><strong>Question {i+1}:</strong> {q['question']}</p>", unsafe_allow_html=True)
        user_answer = st.radio("Select your answer:", q['options'], key=f"q{i}")
        
        if st.button("Check Answer", key=f"check{i}"):
            if q['options'].index(user_answer) == q['correct']:
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error("Incorrect. Try again! 🤔")
            st.info(q['explanation'])
        st.markdown("---")

    if st.button("Show Final Score"):
        st.markdown(f"<p class='big-font'>Your score: {score}/{len(questions)}</p>", unsafe_allow_html=True)
        if score == len(questions):
            st.balloons()

# Conclusion
st.markdown("<p class='big-font'>Congratulations! 🎊</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>You've explored Bayes' Theorem through examples, calculations, and interactive elements. This powerful tool is essential in many fields, including medicine, finance, and machine learning. Keep practicing and applying Bayes' Theorem to real-world problems!</p>", unsafe_allow_html=True)