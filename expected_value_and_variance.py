
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(layout="wide", page_title="Expected Value and Variance Explorer", page_icon="📊")

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
    
    .highlight {
        background-color: #F9E79F;
        padding: 5px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📊 Expected Value and Variance Explorer 📊</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the Expected Value and Variance Explorer!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's dive into these fundamental concepts of probability and statistics.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What are Expected Value and Variance?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
<strong>Expected Value (E(X)):</strong> The average outcome of an experiment if it is repeated many times.
<span class='highlight'>E(X) = Σ(x * P(X = x))</span>, where x is each possible value and P(X = x) is its probability.

<strong>Variance (Var(X)):</strong> A measure of variability that describes how far the values are from the expected value.
<span class='highlight'>Var(X) = E((X - E(X))^2) = Σ((x - E(X))^2 * P(X = x))</span>

<strong>Standard Deviation (σ):</strong> The square root of the variance, which gives a measure of spread in the same units as the original data.
<span class='highlight'>σ = sqrt(Var(X))</span>
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dice Roll", "💰 Investment Scenario", "🎲 Interactive Calculator", "🧠 Quiz"])

with tab1:
    st.markdown("<p class='medium-font'>Example: Rolling a Fair Die</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='small-font'>
    Let's consider rolling a fair six-sided die. We'll calculate the expected value and variance for this scenario.
    </p>
    """, unsafe_allow_html=True)
    
    # Calculations
    outcomes = [1, 2, 3, 4, 5, 6]
    probabilities = [1/6] * 6
    
    expected_value = sum([x * p for x, p in zip(outcomes, probabilities)])
    variance = sum([(x - expected_value)**2 * p for x, p in zip(outcomes, probabilities)])
    std_dev = np.sqrt(variance)

    st.markdown(f"""
    <p class='small-font'>
    Expected Value: E(X) = {expected_value:.2f}<br>
    Variance: Var(X) = {variance:.2f}<br>
    Standard Deviation: σ = {std_dev:.2f}
    </p>
    """, unsafe_allow_html=True)

    # Visualization
    fig, ax = plt.subplots()
    ax.bar(outcomes, probabilities, color='#3498DB')
    ax.axvline(x=expected_value, color='#E74C3C', linestyle='--', label='Expected Value')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Probability')
    ax.set_title('Probability Distribution of Die Roll')
    ax.legend()
    st.pyplot(fig)

with tab2:
    st.markdown("<p class='medium-font'>Investment Scenario</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='small-font'>
    Consider an investment opportunity with the following possible returns and their probabilities:
    </p>
    """, unsafe_allow_html=True)

    # Investment scenario
    returns = [-1000, 0, 1000, 2000]
    probabilities = [0.1, 0.3, 0.4, 0.2]

    expected_return = sum([r * p for r, p in zip(returns, probabilities)])
    variance = sum([(r - expected_return)**2 * p for r, p in zip(returns, probabilities)])
    std_dev = np.sqrt(variance)

    st.markdown(f"""
    <p class='small-font'>
    Possible Returns: {returns}<br>
    Probabilities: {probabilities}<br><br>
    Expected Return: ${expected_return:.2f}<br>
    Variance: ${variance:.2f}<br>
    Standard Deviation: ${std_dev:.2f}
    </p>
    """, unsafe_allow_html=True)

    # Visualization
    fig = go.Figure(data=[go.Bar(x=returns, y=probabilities, marker_color='#3498DB')])
    fig.add_vline(x=expected_return, line_dash="dash", line_color="#E74C3C", annotation_text="Expected Return")
    fig.update_layout(title="Investment Return Distribution",
                      xaxis_title="Return ($)",
                      yaxis_title="Probability")
    st.plotly_chart(fig)

with tab3:
    st.markdown("<p class='medium-font'>Interactive Expected Value and Variance Calculator</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='small-font'>Enter up to 5 outcomes and their probabilities:</p>", unsafe_allow_html=True)
    
    outcomes = []
    probabilities = []

    for i in range(5):
        col1, col2 = st.columns(2)
        with col1:
            outcome = st.number_input(f"Outcome {i+1}", value=0.0, key=f"outcome_{i}")
        with col2:
            probability = st.number_input(f"Probability {i+1}", value=0.0, min_value=0.0, max_value=1.0, key=f"prob_{i}")
        
        if probability > 0:
            outcomes.append(outcome)
            probabilities.append(probability)

    if sum(probabilities) != 1.0:
        st.warning("The sum of probabilities should be 1.0")
    else:
        expected_value = sum([x * p for x, p in zip(outcomes, probabilities)])
        variance = sum([(x - expected_value)**2 * p for x, p in zip(outcomes, probabilities)])
        std_dev = np.sqrt(variance)

        st.markdown(f"""
        <p class='medium-font'>Results:</p>
        <p class='small-font'>
        Expected Value: {expected_value:.2f}<br>
        Variance: {variance:.2f}<br>
        Standard Deviation: {std_dev:.2f}
        </p>
        """, unsafe_allow_html=True)

        # Visualization
        fig = go.Figure(data=[go.Bar(x=outcomes, y=probabilities, marker_color='#3498DB')])
        fig.add_vline(x=expected_value, line_dash="dash", line_color="#E74C3C", annotation_text="Expected Value")
        fig.update_layout(title="Probability Distribution",
                          xaxis_title="Outcome",
                          yaxis_title="Probability")
        st.plotly_chart(fig)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "For a fair coin toss where heads=1 and tails=0, what is the expected value?",
            "options": ["0", "0.5", "1", "2"],
            "correct": 1,
            "explanation": """For a fair coin: P(Heads) = P(Tails) = 0.5
            E(X) = 1 * 0.5 + 0 * 0.5 = 0.5
            
            This represents the average outcome if you were to toss the coin many times."""
        },
        {
            "question": "A game costs $10 to play. You have a 20% chance of winning $30 and an 80% chance of winning nothing. What's the expected value of playing this game?",
            "options": ["-$4", "$0", "$4", "$6"],
            "correct": 0,
            "explanation": """Let's calculate:
            E(X) = (30 * 0.2) + (0 * 0.8) - 10 = 6 - 10 = -4
            
            The negative expected value means that, on average, you lose $4 each time you play this game."""
        },
        {
            "question": "If a random variable X has E(X) = 10 and Var(X) = 9, what is its standard deviation?",
            "options": ["3", "9", "18", "81"],
            "correct": 0,
            "explanation": """The standard deviation is the square root of the variance:
            σ = sqrt(Var(X)) = sqrt(9) = 3
            
            This tells us that, on average, values of X deviate from the expected value by 3 units."""
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
st.markdown("<p class='small-font'>You've explored the concepts of Expected Value and Variance through examples, calculations, and interactive elements. These fundamental concepts are crucial in understanding probability distributions and making informed decisions in various fields, from finance to science. Keep practicing and applying these concepts!</p>", unsafe_allow_html=True)