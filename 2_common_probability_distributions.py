import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats
import random
from math import comb

st.set_page_config(layout="wide", page_title="Probability Distributions Explorer")

st.title("🎲 Exploring Common Probability Distributions")
st.write("**Developed by : Venugopal Adep**")

st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .main > div {
        padding: 2rem;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.write("""
This interactive demo will help you understand four common probability distributions:
Bernoulli, Binomial, Uniform, and Normal. Each distribution has unique characteristics,
real-world applications, and mathematical formulas.
""")

def bernoulli_demo():
    st.header("📊 Bernoulli Distribution")
    st.write("""
    The Bernoulli distribution models events with only two possible outcomes, 
    often referred to as "success" or "failure".
    
    Example: A company introduces a new drug to cure a disease. It either cures
    the disease (success) or it doesn't (failure).
    """)
    
    st.latex(r"P(X=x) = p^x(1-p)^{1-x}, \text{ where } x \in \{0,1\}")
    
    st.subheader("Numerical Example")
    st.write("""
    If the probability of the drug being successful is 0.7:
    P(Success) = 0.7
    P(Failure) = 1 - 0.7 = 0.3
    """)
    
    p = st.slider("Probability of success", 0.0, 1.0, 0.7, 0.01)
    
    x = [0, 1]
    y = [1-p, p]
    
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title="Bernoulli Distribution", xaxis_title="Outcome (0=Failure, 1=Success)",
                      yaxis_title="Probability")
    st.plotly_chart(fig)
    
    st.subheader("Quiz")
    q_p = random.randint(1, 9) / 10
    st.write(f"If the probability of success in a Bernoulli trial is {q_p}, what is the probability of failure?")
    user_answer = st.number_input("Your answer:", min_value=0.0, max_value=1.0, step=0.1)
    if st.button("Check Answer", key="bernoulli"):
        correct_answer = 1 - q_p
        if abs(user_answer - correct_answer) < 0.01:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is {correct_answer:.1f}")
        
        st.write("Explanation:")
        st.write(f"""
        In a Bernoulli distribution, there are only two outcomes: success and failure.
        The probabilities of these outcomes must sum to 1.
        
        Given:
        P(Success) = {q_p}
        
        Calculation:
        P(Failure) = 1 - P(Success)
                   = 1 - {q_p}
                   = {correct_answer:.1f}
        
        Therefore, the probability of failure is {correct_answer:.1f}.
        """)

def binomial_demo():
    st.header("📈 Binomial Distribution")
    st.write("""
    The Binomial distribution models the number of successes in a fixed number of 
    independent Bernoulli trials.
    
    Example: The number of defective products in a production run.
    """)
    
    st.latex(r"P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}")
    
    st.subheader("Numerical Example")
    st.write("""
    In a production run of 20 items, if each item has a 10% chance of being defective:
    n = 20, p = 0.1
    P(X=2) = C(20,2) * 0.1^2 * 0.9^18 ≈ 0.285
    """)
    
    n = st.slider("Number of trials", 1, 100, 20)
    p = st.slider("Probability of success on each trial", 0.0, 1.0, 0.1, 0.01)
    
    x = np.arange(0, n+1)
    y = stats.binom.pmf(x, n, p)
    
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title="Binomial Distribution", xaxis_title="Number of Successes",
                      yaxis_title="Probability")
    st.plotly_chart(fig)
    
    st.subheader("Quiz")
    q_n = random.randint(10, 30)
    q_p = random.randint(1, 5) / 10
    q_k = random.randint(0, q_n)
    st.write(f"In a binomial distribution with n={q_n} and p={q_p}, what is the probability of exactly {q_k} successes?")
    user_answer = st.number_input("Your answer (rounded to 3 decimal places):", min_value=0.0, max_value=1.0, step=0.001)
    if st.button("Check Answer", key="binomial"):
        correct_answer = stats.binom.pmf(q_k, q_n, q_p)
        if abs(user_answer - correct_answer) < 0.001:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is {correct_answer:.3f}")
        
        st.write("Explanation:")
        st.write(f"""
        We use the binomial probability mass function:
        P(X=k) = C(n,k) * p^k * (1-p)^(n-k)
        
        Given:
        n = {q_n} (number of trials)
        p = {q_p} (probability of success on each trial)
        k = {q_k} (number of successes we're interested in)
        
        Calculation:
        P(X={q_k}) = C({q_n},{q_k}) * {q_p}^{q_k} * (1-{q_p})^({q_n}-{q_k})
                   = {comb(q_n, q_k)} * {q_p**q_k:.6f} * {(1-q_p)**(q_n-q_k):.6f}
                   = {correct_answer:.6f}
        
        Therefore, the probability of exactly {q_k} successes is {correct_answer:.3f}.
        """)

def uniform_demo():
    st.header("📏 Uniform Distribution")
    st.write("""
    The Uniform distribution models scenarios where any outcome within a range 
    is equally likely.
    
    Example: The number of microwave ovens sold daily at an electronic store, 
    assuming sales are consistent and fall within a specific range.
    """)
    
    st.latex(r"f(x) = \begin{cases}\frac{1}{b-a} & \text{for } a \leq x \leq b \\ 0 & \text{otherwise}\end{cases}")
    
    st.subheader("Numerical Example")
    st.write("""
    If microwave oven sales are uniformly distributed between 5 and 15 per day:
    P(X ≤ 10) = (10 - 5) / (15 - 5) = 0.5
    """)
    
    a = st.number_input("Minimum value", value=5)
    b = st.number_input("Maximum value", value=15)
    
    x = np.linspace(a-1, b+1, 1000)
    y = stats.uniform.pdf(x, a, b-a)
    
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
    fig.update_layout(title="Uniform Distribution", xaxis_title="Value",
                      yaxis_title="Probability Density")
    st.plotly_chart(fig)
    
    st.subheader("Quiz")
    q_a = random.randint(0, 5)
    q_b = q_a + random.randint(5, 10)
    q_x = random.randint(q_a, q_b)
    st.write(f"For a uniform distribution between {q_a} and {q_b}, what is the probability that X ≤ {q_x}?")
    user_answer = st.number_input("Your answer (rounded to 2 decimal places):", min_value=0.0, max_value=1.0, step=0.01)
    if st.button("Check Answer", key="uniform"):
        correct_answer = (q_x - q_a) / (q_b - q_a)
        if abs(user_answer - correct_answer) < 0.01:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is {correct_answer:.2f}")
        
        st.write("Explanation:")
        st.write(f"""
        For a uniform distribution, the probability is proportional to the length of the interval.
        
        Given:
        a = {q_a} (minimum value)
        b = {q_b} (maximum value)
        x = {q_x} (value we're interested in)
        
        Calculation:
        P(X ≤ {q_x}) = (x - a) / (b - a)
                     = ({q_x} - {q_a}) / ({q_b} - {q_a})
                     = {q_x - q_a} / {q_b - q_a}
                     = {correct_answer:.2f}
        
        Therefore, the probability that X ≤ {q_x} is {correct_answer:.2f}.
        """)

def normal_demo():
    st.header("🔔 Normal Distribution")
    st.write("""
    The Normal distribution is a symmetric, bell-shaped curve that's ubiquitous in nature and statistics.
    
    Example: Income distribution in a country where the middle-class population 
    is slightly larger than the rich and poor populations.
    """)
    
    st.latex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}")
    
    st.subheader("Numerical Example")
    st.write("""
    If the mean income is $50,000 with a standard deviation of $10,000:
    P(40000 ≤ X ≤ 60000) ≈ 0.68 (68% of the population falls within one standard deviation of the mean)
    """)
    
    mu = st.slider("Mean", -10.0, 10.0, 0.0, 0.1)
    sigma = st.slider("Standard deviation", 0.1, 10.0, 1.0, 0.1)
    
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = stats.norm.pdf(x, mu, sigma)
    
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
    fig.update_layout(title="Normal Distribution", xaxis_title="Value",
                      yaxis_title="Probability Density")
    st.plotly_chart(fig)
    
    st.subheader("Quiz")
    q_mu = random.randint(40, 60) * 1000
    q_sigma = random.randint(5, 15) * 1000
    q_x = q_mu + random.choice([-1, 1]) * q_sigma
    st.write(f"For a normal distribution with mean ${q_mu} and standard deviation ${q_sigma}, what is the z-score for ${q_x}?")
    user_answer = st.number_input("Your answer (rounded to 2 decimal places):", min_value=-5.0, max_value=5.0, step=0.01)
    if st.button("Check Answer", key="normal"):
        correct_answer = (q_x - q_mu) / q_sigma
        if abs(user_answer - correct_answer) < 0.01:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is {correct_answer:.2f}")
        
        st.write("Explanation:")
        st.write(f"""
        The z-score represents the number of standard deviations a value is from the mean.
        
        Formula: z = (x - μ) / σ
        
        Given:
        μ (mean) = ${q_mu}
        σ (standard deviation) = ${q_sigma}
        x (value) = ${q_x}
        
        Calculation:
        z = (x - μ) / σ
          = (${q_x} - ${q_mu}) / ${q_sigma}
          = {q_x - q_mu} / {q_sigma}
          = {correct_answer:.2f}
        
        Therefore, the z-score for ${q_x} is {correct_answer:.2f}.
        """)

distribution = st.sidebar.selectbox(
    "Choose a distribution to explore",
    ("Bernoulli", "Binomial", "Uniform", "Normal")
)

col1, col2 = st.columns([3, 1])

with col1:
    if distribution == "Bernoulli":
        bernoulli_demo()
    elif distribution == "Binomial":
        binomial_demo()
    elif distribution == "Uniform":
        uniform_demo()
    else:
        normal_demo()

with col2:
    st.sidebar.markdown("""
    ### 📚 About This Demo

    This interactive application helps you visualize and understand four common 
    probability distributions. Use the sidebar to select a distribution, then 
    adjust the parameters using the sliders to see how the distribution changes.

    Each distribution is explained with:
    - 🌍 Real-world example
    - 📐 Mathematical formula
    - 🧮 Numerical example
    - 🧠 Quiz question

    Detailed explanations are provided for each quiz answer to enhance your understanding.
    """)

    st.sidebar.markdown("""
    ### 🔍 Key Features:
    - Interactive visualizations
    - Real-time parameter adjustments
    - Practical examples
    - Self-assessment quizzes
    """)

    st.sidebar.markdown("""
    ### 🎓 Learn More:
    For a deeper dive into probability theory and statistics, check out these resources:
    - [Khan Academy: Probability](https://www.khanacademy.org/math/statistics-probability/probability-library)
    - [StatQuest YouTube Channel](https://www.youtube.com/user/joshstarmer)
    - [OpenIntro Statistics](https://www.openintro.org/book/os/)
    """)

st.markdown("""
---
Created with ❤️ using Streamlit | [Source Code](https://github.com/yourusername/prob-distributions-demo)
""")
