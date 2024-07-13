import streamlit as st
import plotly.graph_objects as go
import numpy as np

def introduction():
    st.write("""
    The uniform distribution is a probability distribution where all outcomes are equally likely. 
    It's often visualized as a rectangular shape in probability density functions.
    """)
    
    st.subheader("🌍 Real-world Examples")
    examples = [
        "Lottery: Each number has an equal chance of being drawn",
        "Roulette wheel: Each number is equally likely to come up",
        "Random number generator: Each number in the range has equal probability"
    ]
    for ex in examples:
        st.info(ex)

def interactive_simulation():
    st.subheader("🎭 Interactive Simulation")
    if st.button("Roll a Die 🎲"):
        result = np.random.randint(1, 7)
        st.success(f"You rolled a {result}!")
        st.balloons()
    
    st.subheader("🧮 Probability Calculator")
    n_outcomes = st.number_input("Number of possible outcomes", min_value=1, value=6)
    prob = 1 / n_outcomes
    st.write(f"Probability of each outcome: 1/{n_outcomes} = {prob:.4f}")

def visualization():
    st.subheader("📊 Uniform Distribution Visualizer")
    a, b = st.slider("Range (a, b)", 0, 10, (0, 5))
    x = np.linspace(a-1, b+1, 1000)
    y = np.where((x >= a) & (x <= b), 1/(b-a), 0)
    fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', fill='tozeroy', line_color='#FF4B4B'))
    fig.update_layout(
        title='Probability Density Function',
        xaxis_title='x',
        yaxis_title='P(x)',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig)

def solved_numerical():
    st.subheader("🔢 Solved Numerical")
    st.write("A uniform distribution has a range [3, 9].")
    st.write("Calculate the mean and variance.")
    
    with st.expander("See Solution"):
        st.latex(r"Mean = \mu = \frac{a + b}{2}")
        st.latex(r"Variance = \sigma^2 = \frac{(b - a)^2}{12}")
        st.write("Given: a = 3, b = 9")
        st.write("Mean = (3 + 9) / 2 = 6")
        st.write("Variance = (9 - 3)² / 12 = 36 / 12 = 3")
        st.success("Therefore, μ = 6 and σ² = 3")

def quiz():
    st.subheader("❓ Quiz Time!")
    questions = [
        {
            "question": "What is the probability of rolling an even number on a fair six-sided die?",
            "options": ["1/3", "1/2", "2/3", "1/6"],
            "correct": "1/2",
            "explanation": "There are 3 even numbers (2, 4, 6) out of 6 possible outcomes. So, the probability is 3/6 = 1/2."
        },
        {
            "question": "In a uniform distribution with range [0, 10], what is the probability of getting a value less than or equal to 5?",
            "options": ["0.25", "0.5", "0.75", "1"],
            "correct": "0.5",
            "explanation": "The probability is proportional to the length of the interval. Here, it's 5 / (10 - 0) = 0.5 or 50%."
        },
        {
            "question": "What is the mean of a uniform distribution with range [2, 8]?",
            "options": ["3", "4", "5", "6"],
            "correct": "5",
            "explanation": "The mean of a uniform distribution is (a + b) / 2. Here, it's (2 + 8) / 2 = 5."
        }
    ]
    
    for i, q in enumerate(questions, 1):
        st.write(f"Q{i}: {q['question']}")
        answer = st.radio(f"Select your answer for Q{i}:", q['options'], key=f"q{i}")
        if st.button(f"Check Answer for Q{i}"):
            if answer == q['correct']:
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect. Try again!")
            st.info(f"Explanation: {q['explanation']}")
        st.write("---")

def main():
    st.set_page_config(page_title="Uniform Distribution Explorer", layout="wide")
    
    st.title("🎲 Understanding Uniform Distribution")
    st.write("**Developed by : Venugopal Adep**")
    st.markdown("---")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introduction", "Interactive Simulation", "Visualization", "Solved Numerical", "Quiz"])
    
    with tab1:
        introduction()
    
    with tab2:
        interactive_simulation()
    
    with tab3:
        visualization()
    
    with tab4:
        solved_numerical()
    
    with tab5:
        quiz()

if __name__ == "__main__":
    main()
