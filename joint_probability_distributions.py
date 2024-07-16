import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy import stats

# Set page config
st.set_page_config(layout="wide", page_title="Joint Probability Distributions Explorer", page_icon="📊")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background-color: #FFFFFF;
    }
    
    .big-font {
        font-size: 34px !important;
        font-weight: 600;
        color: #2C3E50;
    }
    
    .medium-font {
        font-size: 28px !important;
        font-weight: 600;
        color: #E74C3C;
    }
    
    .small-font {
        font-size: 18px !important;
        color: #34495E;
    }
    
    .stButton>button {
        color: #FFFFFF;
        background-color: #3498DB;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(52, 152, 219, 0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980B9;
        box-shadow: 0 6px 8px rgba(52, 152, 219, 0.2);
        transform: translateY(-2px);
    }
    
    .stSlider>div>div>div>div {
        background-color: #3498DB;
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #3498DB;
    }
    
    .highlight {
        background-color: #F9E79F;
        padding: 5px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📊 Joint Probability Distributions Explorer 📊</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the Joint Probability Distributions Explorer!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's explore how two random variables can be related and their joint probabilities.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What are Joint Probability Distributions?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
A joint probability distribution is a probability distribution that gives the probability of two or more random variables occurring together. Key points:

- It describes the likelihood of two or more events happening simultaneously
- Can be represented as tables, functions, or graphs
- Allows calculation of marginal and conditional probabilities
- Crucial in understanding relationships between variables in many fields
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["📊 Discrete Example", "🔄 Continuous Example (3D)", "🎲 Interactive Simulation (3D)", "🧠 Quiz"])

with tab1:
    st.markdown("<p class='medium-font'>Discrete Joint Probability Distribution</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's consider a simple example of rolling two dice. We'll look at the joint probability of the sum and the difference of the dice rolls.
        </p>
        """, unsafe_allow_html=True)
        
        # Create joint probability matrix
        dice_sums = np.arange(2, 13)
        dice_diffs = np.arange(0, 6)
        joint_prob = np.zeros((len(dice_sums), len(dice_diffs)))

        for i in range(1, 7):
            for j in range(1, 7):
                sum_idx = i + j - 2
                diff_idx = abs(i - j)
                joint_prob[sum_idx, diff_idx] += 1/36

        st.markdown("""
        <p class='small-font'>
        The heatmap shows the joint probability distribution. Brighter colors indicate higher probabilities.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        fig = go.Figure(data=go.Heatmap(
            z=joint_prob,
            x=dice_diffs,
            y=dice_sums,
            colorscale='Viridis'))

        fig.update_layout(
            title='Joint Probability Distribution of Dice Sum and Difference',
            xaxis_title='Difference between dice',
            yaxis_title='Sum of dice')

        st.plotly_chart(fig)

with tab2:
    st.markdown("<p class='medium-font'>Continuous Joint Probability Distribution (3D)</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Now let's look at a continuous joint probability distribution in 3D. We'll use a bivariate normal distribution as an example.
        </p>
        """, unsafe_allow_html=True)

        mean_x = st.slider("Mean of X", -3.0, 3.0, 0.0, 0.1)
        mean_y = st.slider("Mean of Y", -3.0, 3.0, 0.0, 0.1)
        std_x = st.slider("Standard Deviation of X", 0.1, 2.0, 1.0, 0.1)
        std_y = st.slider("Standard Deviation of Y", 0.1, 2.0, 1.0, 0.1)
        correlation = st.slider("Correlation", -1.0, 1.0, 0.0, 0.1)

        st.markdown("""
        <p class='small-font'>
        The 3D surface plot shows the joint probability density. Height and color indicate probability density.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        pos = np.dstack((X, Y))

        rv = stats.multivariate_normal([mean_x, mean_y], [[std_x**2, correlation*std_x*std_y], 
                                                          [correlation*std_x*std_y, std_y**2]])
        
        Z = rv.pdf(pos)

        fig = go.Figure(data=[go.Surface(z=Z, x=x, y=y)])
        fig.update_layout(title='Bivariate Normal Distribution (3D)',
                          scene=dict(xaxis_title='X',
                                     yaxis_title='Y',
                                     zaxis_title='Probability Density'),
                          width=600, height=600)

        st.plotly_chart(fig)

with tab3:
    st.markdown("<p class='medium-font'>Interactive Joint Probability Simulation (3D)</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <p class='small-font'>
        Let's simulate drawing samples from a bivariate normal distribution and visualize the joint distribution in 3D.
        </p>
        """, unsafe_allow_html=True)

        num_samples = st.slider("Number of samples", 100, 10000, 1000, 100)
        mean_x = st.slider("Mean of X", -3.0, 3.0, 0.0, 0.1, key="sim_mean_x")
        mean_y = st.slider("Mean of Y", -3.0, 3.0, 0.0, 0.1, key="sim_mean_y")
        std_x = st.slider("Standard Deviation of X", 0.1, 2.0, 1.0, 0.1, key="sim_std_x")
        std_y = st.slider("Standard Deviation of Y", 0.1, 2.0, 1.0, 0.1, key="sim_std_y")
        correlation = st.slider("Correlation", -1.0, 1.0, 0.0, 0.1, key="sim_correlation")

        if st.button("Run Simulation"):
            cov = [[std_x**2, correlation*std_x*std_y], 
                   [correlation*std_x*std_y, std_y**2]]
            samples = np.random.multivariate_normal([mean_x, mean_y], cov, num_samples)

            st.markdown("""
            <p class='small-font'>
            The 3D scatter plot shows the joint distribution of samples. The histograms show the marginal distributions.
            </p>
            """, unsafe_allow_html=True)

    with col2:
        if 'samples' in locals():
            # Create 3D scatter plot
            trace1 = go.Scatter3d(
                x=samples[:, 0],
                y=samples[:, 1],
                z=np.zeros(num_samples),
                mode='markers',
                marker=dict(
                    size=2,
                    color=samples[:, 1],
                    colorscale='Viridis',
                    opacity=0.8
                )
            )

            # Create histogram for X
            trace2 = go.Histogram(
                x=samples[:, 0],
                nbinsx=50,
                name='X distribution',
                marker_color='#1f77b4',
                opacity=0.7
            )

            # Create histogram for Y
            trace3 = go.Histogram(
                y=samples[:, 1],
                nbinsy=50,
                name='Y distribution',
                marker_color='#1f77b4',
                opacity=0.7
            )

            # Create 3D surface for theoretical distribution
            x = np.linspace(min(samples[:, 0]), max(samples[:, 0]), 50)
            y = np.linspace(min(samples[:, 1]), max(samples[:, 1]), 50)
            X, Y = np.meshgrid(x, y)
            pos = np.dstack((X, Y))
            Z = rv.pdf(pos)

            trace4 = go.Surface(
                x=x,
                y=y,
                z=Z,
                opacity=0.3,
                colorscale='Viridis'
            )

            # Combine all traces and create the layout
            fig = go.Figure(data=[trace1, trace2, trace3, trace4])
            fig.update_layout(
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Density',
                    aspectmode='manual',
                    aspectratio=dict(x=1, y=1, z=0.5)
                ),
                width=700,
                height=700,
                margin=dict(l=0, r=0, b=0, t=30)
            )

            st.plotly_chart(fig)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "What does a joint probability distribution describe?",
            "options": [
                "The probability of a single event occurring",
                "The probability of two or more events occurring together",
                "The difference between two probabilities",
                "The sum of all probabilities in a system"
            ],
            "correct": 1,
            "explanation": "A joint probability distribution describes the probability of two or more events occurring together. It shows how different random variables are related to each other."
        },
        {
            "question": "In a bivariate normal distribution, what does the correlation parameter control?",
            "options": [
                "The mean of the distribution",
                "The standard deviation of each variable",
                "The relationship between the two variables",
                "The total probability of the system"
            ],
            "correct": 2,
            "explanation": "In a bivariate normal distribution, the correlation parameter controls the relationship between the two variables. It determines how strongly the variables are related and in what direction (positive or negative)."
        },
        {
            "question": "What can we calculate from a joint probability distribution?",
            "options": [
                "Only marginal probabilities",
                "Only conditional probabilities",
                "Both marginal and conditional probabilities",
                "Neither marginal nor conditional probabilities"
            ],
            "correct": 2,
            "explanation": "From a joint probability distribution, we can calculate both marginal probabilities (the probability of one variable regardless of the others) and conditional probabilities (the probability of one variable given a specific value of another)."
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"<p class='small-font'><strong>Question {i+1}:</strong> {q['question']}</p>", unsafe_allow_html=True)
        user_answer = st.radio("Select your answer:", q['options'], key=f"q{i}")
        
        if st.button("Check Answer", key=f"check{i}"):
            if q['options'].index(user_answer) == q['correct']:
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error("Incorrect. Try again! 🤔")
            st.info(q['explanation'])
        st.markdown("---")

    if st.button("Show Final Score"):
        st.markdown(f"<p class='big-font'>Your score: {score}/{len(questions)}</p>", unsafe_allow_html=True)
        if score == len(questions):
            st.balloons()

# Conclusion
st.markdown("<p class='big-font'>Congratulations! 🎊</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>You've explored Joint Probability Distributions through interactive examples and simulations. These concepts are crucial in understanding relationships between variables in many fields, including statistics, machine learning, and data science. Keep exploring and applying these concepts in various scenarios!</p>", unsafe_allow_html=True)