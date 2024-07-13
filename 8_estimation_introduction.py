import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

# Set page config
st.set_page_config(layout="wide", page_title="Statistical Estimation Explorer", page_icon="📊")

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
st.title("📊 Statistical Estimation Explorer")
st.write("**Developed by: Your Name**")
st.markdown("Dive into the world of statistical estimation and discover how we make inferences about populations from samples.")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Concept", "📏 Point Estimation", "🔍 Interval Estimation", "🧠 Quiz"])

with tab1:
    st.header("Understanding Statistical Estimation")
    
    st.markdown("""
    <div class="info-box">
    <h3>🎯 What is Estimation?</h3>
    Estimation is the process of making inferences about a population parameter based on a sample statistic. 
    It's like trying to guess the number of jellybeans in a jar by looking at just a handful of them!
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>📍 Point Estimation</h3>
        <ul>
        <li>A single value estimate of a population parameter</li>
        <li>Simple but doesn't account for uncertainty</li>
        <li>Example: The average height of all students is 170 cm</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="info-box">
        <h3>📏 Interval Estimation</h3>
        <ul>
        <li>A range of values likely to contain the true parameter</li>
        <li>Accounts for uncertainty in the estimate</li>
        <li>Example: The average height is between 168 cm and 172 cm with 95% confidence</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    <h4>Real-life Example: Polling in Elections</h4>
    Imagine you're trying to predict the outcome of an election:

    <b>Point Estimation:</b> Based on a poll of 1000 voters, you estimate that Candidate A will receive 52% of the votes.

    <b>Interval Estimation:</b> You estimate that Candidate A will receive between 49% and 55% of the votes, with 95% confidence.

    The interval estimation gives a more complete picture, accounting for the uncertainty in your prediction!
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.header("📍 Point Estimation in Action")
    
    st.markdown("""
    Let's explore point estimation using a simulated population. Adjust the parameters to see how sample size affects our estimate.
    """)
    
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.subheader("Population Parameters")
        true_mean = st.number_input("True Population Mean", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        true_std = st.number_input("True Population Std Dev", min_value=1.0, max_value=20.0, value=10.0, step=0.1)
        
        st.subheader("Sample Size")
        sample_size = st.slider("Number of Samples", min_value=10, max_value=1000, value=100, step=10)
        
        if st.button("Generate New Sample"):
            st.session_state.sample = np.random.normal(true_mean, true_std, sample_size)
    
    with col2:
        if 'sample' not in st.session_state:
            st.session_state.sample = np.random.normal(true_mean, true_std, sample_size)
        
        sample = st.session_state.sample
        sample_mean = np.mean(sample)
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=sample, name="Sample Distribution"))
        fig.add_vline(x=true_mean, line_dash="dash", line_color="red", annotation_text="True Mean")
        fig.add_vline(x=sample_mean, line_dash="dash", line_color="green", annotation_text="Sample Mean")
        
        fig.update_layout(
            title="Sample Distribution with Point Estimate",
            xaxis_title="Value",
            yaxis_title="Frequency",
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div class="info-box">
        <h4>Results:</h4>
        <ul>
        <li>True Population Mean: {true_mean:.2f}</li>
        <li>Point Estimate (Sample Mean): {sample_mean:.2f}</li>
        <li>Estimation Error: {abs(sample_mean - true_mean):.2f}</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    <h4>What's happening here?</h4>
    - We're simulating a population with a known mean (red line) and standard deviation.
    - We then take a sample from this population and calculate its mean (green line).
    - This sample mean serves as our point estimate for the true population mean.
    - Notice how the sample mean isn't always exactly the same as the true mean!
    - Try increasing the sample size. Does the estimate generally get better?
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("🔍 Interval Estimation Explored")
    
    st.markdown("""
    Now, let's see how interval estimation provides a range of likely values for our population parameter.
    """)
    
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.subheader("Population Parameters")
        true_mean = st.number_input("True Population Mean", min_value=0.0, max_value=100.0, value=50.0, step=0.1, key="int_true_mean")
        true_std = st.number_input("True Population Std Dev", min_value=1.0, max_value=20.0, value=10.0, step=0.1, key="int_true_std")
        
        st.subheader("Sample Size")
        sample_size = st.slider("Number of Samples", min_value=10, max_value=1000, value=100, step=10, key="int_sample_size")
        
        confidence_level = st.slider("Confidence Level", min_value=0.80, max_value=0.99, value=0.95, step=0.01)
        
        if st.button("Generate New Sample", key="int_generate"):
            st.session_state.int_sample = np.random.normal(true_mean, true_std, sample_size)
    
    with col2:
        if 'int_sample' not in st.session_state:
            st.session_state.int_sample = np.random.normal(true_mean, true_std, sample_size)
        
        sample = st.session_state.int_sample
        sample_mean = np.mean(sample)
        sample_std = np.std(sample, ddof=1)
        
        margin_of_error = stats.t.ppf((1 + confidence_level) / 2, df=sample_size-1) * (sample_std / np.sqrt(sample_size))
        ci_lower = sample_mean - margin_of_error
        ci_upper = sample_mean + margin_of_error
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=sample, name="Sample Distribution"))
        fig.add_vline(x=true_mean, line_dash="dash", line_color="red", annotation_text="True Mean")
        fig.add_vline(x=sample_mean, line_dash="dash", line_color="green", annotation_text="Sample Mean")
        fig.add_vrect(x0=ci_lower, x1=ci_upper, fillcolor="rgba(0,255,0,0.1)", layer="below", line_width=0,
                      annotation_text="Confidence Interval", annotation_position="top left")
        
        fig.update_layout(
            title="Sample Distribution with Confidence Interval",
            xaxis_title="Value",
            yaxis_title="Frequency",
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div class="info-box">
        <h4>Results:</h4>
        <ul>
        <li>True Population Mean: {true_mean:.2f}</li>
        <li>Point Estimate (Sample Mean): {sample_mean:.2f}</li>
        <li>{confidence_level*100:.0f}% Confidence Interval: ({ci_lower:.2f}, {ci_upper:.2f})</li>
        <li>Does the interval contain the true mean? {"Yes" if ci_lower <= true_mean <= ci_upper else "No"}</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    <h4>What's happening here?</h4>
    - We're now calculating a confidence interval around our point estimate.
    - The green shaded area shows the range where we're {confidence_level*100:.0f}% confident the true population mean lies.
    - This interval gives us a measure of the uncertainty in our estimate.
    - Try changing the confidence level. Notice how the interval width changes?
    - A wider interval is more likely to contain the true mean but gives us less precise information.
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.header("Test Your Estimation Knowledge!")
    
    st.markdown("""
    <div class="quiz-container">
    Let's see how well you understand statistical estimation concepts:
    </div>
    """, unsafe_allow_html=True)
    
    q1 = st.radio(
        "1. What is the main advantage of interval estimation over point estimation?",
        ["It's always more accurate", "It provides a measure of uncertainty", "It's easier to calculate", "It always includes the true parameter"]
    )
    
    if st.button("Check Answer", key="q1"):
        if q1 == "It provides a measure of uncertainty":
            st.success("Correct! 🎉")
            st.markdown("""
            <div class="example-box">
            <h4>Explanation:</h4>
            Interval estimation provides a range of plausible values for the population parameter, along with a 
            confidence level. This gives us a measure of how certain we are about our estimate.

            For example, if we say "the average height is between 168 cm and 172 cm with 95% confidence", we're 
            acknowledging that our estimate isn't exact, but we're pretty sure the true average is in this range.

            Point estimation, on the other hand, gives a single value without any indication of how precise or 
            reliable that estimate is.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Not quite. Think about what additional information interval estimation provides.")

    q2 = st.radio(
        "2. As sample size increases, what typically happens to the width of a confidence interval?",
        ["It increases", "It decreases", "It stays the same", "It becomes zero"]
    )

    if st.button("Check Answer", key="q2"):
        if q2 == "It decreases":
            st.success("Spot on! 🎉")
            st.markdown("""
            <div class="example-box">
            <h4>Explanation:</h4>
            As the sample size increases, the width of the confidence interval typically decreases. This is because:

            1. Larger samples tend to be more representative of the population.
            2. The standard error (which affects the margin of error) decreases with larger sample sizes.

            Think of it like this: If you're estimating the average height of all students in a school, you'd be 
            more confident in your estimate if you measured 100 students rather than just 10. With 100 students, 
            you might say "the average is between 165 cm and 170 cm", but with only 10 students, you might have to 
            say "the average is between 160 cm and 175 cm" to be equally confident.

            This is why researchers often try to get larger sample sizes - it allows for more precise estimates!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Not quite. Consider how more data might affect our certainty about an estimate.")

    q3 = st.radio(
        "3. What does a 95% confidence interval mean?",
        ["The true parameter has a 95% chance of being in this interval", 
         "95% of the data falls within this interval", 
         "If we repeated the sampling process many times, about 95% of the intervals would contain the true parameter", 
         "The sample mean is 95% accurate"]
    )

    if st.button("Check Answer", key="q3"):
        if q3 == "If we repeated the sampling process many times, about 95% of the intervals would contain the true parameter":
            st.success("You've got it! 🎉")
            st.markdown("""
            <div class="example-box">
            <h4>Explanation:</h4>
            If we repeated our sampling process many times and calculated the interval each time, about 95% of these intervals would contain the true population parameter.

            This is a subtle but important point:
            1. We're not saying there's a 95% chance the true parameter is in this specific interval.
            2. We're not saying 95% of the data is in this interval.
            3. Instead, it's about the reliability of our method over many repetitions.

            Think of it like this: Imagine you're a weather forecaster. If you say there's a 95% chance of rain 
            tomorrow, and it doesn't rain, were you wrong? Not necessarily. But if you make 100 such "95% chance" 
            predictions over time, you'd expect to be right about 95 times.

            In the same way, our 95% confidence interval is a statement about how often this method of creating 
            intervals will include the true parameter, not about the probability of this specific interval 
            including it.

            This is why researchers often use confidence intervals: they give us a sense of how reliable our 
            estimation method is, even if we can't be certain about any single estimate.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Not quite. The interpretation of confidence intervals can be tricky - think about what it means over many repetitions.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #777;">
© 2024 Statistical Estimation Explorer | Developed by Your Name<br>
This interactive tool is for educational purposes only and does not represent any specific research study.
</div>
""", unsafe_allow_html=True)
