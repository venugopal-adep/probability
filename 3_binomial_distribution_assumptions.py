import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import binom

# Set page configuration
st.set_page_config(page_title="Binomial Distribution Demo", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
        background-color: #f0f2f6;
    }
    .stTitle, .stHeader {
        color: #0e1117;
    }
    .stSubheader {
        color: #31333F;
    }
    .stRadio > label {
        color: #31333F;
        font-weight: bold;
    }
    .stButton > button {
        color: #ffffff;
        background-color: #FF4B4B;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #FF2B2B;
    }
</style>
""", unsafe_allow_html=True)

def binomial_pmf(n, p, k):
    return binom.pmf(k, n, p)

def binomial_cdf(n, p, k):
    return binom.cdf(k, n, p)

st.title("📊 Binomial Distribution Interactive Demo")

with st.expander("ℹ️ What is a Binomial Distribution?"):
    st.write("""
    The binomial distribution models the number of successes in a fixed number of independent trials, 
    each with the same probability of success. It's widely used in statistics and probability theory.
    """)

with st.expander("🔑 Key Assumptions"):
    st.write("""
    1. **Fixed number of trials (n):** The number of trials is determined beforehand and doesn't change.
    2. **Independence:** Each trial is independent of the others.
    3. **Binary outcomes:** There are only two possible outcomes for each trial (usually called "success" and "failure").
    4. **Constant probability:** The probability of success (p) remains the same for each trial.
    """)

st.header("🎛️ Interactive Binomial Distribution Plot")

col1, col2 = st.columns(2)
with col1:
    n = st.slider("Number of trials (n)", 1, 100, 20)
with col2:
    p = st.slider("Probability of success (p)", 0.0, 1.0, 0.5, 0.01)

x = np.arange(0, n+1)
pmf = [binomial_pmf(n, p, k) for k in x]

fig = go.Figure()
fig.add_trace(go.Bar(x=x, y=pmf, name="Probability Mass Function", marker_color='#FF4B4B'))
fig.update_layout(
    title=f"Binomial Distribution (n={n}, p={p:.2f})",
    xaxis_title="Number of Successes",
    yaxis_title="Probability",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)
st.plotly_chart(fig, use_container_width=True)

st.info("""
This interactive plot shows the probability mass function (PMF) of the binomial distribution. 
Each bar represents the probability of getting exactly that number of successes in n trials.
""")

st.header("💡 Examples")

with st.expander("Example 1: Coin Flipping"):
    st.write("""
    Suppose you flip a fair coin 10 times. What's the probability of getting exactly 6 heads?

    We can use the binomial distribution with:
    - n = 10 (number of flips)
    - p = 0.5 (probability of heads on a single flip)
    - k = 6 (number of successes we're interested in)
    """)

    prob_6_heads = binomial_pmf(10, 0.5, 6)
    st.success(f"The probability of getting exactly 6 heads in 10 flips is: {prob_6_heads:.4f}")

with st.expander("Example 2: Quality Control"):
    st.write("""
    A manufacturer knows that 5% of the products they produce are defective. 
    In a batch of 100 items, what's the probability that 3 or fewer items are defective?

    We can use the cumulative distribution function (CDF) of the binomial distribution:
    - n = 100 (batch size)
    - p = 0.05 (probability of a defective item)
    - k = 3 (we want 3 or fewer defectives)
    """)

    prob_3_or_fewer = binomial_cdf(100, 0.05, 3)
    st.success(f"The probability of 3 or fewer defective items in a batch of 100 is: {prob_3_or_fewer:.4f}")

st.header("🧠 Quiz")
st.subheader("Question")
st.write("""
A basketball player has a 70% free throw success rate. 
If they attempt 5 free throws, what is the probability of making exactly 4 shots?
""")

answer = st.radio("Select your answer:", ["A) 0.1323", "B) 0.3087", "C) 0.2352", "D) 0.4202"])

if st.button("Check Answer"):
    correct_answer = "B) 0.3087"
    if answer == correct_answer:
        st.success("Correct! Great job! 🎉")
    else:
        st.error("Sorry, that's not correct. Try again! 🔄")
    
    with st.expander("See explanation"):
        st.write("""
        The correct answer is B) 0.3087.

        We can calculate this using the binomial probability mass function:
        - n = 5 (number of free throws)
        - p = 0.7 (probability of success for each throw)
        - k = 4 (number of successful shots we're interested in)

        P(X = 4) = C(5,4) * (0.7)^4 * (0.3)^1
                 = 5 * (0.7)^4 * (0.3)
                 ≈ 0.3087

        Where C(5,4) is the number of ways to choose 4 items from 5, which is 5.

        This problem demonstrates how the binomial distribution can be applied to real-world scenarios 
        involving a fixed number of independent trials with constant probability.
        """)

st.header("📐 Formula")
st.latex(r"""
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
""")
st.write("""
Where:
- n is the number of trials
- k is the number of successes
- p is the probability of success on each trial
- \\binom{n}{k} is the binomial coefficient, calculated as n! / (k! * (n-k)!)
""")

st.header("🎓 Conclusion")
st.info("""
The binomial distribution is a powerful tool for modeling scenarios with a fixed number of 
independent trials, each with a constant probability of success. Understanding its assumptions 
and applications can greatly enhance your ability to analyze and predict outcomes in various 
fields, from statistics and probability theory to real-world applications in quality control, 
sports analytics, and more.
""")