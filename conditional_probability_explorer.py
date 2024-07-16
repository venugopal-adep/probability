import streamlit as st
import plotly.graph_objects as go
import random
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(layout="wide", page_title="Conditional Probability Explorer", page_icon="🎲")

# Custom CSS with white background
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background-color: #FFFFFF;
    }
    
    .big-font {
        font-size: 34px !important;
        font-weight: 600;
        color: #2C3E50;
    }
    
    .medium-font {
        font-size: 28px !important;
        font-weight: 600;
        color: #E74C3C;
    }
    
    .small-font {
        font-size: 18px !important;
        color: #34495E;
    }
    
    .stButton>button {
        color: #FFFFFF;
        background-color: #3498DB;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(52, 152, 219, 0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980B9;
        box-shadow: 0 6px 8px rgba(52, 152, 219, 0.2);
        transform: translateY(-2px);
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #3498DB;
    }
    
    .stRadio>div {
        background-color: #F0F3F4;
        border-radius: 10px;
        padding: 10px;
    }
    
    .highlight {
        background-color: #F9E79F;
        padding: 5px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>🎲 Conditional Probability Explorer 🎲</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the Conditional Probability Explorer!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's dive into the concept of conditional probability and how it relates to real-world scenarios.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What is Conditional Probability?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
Conditional probability is the probability of an event occurring, given that another event has already occurred. It is denoted as P(A|B), which reads as "the probability of A given B".

The formula for conditional probability is:
<span class='highlight'>P(A|B) = P(A and B) / P(B)</span>

Where:
- P(A|B) is the probability of A given B has occurred
- P(A and B) is the probability of both A and B occurring
- P(B) is the probability of B occurring
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["📊 Example", "🎲 Interactive Calculator", "🃏 Card Game", "🧠 Quiz"])

with tab1:
    st.markdown("<p class='medium-font'>Example: Medical Test</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='small-font'>
    Let's consider a medical test for a rare disease:
    • 1% of the population has the disease
    • The test is 95% accurate for people who have the disease
    • The test is 90% accurate for people who don't have the disease

    What is the probability that a person actually has the disease, given that they tested positive?
    </p>
    """, unsafe_allow_html=True)
    
    # Calculations
    p_disease = 0.01
    p_positive_given_disease = 0.95
    p_negative_given_no_disease = 0.90
    p_positive_given_no_disease = 1 - p_negative_given_no_disease

    p_positive = p_disease * p_positive_given_disease + (1 - p_disease) * p_positive_given_no_disease
    p_disease_given_positive = (p_disease * p_positive_given_disease) / p_positive

    st.markdown(f"""
    <p class='small-font'>
    P(Disease | Positive) = P(Disease and Positive) / P(Positive)<br>
    = (P(Disease) × P(Positive | Disease)) / P(Positive)<br>
    = ({p_disease:.4f} × {p_positive_given_disease:.4f}) / {p_positive:.4f}<br>
    = {p_disease_given_positive:.4f}
    </p>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <p class='small-font'>
    Therefore, the probability that a person actually has the disease, given a positive test result, is about {p_disease_given_positive:.2%}.
    </p>
    """, unsafe_allow_html=True)

    # Visualization
    fig, ax = plt.subplots()
    ax.bar(['P(Disease)', 'P(Positive)', 'P(Disease|Positive)'], [p_disease, p_positive, p_disease_given_positive], color=['#3498DB', '#E74C3C', '#F1C40F'])
    ax.set_ylabel('Probability')
    ax.set_title('Probabilities in Medical Test Example')
    st.pyplot(fig)

with tab2:
    st.markdown("<p class='medium-font'>Interactive Conditional Probability Calculator</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        p_a = st.slider("P(A)", 0.0, 1.0, 0.5, 0.01)
        p_b = st.slider("P(B)", 0.0, 1.0, 0.5, 0.01)
    with col2:
        p_a_and_b = st.slider("P(A and B)", 0.0, min(p_a, p_b), min(p_a, p_b)/2, 0.01)

    p_a_given_b = p_a_and_b / p_b if p_b != 0 else 0
    p_b_given_a = p_a_and_b / p_a if p_a != 0 else 0

    st.markdown(f"""
    <p class='medium-font'>Results:</p>
    <p class='small-font'>
    P(A|B) = {p_a_given_b:.4f}<br>
    P(B|A) = {p_b_given_a:.4f}
    </p>
    """, unsafe_allow_html=True)

    # Visualization
    fig = go.Figure(data=[go.Bar(x=['P(A)', 'P(B)', 'P(A and B)', 'P(A|B)', 'P(B|A)'], 
                                 y=[p_a, p_b, p_a_and_b, p_a_given_b, p_b_given_a],
                                 marker_color=['#3498DB', '#E74C3C', '#F1C40F', '#2ECC71', '#9B59B6'])])
    fig.update_layout(title="Visualization of Probabilities",
                      xaxis_title="Probabilities",
                      yaxis_title="Value",
                      plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig)

    st.markdown("<p class='small-font'>Try adjusting the sliders to see how the conditional probabilities change!</p>", unsafe_allow_html=True)

with tab3:
    st.markdown("<p class='medium-font'>Card Game: Conditional Probability in Action</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='small-font'>
    Let's play a card game to understand conditional probability. We'll draw two cards from a standard deck without replacement.
    What's the probability of drawing a King on the second draw, given that the first card was a Heart?
    </p>
    """, unsafe_allow_html=True)

    if st.button("Draw Cards"):
        suits = ['♥️', '♦️', '♣️', '♠️']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        first_card = f"{random.choice(ranks)}{random.choice(suits)}"
        remaining_cards = [f"{rank}{suit}" for rank in ranks for suit in suits]
        remaining_cards.remove(first_card)
        second_card = random.choice(remaining_cards)

        st.markdown(f"""
        <p class='small-font'>
        First card: {first_card}<br>
        Second card: {second_card}
        </p>
        """, unsafe_allow_html=True)

        if "♥️" in first_card:
            p_king_given_heart = 3 / 51
            st.markdown(f"""
            <p class='small-font'>
            The first card is a Heart. The probability of drawing a King on the second draw is:
            P(King | Heart) = 3 / 51 ≈ {p_king_given_heart:.4f}
            </p>
            """, unsafe_allow_html=True)
        else:
            p_king_given_not_heart = 4 / 51
            st.markdown(f"""
            <p class='small-font'>
            The first card is not a Heart. The probability of drawing a King on the second draw is:
            P(King | Not Heart) = 4 / 51 ≈ {p_king_given_not_heart:.4f}
            </p>
            """, unsafe_allow_html=True)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "If P(A) = 0.4, P(B) = 0.3, and P(A and B) = 0.2, what is P(A|B)?",
            "options": ["0.67", "0.50", "0.75", "0.60"],
            "correct": 0,
            "explanation": """Using the formula P(A|B) = P(A and B) / P(B):
            P(A|B) = 0.2 / 0.3 ≈ 0.67
            
            This means that given B has occurred, there's a 67% chance that A will also occur."""
        },
        {
            "question": "In a bag of 10 marbles (7 red, 3 blue), you draw 2 marbles without replacement. What's the probability of drawing a blue marble second, given that the first was red?",
            "options": ["0.3", "0.33", "0.29", "0.4"],
            "correct": 1,
            "explanation": """After drawing a red marble, there are 9 marbles left (6 red, 3 blue).
            The probability of drawing a blue marble second is:
            P(Blue | Red) = 3 / 9 = 1 / 3 ≈ 0.33
            
            This demonstrates how the condition (first draw being red) affects the probability of the second draw."""
        },
        {
            "question": "If P(A|B) = 0.8 and P(B) = 0.5, what is P(A and B)?",
            "options": ["0.4", "0.3", "0.6", "0.2"],
            "correct": 0,
            "explanation": """We can rearrange the conditional probability formula:
            P(A|B) = P(A and B) / P(B)
            
            Therefore:
            P(A and B) = P(A|B) × P(B) = 0.8 × 0.5 = 0.4
            
            This shows how we can use conditional probability to find joint probability."""
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
st.markdown("<p class='small-font'>You've explored the concept of conditional probability through examples, calculations, and interactive elements. This fundamental concept is crucial in many real-world applications, from medical diagnoses to weather forecasting. Keep practicing and applying these concepts!</p>", unsafe_allow_html=True)