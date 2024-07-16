import streamlit as st
import plotly.graph_objects as go
import random
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(layout="wide", page_title="Probability Rules Playground", page_icon="🎲")

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
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>🎲 Probability Rules Playground: Addition and Multiplication 🎲</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the Probability Rules Explorer!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's dive into the fundamental rules of probability: Addition and Multiplication.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What are the Addition and Multiplication Rules?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
- <strong class='highlight'>Addition Rule:</strong> Used for calculating the probability of either one event OR another occurring.<br>
- <strong class='highlight'>Multiplication Rule:</strong> Used for calculating the probability of one event AND another occurring.
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["🧮 Addition Rule", "✖️ Multiplication Rule", "🎲 Interactive Example", "🧠 Quiz"])

with tab1:
    st.markdown("<p class='medium-font'>Addition Rule of Probability</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='small-font'>
    The addition rule is used when we want to calculate the probability of either Event A OR Event B occurring.
    
    For mutually exclusive events (events that cannot occur at the same time):
    <span class='highlight'>P(A or B) = P(A) + P(B)</span>
    
    For non-mutually exclusive events:
    <span class='highlight'>P(A or B) = P(A) + P(B) - P(A and B)</span>
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='small-font'>Let's calculate the probability of drawing a King OR a Heart from a standard deck of cards:</p>", unsafe_allow_html=True)
    
    p_king = 4/52
    p_heart = 13/52
    p_king_of_hearts = 1/52
    
    p_king_or_heart = p_king + p_heart - p_king_of_hearts
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <p class='small-font'>
        P(King) = 4/52 = {p_king:.4f}<br>
        P(Heart) = 13/52 = {p_heart:.4f}<br>
        P(King of Hearts) = 1/52 = {p_king_of_hearts:.4f}<br>
        P(King or Heart) = P(King) + P(Heart) - P(King of Hearts) = {p_king_or_heart:.4f}
        </p>
        """, unsafe_allow_html=True)
    with col2:
        fig, ax = plt.subplots()
        ax.pie([p_king, p_heart - p_king_of_hearts, p_king_or_heart, 1 - p_king_or_heart], 
               labels=['Kings (not Hearts)', 'Hearts (not Kings)', 'King of Hearts', 'Other'],
               autopct='%1.1f%%', startangle=90, colors=['#3498DB', '#E74C3C', '#F1C40F', '#95A5A6'])
        ax.axis('equal')
        st.pyplot(fig)

with tab2:
    st.markdown("<p class='medium-font'>Multiplication Rule of Probability</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='small-font'>
    The multiplication rule is used when we want to calculate the probability of Event A AND Event B occurring.
    
    For independent events (the occurrence of one event doesn't affect the other):
    <span class='highlight'>P(A and B) = P(A) × P(B)</span>
    
    For dependent events:
    <span class='highlight'>P(A and B) = P(A) × P(B|A)</span>  [where P(B|A) is the probability of B given A has occurred]
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='small-font'>Let's calculate the probability of drawing two Hearts in a row from a standard deck of cards (without replacement):</p>", unsafe_allow_html=True)
    
    p_first_heart = 13/52
    p_second_heart = 12/51
    
    p_two_hearts = p_first_heart * p_second_heart
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <p class='small-font'>
        P(First Heart) = 13/52 = {p_first_heart:.4f}<br>
        P(Second Heart | First Heart) = 12/51 = {p_second_heart:.4f}<br>
        P(Two Hearts) = P(First Heart) × P(Second Heart | First Heart) = {p_two_hearts:.4f}
        </p>
        """, unsafe_allow_html=True)
    with col2:
        fig, ax = plt.subplots()
        ax.bar(['First Draw', 'Second Draw', 'Both Hearts'], [p_first_heart, p_second_heart, p_two_hearts], color=['#3498DB', '#E74C3C', '#F1C40F'])
        ax.set_ylim(0, 1)
        ax.set_ylabel('Probability')
        st.pyplot(fig)

with tab3:
    st.markdown("<p class='medium-font'>Interactive Probability Calculator</p>", unsafe_allow_html=True)
    
    rule = st.radio("Select Probability Rule:", ["Addition Rule", "Multiplication Rule"])
    
    if rule == "Addition Rule":
        st.markdown("<p class='small-font'>Calculate P(A or B) for non-mutually exclusive events:</p>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            p_a = st.slider("P(A)", 0.0, 1.0, 0.5, 0.01)
            p_b = st.slider("P(B)", 0.0, 1.0, 0.5, 0.01)
        with col2:
            p_a_and_b = st.slider("P(A and B)", 0.0, min(p_a, p_b), 0.1, 0.01)
        
        result = p_a + p_b - p_a_and_b
        st.markdown(f"<p class='medium-font'>P(A or B) = {result:.4f}</p>", unsafe_allow_html=True)
        
    else:
        st.markdown("<p class='small-font'>Calculate P(A and B) for independent events:</p>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            p_a = st.slider("P(A)", 0.0, 1.0, 0.5, 0.01)
        with col2:
            p_b = st.slider("P(B)", 0.0, 1.0, 0.5, 0.01)
        
        result = p_a * p_b
        st.markdown(f"<p class='medium-font'>P(A and B) = {result:.4f}</p>", unsafe_allow_html=True)
    
    # Visualization
    fig = go.Figure(data=[go.Bar(x=['P(A)', 'P(B)', f'P(A {rule.split()[0]} B)'], 
                                 y=[p_a, p_b, result],
                                 marker_color=['#3498DB', '#E74C3C', '#F1C40F'])])
    fig.update_layout(title=f"Visualization of {rule}",
                      xaxis_title="Probabilities",
                      yaxis_title="Value",
                      plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig)

    st.markdown("<p class='small-font'>Try adjusting the sliders to see how the probabilities change!</p>", unsafe_allow_html=True)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "If P(A) = 0.3 and P(B) = 0.4, and A and B are mutually exclusive events, what is P(A or B)?",
            "options": ["0.7", "0.12", "0.1", "0.5"],
            "correct": 0,
            "explanation": """For mutually exclusive events, we use the addition rule: P(A or B) = P(A) + P(B)
            In this case: P(A or B) = 0.3 + 0.4 = 0.7
            
            Mutually exclusive events cannot occur at the same time, so we don't need to subtract their intersection."""
        },
        {
            "question": "If P(A) = 0.6 and P(B) = 0.5, and A and B are independent events, what is P(A and B)?",
            "options": ["0.3", "1.1", "0.55", "0.11"],
            "correct": 0,
            "explanation": """For independent events, we use the multiplication rule: P(A and B) = P(A) × P(B)
            In this case: P(A and B) = 0.6 × 0.5 = 0.3
            
            Independent events don't affect each other's probability of occurring."""
        },
        {
            "question": "If P(A) = 0.4, P(B) = 0.6, and P(A and B) = 0.2, what is P(A or B)?",
            "options": ["1.0", "0.8", "0.24", "0.5"],
            "correct": 1,
            "explanation": """For non-mutually exclusive events, we use the formula: P(A or B) = P(A) + P(B) - P(A and B)
            In this case: P(A or B) = 0.4 + 0.6 - 0.2 = 0.8
            
            We subtract P(A and B) to avoid counting the overlap twice."""
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
st.markdown("<p class='small-font'>You've explored the addition and multiplication rules of probability. These fundamental concepts are crucial in calculating complex probabilities in various real-world scenarios. Keep practicing!</p>", unsafe_allow_html=True)