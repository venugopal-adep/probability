import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(layout="wide", page_title="Sampling & Inference Demo", page_icon="📊")

# Custom CSS for better visual appeal
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
st.title("📊 Understanding Sampling and Population Inference")
st.write("**Developed by : Venugopal Adep**")
st.markdown("""
This interactive demo explores the fundamental concepts of sampling and making inferences about a population.
Navigate through the tabs below to learn about different aspects of sampling and statistical inference.
""")

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Concepts", "📈 Interactive Demo", "🧮 Calculations", "🧠 Quiz"])

with tab1:
    st.header("Key Concepts in Sampling")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Population")
        st.info("The entire group we want to study. In practice, it's often too large or impractical to measure entirely.")
    
    with col2:
        st.subheader("🔍 Sample")
        st.info("A subset of the population that we actually measure. It should be representative of the population.")
    
    st.subheader("🧠 Inference")
    st.success("The process of drawing conclusions about the population based on the sample data.")
    
    st.markdown("""
    ### Why Sampling is Important
    1. **Cost-effective**: Measuring an entire population can be expensive and time-consuming.
    2. **Practicality**: In many cases, it's impossible to measure every member of a population.
    3. **Timeliness**: Sampling allows for quicker data collection and analysis.
    4. **Non-destructive**: For some studies, measuring the entire population would be destructive.
    """)

with tab2:
    st.header("Interactive Sampling Demo")
    
    # Simulate a population
    np.random.seed(42)
    population = np.random.normal(loc=170, scale=10, size=10000)

    # Function to take a sample
    def take_sample(population, sample_size):
        return np.random.choice(population, size=sample_size, replace=False)

    # Interactive sample size selector
    sample_size = st.slider("Select sample size:", min_value=10, max_value=1000, value=100, step=10)

    # Take a sample
    sample = take_sample(population, sample_size)

    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=population, name="Population", opacity=0.7, marker_color='#1f77b4'))
    fig.add_trace(go.Histogram(x=sample, name="Sample", opacity=0.7, marker_color='#ff7f0e'))
    fig.update_layout(
        title="Population vs Sample Distribution",
        xaxis_title="Height (cm)",
        yaxis_title="Count",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Statistics
    st.subheader("Statistics Comparison")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Population Mean", f"{population.mean():.2f} cm")
        st.metric("Population Std Dev", f"{population.std():.2f} cm")
    with col2:
        st.metric("Sample Mean", f"{sample.mean():.2f} cm")
        st.metric("Sample Std Dev", f"{sample.std():.2f} cm")

    st.info("""
    **Interpretation:**
    - The blue histogram represents the entire population (10,000 individuals).
    - The orange histogram represents our sample (adjustable size).
    - Notice how the sample distribution approximates the population distribution as the sample size increases.
    - The sample statistics (mean and standard deviation) are estimates of the population parameters.
    """)

with tab3:
    st.header("Statistical Calculations")
    
    st.subheader("Confidence Interval for Population Mean")
    confidence_level = st.selectbox("Select Confidence Level:", ["90%", "95%", "99%"])
    
    z_scores = {"90%": 1.645, "95%": 1.96, "99%": 2.576}
    z_score = z_scores[confidence_level]

    margin_of_error = z_score * (sample.std() / np.sqrt(sample_size))
    ci_lower = sample.mean() - margin_of_error
    ci_upper = sample.mean() + margin_of_error

    st.markdown(f"""
    **Formula:** CI = X̄ ± (z * (s / √n))
    
    Where:
    - X̄ is the sample mean: {sample.mean():.2f}
    - z is the z-score for {confidence_level} confidence: {z_score}
    - s is the sample standard deviation: {sample.std():.2f}
    - n is the sample size: {sample_size}
    """)

    st.latex(r"\text{CI} = \bar{X} \pm \left(z \cdot \frac{s}{\sqrt{n}}\right)")

    st.markdown(f"""
    **Calculation:**
    CI = {sample.mean():.2f} ± ({z_score} * ({sample.std():.2f} / √{sample_size}))
    CI = ({ci_lower:.2f}, {ci_upper:.2f})
    """)

    st.success(f"""
    **Interpretation:** We are {confidence_level} confident that the true population mean 
    falls between {ci_lower:.2f} cm and {ci_upper:.2f} cm.
    """)

with tab4:
    st.header("Test Your Knowledge")
    
    questions = [
        {
            "question": "What happens to the accuracy of our population estimate as we increase the sample size?",
            "options": ["It increases", "It decreases", "It stays the same"],
            "correct": "It increases",
            "explanation": "As the sample size increases, our estimate of the population parameters becomes more accurate. This is because a larger sample is more likely to be representative of the entire population."
        },
        {
            "question": "What does a 95% confidence interval mean?",
            "options": [
                "95% of the population falls within this interval",
                "We are 95% certain that the population mean falls within this interval",
                "95% of samples will contain the true population mean"
            ],
            "correct": "We are 95% certain that the population mean falls within this interval",
            "explanation": "A 95% confidence interval means that if we repeated this sampling process many times, about 95% of the calculated intervals would contain the true population parameter."
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
1. Sampling allows us to make inferences about a large population without measuring every individual.
2. Larger samples generally provide more accurate estimates of population parameters.
3. Statistical techniques like confidence intervals help quantify the uncertainty in our estimates.
4. Always consider potential biases in your sampling method to ensure your sample is representative of the population.
""")
