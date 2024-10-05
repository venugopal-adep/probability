import streamlit as st
import plotly.graph_objs as go
import numpy as np
from scipy import stats

st.set_page_config(layout="wide", page_title="Understanding Random Variables")

# Custom CSS for better visual appeal
st.markdown("""
<style>
    .main {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #1E90FF;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("Understanding Random Variables")

st.markdown("""
<div class="info-box">
<h2>What is a Random Variable?</h2>
<p>A random variable is a function that assigns a numerical value to each outcome of an experiment. It assumes different values with different probabilities. It is usually denoted by a capital letter X and the probability associated with any particular value of X is denoted by P(X=x).</p>
</div>
""", unsafe_allow_html=True)

# Example of coin toss
st.subheader("Example: Coin Toss")
st.write("""
Suppose that a fair coin is tossed twice and the possible outcomes are {HH, HT, TH, TT}. Let X be the random variable representing the number of heads that can come up. So, X can take values from the set {2, 1, 0}.
The probability of two heads coming up is P(X=2) = 1/4.
""")

# Visualization of Random Variable types
st.subheader("Types of Random Variables")
col1, col2 = st.columns(2)

with col1:
    st.info("**Discrete random variable:** It can take only a finite number of values.\n\nFor example: Number of employees getting promoted in an organization.")
    
    # Interactive example for discrete random variable
    st.subheader("Interactive Example: Employee Promotions")
    num_employees = st.slider("Total number of employees", 10, 100, 50)
    promotion_rate = st.slider("Promotion rate (%)", 0, 100, 10) / 100
    
    if st.button("Simulate Promotions"):
        promotions = np.random.binomial(num_employees, promotion_rate)
        st.success(f"Number of employees promoted: {promotions}")
        
        # Plot probability distribution
        x = list(range(num_employees + 1))  # Convert to list
        y = [stats.binom.pmf(k, num_employees, promotion_rate) for k in x]
        fig = go.Figure(go.Bar(x=x, y=y))
        fig.update_layout(title="Probability Distribution of Promotions",
                          xaxis_title="Number of Promotions",
                          yaxis_title="Probability")
        st.plotly_chart(fig)

with col2:
    st.info("**Continuous random variable:** It can take uncountable number of values in a given range.\n\nFor example: Speed of an aircraft.")
    
    # Interactive example for continuous random variable
    st.subheader("Interactive Example: Aircraft Speed")
    mean_speed = st.slider("Average speed (km/h)", 500, 1000, 800)
    std_dev = st.slider("Standard deviation of speed", 10, 100, 50)
    
    if st.button("Simulate Aircraft Speeds"):
        speeds = np.random.normal(mean_speed, std_dev, 1000)
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=speeds, nbinsx=30, name="Simulated Speeds"))
        fig.add_trace(go.Scatter(x=np.linspace(mean_speed-3*std_dev, mean_speed+3*std_dev, 100),
                                 y=stats.norm.pdf(np.linspace(mean_speed-3*std_dev, mean_speed+3*std_dev, 100), mean_speed, std_dev) * len(speeds) * (speeds.max()-speeds.min())/30,
                                 mode="lines", name="Theoretical Distribution"))
        fig.update_layout(title="Distribution of Aircraft Speeds",
                          xaxis_title="Speed (km/h)",
                          yaxis_title="Frequency")
        st.plotly_chart(fig)

st.sidebar.title("📚 Learning Guide")
st.sidebar.info("""
1. Start by understanding the definition of a random variable.
2. Explore the difference between discrete and continuous random variables.
3. Experiment with the interactive examples to see how different parameters affect the distributions.
4. Observe how the probability distributions change for different scenarios.
5. Try to identify real-world situations where you might encounter discrete or continuous random variables.
""")
st.sidebar.success("Happy learning! 🚀")
