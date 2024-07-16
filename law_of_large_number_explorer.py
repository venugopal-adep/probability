import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(layout="wide", page_title="Law of Large Numbers Explorer", page_icon="📊")

# Custom CSS (unchanged, omitted for brevity)
st.markdown("""
<style>
    # ... (keep the existing CSS)
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📊 Law of Large Numbers Explorer 📊</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the Law of Large Numbers Explorer!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's explore how sample means converge to the expected value as sample size increases.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What is the Law of Large Numbers?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
The Law of Large Numbers (LLN) is a fundamental principle in probability theory. It states that as the number of trials (sample size) increases, the sample mean tends to converge to the expected value (theoretical mean) of the distribution.

Key points:
- As sample size grows, sample statistics become more stable
- Helps explain why casinos always win in the long run
- Forms the basis for many statistical inference techniques
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["📊 Coin Toss", "🎲 Dice Roll", "📈 Normal Distribution", "🧠 Quiz"])

def plot_convergence(data, expected_value, title):
    cumulative_means = np.cumsum(data) / np.arange(1, len(data) + 1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=cumulative_means, mode='lines', name='Sample Mean'))
    fig.add_hline(y=expected_value, line_dash="dash", line_color="red", annotation_text="Expected Value")
    
    fig.update_layout(
        title=title,
        xaxis_title="Number of Trials",
        yaxis_title="Sample Mean",
        showlegend=True
    )
    return fig

with tab1:
    st.markdown("<p class='medium-font'>Coin Toss Experiment</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's simulate coin tosses and see how the proportion of heads converges to 0.5 as the number of tosses increases.
        </p>
        """, unsafe_allow_html=True)
        
        num_tosses = st.slider("Number of coin tosses", 100, 10000, 1000, 100)
        
        if st.button("Run Coin Toss Simulation"):
            tosses = np.random.choice([0, 1], size=num_tosses)  # 0 for tails, 1 for heads
            expected_value = 0.5
            
            st.markdown(f"""
            <p class='small-font'>
            Number of tosses: {num_tosses}<br>
            Final proportion of heads: {np.mean(tosses):.4f}
            </p>
            """, unsafe_allow_html=True)

    with col2:
        if 'tosses' in locals():
            fig = plot_convergence(tosses, expected_value, "Convergence of Coin Toss Proportion")
            st.plotly_chart(fig)

with tab2:
    st.markdown("<p class='medium-font'>Dice Roll Experiment</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's simulate rolling a fair six-sided die and observe how the average roll converges to 3.5 as the number of rolls increases.
        </p>
        """, unsafe_allow_html=True)
        
        num_rolls = st.slider("Number of dice rolls", 100, 10000, 1000, 100)
        
        if st.button("Run Dice Roll Simulation"):
            rolls = np.random.randint(1, 7, size=num_rolls)
            expected_value = 3.5
            
            st.markdown(f"""
            <p class='small-font'>
            Number of rolls: {num_rolls}<br>
            Final average roll: {np.mean(rolls):.4f}
            </p>
            """, unsafe_allow_html=True)

    with col2:
        if 'rolls' in locals():
            fig = plot_convergence(rolls, expected_value, "Convergence of Dice Roll Average")
            st.plotly_chart(fig)

with tab3:
    st.markdown("<p class='medium-font'>Normal Distribution Sampling</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's sample from a normal distribution and see how the sample mean converges to the true mean as the sample size increases.
        </p>
        """, unsafe_allow_html=True)
        
        mean = st.number_input("True mean", value=0.0)
        std_dev = st.number_input("Standard deviation", value=1.0, min_value=0.1)
        sample_size = st.slider("Sample size", 100, 10000, 1000, 100)
        
        if st.button("Run Normal Distribution Simulation"):
            samples = np.random.normal(mean, std_dev, size=sample_size)
            expected_value = mean
            
            st.markdown(f"""
            <p class='small-font'>
            Sample size: {sample_size}<br>
            True mean: {mean}<br>
            Final sample mean: {np.mean(samples):.4f}
            </p>
            """, unsafe_allow_html=True)

    with col2:
        if 'samples' in locals():
            fig = plot_convergence(samples, expected_value, "Convergence of Sample Mean (Normal Distribution)")
            st.plotly_chart(fig)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "What does the Law of Large Numbers state?",
            "options": [
                "The sample size always equals the population size",
                "Larger samples are always more biased",
                "As sample size increases, the sample mean approaches the expected value",
                "The sample variance is always zero"
            ],
            "correct": 2,
            "explanation": "The Law of Large Numbers states that as the sample size increases, the sample mean tends to converge to the expected value (theoretical mean) of the distribution."
        },
        {
            "question": "In the context of coin tosses, what value does the proportion of heads converge to according to the Law of Large Numbers?",
            "options": ["0.25", "0.5", "0.75", "1"],
            "correct": 1,
            "explanation": "For a fair coin, the expected proportion of heads is 0.5. The Law of Large Numbers tells us that as we increase the number of tosses, the observed proportion will converge to this expected value."
        },
        {
            "question": "Why is the Law of Large Numbers important in statistics and probability?",
            "options": [
                "It guarantees exact results for small samples",
                "It eliminates the need for hypothesis testing",
                "It forms the basis for many statistical inference techniques",
                "It proves that all random variables are normally distributed"
            ],
            "correct": 2,
            "explanation": "The Law of Large Numbers is crucial because it forms the foundation for many statistical inference techniques. It helps explain why larger samples tend to provide more reliable estimates of population parameters."
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"<p class='small-font'><strong>Question {i+1}:</strong> {q['question']}</p>", unsafe_allow_html=True)
        user_answer = st.radio("Select your answer:", q['options'], key=f"q{i}")
        
        if st.button("Check Answer", key=f"check{i}"):
            if q['options'].index(user_answer) == q['correct']:
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error("Incorrect. Try again! 🤔")
            st.info(q['explanation'])
        st.markdown("---")

    if st.button("Show Final Score"):
        st.markdown(f"<p class='big-font'>Your score: {score}/{len(questions)}</p>", unsafe_allow_html=True)
        if score == len(questions):
            st.balloons()

# Conclusion
st.markdown("<p class='big-font'>Congratulations! 🎊</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>You've explored the Law of Large Numbers through interactive simulations and examples. This fundamental principle is crucial in understanding sampling behavior and forms the basis for many statistical techniques. Keep exploring and applying this concept in various scenarios!</p>", unsafe_allow_html=True)