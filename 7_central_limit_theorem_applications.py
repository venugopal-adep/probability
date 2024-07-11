import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def set_page_config():
    st.set_page_config(page_title="CLT Applications", layout="wide")
    st.markdown("""
    <style>
    .big-font {font-size:30px !important; color: #0066cc; font-weight: bold;}
    .medium-font {font-size:24px !important; color: #009933;}
    .small-font {font-size:18px !important; color: #666666;}
    .info-box {background-color: #e6f2ff; padding: 15px; border-radius: 5px;}
    </style>
    """, unsafe_allow_html=True)

def intro():
    st.markdown('<p class="big-font">Applications of the Central Limit Theorem</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Discover how the CLT shapes our understanding of the world!</p>', unsafe_allow_html=True)
    st.markdown("<div class='info-box'>The Central Limit Theorem (CLT) states that the distribution of sample means approximates a normal distribution as the sample size becomes larger, regardless of the population's distribution.</div>", unsafe_allow_html=True)

def quality_control():
    st.markdown('<p class="medium-font">Quality Control in Manufacturing</p>', unsafe_allow_html=True)
    st.write("Imagine you're running a potato chip factory. You want to ensure that each bag contains close to 100 grams of chips.")

    mean_weight = st.slider("Set the mean weight of chips per bag (grams):", 95.0, 105.0, 100.0, 0.1)
    std_dev = st.slider("Set the standard deviation of chip weights (grams):", 1.0, 5.0, 2.0, 0.1)

    population = np.random.normal(mean_weight, std_dev, 10000)
    
    sample_sizes = [10, 30, 100]
    fig = go.Figure()
    
    for size in sample_sizes:
        sample_means = [np.mean(np.random.choice(population, size=size)) for _ in range(1000)]
        fig.add_trace(go.Histogram(x=sample_means, name=f'Sample Size: {size}', opacity=0.7))

    fig.update_layout(title="Distribution of Sample Means for Different Sample Sizes",
                      xaxis_title="Sample Mean Weight (grams)", yaxis_title="Frequency")
    st.plotly_chart(fig)

    st.markdown('<div class="info-box">As the sample size increases, the distribution of sample means becomes more normal and tighter around the true population mean. This allows quality control managers to more accurately predict the average weight of chips in bags, ensuring consistent product quality.</div>', unsafe_allow_html=True)

def polling():
    st.markdown('<p class="medium-font">Political Polling and Surveys</p>', unsafe_allow_html=True)
    st.write("Let's simulate a political poll for an upcoming election between two candidates.")

    true_support = st.slider("Set the true support for Candidate A:", 0.0, 100.0, 52.0, 0.1) / 100
    sample_size = st.slider("Set the sample size for each poll:", 100, 2000, 500)

    polls = [np.mean(np.random.binomial(1, true_support, sample_size)) for _ in range(1000)]
    
    fig = px.histogram(polls, nbins=30, labels={'value': 'Estimated Support for Candidate A'})
    fig.update_layout(title=f"Distribution of Poll Results (Sample Size: {sample_size})")
    st.plotly_chart(fig)

    margin_of_error = 1.96 * np.sqrt(true_support * (1 - true_support) / sample_size)
    st.markdown(f'<div class="info-box">The margin of error for this poll is approximately ±{margin_of_error:.1%}. This means we can be 95% confident that the true population support lies within this range of our poll estimate. The CLT allows pollsters to make these precise predictions even when sampling only a small fraction of the population.</div>', unsafe_allow_html=True)

def financial_risk():
    st.markdown('<p class="medium-font">Financial Risk Assessment</p>', unsafe_allow_html=True)
    st.write("Let's model the daily returns of a stock portfolio.")

    mean_return = st.slider("Set the mean daily return (%):", -1.0, 1.0, 0.05, 0.01)
    std_dev = st.slider("Set the standard deviation of daily returns (%):", 0.1, 5.0, 1.0, 0.1)

    daily_returns = np.random.normal(mean_return, std_dev, 10000)
    
    holding_periods = [1, 10, 30, 100]
    fig = go.Figure()
    
    for period in holding_periods:
        period_returns = [np.mean(np.random.choice(daily_returns, size=period)) for _ in range(1000)]
        fig.add_trace(go.Histogram(x=period_returns, name=f'{period} Day Period', opacity=0.7))

    fig.update_layout(title="Distribution of Average Returns for Different Holding Periods",
                      xaxis_title="Average Return (%)", yaxis_title="Frequency")
    st.plotly_chart(fig)

    st.markdown('<div class="info-box">The CLT helps financial analysts understand how the risk (volatility) of returns changes over different time horizons. As the holding period increases, the distribution of average returns becomes more normal and less spread out, illustrating how longer-term investments tend to be less volatile.</div>', unsafe_allow_html=True)

def main():
    set_page_config()
    intro()
    
    tab1, tab2, tab3 = st.tabs(["Quality Control", "Political Polling", "Financial Risk"])
    
    with tab1:
        quality_control()
    with tab2:
        polling()
    with tab3:
        financial_risk()

if __name__ == "__main__":
    main()