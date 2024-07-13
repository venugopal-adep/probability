import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

# Set page config
st.set_page_config(layout="wide", page_title="Common Probability Distributions Explorer", page_icon="📊")

# Custom CSS
st.markdown("""
<style>
    body {font-family: Arial, sans-serif;}
    .main {padding: 1rem;}
    .stApp {background-color: #f0f4f8;}
    .st-emotion-cache-10trblm {text-align: center;}
    .info-box {background-color: #e1e5eb; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .example-box {background-color: #d4edda; padding: 15px; border-radius: 10px; margin-top: 10px; border-left: 5px solid #28a745;}
    .quiz-container {background-color: #d0e1f9; padding: 20px; border-radius: 10px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .stTabs {background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .plot-container {display: flex; justify-content: space-between; align-items: flex-start;}
    .sliders {width: 30%; padding-right: 20px;}
    .plot {width: 70%;}
    .stButton>button {background-color: #4e8cff; color: white; border-radius: 5px; border: none; padding: 10px 20px; font-size: 16px;}
    .stButton>button:hover {background-color: #3a7be0;}
    h1, h2, h3 {color: #2c3e50;}
    .stSlider {margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("📊 Common Probability Distributions Explorer")
st.write("**Developed by: Venugopal Adep**")
st.markdown("Explore common probability distributions and their real-world applications.")

# Create tabs for each distribution
tab1, tab2, tab3, tab4 = st.tabs(["Bernoulli", "Binomial", "Uniform", "Normal"])

with tab1:
    st.header("Bernoulli Distribution")
    st.markdown("""
    The Bernoulli distribution models a single trial with two possible outcomes: success or failure.
    
    **Example: The outcome of tossing a fair coin**
    """)
    
    p = st.slider("Probability of Success (p)", 0.0, 1.0, 0.5, 0.01, key="bernoulli_p")
    
    x = [0, 1]
    y = [1-p, p]
    
    fig = go.Figure(data=[go.Bar(x=x, y=y, text=[f'{y[0]:.2f}', f'{y[1]:.2f}'], textposition='auto')])
    fig.update_layout(title="Bernoulli Distribution", xaxis_title="Outcome (0: Failure, 1: Success)", yaxis_title="Probability")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="example-box">
    In this coin toss example:
    - 0 represents "Tails" (failure)
    - 1 represents "Heads" (success)
    - The probability of getting heads (p) is typically 0.5 for a fair coin
    
    Adjust the slider to see how changing the probability affects the distribution!
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.header("Binomial Distribution")
    st.markdown("""
    The Binomial distribution models the number of successes in a fixed number of independent Bernoulli trials.
    
    **Example: The number of non-defective products in a production run**
    """)
    
    n = st.slider("Number of Trials (n)", 1, 100, 20, 1, key="binomial_n")
    p = st.slider("Probability of Success (p)", 0.0, 1.0, 0.8, 0.01, key="binomial_p")
    
    x = np.arange(0, n+1)
    y = stats.binom.pmf(x, n, p)
    
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=f"Binomial Distribution (n={n}, p={p})", 
                      xaxis_title="Number of Successes", yaxis_title="Probability")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="example-box">
    In this production run example:
    - n represents the total number of products manufactured
    - p represents the probability of a product being non-defective
    - The graph shows the probability of getting different numbers of non-defective products
    
    Try adjusting n and p to see how they affect the shape of the distribution!
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("Uniform Distribution")
    st.markdown("""
    The Uniform distribution models a situation where all outcomes in a range are equally likely.
    
    **Example: The number of books sold weekly at a bookstore**
    """)
    
    a = st.slider("Minimum Value (a)", 0, 50, 10, 1, key="uniform_a")
    b = st.slider("Maximum Value (b)", a+1, 100, 50, 1, key="uniform_b")
    
    x = np.linspace(a-5, b+5, 1000)
    y = np.where((x >= a) & (x <= b), 1/(b-a), 0)
    
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', fill='tozeroy')])
    fig.update_layout(title=f"Uniform Distribution [a={a}, b={b}]", 
                      xaxis_title="Number of Books Sold", yaxis_title="Probability Density")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="example-box">
    In this bookstore example:
    - a represents the minimum number of books sold in a week
    - b represents the maximum number of books sold in a week
    - All values between a and b are equally likely
    
    Adjust a and b to see how the range affects the distribution!
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.header("Normal Distribution")
    st.markdown("""
    The Normal (or Gaussian) distribution is a continuous probability distribution that is symmetric about the mean.
    
    **Example: IQ distribution of all seven-year-old children in New York**
    """)
    
    mu = st.slider("Mean (μ)", 70, 130, 100, 1, key="normal_mu")
    sigma = st.slider("Standard Deviation (σ)", 1, 30, 15, 1, key="normal_sigma")
    
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = stats.norm.pdf(x, mu, sigma)
    
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', fill='tozeroy')])
    fig.update_layout(title=f"Normal Distribution (μ={mu}, σ={sigma})", 
                      xaxis_title="IQ Score", yaxis_title="Probability Density")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="example-box">
    In this IQ distribution example:
    - μ (mu) represents the average IQ score
    - σ (sigma) represents the standard deviation of IQ scores
    - The bell-shaped curve shows the relative likelihood of different IQ scores
    
    Try adjusting μ and σ to see how they affect the shape and position of the distribution!
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #777;">
© 2024 Common Probability Distributions Explorer | Developed by Your Name<br>
This interactive tool is for educational purposes only and does not represent any specific research study.
</div>
""", unsafe_allow_html=True)
