import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def main():
    st.set_page_config(page_title="Standard Normal Distribution Explorer", layout="wide")
    
    st.title("🔔 Standard Normal Distribution Explorer")
    
    st.markdown("""
    Welcome to the Standard Normal Distribution Explorer! This interactive tool will help you understand
    the concept of standard normal distribution and how to standardize normal distributions.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Interactive Plot", "🧮 Standardization Calculator", "📚 Examples", "🧠 Quiz"])
    
    with tab1:
        interactive_plot()
    
    with tab2:
        standardization_calculator()
    
    with tab3:
        examples()
    
    with tab4:
        quiz()

def interactive_plot():
    st.header("Interactive Normal Distribution Plot")
    
    col1, col2 = st.columns(2)
    with col1:
        mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0, 0.1)
    with col2:
        std_dev = st.slider("Standard Deviation (σ)", 0.1, 3.0, 1.0, 0.1)
    
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    
    x_standard = (x - mean) / std_dev
    y_standard = stats.norm.pdf(x_standard, 0, 1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Original Distribution', line=dict(color='green', width=3)))
    fig.add_trace(go.Scatter(x=x_standard, y=y_standard, mode='lines', name='Standard Normal Distribution', line=dict(color='blue', width=3)))
    
    fig.update_layout(
        title="Normal Distribution vs Standard Normal Distribution",
        xaxis_title="Value",
        yaxis_title="Probability Density",
        height=600,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### Key Concepts
    
    1. **Standard Normal Distribution (Z-distribution):**
       - Always has a mean (μ) of 0 and standard deviation (σ) of 1
       - Used to compare different normal distributions
    
    2. **Standardization:**
       - Process of converting a normal distribution to a standard normal distribution
       - Formula: Z = (X - μ) / σ
         Where X is the original value, μ is the mean, and σ is the standard deviation
    
    3. **Interpretation:**
       - Z-score represents the number of standard deviations a value is from the mean
       - Positive Z-score: value is above the mean
       - Negative Z-score: value is below the mean
    
    Try adjusting the sliders to see how changes in μ and σ affect the original distribution and its standardized form!
    """)

def standardization_calculator():
    st.header("Standardization Calculator")
    
    st.markdown("""
    Use this calculator to convert values from a normal distribution to their standardized (Z-score) equivalents.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        x = st.number_input("Value (X)", value=0.0, step=0.1)
    with col2:
        mean = st.number_input("Mean (μ)", value=0.0, step=0.1)
    with col3:
        std_dev = st.number_input("Standard Deviation (σ)", value=1.0, step=0.1, min_value=0.1)
    
    z_score = (x - mean) / std_dev
    
    st.markdown(f"""
    ### Result
    
    Z-score = (X - μ) / σ = ({x} - {mean}) / {std_dev} = **{z_score:.4f}**
    
    Interpretation: The value {x} is {abs(z_score):.4f} standard deviations {'above' if z_score > 0 else 'below'} the mean.
    """)

def examples():
    st.header("Standardization Examples")
    
    st.subheader("Example 1: IQ Scores")
    st.write("""
    IQ scores are normally distributed with a mean (μ) of 100 and a standard deviation (σ) of 15.
    
    Question: What is the Z-score for an IQ of 130?
    
    Solution:
    1. Use the standardization formula: Z = (X - μ) / σ
    2. Z = (130 - 100) / 15 = 2
    
    Interpretation: An IQ of 130 is 2 standard deviations above the mean.
    """)
    
    st.subheader("Example 2: Height of Adult Males")
    st.write("""
    The height of adult males in a certain population follows a normal distribution with a mean of 170 cm and a standard deviation of 7 cm.
    
    Question: What is the Z-score for a height of 184 cm?
    
    Solution:
    1. Use the standardization formula: Z = (X - μ) / σ
    2. Z = (184 - 170) / 7 = 2
    
    Interpretation: A height of 184 cm is 2 standard deviations above the mean.
    """)
    
    st.subheader("Example 3: Comparing Different Distributions")
    st.write("""
    Student A scored 85 on a test with a mean of 75 and standard deviation of 8.
    Student B scored 92 on a different test with a mean of 80 and standard deviation of 10.
    
    Question: Which student performed better relative to their class?
    
    Solution:
    1. Calculate Z-scores for both students:
       Student A: Z = (85 - 75) / 8 = 1.25
       Student B: Z = (92 - 80) / 10 = 1.2
    
    2. Compare Z-scores:
       Student A's Z-score (1.25) is slightly higher than Student B's (1.2)
    
    Interpretation: Student A performed slightly better relative to their class, as their score was 1.25 standard deviations above their class mean, while Student B's score was 1.2 standard deviations above their class mean.
    """)

def quiz():
    st.header("Standard Normal Distribution Quiz")
    
    questions = [
        {
            "question": "What are the mean and standard deviation of a standard normal distribution?",
            "options": ["Mean = 0, SD = 1", "Mean = 1, SD = 0", "Mean = 0, SD = 0", "Mean = 1, SD = 1"],
            "correct": 0,
            "explanation": "A standard normal distribution, also known as the Z-distribution, always has a mean of 0 and a standard deviation of 1. This is what makes it 'standard' and useful for comparing different normal distributions."
        },
        {
            "question": "If a Z-score is negative, what does it indicate about the original value?",
            "options": ["It's above the mean", "It's equal to the mean", "It's below the mean", "It's impossible to tell"],
            "correct": 2,
            "explanation": "A negative Z-score indicates that the original value is below the mean. The Z-score represents how many standard deviations a value is from the mean, with negative values indicating below the mean and positive values indicating above the mean."
        },
        {
            "question": "Which formula is used to calculate the Z-score?",
            "options": ["Z = (X + μ) / σ", "Z = (X - μ) * σ", "Z = (X - μ) / σ", "Z = (μ - X) / σ"],
            "correct": 2,
            "explanation": "The correct formula for calculating the Z-score is Z = (X - μ) / σ, where X is the original value, μ is the mean, and σ is the standard deviation. This formula standardizes the value by subtracting the mean and dividing by the standard deviation."
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