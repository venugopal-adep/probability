import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(layout="wide", page_title="Simple Random Sampling Demo", page_icon="🎲")

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
st.title("🎲 Simple Random Sampling")
st.write("**Developed by : Venugopal Adep**")
st.markdown("""
This interactive demo explores the concept of Simple Random Sampling and its importance in statistical analysis.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📚 Concept", "🔍 Interactive Demo", "🧠 Quiz"])

with tab1:
    st.header("What is Simple Random Sampling?")
    
    st.info("""
    Simple Random Sampling is a sampling technique where every item in the population has an equal chance of being selected.
    """)
    
    st.subheader("Why are simple random samples important?")
    st.success("""
    Allows all the entities in the population to have an equal chance of being selected and so the
    sample is likely to be representative of the population.
    """)
    
    st.markdown("""
    ### Key Advantages:
    1. **Unbiased**: Each member of the population has an equal probability of selection.
    2. **Representative**: The sample is likely to reflect the characteristics of the entire population.
    3. **Simplicity**: It's straightforward to implement and understand.
    4. **Statistical Validity**: Many statistical methods assume random sampling.
    
    ### Limitations:
    1. Requires a complete list of the population, which may not always be available.
    2. Can be impractical for very large populations.
    3. May not capture specific subgroups in small samples of diverse populations.
    """)

with tab2:
    st.header("Interactive Simple Random Sampling Demo")
    
    # Create a population
    np.random.seed(42)
    population_size = 1000
    population = pd.DataFrame({
        'ID': range(1, population_size + 1),
        'Value': np.random.normal(loc=100, scale=15, size=population_size)
    })
    
    # Sampling function
    def simple_random_sample(population, sample_size):
        return population.sample(n=sample_size)
    
    # User input
    sample_size = st.slider("Select sample size:", min_value=10, max_value=500, value=50, step=10)
    
    # Take a sample
    sample = simple_random_sample(population, sample_size)
    
    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=population['ID'], y=population['Value'], mode='markers', name='Population', 
                             marker=dict(color='lightblue', size=5)))
    fig.add_trace(go.Scatter(x=sample['ID'], y=sample['Value'], mode='markers', name='Sample', 
                             marker=dict(color='red', size=8)))
    fig.update_layout(title="Population vs Sample",
                      xaxis_title="ID",
                      yaxis_title="Value",
                      showlegend=True)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Population Mean", f"{population['Value'].mean():.2f}")
        st.metric("Population Std Dev", f"{population['Value'].std():.2f}")
    with col2:
        st.metric("Sample Mean", f"{sample['Value'].mean():.2f}")
        st.metric("Sample Std Dev", f"{sample['Value'].std():.2f}")
    
    st.info("""
    **Observation:**
    - Red dots represent the randomly selected sample.
    - Notice how the sample is spread across the entire population.
    - As you increase the sample size, the sample statistics get closer to the population statistics.
    """)

with tab3:
    st.header("Test Your Knowledge")
    
    questions = [
        {
            "question": "What is the main characteristic of Simple Random Sampling?",
            "options": [
                "Every item has an equal chance of being selected",
                "Items are selected based on specific criteria",
                "The first n items are always selected",
                "Only the most representative items are selected"
            ],
            "correct": "Every item has an equal chance of being selected",
            "explanation": "In Simple Random Sampling, every item in the population has an equal probability of being selected, ensuring unbiased representation."
        },
        {
            "question": "Why is Simple Random Sampling important?",
            "options": [
                "It's the fastest sampling method",
                "It always produces perfect results",
                "It likely produces a representative sample of the population",
                "It requires the smallest sample size"
            ],
            "correct": "It likely produces a representative sample of the population",
            "explanation": "Simple Random Sampling is important because it allows all entities in the population to have an equal chance of being selected, making the sample likely to be representative of the entire population."
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
1. Simple Random Sampling gives every item in the population an equal chance of selection.
2. It helps in obtaining a representative sample of the population.
3. The larger the sample size, the more likely it is to reflect the characteristics of the population.
4. While simple and unbiased, it may not always be practical for very large or complex populations.
""")
