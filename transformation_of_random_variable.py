import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

st.set_page_config(layout="wide", page_title="Transformations of Random Variables", page_icon="🔄")

st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stApp {
        background-color: #F5F5F5;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #3498DB;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔄 Transformations of Random Variables")

tab1, tab2, tab3, tab4 = st.tabs(["Linear", "Quadratic", "Exponential", "Logarithmic"])

def plot_transformation(x, y_original, y_transformed, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_original, mode='lines', name='Original', line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=x, y=y_transformed, mode='lines', name='Transformed', line=dict(color='firebrick')))
    fig.update_layout(title=title, xaxis_title="Value", yaxis_title="Probability Density", height=400)
    return fig

with tab1:
    st.header("Linear Transformation: Y = aX + b")
    col1, col2 = st.columns([1, 2])
    with col1:
        mu = st.slider("Mean (μ) of X:", -5.0, 5.0, 0.0, 0.1, key='linear_mu')
        sigma = st.slider("Std Dev (σ) of X:", 0.1, 5.0, 1.0, 0.1, key='linear_sigma')
        a = st.slider("Coefficient (a):", -5.0, 5.0, 1.0, 0.1, key='linear_a')
        b = st.slider("Constant (b):", -5.0, 5.0, 0.0, 0.1, key='linear_b')
        
        new_mu = a * mu + b
        new_sigma = abs(a) * sigma
        st.write(f"New Distribution: Y ~ N({new_mu:.2f}, {new_sigma**2:.2f})")
    
    with col2:
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        y_original = stats.norm.pdf(x, mu, sigma)
        y_transformed = stats.norm.pdf((x - b) / a, mu, sigma) / abs(a)
        fig = plot_transformation(x, y_original, y_transformed, "Linear Transformation")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Quadratic Transformation: Y = X²")
    col1, col2 = st.columns([1, 2])
    with col1:
        mu = st.slider("Mean (μ) of X:", -5.0, 5.0, 0.0, 0.1, key='quad_mu')
        sigma = st.slider("Std Dev (σ) of X:", 0.1, 5.0, 1.0, 0.1, key='quad_sigma')
        
        new_mu = mu**2 + sigma**2
        new_var = 2*sigma**2 * (2*mu**2 + sigma**2)
        st.write(f"E[Y] = {new_mu:.2f}")
        st.write(f"Var(Y) = {new_var:.2f}")
    
    with col2:
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        y_original = stats.norm.pdf(x, mu, sigma)
        y_transformed = stats.chi2.pdf(x**2, df=1)
        fig = plot_transformation(x, y_original, y_transformed, "Quadratic Transformation")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Exponential Transformation: Y = e^X")
    col1, col2 = st.columns([1, 2])
    with col1:
        mu = st.slider("Mean (μ) of X:", -2.0, 2.0, 0.0, 0.1, key='exp_mu')
        sigma = st.slider("Std Dev (σ) of X:", 0.1, 2.0, 1.0, 0.1, key='exp_sigma')
        
        new_mu = np.exp(mu + sigma**2/2)
        new_var = (np.exp(sigma**2) - 1) * np.exp(2*mu + sigma**2)
        st.write(f"E[Y] = {new_mu:.2f}")
        st.write(f"Var(Y) = {new_var:.2f}")
    
    with col2:
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        y_original = stats.norm.pdf(x, mu, sigma)
        y_transformed = stats.lognorm.pdf(np.exp(x), s=sigma, scale=np.exp(mu))
        fig = plot_transformation(x, y_original, y_transformed, "Exponential Transformation")
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Logarithmic Transformation: Y = ln(X)")
    col1, col2 = st.columns([1, 2])
    with col1:
        mu = st.slider("Mean (μ) of ln(X):", -2.0, 2.0, 0.0, 0.1, key='log_mu')
        sigma = st.slider("Std Dev (σ) of ln(X):", 0.1, 2.0, 1.0, 0.1, key='log_sigma')
        st.write("Original: X ~ Log-normal(μ, σ²)")
        st.write(f"Transformed: Y ~ N({mu:.2f}, {sigma**2:.2f})")
    
    with col2:
        x = np.linspace(0, np.exp(mu + 4*sigma), 1000)
        y_original = stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu))
        y_transformed = stats.norm.pdf(np.log(x), mu, sigma)
        fig = plot_transformation(x, y_original, y_transformed, "Logarithmic Transformation")
        st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### Key Points:
- Linear transformation shifts and scales the distribution
- Quadratic transformation often results in a right-skewed distribution
- Exponential transformation can dramatically change the shape, often resulting in a highly skewed distribution
- Logarithmic transformation can compress the scale and is often used to handle right-skewed data
""")