import streamlit as st
import plotly.graph_objects as go
import numpy as np
import scipy.stats as stats

# Set page configuration
st.set_page_config(page_title="Hypothesis Testing Intro", layout="wide")

# Title
st.title("Introduction to Hypothesis Testing")

# Section 1: What is Hypothesis Testing?
st.header("What is Hypothesis Testing?")

st.markdown("""
Imagine you're a detective trying to solve a mystery. You have a hunch about who did it, but you need evidence to prove your suspicion is correct. **Hypothesis testing** in statistics works similarly. It's a method used to make decisions or draw conclusions about a larger group (called a **population**) based on information from a smaller part of that group (called a **sample**).

In simpler terms, hypothesis testing helps you answer questions like:
- **Is this new teaching method better than the old one?**
- **Does a new drug really lower blood pressure?**
- **Are people happier with the new product design?**
""")

# Section 2: Why is Hypothesis Testing Important?
st.header("Why is Hypothesis Testing Important?")

st.markdown("""
Hypothesis testing is crucial because it provides a systematic way to make informed decisions using data. Instead of relying on guesses or assumptions, you use statistical evidence to support or reject your ideas. This process helps ensure that conclusions are based on solid evidence rather than random chance.
""")

# Section 3: Basic Components of Hypothesis Testing
st.header("Basic Components of Hypothesis Testing")

st.markdown("""
1. **Hypotheses**: These are statements about the population. There are two main types:
   - **Null Hypothesis (H₀)**: This is the default assumption that there is no effect or no difference. It represents a statement of "no change" or "no association."
   - **Alternative Hypothesis (H₁ or Ha)**: This is what you want to prove. It suggests that there is an effect or a difference.

2. **Data Collection**: Gather information from a sample that represents the population you're interested in.

3. **Decision Making**: Use statistical methods to decide whether to reject the null hypothesis in favor of the alternative hypothesis or not.
""")

# Section 4: Interactive Example
st.header("Interactive Example: Testing a New Study Technique")

st.markdown("""
**Scenario:** Imagine you're a teacher who believes that a new study technique improves students' test scores.

- **Null Hypothesis (H₀):** The new study technique does not improve test scores. (The average test score remains the same.)
- **Alternative Hypothesis (H₁):** The new study technique improves test scores. (The average test score is higher.)
""")

# Create two columns: Inputs on the left, Plots on the right
input_col, plot_col = st.columns([1, 2])  # Adjust column widths as needed

with input_col:
    st.subheader("Simulate the Study")

    st.markdown("**Control Group (Traditional Method)**")
    control_mean = st.number_input(
        "Control Group Mean Score (μ₀)",
        value=75.0,            # Changed to float
        step=1.0,              # Changed to float
        format="%.1f",         # Display one decimal place
        key='control_mean'
    )
    control_std = st.number_input(
        "Control Group Std Dev (σ)",
        value=10.0,            # Changed to float
        step=0.1,              # Changed to float
        min_value=0.1,
        format="%.1f",
        key='control_std'
    )
    control_size = st.slider(
        "Control Group Size (n)",
        min_value=10,
        max_value=200,
        value=50,
        step=10,
        key='control_size'
    )

    st.markdown("---")

    st.markdown("**Treatment Group (New Technique)**")
    treatment_mean = st.number_input(
        "Treatment Group Mean Score",
        value=78.0,            # Changed to float
        step=1.0,              # Changed to float
        format="%.1f",
        key='treatment_mean'
    )
    treatment_std = st.number_input(
        "Treatment Group Std Dev (σ)",
        value=10.0,            # Changed to float
        step=0.1,              # Changed to float
        min_value=0.1,
        format="%.1f",
        key='treatment_std'
    )
    treatment_size = st.slider(
        "Treatment Group Size (n)",
        min_value=10,
        max_value=200,
        value=50,
        step=10,
        key='treatment_size'
    )

    st.markdown("---")

    st.subheader("Decision Making")

    alpha = st.number_input(
        "Significance Level (α)",
        value=0.05,
        step=0.01,
        min_value=0.01,
        max_value=0.1,
        format="%.2f",
        key='alpha'
    )

with plot_col:
    # Input Validation
    if (control_std <= 0) or (treatment_std <= 0):
        st.error("Standard deviations must be positive numbers.")
    elif (control_size <= 1) or (treatment_size <= 1):
        st.error("Sample sizes must be greater than 1.")
    else:
        # Generate Data
        np.random.seed(42)
        control_scores = np.random.normal(control_mean, control_std, control_size)
        treatment_scores = np.random.normal(treatment_mean, treatment_std, treatment_size)

        # Calculate means
        control_sample_mean = np.mean(control_scores)
        treatment_sample_mean = np.mean(treatment_scores)

        # Perform two-sample t-test
        t_stat, p_value = stats.ttest_ind(treatment_scores, control_scores, equal_var=False)

        # Degrees of freedom for Welch's t-test
        df_num = (control_std**2 / control_size + treatment_std**2 / treatment_size)**2
        df_den = ((control_std**2 / control_size)**2) / (control_size - 1) + ((treatment_std**2 / treatment_size)**2) / (treatment_size - 1)
        df = df_num / df_den

        # Critical values for two-tailed test
        t_critical = stats.t.ppf(1 - alpha/2, df)

        # Decision
        if p_value < alpha:
            decision = f"Since the **p-value ({p_value:.4f})** is less than **α ({alpha})**, we **reject the null hypothesis (H₀)**."
            conclusion = "**Conclusion:** The new study technique **improves** test scores."
            result_color = "green"
            reject = True
        else:
            decision = f"Since the **p-value ({p_value:.4f})** is **not** less than **α ({alpha})**, we **fail to reject the null hypothesis (H₀)**."
            conclusion = "**Conclusion:** There is **no sufficient evidence** that the new study technique improves test scores."
            result_color = "red"
            reject = False

        # Visualization: Test Score Distributions
        # st.subheader("Test Score Distributions")

        # fig1 = go.Figure()

        # fig1.add_trace(go.Histogram(
        #     x=control_scores,
        #     name='Control Group',
        #     opacity=0.6,
        #     nbinsx=20,
        #     marker_color='blue'
        # ))

        # fig1.add_trace(go.Histogram(
        #     x=treatment_scores,
        #     name='Treatment Group',
        #     opacity=0.6,
        #     nbinsx=20,
        #     marker_color='orange'
        # ))

        # fig1.update_layout(
        #     barmode='overlay',
        #     title='Distribution of Test Scores',
        #     xaxis_title='Test Score',
        #     yaxis_title='Frequency',
        #     legend=dict(x=0.7, y=0.95)
        # )

        # st.plotly_chart(fig1, use_container_width=True)

        # Visualization: T-Distribution with Critical Regions
        st.subheader("T-Distribution and Hypothesis Testing")

        # Define range for t-distribution plot
        t_range = np.linspace(-4, 4, 1000)
        t_dist = stats.t.pdf(t_range, df)

        # Create figure
        fig2 = go.Figure()

        # Add t-distribution curve
        fig2.add_trace(go.Scatter(
            x=t_range,
            y=t_dist,
            mode='lines',
            name='t-Distribution',
            line=dict(color='black')
        ))

        # Shade rejection regions
        fig2.add_trace(go.Scatter(
            x=np.concatenate([t_range[t_range <= -t_critical], [-t_critical]]),
            y=np.concatenate([t_dist[t_range <= -t_critical], [0]]),
            fill='toself',
            fillcolor='rgba(255, 0, 0, 0.3)',
            line=dict(color='rgba(255,0,0,0)'),
            hoverinfo='skip',
            showlegend=True,
            name='Rejection Region'
        ))

        fig2.add_trace(go.Scatter(
            x=np.concatenate([t_range[t_range >= t_critical], [t_critical]]),
            y=np.concatenate([t_dist[t_range >= t_critical], [0]]),
            fill='toself',
            fillcolor='rgba(255, 0, 0, 0.3)',
            line=dict(color='rgba(255,0,0,0)'),
            hoverinfo='skip',
            showlegend=True,
            name='Rejection Region'
        ))

        # Shade acceptance region
        fig2.add_trace(go.Scatter(
            x=np.concatenate([t_range[(t_range > -t_critical) & (t_range < t_critical)], [t_critical, -t_critical]]),
            y=np.concatenate([t_dist[(t_range > -t_critical) & (t_range < t_critical)], [0, 0]]),
            fill='toself',
            fillcolor='rgba(0, 255, 0, 0.1)',
            line=dict(color='rgba(0,255,0,0)'),
            hoverinfo='skip',
            showlegend=True,
            name='Acceptance Region'
        ))

        # Mark the observed t-statistic
        fig2.add_trace(go.Scatter(
            x=[t_stat],
            y=[stats.t.pdf(t_stat, df)],
            mode='markers',
            marker=dict(color='purple', size=10),
            name='Observed t-Statistic'
        ))

        # Add vertical lines for critical values
        fig2.add_trace(go.Scatter(
            x=[-t_critical, -t_critical],
            y=[0, stats.t.pdf(-t_critical, df)],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Critical Value'
        ))

        fig2.add_trace(go.Scatter(
            x=[t_critical, t_critical],
            y=[0, stats.t.pdf(t_critical, df)],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Critical Value'
        ))

        # Update layout
        fig2.update_layout(
            title='t-Distribution with Rejection and Acceptance Regions',
            xaxis_title='t-Statistic',
            yaxis_title='Probability Density',
            showlegend=True
        )

        # Add annotations for critical values
        fig2.add_annotation(
            x=-t_critical,
            y=stats.t.pdf(-t_critical, df),
            text=f"-t_critical = {-t_critical:.2f}",
            showarrow=True,
            arrowhead=1,
            ax=-30,
            ay=-40
        )

        fig2.add_annotation(
            x=t_critical,
            y=stats.t.pdf(t_critical, df),
            text=f"t_critical = {t_critical:.2f}",
            showarrow=True,
            arrowhead=1,
            ax=30,
            ay=-40
        )

        # Add annotation for observed t-statistic
        fig2.add_annotation(
            x=t_stat,
            y=stats.t.pdf(t_stat, df),
            text=f"t = {t_stat:.2f}",
            showarrow=True,
            arrowhead=1,
            ax=0,
            ay=-40
        )

        fig2.update_xaxes(range=[min(-4, t_stat - 1), max(4, t_stat + 1)])

        st.plotly_chart(fig2, use_container_width=True)

        # Display Statistical Test Results
        st.subheader("Statistical Test Results")

        st.markdown(f"**Control Group Mean:** {control_sample_mean:.2f}")
        st.markdown(f"**Treatment Group Mean:** {treatment_sample_mean:.2f}")
        st.markdown(f"**Difference in Means:** {treatment_sample_mean - control_sample_mean:.2f}")
        st.markdown(f"**T-Statistic:** {t_stat:.2f}")
        st.markdown(f"**Degrees of Freedom:** {df:.2f}")
        st.markdown(f"**P-Value:** {p_value:.4f}")

        # Display Decision and Conclusion
        st.markdown("---")
        st.markdown(f"<span style='color:{result_color};'>{decision}</span>", unsafe_allow_html=True)
        st.markdown(conclusion)

    st.markdown("**Visualizations update automatically based on your inputs.**")

# Section 5: Real-World Example
st.header("Real-World Example: Medical Trial")

st.markdown("""
**Scenario:** Researchers want to test if a new drug effectively lowers blood pressure.

- **Null Hypothesis (H₀):** The new drug has no effect on lowering blood pressure.
- **Alternative Hypothesis (H₁):** The new drug effectively lowers blood pressure.
""")

# Placeholder for further interactive content
st.markdown("*(Future interactive sections can be added here to explore the medical trial example.)*")

# Section 6: Key Takeaways
st.header("Key Takeaways")

st.markdown("""
- **Hypothesis Testing** is a fundamental tool in statistics for making data-driven decisions.
- It involves setting up a **null hypothesis** and an **alternative hypothesis** to evaluate claims or beliefs.
- By analyzing sample data, you can determine whether there is enough evidence to support a specific claim about the population.
- This method is widely used in various fields, including medicine, business, psychology, and engineering, to ensure that conclusions are based on reliable evidence.
""")

# Footer
st.markdown("---")
st.markdown("© 2024 Interactive Hypothesis Testing Tutorial")
