import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def main():
    st.set_page_config(page_title="Normal Distribution Explorer", layout="wide")
    
    st.title("🔔 Normal Distribution Explorer")
    
    st.markdown("""
    Welcome to the Normal Distribution Explorer! This interactive tool will help you understand
    the properties and characteristics of the normal distribution, also known as the Gaussian distribution.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Concept Explorer", "📊 Interactive Plot", "🧮 Numerical Examples", "🧠 Quiz"])
    
    with tab1:
        concept_explorer()
    
    with tab2:
        interactive_plot()
    
    with tab3:
        numerical_examples()
    
    with tab4:
        quiz()

def concept_explorer():
    st.header("Key Concepts of Normal Distribution")
    
    st.subheader("1. The Normal Curve")
    st.write("""
    The graph of a normal distribution is called the normal curve. It's bell-shaped and symmetric
    around the mean. This shape is fundamental to many natural phenomena and statistical analyses.
    """)
    
    st.subheader("2. Symmetry")
    st.write("""
    The normal curve is perfectly symmetric around the mean. This means that the left and right
    halves of the curve are mirror images of each other.
    """)
    
    st.subheader("3. Measures of Central Tendency")
    st.write("""
    In a normal distribution, the mean, median, and mode are all equal. This is due to the
    perfect symmetry of the distribution.
    """)
    
    st.subheader("4. Area Under the Curve")
    st.write("""
    The total area under the normal curve is always 1 (or 100%). This property makes it useful
    for probability calculations.
    """)
    
    st.subheader("5. The 68-95-99.7 Rule")
    st.write("""
    This rule describes the percentage of data that falls within certain ranges of standard deviations:
    - About 68% of the data falls within 1 standard deviation of the mean
    - About 95% of the data falls within 2 standard deviations of the mean
    - About 99.7% of the data falls within 3 standard deviations of the mean
    """)

def interactive_plot():
    st.header("Interactive Normal Distribution Plot")
    
    col1, col2 = st.columns(2)
    with col1:
        mean = st.slider("Select the mean", -5.0, 5.0, 0.0, 0.1)
    with col2:
        std_dev = st.slider("Select the standard deviation", 0.1, 3.0, 1.0, 0.1)
    
    x = np.linspace(-10, 10, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution', line=dict(color='royalblue', width=3)))
    
    # Add vertical lines for standard deviations
    colors = ['red', 'green', 'orange']
    for i in range(1, 4):
        fig.add_vline(x=mean + i*std_dev, line_dash="dash", line_color=colors[i-1], annotation_text=f"+{i}σ")
        fig.add_vline(x=mean - i*std_dev, line_dash="dash", line_color=colors[i-1], annotation_text=f"-{i}σ")
    
    fig.add_vline(x=mean, line_dash="solid", line_color="black", annotation_text="Mean")
    
    fig.update_layout(
        title=f"Normal Distribution (μ={mean}, σ={std_dev})",
        xaxis_title="Value",
        yaxis_title="Probability Density",
        xaxis_range=[-10, 10],
        showlegend=False,
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Probability Calculations")
    lower = st.number_input("Lower bound", value=mean-std_dev, format="%.2f")
    upper = st.number_input("Upper bound", value=mean+std_dev, format="%.2f")
    
    prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(lower, mean, std_dev)
    st.write(f"Probability of a value between {lower:.2f} and {upper:.2f}: {prob:.4f}")

def numerical_examples():
    st.header("Numerical Examples")
    
    st.subheader("Example 1: IQ Scores")
    st.write("""
    IQ scores are normally distributed with a mean (μ) of 100 and a standard deviation (σ) of 15.
    
    Question: What percentage of people have an IQ between 85 and 115?
    
    Solution:
    1. Calculate z-scores for 85 and 115:
       z₁ = (85 - 100) / 15 = -1
       z₂ = (115 - 100) / 15 = 1
    
    2. Use the standard normal distribution table or calculator:
       P(-1 < Z < 1) = 0.6826
    
    3. Convert to percentage: 0.6826 * 100 = 68.26%
    
    Therefore, approximately 68.26% of people have an IQ between 85 and 115.
    """)
    
    st.subheader("Example 2: Height of Adult Males")
    st.write("""
    The height of adult males in a country follows a normal distribution with a mean of 170 cm and a standard deviation of 7 cm.
    
    Question: What is the probability that a randomly selected adult male is taller than 184 cm?
    
    Solution:
    1. Calculate the z-score for 184 cm:
       z = (184 - 170) / 7 = 2
    
    2. We want P(X > 184), which is equivalent to P(Z > 2)
    
    3. Using a standard normal table or calculator:
       P(Z > 2) = 1 - P(Z < 2) = 1 - 0.9772 = 0.0228
    
    4. Convert to percentage: 0.0228 * 100 = 2.28%
    
    Therefore, the probability that a randomly selected adult male is taller than 184 cm is approximately 2.28%.
    """)

def quiz():
    st.header("Normal Distribution Quiz")
    
    questions = [
        {
            "question": "What percentage of data falls within two standard deviations of the mean in a normal distribution?",
            "options": ["68%", "95%", "99.7%", "50%"],
            "correct": 1,
            "explanation": "In a normal distribution, approximately 95% of the data falls within two standard deviations of the mean. This is part of the 68-95-99.7 rule."
        },
        {
            "question": "If a normal distribution has a mean of 50 and a standard deviation of 10, what is the value that is one standard deviation above the mean?",
            "options": ["40", "50", "60", "70"],
            "correct": 2,
            "explanation": "One standard deviation above the mean is calculated as: mean + 1*standard deviation = 50 + 1*10 = 60."
        },
        {
            "question": "In a standard normal distribution (μ=0, σ=1), what is the approximate probability of a value being between -1 and 1?",
            "options": ["0.50", "0.68", "0.95", "0.99"],
            "correct": 1,
            "explanation": "In a standard normal distribution, approximately 68% (0.68) of the data falls within one standard deviation of the mean, which is the range from -1 to 1."
        }
    ]
    
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer {i+1}"):
            if q["options"].index(answer) == q["correct"]:
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect. Try again!")
            st.write(f"Explanation: {q['explanation']}")

if __name__ == "__main__":
    main()