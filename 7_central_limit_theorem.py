import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

# Page configuration
st.set_page_config(layout="wide", page_title="Central Limit Theorem Demo", page_icon="🔔")

# Custom CSS
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #fff;
        border-radius: 5px;
        color: #4F8BF9;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4F8BF9;
        color: white;
    }
    .stMarkdown {
        text-align: justify;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🔔 Central Limit Theorem Demonstration")
st.markdown("""
This interactive demo explores the Central Limit Theorem and its assumptions. 
It shows how the sampling distribution of the sample means approaches a normal distribution 
as the sample size increases, regardless of the shape of the population distribution.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📚 Concept", "🔍 Interactive Demo", "🧠 Quiz"])

with tab1:
    st.header("Central Limit Theorem")
    
    st.info("""
    The sampling distribution of the sample means will approach normal distribution as the sample size gets bigger, 
    no matter what the shape of the population distribution is.
    """)
    
    st.subheader("Assumptions")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- Data must be **randomly sampled**")
        st.markdown("- Samples should come from the **same distribution**")
    with col2:
        st.markdown("- Sample values must be **independent** of each other")
        st.markdown("- Sample size must be **sufficiently large** (≥30)")
    
    st.markdown("""
    ### Why is the Central Limit Theorem important?
    1. It allows us to use normal distribution-based statistical methods even when the population is not normally distributed.
    2. It forms the foundation for many inferential statistical techniques.
    3. It helps in constructing confidence intervals and performing hypothesis tests for large samples.
    """)

with tab2:
    st.header("Interactive CLT Demonstration")
    
    # Function to generate population based on selected distribution
    def generate_population(dist_type, size=100000):
        if dist_type == "Normal":
            return np.random.normal(loc=0, scale=1, size=size)
        elif dist_type == "Uniform":
            return np.random.uniform(low=-3, high=3, size=size)
        elif dist_type == "Exponential":
            return np.random.exponential(scale=1, size=size)
        elif dist_type == "Bimodal":
            return np.concatenate([np.random.normal(-1, 0.4, size=size//2), np.random.normal(1, 0.4, size=size//2)])
    
    # Function to take samples and calculate means
    def sample_means(population, sample_size, num_samples):
        return [np.mean(np.random.choice(population, size=sample_size, replace=True)) for _ in range(num_samples)]
    
    # User inputs
    dist_type = st.selectbox("Select population distribution:", ["Normal", "Uniform", "Exponential", "Bimodal"])
    sample_size = st.slider("Select sample size:", min_value=2, max_value=500, value=30, step=1)
    num_samples = st.slider("Number of samples to draw:", min_value=100, max_value=10000, value=1000, step=100)
    
    # Generate population and sample means
    population = generate_population(dist_type)
    means = sample_means(population, sample_size, num_samples)
    
    # Create subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Population Distribution", "Sampling Distribution of Means"))
    
    # Population distribution
    fig.add_trace(go.Histogram(x=population, name="Population", marker_color='lightblue'), row=1, col=1)
    
    # Sampling distribution of means
    fig.add_trace(go.Histogram(x=means, name="Sample Means", marker_color='lightgreen'), row=1, col=2)
    
    # Add normal curve to sampling distribution
    x = np.linspace(min(means), max(means), 100)
    y = stats.norm.pdf(x, np.mean(means), np.std(means))
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Curve', line=dict(color='red')), row=1, col=2)
    
    # Update layout
    fig.update_layout(height=500, showlegend=False)
    fig.update_xaxes(title_text="Value", row=1, col=1)
    fig.update_xaxes(title_text="Sample Mean", row=1, col=2)
    fig.update_yaxes(title_text="Frequency", row=1, col=1)
    fig.update_yaxes(title_text="Frequency", row=1, col=2)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Population Mean", f"{np.mean(population):.4f}")
        st.metric("Population Std Dev", f"{np.std(population):.4f}")
    with col2:
        st.metric("Mean of Sample Means", f"{np.mean(means):.4f}")
        st.metric("Std Dev of Sample Means", f"{np.std(means):.4f}")
    with col3:
        st.metric("Expected Std Error", f"{np.std(population)/np.sqrt(sample_size):.4f}")
        st.metric("Normality Test p-value", f"{stats.normaltest(means)[1]:.4f}")
    
    st.info("""
    **Observations:**
    1. The population distribution can have various shapes based on your selection.
    2. As the sample size increases, the sampling distribution of means becomes more normal.
    3. The mean of sample means closely approximates the population mean.
    4. The standard deviation of sample means (standard error) decreases with larger sample sizes.
    5. The normality test p-value typically increases with larger sample sizes, indicating closer approximation to normal distribution.
    """)

with tab3:
    st.header("Test Your Knowledge")
    
    questions = [
        {
            "question": "What does the Central Limit Theorem state?",
            "options": [
                "All populations are normally distributed",
                "The sampling distribution of the sample means approaches a normal distribution as sample size increases",
                "Larger samples are always better than smaller samples",
                "The population mean is always equal to the sample mean"
            ],
            "correct": "The sampling distribution of the sample means approaches a normal distribution as sample size increases",
            "explanation": "The Central Limit Theorem states that the sampling distribution of the sample means will approach a normal distribution as the sample size gets larger, regardless of the shape of the population distribution."
        },
        {
            "question": "What is the minimum recommended sample size for the Central Limit Theorem to apply?",
            "options": ["10", "20", "30", "50"],
            "correct": "30",
            "explanation": "Generally, a sample size of 30 or more is considered sufficient for the Central Limit Theorem to apply, although this can vary depending on the population distribution."
        },
        {
            "question": "Which of the following is NOT an assumption of the Central Limit Theorem?",
            "options": [
                "Data must be randomly sampled",
                "Sample values must be independent of each other",
                "The population must be normally distributed",
                "Samples should come from the same distribution"
            ],
            "correct": "The population must be normally distributed",
            "explanation": "The Central Limit Theorem does not require the population to be normally distributed. In fact, it works for any population distribution, given that the other assumptions are met and the sample size is sufficiently large."
        }
    ]

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        if st.button("Check Answer", key=f"check{i}"):
            if answer == q["correct"]:
                st.success("Correct! " + q["explanation"])
            else:
                st.error("Incorrect. " + q["explanation"])

st.markdown("""
---
### Key Takeaways:
1. The Central Limit Theorem states that the sampling distribution of the sample means approaches a normal distribution as the sample size increases, regardless of the population distribution.
2. This theorem holds true under certain assumptions: random sampling, independent samples, samples from the same distribution, and sufficiently large sample size.
3. The CLT is crucial for statistical inference, allowing us to use normal distribution-based methods even when the population is not normally distributed.
4. As sample size increases, the sampling distribution becomes more normal, and the standard error decreases.
5. Understanding the CLT is essential for constructing confidence intervals and performing hypothesis tests in many real-world scenarios.
""")