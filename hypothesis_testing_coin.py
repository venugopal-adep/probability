import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.stats import binom

def calculate_p_value(heads):
    return 2 * min(binom.cdf(heads, 10, 0.5), 1 - binom.cdf(heads-1, 10, 0.5))

# Interface setup
st.set_page_config(layout="wide")
st.title("🎲 Coin Fairness Analyzer")

with st.sidebar:
    st.header("Settings")
    alpha = st.selectbox("Significance Level (α):", 
                        [0.10, 0.05, 0.01],
                        help="Probability threshold for rejecting null hypothesis")

# Calculate critical values
x = np.arange(0, 11)
pmf = binom.pmf(x, 10, 0.5)

# Find critical values
critical_low = binom.ppf(alpha/2, 10, 0.5)
critical_high = binom.ppf(1-alpha/2, 10, 0.5)

# Calculate p-values for each possible outcome
p_values = [calculate_p_value(h) for h in x]

# Create figure
fig = go.Figure()

# Add main probability bars with hover text
fig.add_trace(go.Bar(
    x=x,
    y=pmf,
    name='Probability',
    marker_color=['red' if (k <= critical_low or k >= critical_high) else 'blue' for k in x],
    hovertemplate=(
        "<b>Number of Heads</b>: %{x}\n" +
        "<b>Probability</b>: %{y:.4f}\n" +
        "<b>p-value</b>: %{customdata:.4f}\n" +
        "<b>α/2</b>: " + f"{alpha/2:.4f}" + "\n" +
        "<b>Decision Rule</b>: " + 
        f"Reject H₀ if p-value < {alpha/2:.4f}\n" +
        "<extra></extra>"
    )

# Add regions
fig.add_shape(
    type="rect",
    x0=-0.5,
    x1=critical_low,
    y0=0,
    y1=max(pmf)*1.1,
    fillcolor="rgba(255,0,0,0.1)",
    line_width=0,
    layer="below"
)

fig.add_shape(
    type="rect",
    x0=critical_high,
    x1=10.5,
    y0=0,
    y1=max(pmf)*1.1,
    fillcolor="rgba(255,0,0,0.1)",
    line_width=0,
    layer="below"
)

# Update layout
fig.update_layout(
    title=f"Binomial Distribution (n=10, p=0.5) with α={alpha}",
    xaxis_title="Number of Heads",
    yaxis_title="Probability",
    annotations=[
        dict(
            x=5,
            y=max(pmf)*1.15,
            text="Acceptance Region",
            showarrow=False,
            font=dict(size=14, color="blue")
        ),
        dict(
            x=1,
            y=max(pmf)*1.15,
            text="Rejection Region",
            showarrow=False,
            font=dict(size=14, color="red")
        ),
        dict(
            x=9,
            y=max(pmf)*1.15,
            text="Rejection Region",
            showarrow=False,
            font=dict(size=14, color="red")
        )
    ]
)

# Display results
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Test Results")
    st.write(f"**Significance Level (α):** {alpha}")
    st.write(f"**Critical Values:**")
    st.write(f"- Lower: ≤ {int(critical_low)} heads")
    st.write(f"- Upper: ≥ {int(critical_high)} heads")
    
    st.write("**Decision Rule:**")
    st.write("- Accept H₀ (fair coin) if heads are between "
             f"{int(critical_low+1)} and {int(critical_high-1)}")
    st.write("- Reject H₀ (biased coin) if heads ≤ "
             f"{int(critical_low)} or ≥ {int(critical_high)}")

with col2:
    st.plotly_chart(fig, use_container_width=True)

st.caption("""
**Interpretation:**  
- **Blue bars**: Acceptance region - Results consistent with a fair coin
- **Red bars**: Rejection regions - Results suggest the coin is biased
- **Shaded areas**: Visual representation of rejection regions
- **H₀**: Null hypothesis (coin is fair, p = 0.5)
- **H₁**: Alternative hypothesis (coin is biased, p ≠ 0.5)
""")

# After the plot, add explanations
st.write("---")
st.subheader("Statistical Concepts")

st.write("""
**P-value Explanation:**
- In this coin toss context, the p-value is the probability of observing results as extreme as or more extreme than the current number of heads, assuming the coin is fair (H₀ is true).
- If p-value < α, we reject the null hypothesis (conclude the coin is biased)
- If p-value ≥ α, we fail to reject the null hypothesis (insufficient evidence to conclude the coin is biased)

**Significance Level (α) Explanation:**
- α represents the probability of rejecting H₀ when it is actually true (Type I error)
- In this test:
  - α = {alpha} means we accept a {alpha*100}% chance of incorrectly concluding the coin is biased when it's actually fair
  - Lower α values (e.g., 0.01) are more conservative and require stronger evidence to conclude bias
  - Higher α values (e.g., 0.10) are more lenient in concluding bias
""")

# Update the Statistical Concepts section
st.write("""
**Two-Sided Test Explanation:**
- Since this is a two-sided test, we compare the p-value with α/2 (not α)
- If p-value < α/2, we reject the null hypothesis (conclude the coin is biased)
- If p-value ≥ α/2, we fail to reject the null hypothesis (insufficient evidence to conclude the coin is biased)
- Current α/2 = {:.4f}

**Why α/2?**
- We're testing for bias in both directions (too many or too few heads)
- The significance level α is split between both tails of the distribution
- Each tail gets α/2 of the total significance level
""".format(alpha/2))
 
