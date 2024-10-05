import streamlit as st
import plotly.graph_objs as go
import numpy as np
from scipy import stats

st.set_page_config(layout="wide", page_title="Understanding Random Variables")

# Custom CSS (unchanged)
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

# Visualization of Random Variable types
st.subheader("Types of Random Variables")
col1, col2 = st.columns(2)

with col1:
    st.info("**Discrete random variable:** It can take only a finite number of values (countable, finite, specific value).\n\nFor example: Number of employees getting promoted in an organization.")
    
    # Interactive example for discrete random variable
    st.subheader("Interactive Example: Employee Promotions")
    num_employees = st.slider("Total number of employees", 10, 100, 50)
    promotion_rate = st.slider("Promotion rate (%)", 0, 100, 10) / 100
    
    if st.button("Simulate Promotions"):
        promotions = np.random.binomial(num_employees, promotion_rate)
        st.success(f"Number of employees promoted in this simulation: {promotions}")
        
        # Calculations
        expected_promotions = num_employees * promotion_rate
        variance = num_employees * promotion_rate * (1 - promotion_rate)
        std_dev = np.sqrt(variance)
        
        st.write(f"Expected number of promotions: {expected_promotions:.2f}")
        st.write(f"Variance: {variance:.2f}")
        st.write(f"Standard Deviation: {std_dev:.2f}")
        
        # Plot probability distribution
        x = list(range(num_employees + 1))
        y = [stats.binom.pmf(k, num_employees, promotion_rate) for k in x]
        fig = go.Figure(go.Bar(x=x, y=y))
        fig.update_layout(title="Probability Distribution of Promotions",
                          xaxis_title="Number of Promotions",
                          yaxis_title="Probability")
        st.plotly_chart(fig)
        
        st.write("""
        **Explanation:**
        - The binomial distribution models the number of successes in a fixed number of independent trials.
        - In this case, each employee has an independent chance of being promoted.
        - The shape of the distribution depends on the number of employees and the promotion rate.
        - A higher promotion rate will shift the peak to the right, while a lower rate will shift it to the left.
        - The width of the distribution (spread) increases with the number of employees.
        """)

with col2:
    st.info("**Continuous random variable:** It can take uncountable number of values in a given range (uncountable, infinite, range).\n\nFor example: Speed of an aircraft.")
    
    # Interactive example for continuous random variable
    st.subheader("Interactive Example: Aircraft Speed")
    mean_speed = st.slider("Average speed (km/h)", 500, 1000, 800)
    std_dev = st.slider("Standard deviation of speed", 10, 100, 50)
    
    if st.button("Simulate Aircraft Speeds"):
        speeds = np.random.normal(mean_speed, std_dev, 1000)
        
        st.success(f"Simulated average speed: {np.mean(speeds):.2f} km/h")
        
        # Calculations
        variance = std_dev ** 2
        
        st.write(f"Population mean (μ): {mean_speed} km/h")
        st.write(f"Population standard deviation (σ): {std_dev} km/h")
        st.write(f"Population variance (σ²): {variance} (km/h)²")
        
        # Probability calculations
        prob_below_mean = stats.norm.cdf(mean_speed, mean_speed, std_dev)
        prob_above_mean_plus_sigma = 1 - stats.norm.cdf(mean_speed + std_dev, mean_speed, std_dev)
        
        st.write(f"Probability of speed below mean: {prob_below_mean:.2%}")
        st.write(f"Probability of speed above mean + 1σ: {prob_above_mean_plus_sigma:.2%}")
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=speeds, nbinsx=30, name="Simulated Speeds"))
        x_range = np.linspace(mean_speed - 3*std_dev, mean_speed + 3*std_dev, 100)
        fig.add_trace(go.Scatter(x=x_range,
                                 y=stats.norm.pdf(x_range, mean_speed, std_dev) * len(speeds) * (speeds.max()-speeds.min())/30,
                                 mode="lines", name="Theoretical Distribution"))
        fig.update_layout(title="Distribution of Aircraft Speeds",
                          xaxis_title="Speed (km/h)",
                          yaxis_title="Frequency")
        st.plotly_chart(fig)
        
        st.write("""
        **Explanation:**
        - The normal distribution is often used to model continuous variables like speed.
        - It's symmetric around the mean, with about 68% of values within one standard deviation of the mean.
        - The mean determines the center of the distribution, while the standard deviation affects its spread.
        - A larger standard deviation results in a wider, flatter distribution.
        - The probability of a speed falling in any specific range can be calculated using the cumulative distribution function (CDF).
        """)

st.sidebar.title("📚 Learning Guide")
st.sidebar.info("""
1. Understand the definition of a random variable and its types.
2. Explore how parameters affect the shape and properties of distributions.
3. Compare discrete (binomial) and continuous (normal) distributions.
4. Interpret probabilities and statistics for each distribution type.
5. Experiment with different parameter values to see how they change the distributions.
6. Consider real-world applications of these concepts in various fields.
""")
st.sidebar.success("Happy learning! 🚀")
