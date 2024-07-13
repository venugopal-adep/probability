import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

# Set page config
st.set_page_config(layout="wide", page_title="Probability Distribution Explorer", page_icon="📊")

# Custom CSS
st.markdown("""
<style>
    body {font-family: Arial, sans-serif;}
    .main {padding: 1rem;}
    .stApp {background-color: #f0f4f8;}
    .st-emotion-cache-10trblm {text-align: center;}
    .info-box {background-color: #e1e5eb; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .example-box {background-color: #d4edda; padding: 15px; border-radius: 10px; margin-top: 10px; border-left: 5px solid #28a745;}
    .quiz-container {background-color: #d0e1f9; padding: 20px; border-radius: 10px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .stTabs {background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .plot-container {display: flex; justify-content: space-between; align-items: flex-start;}
    .sliders {width: 30%; padding-right: 20px;}
    .plot {width: 70%;}
    .stButton>button {background-color: #4e8cff; color: white; border-radius: 5px; border: none; padding: 10px 20px; font-size: 16px;}
    .stButton>button:hover {background-color: #3a7be0;}
    h1, h2, h3 {color: #2c3e50;}
    .stSlider {margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("📊 Probability Distribution Explorer")
st.write("**Developed by: Venugopal Adep**")
st.markdown("Dive into the world of probability distributions and discover how they describe random variables.")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Concept", "🎲 Discrete Distributions", "📈 Continuous Distributions", "🧠 Quiz"])

with tab1:
    st.header("Understanding Probability Distributions")
    st.write("**Developed by : Venugopal Adep**")
    st.markdown("""
    <div class="info-box">
    <h3>🎯 What is a Probability Distribution?</h3>
    A probability distribution describes the likelihood of different outcomes for a random variable. 
    It tells us what values the variable can take and how likely each value is.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>🎲 Discrete Probability Distribution</h3>
        <ul>
        <li>Describes random variables with distinct, separate values</li>
        <li>Uses a Probability Mass Function (PMF)</li>
        <li>Example: Number of heads in coin flips</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="info-box">
        <h3>📈 Continuous Probability Distribution</h3>
        <ul>
        <li>Describes random variables with infinitely many possible values</li>
        <li>Uses a Probability Density Function (PDF)</li>
        <li>Example: Height of people in a population</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    <h4>Real-life Example: Weather Forecast</h4>
    
    <b>Discrete Distribution:</b> Predicting the number of rainy days in a week.
    - Possible values: 0, 1, 2, 3, 4, 5, 6, 7 days
    - PMF gives the probability for each specific number of rainy days

    <b>Continuous Distribution:</b> Predicting the amount of rainfall in a day.
    - Possible values: Any non-negative real number (e.g., 0.5 mm, 2.7 mm, 10.3 mm)
    - PDF gives the relative likelihood of different rainfall amounts
    
    The weather forecast uses these distributions to give you probabilities like "30% chance of rain" or "Expected rainfall: 5-10 mm".
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.header("🎲 Discrete Probability Distributions")
    
    st.markdown("""
    Let's explore a common discrete distribution: the Binomial Distribution. 
    It models the number of successes in a fixed number of independent trials.
    """)
    
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.subheader("Binomial Distribution Parameters")
        n = st.slider("Number of Trials (n)", min_value=1, max_value=50, value=10)
        p = st.slider("Probability of Success (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
        
    with col2:
        x = np.arange(0, n+1)
        pmf = stats.binom.pmf(x, n, p)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=pmf, name="Probability"))
        
        fig.update_layout(
            title=f"Binomial Distribution (n={n}, p={p})",
            xaxis_title="Number of Successes",
            yaxis_title="Probability",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    st.markdown("""
    <div class="example-box">
    <h4>Understanding the Binomial Distribution</h4>
    - This distribution shows the probability of getting different numbers of successes in n trials.
    - Each bar represents the probability of getting exactly that many successes.
    - The highest bar shows the most likely outcome.
    
    <b>Example:</b> If you're flipping a fair coin 10 times (n=10, p=0.5):
    - The graph shows the probability of getting 0 heads, 1 head, 2 heads, and so on, up to 10 heads.
    - The highest point is usually around 5 heads, which is the most likely outcome.
    
    Try adjusting n and p to see how the distribution changes!
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("📈 Continuous Probability Distributions")
    
    st.markdown("""
    Now, let's explore a common continuous distribution: the Normal (Gaussian) Distribution. 
    It's often used to model natural phenomena and is characterized by its bell shape.
    """)
    
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.subheader("Normal Distribution Parameters")
        mean = st.slider("Mean (μ)", min_value=-5.0, max_value=5.0, value=0.0, step=0.1)
        std = st.slider("Standard Deviation (σ)", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
        
    with col2:
        # Set fixed x-axis range
        x_min, x_max = -10, 10
        x = np.linspace(x_min, x_max, 1000)
        pdf = stats.norm.pdf(x, mean, std)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=pdf, mode='lines', name="Probability Density"))
        
        fig.update_layout(
            title=f"Normal Distribution (μ={mean}, σ={std})",
            xaxis_title="Value",
            yaxis_title="Probability Density",
            showlegend=False,
            xaxis_range=[x_min, x_max]  # Set fixed x-axis range
        )
        
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Test Your Probability Distribution Knowledge!")
    
    st.markdown("""
    <div class="quiz-container">
    Let's see how well you understand probability distributions:
    </div>
    """, unsafe_allow_html=True)
    
    q1 = st.radio(
        "1. Which type of probability distribution would you use to model the number of cars passing through an intersection in an hour?",
        ["Normal Distribution", "Binomial Distribution", "Poisson Distribution", "Exponential Distribution"]
    )
    
    if st.button("Check Answer", key="q1"):
        if q1 == "Poisson Distribution":
            st.success("Correct! 🎉")
            st.markdown("""
            <div class="example-box">
            <h4>Explanation:</h4>
            The Poisson distribution is ideal for modeling the number of events occurring in a fixed interval of time or space, 
            especially when these events happen with a known average rate and independently of each other.

            In this case:
            - We're counting discrete events (cars passing)
            - It's over a fixed time interval (one hour)
            - Cars generally pass independently of each other
            - There's likely an average rate of cars per hour

            The Poisson distribution could tell us the probability of seeing any specific number of cars in an hour, 
            given the average rate. This is useful for traffic management, urban planning, and even for businesses 
            deciding when to open based on traffic patterns!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Not quite. Think about the characteristics of counting events over a fixed time interval.")

    q2 = st.radio(
        "2. What does the area under the curve of a probability density function (PDF) represent?",
        ["The mean of the distribution", "The standard deviation of the distribution", 
         "The total probability, which always equals 1", "The median of the distribution"]
    )

    if st.button("Check Answer", key="q2"):
        if q2 == "The total probability, which always equals 1":
            st.success("Spot on! 🎉")
            st.markdown("""
            <div class="example-box">
            <h4>Explanation:</h4>
            For a continuous probability distribution, the area under the curve of the probability density function (PDF) 
            always equals 1. This is a fundamental property of PDFs.

            Here's why this makes sense:
            1. Probabilities must always be between 0 and 1.
            2. The PDF covers all possible outcomes for the random variable.
            3. The total probability of all possible outcomes must sum to 1 (or 100%).

            Think of it like this: Imagine you're measuring people's heights. The PDF might show that some heights 
            are more likely than others, but if you consider every possible height (from very short to very tall), 
            the probability of someone falling somewhere on this spectrum is 100% or 1.

            This property is crucial for calculations involving continuous distributions, such as finding probabilities 
            for ranges of values (which is done by calculating the area under the curve for that range).
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Not quite. Consider what the total probability across all possible outcomes should be.")

    q3 = st.radio(
        "3. In a normal distribution, approximately what percentage of the data falls within one standard deviation of the mean?",
        ["50%", "68%", "95%", "99%"]
    )

    if st.button("Check Answer", key="q3"):
        if q3 == "68%":
            st.success("You've got it! 🎉")
            st.markdown("""
            <div class="example-box">
            <h4>Explanation:</h4>
            In a normal distribution, approximately 68% of the data falls within one standard deviation of the mean. 
            This is often called the "68-95-99.7 rule" or the "empirical rule."

            Here's a breakdown:
            - About 68% of the data falls within 1 standard deviation of the mean
            - About 95% falls within 2 standard deviations
            - About 99.7% falls within 3 standard deviations

            This property makes the normal distribution incredibly useful in many fields:

            - In quality control, it helps determine acceptable ranges for products.
            - In psychology, it's used to standardize test scores (like IQ tests).
            - In finance, it's used in risk assessment and portfolio management.

            For example, if human height is normally distributed with a mean of 170 cm and a standard deviation of 10 cm:
            - About 68% of people would be between 160 cm and 180 cm tall
            - About 95% would be between 150 cm and 190 cm
            - Almost everyone (99.7%) would be between 140 cm and 200 cm

            This "clustering" around the mean is what gives the normal distribution its characteristic bell shape!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Not quite. Remember the 68-95-99.7 rule for normal distributions.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #777;">
© 2024 Probability Distribution Explorer | Developed by Venugopal<br>
This interactive tool is for educational purposes only and does not represent any specific research study.
</div>
""", unsafe_allow_html=True)
