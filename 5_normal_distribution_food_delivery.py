import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def main():
    st.set_page_config(page_title="Food Delivery Time Explorer", layout="wide")
    
    st.title("🍕 Food Delivery Time Explorer")
    
    st.markdown("""
    Welcome to the Food Delivery Time Explorer! This interactive tool will help you understand
    how delivery times are distributed and what you can expect from a food delivery service.
    """)
    
    tab1, tab2, tab3 = st.tabs(["📊 Interactive Plot", "🧮 Probability Calculator", "🧠 Quiz"])
    
    with tab1:
        interactive_plot()
    
    with tab2:
        probability_calculator()
    
    with tab3:
        quiz()

def interactive_plot():
    st.header("Interactive Food Delivery Time Distribution")
    
    col1, col2 = st.columns(2)
    with col1:
        mean = st.slider("Average delivery time (minutes)", 20, 60, 40)
    with col2:
        std_dev = st.slider("Standard deviation (minutes)", 1, 20, 10)
    
    x = np.linspace(0, 80, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Delivery Time Distribution', line=dict(color='royalblue', width=3)))
    
    # Add vertical lines for standard deviations
    colors = ['red', 'green', 'orange']
    labels = ['68%', '95%', '99.7%']
    for i in range(1, 4):
        fig.add_vrect(x0=mean - i*std_dev, x1=mean + i*std_dev, 
                      fillcolor=colors[i-1], opacity=0.1, layer="below", line_width=0)
        fig.add_annotation(x=mean, y=max(y)*(1.05-0.1*i),
                           text=f"{labels[i-1]} within {mean-i*std_dev:.0f}-{mean+i*std_dev:.0f} min",
                           showarrow=False, font=dict(color=colors[i-1]))

    fig.add_vline(x=mean, line_dash="solid", line_color="black", annotation_text="Mean")
    
    fig.update_layout(
        title=f"Food Delivery Time Distribution (Mean={mean} min, SD={std_dev} min)",
        xaxis_title="Delivery Time (minutes)",
        yaxis_title="Probability Density",
        xaxis_range=[0, 80],
        showlegend=False,
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### Understanding the Graph
    
    This graph shows how likely different delivery times are for our food delivery service.
    
    - The peak of the curve is at the average (mean) delivery time.
    - The spread of the curve is determined by the standard deviation.
    - The colored areas show the ranges where most deliveries fall:
        - Red: About 68% of deliveries (within 1 standard deviation)
        - Green: About 95% of deliveries (within 2 standard deviations)
        - Orange: About 99.7% of deliveries (within 3 standard deviations)
    
    This pattern is known as the **Empirical Rule** or the **68-95-99.7 Rule**.
    """)

def probability_calculator():
    st.header("Delivery Time Probability Calculator")
    
    mean = st.number_input("Average delivery time (minutes)", value=40, min_value=1, max_value=120)
    std_dev = st.number_input("Standard deviation (minutes)", value=10, min_value=1, max_value=60)
    
    st.subheader("Calculate probability of delivery within a time range")
    col1, col2 = st.columns(2)
    with col1:
        lower = st.number_input("Minimum time (minutes)", value=30, min_value=0, max_value=int(mean*2))
    with col2:
        upper = st.number_input("Maximum time (minutes)", value=50, min_value=int(lower), max_value=int(mean*2))
    
    prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(lower, mean, std_dev)
    
    st.write(f"The probability of a delivery taking between {lower} and {upper} minutes is: {prob:.2%}")
    
    st.markdown("""
    ### How it's calculated:
    
    1. We use the cumulative distribution function (CDF) of the normal distribution.
    2. Calculate: P(lower < X < upper) = CDF(upper) - CDF(lower)
    3. The result gives us the area under the curve between the two time points.
    
    This is a powerful way to estimate delivery times and set customer expectations!
    """)

def quiz():
    st.header("Food Delivery Time Quiz")
    
    questions = [
        {
            "question": "If the mean delivery time is 40 minutes and the standard deviation is 10 minutes, approximately what percentage of deliveries will take between 30 and 50 minutes?",
            "options": ["50%", "68%", "95%", "99.7%"],
            "correct": 1,
            "explanation": "According to the Empirical Rule, about 68% of the data falls within one standard deviation of the mean. Here, one standard deviation is 10 minutes, so 68% of deliveries should take between 30 and 50 minutes."
        },
        {
            "question": "Using the same mean (40 minutes) and standard deviation (10 minutes), what is the approximate range for 95% of the deliveries?",
            "options": ["20-60 minutes", "30-50 minutes", "10-70 minutes", "35-45 minutes"],
            "correct": 0,
            "explanation": "The Empirical Rule states that about 95% of the data falls within two standard deviations of the mean. Two standard deviations is 2 * 10 = 20 minutes. So the range is 40 ± 20 minutes, which is 20-60 minutes."
        },
        {
            "question": "What does it mean if a delivery time is more than 3 standard deviations away from the mean?",
            "options": ["It's a typical delivery", "It's a somewhat unusual delivery", "It's a very rare delivery", "It's impossible"],
            "correct": 2,
            "explanation": "According to the Empirical Rule, 99.7% of the data falls within 3 standard deviations of the mean. So a delivery time more than 3 standard deviations away is in the remaining 0.3%, making it a very rare occurrence."
        }
    ]
    
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer {i+1}"):
            if q["options"].index(answer) == q["correct"]:
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect. Try again!")
            st.write(f"Explanation: {q['explanation']}")

if __name__ == "__main__":
    main()