import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import binom

st.set_page_config(layout="wide", page_title="Binomial Distribution Demo")

st.markdown("""
<style>
body {
    color: #333;
    background-color: #f0f8ff;
}
.main {
    padding: 2rem 3rem;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
h1, h2, h3 {
    color: #1E90FF;
}
.big-font {
    font-size: 20px !important;
    color: #1F77B4;
}
.info-box {
    background-color: #e6f3ff;
    border-left: 5px solid #1E90FF;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
}
.stButton>button {
    background-color: #1E90FF;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title('📊 Binomial Distribution Interactive Demo')
st.write("**Developed by : Venugopal Adep**")

tab1, tab2, tab3 = st.tabs(["📚 Introduction", "🎲 Interactive Example", "🧠 Quiz"])

with tab1:
    st.markdown('<p class="big-font">The binomial distribution is the probability distribution of the number of successes of an experiment that is conducted multiple times and has only two possible outcomes.</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>Example:</b> Suppose you have purchased 10 lottery tickets and the possible outcomes are winning the lottery or not winning the lottery, then you can answer a question like what is the probability of winning 6 lottery tickets using the binomial distribution.
    </div>
    """, unsafe_allow_html=True)

    st.subheader('Assumptions of Binomial Distribution')
    assumptions = [
        "There are only two possible outcomes (success or failure) for each trial.",
        "The number of trials is fixed.",
        "The outcome of each trial is independent. In other words, none of the trials affect the probability of the next trial.",
        "The probability of success is the same for each trial."
    ]
    for i, assumption in enumerate(assumptions, 1):
        st.markdown(f"{i}. {assumption}")

    st.info("Note: In binomial distribution, if the number of trials for a given experiment is equal to 1, then it is called the Bernoulli distribution.")

with tab2:
    st.subheader('Interactive Binomial Distribution Example')

    col1, col2 = st.columns(2)
    with col1:
        n = st.slider('Number of lottery tickets (n)', 1, 20, 10)
        p = st.slider('Probability of winning a single ticket (p)', 0.0, 1.0, 0.1, 0.01)
    with col2:
        x = st.slider('Number of winning tickets (x)', 0, n, 6)

    # Calculate probability
    prob = binom.pmf(x, n, p)

    st.markdown(f"""
    <div class="info-box">
    Probability of winning exactly {x} out of {n} lottery tickets, 
    with a {p:.2%} chance of winning each ticket:
    <br><br>
    <b>P(X = {x}) = {prob:.6f}</b>
    </div>
    """, unsafe_allow_html=True)

    # Plot Binomial Distribution
    fig = go.Figure()

    x_range = np.arange(n + 1)
    y = binom.pmf(x_range, n, p)

    fig.add_trace(go.Bar(
        x=x_range, 
        y=y,
        name='Probability',
        marker_color='lightblue'
    ))

    fig.add_trace(go.Scatter(
        x=[x, x],
        y=[0, binom.pmf(x, n, p)],
        mode='lines',
        name='Selected X',
        line=dict(color='red', width=2, dash='dash')
    ))

    fig.update_layout(
        title=f'Binomial Distribution (n={n}, p={p:.2f})',
        xaxis_title='Number of Successes (X)',
        yaxis_title='Probability',
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Formula
    st.subheader('Binomial Distribution Formula')
    st.latex(r'''
    P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
    ''')
    st.markdown("""
    Where:
    - n is the number of trials
    - k is the number of successes
    - p is the probability of success on each trial
    """)


with tab3:
    st.subheader('Quick Quiz')
    questions = [
        {
            "question": "What happens to the Binomial Distribution when the number of trials (n) is 1?",
            "options": ["Normal", "Poisson", "Bernoulli", "Exponential"],
            "correct": "Bernoulli",
            "explanation": "When n = 1, the Binomial Distribution reduces to a Bernoulli Distribution, which models a single trial with two possible outcomes."
        },
        {
            "question": "Which of the following is NOT an assumption of the Binomial Distribution?",
            "options": ["Independent trials", "Varying success probability", "Two outcomes", "Fixed trials"],
            "correct": "Varying success probability",
            "explanation": "In a Binomial Distribution, the probability of success must be constant for all trials. If it varies, it violates one of the key assumptions."
        },
        {
            "question": "In a Binomial Distribution, what does 'n' represent?",
            "options": ["Successes", "Probability", "Trials", "Failures"],
            "correct": "Trials",
            "explanation": "'n' in a Binomial Distribution represents the total number of trials or experiments conducted."
        },
        {
            "question": "If p = 0.3 in a Binomial Distribution, what is q?",
            "options": ["0.3", "0.7", "0.4", "1.3"],
            "correct": "0.7",
            "explanation": "In a Binomial Distribution, q represents the probability of failure and is equal to 1 - p. So if p = 0.3, then q = 1 - 0.3 = 0.7."
        }
    ]

    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        answer = st.radio(f"Select your answer for Question {i+1}:", q['options'], key=f"q{i}")
        if st.button(f"Check Answer for Question {i+1}"):
            if answer == q['correct']:
                st.success("Correct! 🎉")
            else:
                st.error("That's not correct. Try again!")
            st.info(f"Explanation: {q['explanation']}")
        st.write("---")

st.sidebar.title("About")
st.sidebar.info("This interactive demo helps you understand the Binomial distribution, its properties, and applications.")
st.sidebar.title("Navigation")
st.sidebar.info("Use the tabs above to explore different aspects of the Binomial distribution.")
