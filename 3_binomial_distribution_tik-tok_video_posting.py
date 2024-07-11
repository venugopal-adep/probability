import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import binom
import random

# Set page configuration
st.set_page_config(
    page_title="TikTok Video Posting: Binomial Distribution Explorer",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for improved visual appeal
st.markdown("""
<style>
    body {
        color: #333;
        background-color: #f0f8ff;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTitle {
        color: #1e90ff;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stSubheader {
        color: #4169e1;
        font-size: 1.8rem;
        border-bottom: 2px solid #4169e1;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .stButton>button {
        background-color: #1e90ff;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #4169e1;
        transform: translateY(-2px);
    }
    .stSlider>div>div>div>div {
        background-color: #1e90ff;
    }
    .highlight {
        background-color: #e6f3ff;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions
def binomial_pmf(n, p, k):
    return binom.pmf(k, n, p)

def create_binomial_plot(n, p):
    k = np.arange(0, n+1)
    pmf = [binomial_pmf(n, p, ki) for ki in k]
    
    fig = go.Figure(data=[go.Bar(
        x=k, 
        y=pmf, 
        text=[f'{prob:.3f}' for prob in pmf],
        textposition='auto',
        marker_color='#1e90ff',
        opacity=0.8
    )])
    fig.update_layout(
        title=f'Binomial Distribution (n={n}, p={p:.2f})',
        xaxis_title='Number of TikTok Video Posters (k)',
        yaxis_title='Probability',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# Main content
st.title('TikTok Video Posting: Binomial Distribution Explorer')
st.write('**Developed by : Venugopal Adep**')

st.write("""
Welcome to the TikTok Video Posting Explorer! 🎉 Dive into the world of probability and statistics
as we investigate how many adults in a group have posted videos on TikTok. Get ready for an
exciting journey through the Binomial Distribution! 🚀
""")

# Interactive Parameters
st.subheader('Set Your Parameters')
col1, col2 = st.columns(2)
with col1:
    n = st.slider('Number of adults surveyed (n)', 5, 100, 25)
with col2:
    p = st.slider('Probability an adult has posted a TikTok video (p)', 0.0, 1.0, 0.3, 0.01)

# Visualize the distribution
st.subheader('Visualize the Distribution')
st.plotly_chart(create_binomial_plot(n, p), use_container_width=True)

# Interactive example
st.subheader('Explore Probabilities')
k = st.slider('Number of adults who have posted a TikTok video (k)', 0, n, n//2)

probability = binomial_pmf(n, p, k)
st.write(f"Probability of exactly {k} out of {n} adults having posted a TikTok video: {probability:.4f}")

cumulative = sum([binomial_pmf(n, p, i) for i in range(k+1)])
st.write(f"Probability of {k} or fewer adults having posted a TikTok video: {cumulative:.4f}")

# Expected Value and Variance
st.subheader('Expected Value and Variance')
expected = n * p
variance = n * p * (1-p)
st.write(f"Expected number of adults who have posted a TikTok video: E(X) = np = {expected:.2f}")
st.write(f"Variance: Var(X) = np(1-p) = {variance:.2f}")

# Solved Numericals
st.subheader('Solved Numericals')
st.write("""
Let's solve some practical problems using the Binomial Distribution!
""")

# Example 1
st.markdown("""
<div class="highlight">
<strong>Example 1:</strong> In a group of 20 adults, if the probability of an adult having posted a TikTok video is 0.4, 
what's the probability that exactly 8 adults have posted a video?
</div>
""", unsafe_allow_html=True)

ex1_prob = binomial_pmf(20, 0.4, 8)
st.write(f"Solution: The probability is {ex1_prob:.4f} or about {ex1_prob*100:.2f}%")

# Example 2
st.markdown("""
<div class="highlight">
<strong>Example 2:</strong> In a survey of 50 adults, if 30% are expected to have posted a TikTok video, 
what's the probability that 20 or more adults have posted a video?
</div>
""", unsafe_allow_html=True)

ex2_prob = 1 - sum([binomial_pmf(50, 0.3, i) for i in range(20)])
st.write(f"Solution: The probability is {ex2_prob:.4f} or about {ex2_prob*100:.2f}%")

# Quiz Section
st.subheader('Test Your Knowledge')
st.write("Let's see how well you understand the Binomial Distribution with these fun quizzes!")

# Quiz Question 1
q1 = st.radio(
    "1. If you survey 10 adults and the probability of an adult having posted a TikTok video is 0.5, "
    "what's the expected number of adults who have posted a video?",
    ('3', '5', '7', '10')
)

if st.button('Check Answer for Question 1'):
    if q1 == '5':
        st.success("Correct! The expected value is n * p = 10 * 0.5 = 5.")
    else:
        st.error("That's not correct. The expected value is n * p = 10 * 0.5 = 5.")
    
    st.write("""
    Explanation: In a Binomial Distribution, the expected value (average outcome) is calculated by 
    multiplying the number of trials (n) by the probability of success (p). In this case, 
    n = 10 and p = 0.5, so the expected value is 10 * 0.5 = 5.
    
    This means that if you repeated this survey many times, on average, you'd expect 5 out of 10 
    adults to have posted a TikTok video. It's like flipping a fair coin 10 times - you'd expect 
    about 5 heads on average.
    """)

# Quiz Question 2
q2 = st.radio(
    "2. In a group of 15 adults, if the probability of an adult having posted a TikTok video is 0.2, "
    "what's more likely?",
    ('Exactly 2 adults have posted a video', 'Exactly 5 adults have posted a video', 'Exactly 8 adults have posted a video')
)

if st.button('Check Answer for Question 2'):
    probs = [binomial_pmf(15, 0.2, k) for k in [2, 5, 8]]
    correct_answer = 'Exactly 2 adults have posted a video'
    if q2 == correct_answer:
        st.success(f"Correct! {correct_answer} is the most likely outcome.")
    else:
        st.error(f"That's not correct. {correct_answer} is the most likely outcome.")
    
    st.write("""
    Explanation: Let's break it down:
    - Probability of exactly 2 successes: {:.4f}
    - Probability of exactly 5 successes: {:.4f}
    - Probability of exactly 8 successes: {:.4f}

    The expected value is np = 15 * 0.2 = 3, so outcomes closer to this are more likely. 
    That's why 2 is the most probable outcome among the given options.

    Think of it like this: If you had a bag with 80 red marbles and 20 blue marbles, and you 
    drew 15 marbles, you'd expect to get about 3 blue marbles. Getting 2 blue marbles is closer 
    to this expectation than getting 5 or 8.
    """.format(probs[0], probs[1], probs[2]))

# Quiz Question 3
q3 = st.radio(
    "3. If the probability of an adult having posted a TikTok video increases from 0.3 to 0.6, "
    "how does the shape of the Binomial Distribution change?",
    ('It becomes more spread out', 'It becomes more concentrated', 'It shifts to the right', 'Both a and c')
)

if st.button('Check Answer for Question 3'):
    if q3 == 'Both a and c':
        st.success("Correct! The distribution becomes more spread out and shifts to the right.")
    else:
        st.error("That's not correct. The distribution becomes more spread out and shifts to the right.")
    
    st.write("""
    Explanation: When the probability (p) increases:
    1. The distribution shifts to the right because the expected value (np) increases. 
       This means we expect more successes on average.
    2. The distribution becomes more spread out because the variance (np(1-p)) increases 
       when p moves from 0.3 towards 0.5.

    Imagine you're throwing darts at a target. If you become twice as likely to hit the bullseye:
    - You'd expect to hit more bullseyes overall (shift to the right)
    - There'd be more variability in your possible scores (more spread out)

    Let's visualize this change:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_binomial_plot(20, 0.3), use_container_width=True)
    with col2:
        st.plotly_chart(create_binomial_plot(20, 0.6), use_container_width=True)

st.write("""
Congratulations on completing the TikTok Video Posting Explorer! 🎉 
You've just taken a deep dive into the Binomial Distribution and its applications. 
Keep exploring and happy learning! 📚🚀
""")