import streamlit as st
import plotly.graph_objs as go
import numpy as np
from scipy import stats

# Set page configuration
st.set_page_config(layout="wide", page_title="Statistical Estimation Explorer", page_icon="📊")

# Custom CSS for improved styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
    }
    .stRadio > div {
        flex-direction: row;
    }
    .stRadio label {
        margin-right: 15px;
    }
    h1, h2, h3 {
        color: #0e1117;
    }
    .highlight {
        background-color: #e6f3ff;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .solved-example {
        background-color: #e6ffe6;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .tab-content {
        padding: 20px;
        background-color: white;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main title with emoji
st.title("📊 Statistical Estimation Explorer")
st.write("**Developed by : Venugopal Adep**")

# Introduction
st.markdown("""
Welcome to the Statistical Estimation Explorer! This interactive tool helps you understand 
the concepts of point estimation and interval estimation in statistics. Adjust the parameters
and see how they affect the estimates in real-time.
""")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Interactive Plot", "🧮 Solved Examples", "🧠 Quiz", "📚 Learn More"])

with tab1:
    st.header("Interactive Statistical Estimation Plot")
    
    col1, col2 = st.columns([2, 1])

    with col2:
        st.subheader("📐 Sample Parameters")
        population_mean = st.number_input("True Population Mean", value=100, step=1)
        population_std = st.number_input("Population Standard Deviation", value=15, min_value=1, step=1)
        sample_size = st.slider("Sample Size", min_value=10, max_value=1000, value=30, step=10)
        confidence_level = st.slider("Confidence Level (%)", min_value=80, max_value=99, value=95, step=1)

        # Generate sample data
        np.random.seed(42)
        sample_data = np.random.normal(population_mean, population_std, sample_size)

        # Calculate estimates
        point_estimate = np.mean(sample_data)
        confidence_interval = stats.t.interval(confidence_level/100, df=sample_size-1, 
                                               loc=point_estimate, 
                                               scale=stats.sem(sample_data))

with col1:
    # Plotting
    fig = go.Figure()

    # Set fixed x-axis range
    x_min = 0  # You can adjust this value as needed
    x_max = 200  # You can adjust this value as needed

    # Add distribution curve
    x = np.linspace(x_min, x_max, 1000)
    y = stats.norm.pdf(x, population_mean, population_std)
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Population Distribution', 
                             line=dict(color='rgba(0,100,80,0.2)', width=2)))

    # Add vertical line for true population mean
    fig.add_vline(x=population_mean, line_dash="dash", line_color="red", 
                  annotation_text="True Population Mean", annotation_position="top right")

    # Add point estimate
    fig.add_vline(x=point_estimate, line_color="green", 
                  annotation_text="Point Estimate", annotation_position="top left")

    # Add confidence interval
    fig.add_vrect(x0=confidence_interval[0], x1=confidence_interval[1], 
                  fillcolor="rgba(0,100,80,0.2)", line_width=0,
                  annotation_text=f"{confidence_level}% Confidence Interval", 
                  annotation_position="bottom right")

    fig.update_layout(title="Point Estimate vs Interval Estimate",
                      xaxis_title="Value",
                      yaxis_title="Density",
                      showlegend=False,
                      height=500,
                      xaxis=dict(range=[x_min, x_max]))

    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Solved Examples")
    
    st.markdown("""
    <div class="solved-example">
    <h3>Example 1: Point Estimation</h3>
    <p><strong>Problem:</strong> A company wants to estimate the average daily sales. They collect data for 7 days:</p>
    <p>$500, $450, $600, $525, $575, $490, $610</p>
    <p><strong>Solution:</strong></p>
    <ol>
        <li>Calculate the sum of all values: $500 + $450 + $600 + $525 + $575 + $490 + $610 = $3750</li>
        <li>Divide by the number of days (7) to get the point estimate (sample mean):</li>
    </ol>
    <p>Point Estimate = $3750 / 7 = $535.71</p>
    <p>Therefore, the point estimate for average daily sales is $535.71.</p>
    </div>
    
    <div class="solved-example">
    <h3>Example 2: Interval Estimation</h3>
    <p><strong>Problem:</strong> Using the same data, calculate a 95% confidence interval for the average daily sales.</p>
    <p><strong>Solution:</strong></p>
    <ol>
        <li>We already know the sample mean (x̄) = $535.71</li>
        <li>Calculate the sample standard deviation (s):
           s ≈ $59.76 (using calculator or spreadsheet)</li>
        <li>For a 95% confidence level and 6 degrees of freedom (n-1), the t-value is approximately 2.447</li>
        <li>Calculate the margin of error: (t * s) / √n = (2.447 * 59.76) / √7 ≈ $55.22</li>
        <li>Calculate the confidence interval: x̄ ± margin of error</li>
    </ol>
    <p>95% Confidence Interval: $535.71 ± $55.22 = ($480.49, $590.93)</p>
    <p>We can be 95% confident that the true population mean for daily sales falls between $480.49 and $590.93.</p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("Quiz Time!")
    
    # Quiz questions
    questions = [
        {
            "question": "What does a point estimate provide?",
            "options": ["A range of values", "A single best guess", "Multiple possible outcomes"],
            "correct": "A single best guess",
            "explanation": """A point estimate provides a single best guess for a population parameter based on sample data. 
            For example, if we want to estimate the average height of all students in a school, we might measure the heights of 
            50 randomly selected students and calculate their average. This average is a point estimate for the true average height 
            of all students in the school."""
        },
        {
            "question": "What does a 95% confidence interval mean?",
            "options": ["95% of the data falls within this range", "We are 95% certain the true parameter is in this range", "The interval covers 95% of the population"],
            "correct": "We are 95% certain the true parameter is in this range",
            "explanation": """A 95% confidence interval means that if we were to repeat our sampling process many times and 
            calculate the interval each time, about 95% of these intervals would contain the true population parameter. 
            For instance, if we calculate a 95% confidence interval for the average height of students to be (65 inches, 68 inches), 
            we can be 95% confident that the true average height of all students in the school falls within this range."""
        },
        {
            "question": "How does increasing sample size generally affect the width of a confidence interval?",
            "options": ["Widens it", "Narrows it", "Has no effect"],
            "correct": "Narrows it",
            "explanation": """Increasing the sample size generally narrows the confidence interval. This is because a larger sample 
            size provides more information about the population, reducing uncertainty. For example, if we increase our sample of 
            student heights from 50 to 200, our confidence interval might narrow from (65 inches, 68 inches) to (65.5 inches, 67.5 inches), 
            giving us a more precise estimate of the true average height."""
        }
    ]

    # Display questions and handle responses
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        response = st.radio(q["question"], q["options"], key=f"q{i}")
        if st.button(f"Check Answer {i+1}"):
            if response == q["correct"]:
                st.success("🎉 Correct!")
            else:
                st.error("❌ Incorrect. Try again!")
            st.info(f"Explanation: {q['explanation']}")
        st.markdown("---")

with tab4:
    st.header("Learn More")
    st.markdown("""
    Want to dive deeper into statistical estimation? Check out these resources:
    
    1. [Khan Academy: Confidence Intervals](https://www.khanacademy.org/math/statistics-probability/confidence-intervals-one-sample)
    2. [Statistics How To: Point Estimation](https://www.statisticshowto.com/point-estimation/)
    3. [Yale Statistics: Interval Estimation](http://www.stat.yale.edu/Courses/1997-98/101/confint.htm)
    4. [Interactive Statistics Visualizations](https://seeing-theory.brown.edu/index.html)
    5. [StatQuest: Statistics Fundamentals (YouTube)](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9)
    
    Remember, practice makes perfect! Try working through more examples and problems to solidify your understanding.
    """)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit | © 2024 Statistical Estimation Explorer")
