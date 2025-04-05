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
    
    # Add a slider for true probability (for Type II error demonstration)
    st.subheader("Type II Error Simulation")
    true_p = st.slider("True Coin Probability:", 
                      min_value=0.0, 
                      max_value=1.0, 
                      value=0.7,
                      step=0.05,
                      help="Simulate a biased coin with this probability of heads")

# Calculate critical values
x = np.arange(0, 11)
pmf = binom.pmf(x, 10, 0.5)  # Distribution under H0 (p=0.5)
pmf_alt = binom.pmf(x, 10, true_p)  # Distribution under H1 (p=true_p)

# Find critical values
critical_low = binom.ppf(alpha/2, 10, 0.5)
critical_high = binom.ppf(1-alpha/2, 10, 0.5)

# Calculate p-values for each possible outcome
p_values = [calculate_p_value(h) for h in x]

# Create figure
fig = go.Figure()

# Add main probability bars with hover text (H0 distribution)
fig.add_trace(go.Bar(
    x=x,
    y=pmf,
    name='H₀: p=0.5 (Fair Coin)',
    marker_color=['red' if (k <= critical_low or k >= critical_high) else 'blue' for k in x],
    hovertemplate=(
        "<b>Number of Heads</b>: %{x}\n" +
        "<b>Probability</b>: %{y:.4f}\n" +
        "<b>p-value</b>: %{customdata:.4f}\n" +
        "<b>α/2</b>: " + f"{alpha/2:.4f}\n" +
        "<b>Decision Rule</b>: " + 
        f"Reject H₀ if p-value < {alpha/2:.4f}\n" +
        "<extra></extra>"
    ),
    customdata=p_values,
    opacity=0.7
))

# Add alternative hypothesis distribution (H1)
fig.add_trace(go.Bar(
    x=x,
    y=pmf_alt,
    name=f'H₁: p={true_p} (Biased Coin)',
    marker_color='rgba(255, 165, 0, 0.7)',
    hovertemplate=(
        "<b>Number of Heads</b>: %{x}\n" +
        "<b>Probability</b>: %{y:.4f}\n" +
        "<extra></extra>"
    ),
    opacity=0.7
))

# Add regions for Type I and Type II errors
# Type I error: Rejecting H0 when it's true (red areas under blue distribution)
type_I_prob = alpha  # By definition

# Type II error: Failing to reject H0 when it's false
# Calculate probability of outcomes in acceptance region under H1
type_II_region = [k for k in x if (k > critical_low and k < critical_high)]
type_II_prob = sum(binom.pmf(k, 10, true_p) for k in type_II_region)

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

# Add Type II error region (shaded area for acceptance region under alternative hypothesis)
fig.add_shape(
    type="rect",
    x0=critical_low,
    x1=critical_high,
    y0=0,
    y1=max(max(pmf), max(pmf_alt))*1.1,
    fillcolor="rgba(0,255,0,0.1)",
    line_width=0,
    layer="below"
)

# Update layout
fig.update_layout(
    title=f"Binomial Distribution (n=10) with α={alpha}",
    xaxis_title="Number of Heads",
    yaxis_title="Probability",
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    annotations=[
        dict(
            x=5,
            y=max(max(pmf), max(pmf_alt))*1.15,
            text="Acceptance Region",
            showarrow=False,
            font=dict(size=14, color="blue")
        ),
        dict(
            x=1,
            y=max(max(pmf), max(pmf_alt))*1.15,
            text="Rejection Region",
            showarrow=False,
            font=dict(size=14, color="red")
        ),
        dict(
            x=9,
            y=max(max(pmf), max(pmf_alt))*1.15,
            text="Rejection Region",
            showarrow=False,
            font=dict(size=14, color="red")
        ),
        # Type I error annotation
        dict(
            x=1,
            y=max(max(pmf), max(pmf_alt))*0.5,
            text=f"Type I Error<br>α = {type_I_prob:.4f}",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="red",
            font=dict(size=12, color="red")
        ),
        # Type II error annotation
        dict(
            x=5,
            y=max(max(pmf), max(pmf_alt))*0.5,
            text=f"Type II Error<br>β = {type_II_prob:.4f}",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="green",
            font=dict(size=12, color="green")
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
    
    st.write("**Error Probabilities:**")
    st.write(f"- Type I Error (α): {type_I_prob:.4f}")
    st.write(f"- Type II Error (β): {type_II_prob:.4f}")
    st.write(f"- Power (1-β): {1-type_II_prob:.4f}")

with col2:
    st.plotly_chart(fig, use_container_width=True)

st.caption("""
**Interpretation:**  
- **Blue bars**: H₀ distribution (fair coin, p=0.5)
- **Orange bars**: H₁ distribution (biased coin with selected probability)
- **Red shaded areas**: Rejection regions - Results suggest the coin is biased
- **Green shaded area**: Type II error region - Failing to detect a biased coin
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

# Add Type I and Type II error explanations
st.write("""
## Type I and Type II Errors

**Type I Error (False Positive):**
- Rejecting H₀ when it is actually true
- In our context: Concluding the coin is biased when it's actually fair
- Probability = α = {alpha}
- Controlled directly by setting the significance level

**Type II Error (False Negative):**
- Failing to reject H₀ when it is actually false
- In our context: Concluding the coin is fair when it's actually biased
- Probability = β = {:.4f} (for true p = {})
- Depends on:
  - Sample size (n)
  - Effect size (how far the true p is from 0.5)
  - Significance level (α)

**Statistical Power:**
- Probability of correctly rejecting H₀ when it is false
- Power = 1 - β = {:.4f}
- Higher power means better ability to detect a biased coin when it truly is biased
""".format(type_II_prob, true_p, 1-type_II_prob))

# Add an interactive example
st.write("---")
st.subheader("Interactive Example")

# Let user input their own coin toss results
user_heads = st.number_input("Enter number of heads observed (out of 10 tosses):", 
                            min_value=0, max_value=10, value=5)

# Calculate p-value for user input
user_p_value = calculate_p_value(user_heads)

# Determine test result
if user_p_value < alpha:
    result = "Reject H₀ (Evidence suggests the coin is biased)"
    result_color = "red"
else:
    result = "Fail to reject H₀ (Insufficient evidence to conclude the coin is biased)"
    result_color = "blue"

# Display results
st.write(f"**Number of Heads:** {user_heads}")
st.write(f"**P-value:** {user_p_value:.4f}")
st.write(f"**Significance Level (α):** {alpha}")
st.markdown(f"**Test Result:** <span style='color:{result_color}'>{result}</span>", unsafe_allow_html=True)

# Explain possible errors in the user's case
if user_p_value < alpha and true_p == 0.5:
    st.write("**Note:** If the coin is actually fair, this is a Type I error (false positive).")
elif user_p_value >= alpha and true_p != 0.5:
    st.write("**Note:** If the coin is actually biased, this is a Type II error (false negative).")
