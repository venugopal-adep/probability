import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def main():
    st.set_page_config(page_title="Normal Distribution Area Explorer", layout="wide")
    
    st.title("🔔 Normal Distribution: Area Under the Curve")
    st.write("**Developed by : Venugopal Adep**")
    
    st.markdown("""
    Welcome to the Normal Distribution Area Explorer! This interactive tool will help you understand
    how the area under the density curve relates to probability in a normal distribution.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Interactive Plot", "🧮 Probability Calculator", "📚 Numerical Examples", "🧠 Quiz"])
    
    with tab1:
        interactive_plot()
    
    with tab2:
        probability_calculator()
    
    with tab3:
        numerical_examples()
    
    with tab4:
        quiz()

def interactive_plot():
    st.header("Interactive Normal Distribution Plot")
    
    col1, col2 = st.columns(2)
    with col1:
        mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0, 0.1)
    with col2:
        std_dev = st.slider("Standard Deviation (σ)", 0.1, 3.0, 1.0, 0.1)
    
    x = np.linspace(-10, 10, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution', line=dict(color='royalblue', width=3)))
    
    lower = st.slider("Lower bound", -10.0, 10.0, float(mean - std_dev), 0.1)
    upper = st.slider("Upper bound", lower, 10.0, float(mean + std_dev), 0.1)
    
    x_fill = np.linspace(max(lower, -10), min(upper, 10), 100)
    y_fill = stats.norm.pdf(x_fill, mean, std_dev)
    
    fig.add_trace(go.Scatter(x=x_fill, y=y_fill, fill='tozeroy', fillcolor='rgba(255,0,0,0.3)', line=dict(color='rgba(255,0,0,0.5)'), name='Area'))
    
    prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(lower, mean, std_dev)
    
    fig.update_layout(
        title=f"Normal Distribution (μ={mean:.2f}, σ={std_dev:.2f})",
        xaxis_title="Value",
        yaxis_title="Probability Density",
        xaxis_range=[-10, 10],
        showlegend=False,
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    ### Interpretation
    
    The shaded area represents the probability that a randomly chosen value will fall between {lower:.2f} and {upper:.2f}.
    
    **Probability: {prob:.4f}** (or {prob*100:.2f}%)
    
    This means that there's a {prob*100:.2f}% chance that a randomly selected value from this distribution will be between {lower:.2f} and {upper:.2f}.
    """)
    
    st.markdown("""
    ### Key Concepts
    
    1. The total area under the entire curve is always 1 (or 100%).
    2. The probability of a value falling within a specific range is equal to the area under the curve for that range.
    3. μ (mean) determines the center of the distribution.
    4. σ (standard deviation) determines the spread of the distribution.
    
    Try adjusting the sliders to see how changes in μ, σ, and the interval bounds affect the probability!
    """)

def probability_calculator():
    st.header("Probability Calculator")
    
    st.markdown("""
    Here, we'll calculate probabilities for a normal distribution using Python's SciPy library.
    This saves us from doing complex calculus calculations by hand!
    """)
    
    mean = st.number_input("Mean (μ)", value=0.0, step=0.1)
    std_dev = st.number_input("Standard Deviation (σ)", value=1.0, step=0.1, min_value=0.1)
    
    st.subheader("Calculate probability for a range")
    col1, col2 = st.columns(2)
    with col1:
        lower = st.number_input("Lower bound", value=float(mean - std_dev), step=0.1)
    with col2:
        upper = st.number_input("Upper bound", value=float(mean + std_dev), step=0.1)
    
    prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(lower, mean, std_dev)
    
    st.write(f"The probability of a value between {lower} and {upper} is: {prob:.4f}")
    
    st.markdown("""
    ### How it's calculated:
    
    We use the Cumulative Distribution Function (CDF) of the normal distribution:
    
    1. Calculate CDF at the upper bound: `CDF(upper)`
    2. Calculate CDF at the lower bound: `CDF(lower)`
    3. Subtract: `Probability = CDF(upper) - CDF(lower)`
    
    This gives us the area under the curve between the two points, which is the probability.
    """)

def numerical_examples():
    st.header("Numerical Examples")
    
    st.subheader("Example 1: IQ Scores")
    st.write("""
    IQ scores are normally distributed with a mean (μ) of 100 and a standard deviation (σ) of 15.
    
    Question: What is the probability that a randomly selected person has an IQ between 85 and 115?
    
    Solution:
    1. Standardize the values:
       z₁ = (85 - 100) / 15 = -1
       z₂ = (115 - 100) / 15 = 1
    
    2. Use the standard normal distribution:
       P(-1 < Z < 1) = CDF(1) - CDF(-1) = 0.8413 - 0.1587 = 0.6826
    
    3. Therefore, the probability is 0.6826 or about 68.26%
    """)
    
    st.subheader("Example 2: Height of Adult Females")
    st.write("""
    The height of adult females in a certain population follows a normal distribution with a mean of 165 cm and a standard deviation of 6 cm.
    
    Question: What percentage of adult females are taller than 177 cm?
    
    Solution:
    1. Standardize the value:
       z = (177 - 165) / 6 = 2
    
    2. We want P(X > 177), which is equivalent to P(Z > 2)
    
    3. Using the standard normal table:
       P(Z > 2) = 1 - P(Z < 2) = 1 - 0.9772 = 0.0228
    
    4. Therefore, about 2.28% of adult females are taller than 177 cm
    """)
    
    st.subheader("Example 3: Manufacturing Process")
    st.write("""
    A manufacturing process produces bolts with a diameter that is normally distributed with a mean of 10 mm and a standard deviation of 0.2 mm.
    
    Question: What proportion of bolts will have a diameter between 9.6 mm and 10.4 mm?
    
    Solution:
    1. Standardize the values:
       z₁ = (9.6 - 10) / 0.2 = -2
       z₂ = (10.4 - 10) / 0.2 = 2
    
    2. Calculate the probability:
       P(-2 < Z < 2) = CDF(2) - CDF(-2) = 0.9772 - 0.0228 = 0.9544
    
    3. Therefore, about 95.44% of bolts will have a diameter between 9.6 mm and 10.4 mm
    """)

def quiz():
    st.header("Normal Distribution Quiz")
    
    questions = [
        {
            "question": "What does the total area under a normal distribution curve represent?",
            "options": ["The mean", "The standard deviation", "The total probability (100%)", "The median"],
            "correct": 2,
            "explanation": "The total area under any probability density curve, including the normal distribution, represents the total probability of all possible outcomes, which is always 1 or 100%."
        },
        {
            "question": "If you increase the standard deviation while keeping the mean constant, what happens to the shape of the normal curve?",
            "options": ["It becomes taller and narrower", "It becomes shorter and wider", "It shifts to the right", "It shifts to the left"],
            "correct": 1,
            "explanation": "Increasing the standard deviation while keeping the mean constant makes the normal curve shorter and wider. This represents a greater spread of data around the mean."
        },
        {
            "question": "In a standard normal distribution (mean = 0, standard deviation = 1), approximately what percentage of data falls between -1 and 1?",
            "options": ["50%", "68%", "95%", "99.7%"],
            "correct": 1,
            "explanation": "In a standard normal distribution, about 68% of the data falls within one standard deviation of the mean. Since the standard deviation is 1, this means 68% of the data is between -1 and 1."
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
