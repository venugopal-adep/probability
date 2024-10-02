import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(layout="wide", page_title="Sampling Distribution Demo", page_icon="📊")

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
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("📊 Sampling Distribution")
st.write("**Developed by : Venugopal Adep**")
st.markdown("""
This interactive demo explores the concept of sampling distribution, particularly the sampling distribution of the mean.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📚 Concept", "🔍 Interactive Demo", "🧠 Quiz"])

with tab1:
    st.header("Sampling Distributions")
    
    st.subheader("What is the need for sampling?")
    
    st.write("""
    Given the limited resources and time, it is not always possible to study the population. That's why we choose a
    sample out of the population to make inferences about the population.
    """)
    
    st.write("""
    Example: Suppose a new drug is manufactured and it needs is to be tested for the adverse side effects on a
    country's population. It is almost impossible to conduct a research study that involves everyone.
    """)
    
    st.subheader("What are Sampling Distributions?")
    
    st.write("""
    It is a distribution of a particular sample statistic obtained from all possible samples drawn from a specific
    population.
    """)

with tab2:
    st.header("Interactive Sampling Distribution Demo")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # User inputs
        sample_size = st.slider("Select sample size:", min_value=10, max_value=1000, value=30, step=10)
        num_samples = st.slider("Number of samples to draw:", min_value=100, max_value=10000, value=1000, step=100)
    
    # Create a bimodal population
    np.random.seed(42)
    population_size = 100000
    population = np.concatenate([
        np.random.normal(loc=5, scale=1, size=int(population_size*0.6)),
        np.random.normal(loc=8, scale=1, size=int(population_size*0.4))
    ])
    
    # Function to take samples and calculate means
    def sample_means(population, sample_size, num_samples):
        return [np.mean(np.random.choice(population, size=sample_size, replace=True)) for _ in range(num_samples)]
    
    # Calculate sample means
    means = sample_means(population, sample_size, num_samples)
    
    with col2:
        # Create subplots
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Population Distribution", "Sampling Distribution of Means"))
        
        # Population distribution
        fig.add_trace(go.Histogram(x=population, name="Population", marker_color='lightblue'), row=1, col=1)
        
        # Sampling distribution of means
        fig.add_trace(go.Histogram(x=means, name="Sample Means", marker_color='lightgreen'), row=1, col=2)
        
        # Update layout
        fig.update_layout(height=500, showlegend=False)
        fig.update_xaxes(title_text="Value", row=1, col=1)
        fig.update_xaxes(title_text="Sample Mean", row=1, col=2, range=[4, 9])  # Fixed x-axis range for sampling distribution
        fig.update_yaxes(title_text="Frequency", row=1, col=1)
        fig.update_yaxes(title_text="Frequency", row=1, col=2)
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Statistics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Population Mean", f"{np.mean(population):.2f}")
        st.metric("Population Std Dev", f"{np.std(population):.2f}")
    with col2:
        st.metric("Mean of Sample Means", f"{np.mean(means):.2f}")
        st.metric("Std Dev of Sample Means", f"{np.std(means):.2f}")
    
    st.info("""
    **Observations:**
    1. The population distribution is bimodal.
    2. The sampling distribution of means tends towards a normal distribution (Central Limit Theorem).
    3. The mean of sample means is close to the population mean.
    4. The standard deviation of sample means (standard error) is smaller than the population standard deviation.
    5. As you increase the sample size, the sampling distribution becomes narrower.
    """)

with tab3:
    st.header("Test Your Knowledge")
    
    questions = [
        {
            "question": "What is a sampling distribution?",
            "options": [
                "The distribution of the entire population",
                "The distribution of a sample",
                "The probability distribution of a statistic from many samples",
                "The distribution of sample sizes"
            ],
            "correct": "The probability distribution of a statistic from many samples",
            "explanation": "A sampling distribution shows how a statistic (like the mean) varies across many samples drawn from the same population."
        },
        {
            "question": "What happens to the sampling distribution of the mean as sample size increases?",
            "options": [
                "It becomes wider",
                "It becomes narrower",
                "It doesn't change",
                "It becomes more skewed"
            ],
            "correct": "It becomes narrower",
            "explanation": "As sample size increases, the sampling distribution of the mean becomes narrower, indicating less variability in sample means."
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

