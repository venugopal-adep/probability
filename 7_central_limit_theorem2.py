import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def central_limit_theorem_demo():
    # Set page configuration
    st.set_page_config(page_title="Central Limit Theorem", layout="wide")

    # Custom CSS for better visual appeal
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        color: #0066cc;
        font-weight: bold;
    }
    .medium-font {
        font-size:20px !important;
        color: #009933;
    }
    .small-font {
        font-size:14px !important;
        color: #666666;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Central Limit Theorem Interactive Demo</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Explore the power of the Central Limit Theorem and its impact on statistical inference.</p>', unsafe_allow_html=True)

    # Sidebar for user inputs
    st.sidebar.header("Parameters")
    population_mean = st.sidebar.number_input("Population Mean", value=10.0, step=0.1)
    population_std = st.sidebar.number_input("Population Standard Deviation", value=2.0, step=0.1)
    sample_size = st.sidebar.slider("Sample Size", min_value=5, max_value=100, value=30, step=5)

    # Generate sample data
    population = np.random.normal(population_mean, population_std, 10000)
    sample_means = [np.mean(np.random.choice(population, size=sample_size)) for _ in range(1000)]

    # Create Plotly histogram for sample means distribution
    fig_hist = px.histogram(sample_means, nbins=30, title=f"Distribution of Sample Means (n = {sample_size})")
    fig_hist.update_layout(
        xaxis_title="Sample Mean",
        yaxis_title="Count",
        showlegend=False
    )

    # Create Plotly histogram for population distribution
    fig_pop = px.histogram(population, nbins=50, title="Population Distribution")
    fig_pop.update_layout(
        xaxis_title="Population Values",
        yaxis_title="Count",
        showlegend=False
    )

    # Display formulas and numerical example
    st.markdown('<p class="medium-font">Central Limit Theorem Formula</p>', unsafe_allow_html=True)
    st.latex(r"\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma}{\sqrt{n}}\right)")
    st.markdown('<p class="small-font">Where:</p>', unsafe_allow_html=True)
    st.markdown(r'$\bar{X}$ is the sample mean')
    st.markdown(r'$\mu$ is the population mean')
    st.markdown(r'$\sigma$ is the population standard deviation')
    st.markdown(r'$n$ is the sample size')

    st.markdown('<p class="medium-font">Numerical Example</p>', unsafe_allow_html=True)
    sample = np.random.choice(population, size=sample_size)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample)
    st.write(f"For a sample size of {sample_size}:")
    st.write(f"Sample Mean: {sample_mean:.2f}")
    st.write(f"Sample Standard Deviation: {sample_std:.2f}")
    st.write(f"Theoretical Standard Error: {population_std/np.sqrt(sample_size):.2f}")

    # Display Plotly charts
    st.plotly_chart(fig_pop, use_container_width=True)
    st.plotly_chart(fig_hist, use_container_width=True)

    # Interactive quiz
    st.markdown('<p class="medium-font">Quiz Time!</p>', unsafe_allow_html=True)
    quiz_questions = [
        {
            "question": "What happens to the spread of the sampling distribution as the sample size increases?",
            "options": ["Increases", "Decreases", "Remains the same", "Cannot be determined"],
            "answer": 1,
            "explanation": "As the sample size increases, the spread (standard error) of the sampling distribution decreases. This is because with larger samples, we have more information about the population, leading to more precise estimates."
        },
        {
            "question": "What is the shape of the sampling distribution for sample means when the sample size is large?",
            "options": ["Always normal", "Always skewed", "Depends on the population distribution", "Always uniform"],
            "answer": 0,
            "explanation": "According to the Central Limit Theorem, for large sample sizes, the sampling distribution of the sample mean approaches a normal distribution, regardless of the shape of the population distribution."
        },
        {
            "question": "How does the Central Limit Theorem help in statistical inference?",
            "options": ["It doesn't", "It allows us to make predictions about the population", "It only works for normal distributions", "It increases the sample size"],
            "answer": 1,
            "explanation": "The Central Limit Theorem allows us to make inferences about population parameters using sample statistics. It provides a foundation for many statistical techniques, including hypothesis testing and confidence interval estimation."
        }
    ]

    for i, quiz in enumerate(quiz_questions):
        st.write(f"Question {i+1}: {quiz['question']}")
        user_answer = st.radio(f"Select your answer for Question {i+1}:", quiz['options'], key=f"quiz_{i}")
        if st.button(f"Check Answer for Question {i+1}"):
            if user_answer == quiz['options'][quiz['answer']]:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {quiz['options'][quiz['answer']]}")
            st.info(f"Explanation: {quiz['explanation']}")
        st.write("---")

if __name__ == "__main__":
    central_limit_theorem_demo()