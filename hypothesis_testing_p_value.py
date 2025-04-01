import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
import pandas as pd

# Configure app
st.set_page_config(page_title="Understanding P-Values with Bell Curves", layout="wide")

# Create a simple title
st.title("Understanding P-Values")

# Sidebar controls
with st.sidebar:
    st.header("Experiment Settings")
    total_heads = st.slider("Number of heads", 0, 1000, 500)  # Add this line
    total_flips = st.slider("Number of flips", 10, 100000, 1000)
    
    # Validate heads cannot exceed flips
    if total_heads > total_flips:
        total_heads = total_flips
        st.warning("Number of heads cannot exceed number of flips")
    
    true_heads = (total_heads / total_flips) * 100  # Calculate true probability
    st.metric("True probability of heads", f"{true_heads:.1f}%")
    
    show_p_value = st.checkbox("Show p-value region", True)
    significance = st.selectbox("Significance level (α)", [0.01, 0.05, 0.10], 1)
    st.markdown("---")
    st.subheader("Error Visualization")
    show_errors = st.checkbox("Show Type I & II Errors", False)
    if show_errors:
        true_mean = st.slider("Alternative Hypothesis Mean", -2.0, 2.0, 1.5, 0.1)

# Calculate statistics
observed_prop = total_heads / total_flips
expected_prop = 0.5
std_error = np.sqrt(expected_prop * (1-expected_prop) / total_flips)
z_score = (observed_prop - expected_prop) / std_error
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

# Display results in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Heads Count", f"{total_heads:,}/{total_flips:,}")
with col2:
    st.metric("Observed Proportion", f"{observed_prop:.4f}")
with col3:
    if p_value < significance:
        # Red color for rejection with consistent font size
        st.markdown(f"""
        <div style='text-align: left;'>
            <div style='font-size: 1rem; color: rgb(150, 150, 150); font-family: "Source Sans Pro", sans-serif;'>P-value</div>
            <div style='font-size: 1.8rem; font-weight: 600; font-family: "Source Sans Pro", sans-serif;'>{p_value:.6f}</div>
            <div style='color: rgb(255, 43, 43); font-size: 1rem; font-family: "Source Sans Pro", sans-serif;'>Reject H₀: Coin is Biased</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Default blue color for acceptance
        st.metric("P-value", f"{p_value:.6f}", 
                 delta="Accept H₀: Coin is Fair")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📊 Visualization", "📘 Explanation", "📑 Reference Table"])

with tab1:
    # Visualization tab content
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)

    fig = go.Figure()
    
    # Add main bell curve
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution', 
                            line=dict(color='blue', width=2)))
    
    # Add z-score lines
    fig.add_trace(go.Scatter(x=[z_score, z_score], y=[0, stats.norm.pdf(z_score)], 
                            mode='lines', name='Observed Z-score', 
                            line=dict(color='red', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=[-z_score, -z_score], y=[0, stats.norm.pdf(-z_score)], 
                            mode='lines', showlegend=False, 
                            line=dict(color='red', width=2, dash='dash')))

    # Initialize annotations list at the start
    annotations = []

    # Show regions if enabled
    if show_p_value:
        critical_z = stats.norm.ppf(1 - significance/2)
        
        # Fair coin region (center)
        x_center = np.linspace(-critical_z, critical_z, 100)
        y_center = stats.norm.pdf(x_center)
        fig.add_trace(go.Scatter(x=np.concatenate([x_center, [x_center[-1], x_center[0]]]),
                                y=np.concatenate([y_center, [0, 0]]),
                                fill="toself", fillcolor="rgba(0,255,0,0.1)",
                                line=dict(color="rgba(0,255,0,0)"),
                                name="Accept: Coin is Fair",
                                hoverinfo="skip"))
        
        # Biased coin regions (tails)
        x_right = np.linspace(critical_z, 4, 100)
        y_right = stats.norm.pdf(x_right)
        fig.add_trace(go.Scatter(x=np.concatenate([x_right, [x_right[-1], x_right[0]]]),
                                y=np.concatenate([y_right, [0, 0]]),
                                fill="toself", fillcolor="rgba(255,0,0,0.2)",
                                line=dict(color="rgba(255,0,0,0)"),
                                name="Reject: Coin is Biased",
                                hoverinfo="skip"))
        
        x_left = np.linspace(-4, -critical_z, 100)
        y_left = stats.norm.pdf(x_left)
        fig.add_trace(go.Scatter(x=np.concatenate([x_left, [x_left[-1], x_left[0]]]),
                                y=np.concatenate([y_left, [0, 0]]),
                                fill="toself", fillcolor="rgba(255,0,0,0.2)",
                                line=dict(color="rgba(255,0,0,0)"),
                                showlegend=False,
                                hoverinfo="skip"))

    if show_errors and show_p_value:
        critical_z = stats.norm.ppf(1 - significance/2)
        
        # Add null distribution (fair coin)
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', 
                                name='Fair Coin Distribution (H₀)', 
                                line=dict(color='blue', width=2)))
        
        # Add alternative distribution (biased coin)
        x_alt = np.linspace(-4, 4, 1000)
        y_alt = stats.norm.pdf(x_alt, loc=true_mean)
        fig.add_trace(go.Scatter(x=x_alt, y=y_alt, mode='lines', 
                                name='Biased Coin Distribution (H₁)',
                                line=dict(color='purple', width=2)))

        # Type I Error region (red) - Area under H₀ in rejection region
        x_type1_regions = [np.linspace(-4, -critical_z, 100), 
                          np.linspace(critical_z, 4, 100)]
        y_type1_regions = [stats.norm.pdf(x) for x in x_type1_regions]
        
        for i, (x_region, y_region) in enumerate(zip(x_type1_regions, y_type1_regions)):
            fig.add_trace(go.Scatter(x=x_region, y=y_region,
                                   fill='tozeroy',
                                   fillcolor='rgba(255,0,0,0.2)',  # Light red for Type I
                                   name='Type I Error (α)',
                                   mode='none',
                                   showlegend=True if i == 0 else False))

        # Type II Error region (blue) - Area under H₁ in acceptance region
        x_type2 = np.linspace(-critical_z, critical_z, 100)
        y_type2 = stats.norm.pdf(x_type2, loc=true_mean)
        fig.add_trace(go.Scatter(x=x_type2, y=y_type2,
                                fill='tozeroy',
                                fillcolor='rgba(0,0,255,0.2)',  # Light blue for Type II
                                name='Type II Error (β)',
                                mode='none'))

        # Calculate optimal annotation positions
        type1_height = stats.norm.pdf(critical_z) / 2  # Half height of distribution at critical value
        type2_height = stats.norm.pdf(0, loc=true_mean)  # Peak of alternative distribution
        
        # Calculate Type II error probability (β)
        beta = stats.norm.cdf(critical_z, loc=true_mean) - stats.norm.cdf(-critical_z, loc=true_mean)

        # Dynamic annotations for Type I and II errors
        annotations.extend([
            dict(
                x=critical_z + 0.5,  # Slightly right of critical value
                y=type1_height,
                text=(f"Type I Error (α)<br>"
                      f"P(Reject H₀|H₀ True) = {significance:.2%}<br>"
                      "Wrongly concluding bias<br>"
                      "when coin is fair"),
                showarrow=True,
                arrowhead=1,
                ax=40,
                ay=-20,
                font=dict(size=12),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='rgba(255,0,0,0.5)',  # Red border
                borderwidth=2
            ),
            dict(
                x=true_mean,  # Center of alternative distribution
                y=type2_height * 1.2,  # Slightly above peak
                text=(f"Type II Error (β)<br>"
                      f"P(Accept H₀|H₁ True) = {beta:.2%}<br>"
                      "Missing a biased coin"),
                showarrow=True,
                arrowhead=1,
                ax=-40,
                ay=-40,
                font=dict(size=12),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='rgba(0,0,255,0.5)',  # Blue border
                borderwidth=2
            )
        ])

        # Calculate and display power with more detail
        power = 1 - beta
        st.sidebar.markdown("---")
        st.sidebar.metric(
            "Detection Power (1-β)",
            f"{power:.3f}",
            delta=f"β = {beta:.3f}",
            delta_color="inverse"
        )

    # Update layout with all annotations
    fig.update_layout(
        title={
            'text': "Hypothesis Testing Errors Visualization" if show_errors 
                   else "Visualizing P-Value and Decision Regions",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Z-Score (Standard Deviations from Mean)",
        yaxis_title="Probability Density",
        hovermode="x unified",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        annotations=annotations
    )

    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Explanation tab content
    st.header("Relationship between Z-score and P-value")
    
    st.write("""
    The z-score and p-value are closely related in hypothesis testing:

    - **Z-score**: Measures how many standard deviations an observation is from the mean.
      
    General z-score formula: """)
    
    # Add simplified z-score formula first
    st.latex(r"Z = \frac{x - \mu}{\sigma}")
    
    st.write("""
    where:
    - $x$ is the observed value
    - $\mu$ is the population mean
    - $\sigma$ is the standard deviation
    
    For our coin toss experiment, this becomes: """)
    
    # Add specific formula for coin toss
    st.latex(r"Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}")
    
    st.write("""
    where:
    - $\hat{p}$ is the observed proportion (x)
    - $p_0$ is the expected proportion (μ = 0.5)
    - $\sqrt{\frac{p_0(1-p_0)}{n}}$ is the standard deviation (σ)
    - $n$ is the number of trials
    
    - **P-value**: The probability of obtaining test results at least as extreme as the observed results, assuming the null hypothesis is true.
    """)

    st.write("""
    **Interpreting the results:**

    - If p-value < significance level (α): Reject H₀ (Conclude the coin is biased)
    - If p-value ≥ significance level (α): Accept H₀ (Conclude the coin is fair)

    In this experiment:
    """)

    st.markdown(f"""
    - Observed z-score: {z_score:.4f}
    - Calculated p-value: {p_value:.6f}
    - Significance level (α): {significance}
    - Conclusion: {"Reject H₀: Coin is Biased" if p_value < significance else "Accept H₀: Coin is Fair"}
    """)

with tab3:
    # Reference table tab content
    st.header("Z-score to P-value Reference")
    z_scores = [0, 1, 1.96, 2, 2.58, 3]
    p_values = [2 * (1 - stats.norm.cdf(abs(z))) for z in z_scores]
    relationship_df = pd.DataFrame({
        'Z-score': z_scores,
        'P-value': p_values,
        'Decision (α=0.05)': ['Accept H₀: Coin is Fair' if p >= 0.05 else 'Reject H₀: Coin is Biased' for p in p_values],
        'Interpretation': ['Evidence suggests coin is fair' if p >= 0.05 else 'Evidence suggests coin is biased' for p in p_values]
    })
    relationship_df['P-value'] = relationship_df['P-value'].apply(lambda x: f"{x:.4f}")
    st.table(relationship_df)
