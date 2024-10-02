import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

# Set page configuration
st.set_page_config(layout="wide", page_title="Hypothesis Testing Explorer", page_icon="📊")

# Custom CSS
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #e0e0e0;
        border-radius: 4px;
        color: #1e1e1e;
        font-size: 18px;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50;
        color: white;
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Hypothesis Testing Explorer: An Interactive Journey")

# Create tabs for each topic
tabs = st.tabs(["Z-Test", "T-Test", "Chi-Square Test"])

# Z-Test
with tabs[0]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Z-Test")
        st.markdown("""
        A z-test is used when we know the population standard deviation. It's typically used for large sample sizes (n > 30).
        
        Null Hypothesis (H₀): The sample mean is equal to the population mean.
        Alternative Hypothesis (H₁): The sample mean is different from the population mean.
        """)
        population_mean = st.number_input("Population Mean", value=100.0)
        population_std = st.number_input("Population Standard Deviation", value=15.0, min_value=0.1)
        sample_size = st.number_input("Sample Size", value=50, min_value=1, step=1)
        sample_mean = st.number_input("Sample Mean", value=105.0)
        alpha = st.slider("Significance Level (α)", 0.01, 0.10, 0.05, 0.01)
    
    with col2:
        z_score = (sample_mean - population_mean) / (population_std / np.sqrt(sample_size))
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        
        x = np.linspace(-4, 4, 1000)
        y = stats.norm.pdf(x, 0, 1)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Standard Normal Distribution'))
        fig.add_trace(go.Scatter(x=[z_score, z_score], y=[0, stats.norm.pdf(z_score, 0, 1)], 
                                 mode='lines', name='Z-Score', line=dict(color='red', width=2)))
        
        fig.update_layout(title='Z-Test Visualization', xaxis_title='Z-Score', yaxis_title='Probability Density',
                          width=700, height=400, showlegend=True)
        st.plotly_chart(fig)
        
        st.markdown(f"**Z-Score:** {z_score:.4f}")
        st.markdown(f"**P-value:** {p_value:.4f}")
        if p_value < alpha:
            st.markdown("**Conclusion:** Reject the null hypothesis")
        else:
            st.markdown("**Conclusion:** Fail to reject the null hypothesis")

# T-Test
with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("T-Test")
        st.markdown("""
        A t-test is used when we don't know the population standard deviation, typically for smaller sample sizes.
        
        Null Hypothesis (H₀): The sample mean is equal to the hypothesized population mean.
        Alternative Hypothesis (H₁): The sample mean is different from the hypothesized population mean.
        """)
        hypothesized_mean = st.number_input("Hypothesized Population Mean", value=100.0)
        sample_data = st.text_input("Sample Data (comma-separated)", value="102,98,105,103,101,99,97,104,106,100")
        alpha_t = st.slider("Significance Level (α)", 0.01, 0.10, 0.05, 0.01, key='t_test_alpha')
    
    with col2:
        sample = np.array([float(x.strip()) for x in sample_data.split(',')])
        t_statistic, t_p_value = stats.ttest_1samp(sample, hypothesized_mean)
        
        df = len(sample) - 1
        x_t = np.linspace(-4, 4, 1000)
        y_t = stats.t.pdf(x_t, df)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_t, y=y_t, mode='lines', name=f't-distribution (df={df})'))
        fig.add_trace(go.Scatter(x=[t_statistic, t_statistic], y=[0, stats.t.pdf(t_statistic, df)], 
                                 mode='lines', name='t-statistic', line=dict(color='red', width=2)))
        
        fig.update_layout(title='T-Test Visualization', xaxis_title='t-value', yaxis_title='Probability Density',
                          width=700, height=400, showlegend=True)
        st.plotly_chart(fig)
        
        st.markdown(f"**T-Statistic:** {t_statistic:.4f}")
        st.markdown(f"**P-value:** {t_p_value:.4f}")
        if t_p_value < alpha_t:
            st.markdown("**Conclusion:** Reject the null hypothesis")
        else:
            st.markdown("**Conclusion:** Fail to reject the null hypothesis")

# Chi-Square Test
with tabs[2]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Chi-Square Test")
        st.markdown("""
        A chi-square test is used to determine if there is a significant association between two categorical variables.
        
        Null Hypothesis (H₀): There is no association between the variables.
        Alternative Hypothesis (H₁): There is an association between the variables.
        """)
        observed = st.text_area("Observed Frequencies (comma-separated rows)", value="30,40,30\n20,30,50")
        alpha_chi = st.slider("Significance Level (α)", 0.01, 0.10, 0.05, 0.01, key='chi_square_alpha')
    
    with col2:
        observed_array = np.array([list(map(int, row.split(','))) for row in observed.split('\n')])
        chi2, chi_p_value, dof, expected = stats.chi2_contingency(observed_array)
        
        x_chi = np.linspace(0, 20, 1000)
        y_chi = stats.chi2.pdf(x_chi, dof)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_chi, y=y_chi, mode='lines', name=f'Chi-Square Distribution (df={dof})'))
        fig.add_trace(go.Scatter(x=[chi2, chi2], y=[0, stats.chi2.pdf(chi2, dof)], 
                                 mode='lines', name='Chi-Square Statistic', line=dict(color='red', width=2)))
        
        fig.update_layout(title='Chi-Square Test Visualization', xaxis_title='Chi-Square Value', yaxis_title='Probability Density',
                          width=700, height=400, showlegend=True)
        st.plotly_chart(fig)
        
        st.markdown(f"**Chi-Square Statistic:** {chi2:.4f}")
        st.markdown(f"**P-value:** {chi_p_value:.4f}")
        if chi_p_value < alpha_chi:
            st.markdown("**Conclusion:** Reject the null hypothesis")
        else:
            st.markdown("**Conclusion:** Fail to reject the null hypothesis")
        
        st.subheader("Expected Frequencies:")
        st.write(expected)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by AI Educators | © 2024 Hypothesis Testing Explorer")