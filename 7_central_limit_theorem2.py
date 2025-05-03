import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

def clt_dice(sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        rolls = np.random.randint(1, 7, sample_size)  # Simulate dice rolls
        sample_means.append(np.mean(rolls))
    return sample_means

# Streamlit UI with custom styling
st.markdown("""
<style>
    .main-header {
        color: #FF5733;
        text-align: center;
    }
    .explanation {
        background-color: #F0F8FF;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .math-box {
        background-color: #E6F9E6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .highlight {
        color: #9C27B0;
        font-weight: bold;
    }
    .note {
        font-size: 0.9em;
        font-style: italic;
        color: #555;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Central Limit Theorem Dice Simulator 🎲</h1>", unsafe_allow_html=True)

# Explanation of CLT
with st.expander("What is the Central Limit Theorem?", expanded=True):
    st.markdown("""
    <div class='explanation'>
    <p>The <span class='highlight'>Central Limit Theorem (CLT)</span> is one of the most important principles in statistics. It states that when independent random variables are added together, their properly normalized sum tends toward a normal distribution, regardless of the original distribution's shape.</p>
    
    <p>Why is this important? The CLT allows us to:</p>
    <ul>
        <li>Make reliable statistical inferences about populations without knowing their true distributions</li>
        <li>Calculate confidence intervals for sample means</li>
        <li>Perform hypothesis tests on sample data</li>
        <li>Understand why the normal distribution appears so frequently in nature</li>
    </ul>
    
    <p>In this simulation, we're using dice rolls (which have a uniform distribution) to demonstrate how their sample means approach a normal distribution as sample size increases.</p>
    </div>
    """, unsafe_allow_html=True)

# Mathematical explanation
with st.expander("Mathematical Calculations", expanded=False):
    st.markdown("""
    <div class='math-box'>
    <h4>For a single die (uniform distribution):</h4>
    <ul>
        <li>Mean (μ) = (1+2+3+4+5+6)/6 = 3.5</li>
        <li>Variance (σ²) = ((1-3.5)²+(2-3.5)²+(3-3.5)²+(4-3.5)²+(5-3.5)²+(6-3.5)²)/6 = 2.917</li>
        <li>Standard Deviation (σ) = √2.917 ≈ 1.708</li>
    </ul>
    
    <h4>For the sample mean distribution:</h4>
    <ul>
        <li>Mean of sample means (μₓ) = μ = 3.5</li>
        <li>Variance of sample means (σₓ²) = σ²/n = 2.917/n</li>
        <li>Standard Deviation of sample means (σₓ) = σ/√n = 1.708/√n</li>
    </ul>
    
    <h4>95% Confidence Interval Calculation:</h4>
    <ul>
        <li>For 95% confidence, we use z = 1.96 (from the standard normal distribution)</li>
        <li>CI = Mean ± (z × SE), where SE = σ/√n</li>
        <li>CI = Mean ± (1.96 × σ/√n)</li>
        <li>For dice: CI = x̄ ± (1.96 × 1.708/√n)</li>
    </ul>
    
    <p>As n increases, the distribution of sample means approaches N(3.5, 1.708²/n)</p>
    </div>
    """, unsafe_allow_html=True)

# Interactive controls with colorful layout
st.markdown("<h3 style='color:#4CAF50;'>Simulation Parameters</h3>", unsafe_allow_html=True)

col_params1, col_params2 = st.columns(2)
with col_params1:
    sample_size = st.slider("Sample size (n)", 1, 1000, 5, 
                           help="Number of dice rolls in each sample")
    st.markdown("<p class='note'>Sample size = number of observations/trials in each sample.<br>As sample size increases, the distribution becomes more normal and narrower.</p>", unsafe_allow_html=True)
with col_params2:
    samples = st.slider("Number of samples", 10, 5000, 1000,
                       help="Number of samples to generate")
    st.markdown("<p class='note'>Number of samples = how many different samples we collect.<br>As number of samples increases, our estimate of the sampling distribution becomes more accurate.</p>", unsafe_allow_html=True)

show_options = st.columns(3)
with show_options[0]:
    show_normal = st.checkbox("Show normal curve", True)
with show_options[1]:
    show_mean = st.checkbox("Show mean line", True)
with show_options[2]:
    show_confidence = st.checkbox("Show 95% confidence interval", True)

# Simulation
means = clt_dice(sample_size, samples)

# Calculate statistics
mean_of_means = np.mean(means)
std_of_means = np.std(means)
theoretical_std = 1.708/np.sqrt(sample_size)
confidence_interval = (mean_of_means - 1.96*std_of_means, mean_of_means + 1.96*std_of_means)
theoretical_ci = (3.5 - 1.96*theoretical_std, 3.5 + 1.96*theoretical_std)

# Display statistics
st.markdown(f"""
<div style='background-color:#FFF3E0; padding:15px; border-radius:10px; margin-bottom:20px;'>
    <h3 style='color:#E65100;'>Calculated Statistics</h3>
    <table style='width:100%'>
        <tr>
            <td><b>Theoretical Mean:</b></td>
            <td>3.5</td>
            <td><b>Observed Mean:</b></td>
            <td>{mean_of_means:.4f}</td>
        </tr>
        <tr>
            <td><b>Theoretical Std:</b></td>
            <td>{theoretical_std:.4f}</td>
            <td><b>Observed Std:</b></td>
            <td>{std_of_means:.4f}</td>
        </tr>
        <tr>
            <td><b>Theoretical 95% CI:</b></td>
            <td colspan='3'>({theoretical_ci[0]:.4f}, {theoretical_ci[1]:.4f}) = 3.5 ± {1.96*theoretical_std:.4f}</td>
        </tr>
        <tr>
            <td><b>Observed 95% CI:</b></td>
            <td colspan='3'>({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f}) = {mean_of_means:.4f} ± {1.96*std_of_means:.4f}</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# Visualizations
col1, col2 = st.columns(2)

# Single die distribution
with col1:
    st.markdown("<h3 style='color:#2196F3;'>Single Die Distribution</h3>", unsafe_allow_html=True)
    
    # Use the number of samples parameter to determine how many dice to show
    display_rolls = min(samples, 1000)  # Cap at 1000 for performance
    single_die = np.random.randint(1, 7, display_rolls)
    
    fig1 = px.histogram(
        single_die, 
        title=f"Uniform Distribution (Single Die, {display_rolls} rolls)",
        labels={'value': 'Face Value', 'count': 'Frequency'},
        color_discrete_sequence=['#2196F3'],
        opacity=0.8,
        nbins=6
    )
    fig1.update_layout(
        bargap=0.1,
        title_font_size=18,
        plot_bgcolor='rgba(240,240,240,0.8)'
    )
    st.plotly_chart(fig1, use_container_width=True)

# Sample means distribution
with col2:
    st.markdown("<h3 style='color:#FF5722;'>Sample Means Distribution</h3>", unsafe_allow_html=True)
    fig2 = px.histogram(
        means, 
        title=f"Sample Means Distribution (n={sample_size})",
        labels={'value': 'Sample Mean', 'count': 'Frequency'},
        nbins=30,
        histnorm='probability density' if show_normal else None,
        color_discrete_sequence=['#FF5722'],
        opacity=0.7
    )
    
    # Fix x axis to not change dynamically
    fig2.update_layout(xaxis_range=[1, 6])
    
    # Add normal curve overlay
    if show_normal:
        x = np.linspace(1, 6, 100)
        y = stats.norm.pdf(x, mean_of_means, std_of_means)
        fig2.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            name='Normal Distribution',
            line=dict(color='#9C27B0', width=3)
        ))
    
    # Add mean line
    if show_mean:
        fig2.add_vline(
            x=mean_of_means, 
            line_color="#4CAF50",
            line_width=2,
            line_dash="solid",
            annotation_text="Sample Mean",
            annotation_position="top"
        )
        
        # Also add theoretical mean
        fig2.add_vline(
            x=3.5, 
            line_color="#FFC107",
            line_width=2,
            line_dash="dash",
            annotation_text="Theoretical Mean (3.5)",
            annotation_position="bottom"
        )
    
    # Add confidence interval
    if show_confidence:
        fig2.add_vrect(
            x0=confidence_interval[0],
            x1=confidence_interval[1],
            fillcolor="#E91E63",
            opacity=0.2,
            layer="below",
            line_width=0,
            annotation_text="95% CI",
            annotation_position="top"
        )
    
    fig2.update_layout(
        title_font_size=18,
        plot_bgcolor='rgba(240,240,240,0.8)'
    )
    st.plotly_chart(fig2, use_container_width=True)

# Visual demonstration of convergence
st.markdown("<h3 style='color:#673AB7; text-align:center;'>CLT Convergence Demonstration</h3>", unsafe_allow_html=True)

# Create multiple distributions with increasing sample sizes
sample_sizes = [1, 2, 5, 10, 30, 100]
convergence_data = {}

for n in sample_sizes:
    convergence_data[n] = clt_dice(n, 1000)

# Create a figure with subplots
fig3 = plt.figure(figsize=(12, 8))
fig3.patch.set_facecolor('#f0f0f0')

for i, n in enumerate(sample_sizes, 1):
    ax = fig3.add_subplot(2, 3, i)
    ax.hist(convergence_data[n], bins=30, density=True, alpha=0.7, color=plt.cm.viridis(i/len(sample_sizes)))
    
    # Add normal curve
    x = np.linspace(min(convergence_data[n]), max(convergence_data[n]), 100)
    y = stats.norm.pdf(x, 3.5, 1.708/np.sqrt(n))
    ax.plot(x, y, 'r-', linewidth=2)
    
    ax.set_title(f'n = {n}', fontsize=14, fontweight='bold')
    ax.axvline(x=3.5, color='green', linestyle='--', alpha=0.8)
    ax.set_xlim(1, 6)
    
    # Annotate standard deviation
    std_text = f'σ = {(1.708/np.sqrt(n)):.3f}'
    ax.annotate(std_text, xy=(0.05, 0.95), xycoords='axes fraction', 
                fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="b", alpha=0.8))

plt.tight_layout()
st.pyplot(fig3)

st.markdown("""
<div style='background-color:#E1F5FE; padding:15px; border-radius:10px; text-align:center; margin-top:20px;'>
    <h3 style='color:#0288D1;'>Key Observations</h3>
    <p>As the sample size increases:</p>
    <ul style='display:inline-block; text-align:left;'>
        <li>The distribution of sample means becomes more normal (bell-shaped)</li>
        <li>The spread (standard deviation) of sample means decreases proportionally to √n</li>
        <li>The mean stabilizes around the theoretical value (3.5)</li>
    </ul>
    <p style='font-style:italic; margin-top:10px;'>Try different sample sizes to observe the Central Limit Theorem in action!</p>
</div>
""", unsafe_allow_html=True)

# Add a section to demonstrate the effect of number of samples
st.markdown("<h3 style='color:#009688; text-align:center;'>Effect of Number of Samples on Distribution Accuracy</h3>", unsafe_allow_html=True)

# Allow user to set a constant sample size for this demonstration
constant_sample_size = st.slider("Fixed sample size for demonstration", 10, 100, 30, 
                               help="We'll keep this sample size constant while varying the number of samples")

# Create data with different numbers of samples
sample_counts = [10, 100, 500, 1000, 5000]
sample_count_data = {}
sample_count_statistics = {}

# Generate data for each sample count
for count in sample_counts:
    sample_count_data[count] = clt_dice(constant_sample_size, count)
    sample_count_statistics[count] = {
        'mean': np.mean(sample_count_data[count]),
        'std': np.std(sample_count_data[count])
    }

# Create a figure with subplots
fig4 = plt.figure(figsize=(15, 8))
fig4.patch.set_facecolor('#f0f0f0')

# Create the main grid of histograms
for i, count in enumerate(sample_counts, 1):
    ax = fig4.add_subplot(2, 3, i)
    ax.hist(sample_count_data[count], bins=30, density=True, alpha=0.7, 
            color=plt.cm.plasma(i/len(sample_counts)))
    
    # Add the true normal curve
    x = np.linspace(1, 6, 100)
    y = stats.norm.pdf(x, 3.5, 1.708/np.sqrt(constant_sample_size))
    ax.plot(x, y, 'r-', linewidth=2, label='Theoretical')
    
    # Add the observed normal curve
    y_observed = stats.norm.pdf(x, sample_count_statistics[count]['mean'], 
                               sample_count_statistics[count]['std'])
    ax.plot(x, y_observed, 'g--', linewidth=2, label='Observed')
    
    ax.set_title(f'Samples = {count}', fontsize=14, fontweight='bold')
    ax.axvline(x=3.5, color='black', linestyle='--', alpha=0.5)
    ax.set_xlim(1, 6)
    
    # Add statistics annotation
    stats_text = f"Mean: {sample_count_statistics[count]['mean']:.3f}\nStd: {sample_count_statistics[count]['std']:.3f}"
    ax.annotate(stats_text, xy=(0.05, 0.95), xycoords='axes fraction', 
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec="b", alpha=0.8))
    
    if i == 1:  # Only add legend to the first plot
        ax.legend(loc='upper right', framealpha=0.9)

# Add a summary plot showing how statistics converge
ax_summary = fig4.add_subplot(2, 3, 6)
sample_counts_extended = np.logspace(1, 4, 20).astype(int)  # From 10 to 10,000
means = []
stds = []
mean_errors = []
std_errors = []

# Generate data for convergence curves
for count in sample_counts_extended:
    # Generate just enough data for the statistics
    data = clt_dice(constant_sample_size, count)
    obs_mean = np.mean(data)
    obs_std = np.std(data)
    means.append(obs_mean)
    stds.append(obs_std)
    mean_errors.append(abs(obs_mean - 3.5))
    std_errors.append(abs(obs_std - 1.708/np.sqrt(constant_sample_size)))

# Plot the error convergence
ax_summary.loglog(sample_counts_extended, mean_errors, 'r-', label='Mean Error')
ax_summary.loglog(sample_counts_extended, std_errors, 'b-', label='Std Error')
ax_summary.set_title('Error vs Number of Samples', fontsize=14, fontweight='bold')
ax_summary.set_xlabel('Number of Samples (log scale)')
ax_summary.set_ylabel('Absolute Error (log scale)')
ax_summary.legend()
ax_summary.grid(True, which="both", ls="-", alpha=0.2)

plt.tight_layout()
st.pyplot(fig4)

# Add explanation about the number of samples effect
st.markdown("""
<div style='background-color:#E8F5E9; padding:15px; border-radius:10px; text-align:center; margin-top:20px;'>
    <h3 style='color:#2E7D32;'>How Number of Samples Affects Accuracy</h3>
    <p>As the number of samples increases:</p>
    <ul style='display:inline-block; text-align:left;'>
        <li><strong>The histogram becomes smoother</strong> - With few samples, the distribution appears jagged and irregular</li>
        <li><strong>The sample statistics converge to theoretical values</strong> - The observed mean and standard deviation become closer to their theoretical values</li>
        <li><strong>The error decreases proportionally to √n</strong> - The standard error of the mean decreases as we collect more samples</li>
        <li><strong>Extreme values are better represented</strong> - With more samples, we're more likely to observe the full range of possible values</li>
    </ul>
    <p style='font-style:italic; margin-top:10px;'>The error plot (bottom right) shows how quickly both mean and standard deviation errors decrease as we increase the number of samples.</p>
</div>
""", unsafe_allow_html=True)
