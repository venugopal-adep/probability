import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

# Page configuration
st.set_page_config(layout="wide", page_title="Sampling Distribution Properties", page_icon="📊")

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
st.title("📊 Properties of Sampling Distribution of the Mean")
st.write("**Developed by : Venugopal Adep**")
st.markdown("""
This interactive demo explores the key properties of the sampling distribution of the mean, 
including its relationship to the population parameters and the Central Limit Theorem.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📚 Concept", "🔍 Interactive Demo", "🧠 Quiz"])

with tab1:
    st.header("Important Points")
    
    st.info("""
    Suppose we are sampling from a population with mean μ and standard deviation σ. 
    Let X̄ be the random variable representing the sample mean of n independent observations.
    """)
    
    st.markdown("""
    ### Key Properties:
    1. The mean of X̄ is equal to μ (population mean)
    2. The standard deviation of X̄ is equal to σ/√n (Also called the 'standard error' of X̄)
    3. Even if the population is not normally distributed, for sufficiently large n, X̄ is approximately normally distributed (Central Limit Theorem)

    ### Why are these properties important?
    - They allow us to make inferences about the population based on sample statistics.
    - They form the basis for many statistical tests and confidence interval calculations.
    - They help us understand the relationship between sample size and the precision of our estimates.
    """)

with tab2:
    st.header("Interactive Demonstration")
    
    # Create a non-normal population (e.g., exponential distribution)
    np.random.seed(42)
    population_size = 100000
    population = np.random.exponential(scale=1, size=population_size)
    
    # Function to take samples and calculate means
    def sample_means(population, sample_size, num_samples):
        return [np.mean(np.random.choice(population, size=sample_size, replace=True)) for _ in range(num_samples)]
    
    # User inputs
    sample_size = st.slider("Select sample size (n):", min_value=1, max_value=1000, value=30, step=1)
    num_samples = st.slider("Number of samples to draw:", min_value=100, max_value=10000, value=1000, step=100)
    
    # Calculate sample means
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
        st.metric("Population Mean (μ)", f"{np.mean(population):.4f}")
        st.metric("Population Std Dev (σ)", f"{np.std(population):.4f}")
    with col2:
        st.metric("Mean of Sample Means", f"{np.mean(means):.4f}")
        st.metric("Std Dev of Sample Means", f"{np.std(means):.4f}")
    with col3:
        st.metric("Expected Std Error (σ/√n)", f"{np.std(population)/np.sqrt(sample_size):.4f}")
        st.metric("Normality Test p-value", f"{stats.normaltest(means)[1]:.4f}")
    
    st.info("""
    **Observations:**
    1. The population distribution is not normal (it's exponential in this case).
    2. The sampling distribution of means tends towards a normal distribution (Central Limit Theorem).
    3. The mean of sample means is close to the population mean (μ).
    4. The standard deviation of sample means (standard error) is close to σ/√n.
    5. As you increase the sample size (n), the sampling distribution becomes narrower and more normal.
    6. The normality test p-value increases with larger sample sizes, indicating closer approximation to normal distribution.
    """)

with tab3:
    st.header("Test Your Knowledge")
    
    questions = [
        {
            "question": "What is the relationship between the mean of X̄ and the population mean μ?",
            "options": [
                "The mean of X̄ is always less than μ",
                "The mean of X̄ is equal to μ",
                "The mean of X̄ is always greater than μ",
                "There is no relationship between the mean of X̄ and μ"
            ],
            "correct": "The mean of X̄ is equal to μ",
            "explanation": "The mean of the sampling distribution of the mean (X̄) is equal to the population mean (μ). This property makes X̄ an unbiased estimator of μ."
        },
        {
            "question": "What is the standard error of the mean?",
            "options": [
                "σ",
                "σ/n",
                "σ/√n",
                "σ²/n"
            ],
            "correct": "σ/√n",
            "explanation": "The standard error of the mean is σ/√n, where σ is the population standard deviation and n is the sample size. This represents the standard deviation of the sampling distribution of the mean."
        },
        {
            "question": "What does the Central Limit Theorem state about the sampling distribution of the mean?",
            "options": [
                "It is always normally distributed",
                "It is normally distributed only if the population is normal",
                "It approaches a normal distribution as sample size increases, regardless of the population distribution",
                "It is always skewed"
            ],
            "correct": "It approaches a normal distribution as sample size increases, regardless of the population distribution",
            "explanation": "The Central Limit Theorem states that for sufficiently large sample sizes, the sampling distribution of the mean approaches a normal distribution, even if the underlying population distribution is not normal."
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
1. The mean of the sampling distribution of the mean (X̄) is equal to the population mean (μ).
2. The standard deviation of X̄ (standard error) is σ/√n, where σ is the population standard deviation and n is the sample size.
3. As sample size increases, the standard error decreases, leading to more precise estimates.
4. The Central Limit Theorem states that for sufficiently large sample sizes, the sampling distribution of the mean approaches a normal distribution, regardless of the population distribution.
5. These properties are fundamental to statistical inference, allowing us to make conclusions about populations based on sample data.
""")
