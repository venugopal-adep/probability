import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))

st.set_page_config(layout="wide", page_title="Normal Distribution Explorer", page_icon="🔔")

st.title("🔔 Normal Distribution Interactive Explorer")
st.write("**Developed by : Venugopal Adep**")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Interactive Plot", "🧮 Solved Examples", "🧠 Quiz", "📚 Learn More"])

with tab1:
    col1, col2 = st.columns([2, 1])

    with col2:
        st.write("""
        ### What is Normal Distribution?
        
        The normal distribution is a symmetric bell-shaped curve defined by two parameters:
        - μ (mu): the mean, center of the distribution
        - σ (sigma): the standard deviation, spread of the distribution

        Adjust the sliders to see how these parameters affect the distribution!
        """)

        # Interactive parameters
        mu = st.slider("Mean (μ)", -5.0, 5.0, 0.0, 0.1)
        sigma = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, 0.1)

    with col1:
        # Generate x values (fixed range)
        x = np.linspace(-10, 10, 1000)

        # Calculate y values
        y = normal_pdf(x, mu, sigma)

        # Create the plot
        fig = go.Figure()

        # Add main distribution curve
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution', line=dict(color='royalblue', width=3)))

        # Add colored areas for 68-95-99.7 rule
        fig.add_trace(go.Scatter(x=np.concatenate([x, x[::-1]]), 
                                 y=np.concatenate([normal_pdf(x, mu, sigma) * (abs(x-mu) <= sigma), 
                                                   np.zeros_like(x)[::-1]]),
                                 fill='tozeroy', fillcolor='rgba(255,0,0,0.2)', line=dict(color='rgba(255,0,0,0)'),
                                 name='68% (±1σ)'))
        
        fig.add_trace(go.Scatter(x=np.concatenate([x, x[::-1]]), 
                                 y=np.concatenate([normal_pdf(x, mu, sigma) * (abs(x-mu) <= 2*sigma), 
                                                   np.zeros_like(x)[::-1]]),
                                 fill='tozeroy', fillcolor='rgba(0,255,0,0.2)', line=dict(color='rgba(0,255,0,0)'),
                                 name='95% (±2σ)'))
        
        fig.add_trace(go.Scatter(x=np.concatenate([x, x[::-1]]), 
                                 y=np.concatenate([normal_pdf(x, mu, sigma) * (abs(x-mu) <= 3*sigma), 
                                                   np.zeros_like(x)[::-1]]),
                                 fill='tozeroy', fillcolor='rgba(0,0,255,0.2)', line=dict(color='rgba(0,0,255,0)'),
                                 name='99.7% (±3σ)'))

        # Update layout
        fig.update_layout(
            title=f'Normal Distribution (μ={mu}, σ={sigma})',
            xaxis_title='x', 
            yaxis_title='Probability Density',
            xaxis=dict(range=[-10, 10]),
            legend=dict(x=0.02, y=0.98),
            height=600
        )

        # Add annotations for mean and standard deviations
        fig.add_annotation(x=mu, y=0, text="μ", showarrow=True, arrowhead=2, ax=0, ay=40)
        fig.add_annotation(x=mu+sigma, y=0, text="σ", showarrow=True, arrowhead=2, ax=0, ay=40)
        fig.add_annotation(x=mu-sigma, y=0, text="σ", showarrow=True, arrowhead=2, ax=0, ay=40)

        st.plotly_chart(fig, use_container_width=True)

    st.write("""
    ### 🎯 68-95-99.7 Rule

    This rule, also known as the empirical rule, states that for a normal distribution:
    - About 68% of the data falls within 1σ of the mean (red area)
    - About 95% of the data falls within 2σ of the mean (green area)
    - About 99.7% of the data falls within 3σ of the mean (blue area)

    This rule is visually represented in the shaded areas of the graph above.
    """)

with tab2:
    st.header("🧮 Solved Examples")

    st.write("""
    Let's work through some examples to better understand the normal distribution.
    """)

    st.subheader("Example 1: IQ Scores")
    st.write("""
    IQ scores are normally distributed with a mean (μ) of 100 and a standard deviation (σ) of 15.

    Question: What percentage of people have an IQ between 85 and 115?

    Solution:
    1. Calculate z-scores for 85 and 115:
       z₁ = (85 - 100) / 15 = -1
       z₂ = (115 - 100) / 15 = 1

    2. Use the empirical rule: 68% of data falls within ±1σ of the mean.

    Therefore, approximately 68% of people have an IQ between 85 and 115.
    """)

    st.subheader("Example 2: Height of Adult Males")
    st.write("""
    The height of adult males in a certain population follows a normal distribution with a mean (μ) of 170 cm and a standard deviation (σ) of 7 cm.

    Question: What is the probability that a randomly selected male is taller than 184 cm?

    Solution:
    1. Calculate the z-score for 184 cm:
       z = (184 - 170) / 7 = 2

    2. Use a z-table or statistical function to find the area to the right of z = 2.
    """)

    prob = 1 - stats.norm.cdf(2)
    st.write(f"Probability = {prob:.4f} or {prob*100:.2f}%")

    st.write("""
    This means that approximately 2.28% of adult males in this population are taller than 184 cm.
    """)

with tab3:
    st.header("🧠 Quiz")

    st.write("Test your understanding of the normal distribution with these questions!")

    # Quiz Question 1
    q1 = st.radio(
        "1. What happens to the shape of the normal distribution when you increase the standard deviation?",
        ("It becomes taller and narrower", "It becomes shorter and wider", "It shifts to the right", "It doesn't change")
    )

    if st.button("Check Answer for Question 1"):
        if q1 == "It becomes shorter and wider":
            st.success("🎉 Correct! Increasing the standard deviation makes the distribution more spread out, resulting in a shorter and wider bell curve.")
            st.write("""
            Explanation:
            Think of the standard deviation as a measure of how spread out the data is. When you increase it:
            - The "peak" of the bell curve gets lower because the same amount of data is now spread over a wider range.
            - The "tails" of the distribution stretch out further, making the overall shape wider.

            Example: Imagine you're measuring the height of trees in two forests. Forest A has trees mostly between 10-20 meters (small standard deviation). Forest B has trees ranging from 5-25 meters (larger standard deviation). The distribution for Forest B would be wider and flatter compared to Forest A.
            """)
        else:
            st.error("❌ That's not correct. Increasing the standard deviation makes the distribution more spread out, resulting in a shorter and wider bell curve.")

    # Quiz Question 2
    q2 = st.radio(
        "2. In a normal distribution, what percentage of data falls within one standard deviation of the mean?",
        ("50%", "68%", "95%", "99.7%")
    )

    if st.button("Check Answer for Question 2"):
        if q2 == "68%":
            st.success("🎉 Correct! Approximately 68% of the data falls within one standard deviation of the mean in a normal distribution.")
            st.write("""
            Explanation:
            This is part of the 68-95-99.7 rule (also known as the empirical rule) for normal distributions:
            - 68% of data falls within ±1 standard deviation
            - 95% of data falls within ±2 standard deviations
            - 99.7% of data falls within ±3 standard deviations

            Example: If adult male heights are normally distributed with a mean of 170 cm and a standard deviation of 7 cm, about 68% of adult males would have heights between 163 cm (170 - 7) and 177 cm (170 + 7).
            """)
        else:
            st.error("❌ That's not correct. In a normal distribution, approximately 68% of the data falls within one standard deviation of the mean.")

    # Quiz Question 3
    q3 = st.radio(
        "3. What does the mean (μ) represent in a normal distribution?",
        ("The highest point of the curve", "The middle 50% of the data", "The average of all values", "The most common value")
    )

    if st.button("Check Answer for Question 3"):
        if q3 == "The average of all values":
            st.success("🎉 Correct! The mean (μ) in a normal distribution represents the average of all values in the dataset.")
            st.write("""
            Explanation:
            In a normal distribution:
            - The mean (μ) is the center of the distribution.
            - It represents the average or expected value of the dataset.
            - The distribution is symmetric around the mean.
            - The mean, median, and mode are all equal in a perfectly normal distribution.

            Example: If you measure the weight of 1000 apples and find they're normally distributed with a mean of 150 grams, this means:
            - The average weight of all apples is 150 grams.
            - There are roughly as many apples weighing more than 150g as there are weighing less than 150g.
            - If you randomly pick an apple, your best guess for its weight would be 150g.
            """)
        else:
            st.error("❌ That's not correct. The mean (μ) in a normal distribution represents the average of all values in the dataset.")

with tab4:
    st.header("📚 Learn More")

    st.write("""
    ### Applications of Normal Distribution

    The normal distribution is widely used in various fields:

    1. **Natural Sciences**: Many natural phenomena approximately follow a normal distribution, such as:
       - Heights of people
       - Blood pressure
       - Measurement errors in scientific experiments

    2. **Social Sciences**: Used to model and analyze various social phenomena:
       - IQ scores
       - Test scores in large populations
       - Income distribution in some cases

    3. **Finance**: Applied in various financial models:
       - Stock price movements
       - Risk assessment in portfolio management

    4. **Quality Control**: Used in manufacturing to:
       - Set acceptable limits for product specifications
       - Monitor and improve production processes

    5. **Data Science and Machine Learning**: Many algorithms assume normally distributed data or errors.

    ### Why is it so important?

    1. **Central Limit Theorem**: As sample sizes increase, the distribution of sample means approaches a normal distribution, regardless of the underlying distribution of the data.

    2. **Predictability**: The well-defined properties of normal distributions allow for accurate predictions and inferences.

    3. **Mathematical Convenience**: Many statistical methods are developed assuming normally distributed data, making calculations and interpretations simpler.

    ### Further Reading

    To deepen your understanding of normal distributions and their applications, consider exploring these topics:
    - Z-scores and standardization
    - Probability density functions
    - Cumulative distribution functions
    - Hypothesis testing
    - Confidence intervals

    Remember, while many real-world phenomena approximately follow a normal distribution, it's always important to verify this assumption when applying statistical methods!
    """)

st.sidebar.header("About This App")
st.sidebar.write("""
This interactive app helps you explore and understand the normal distribution. 

Features:
- 📊 Visualize how changing parameters affects the distribution
- 🧮 Work through solved examples
- 🧠 Test your knowledge with a quiz
- 📚 Learn about real-world applications

Enjoy exploring the fascinating world of normal distributions!
""")

st.sidebar.info("Created with ❤️ using Streamlit and Plotly")
