import streamlit as st
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

def bernoulli_pmf(p, x):
    return p if x == 1 else 1-p

def create_bernoulli_plot(p):
    x = [0, 1]
    y = [bernoulli_pmf(p, 0), bernoulli_pmf(p, 1)]
    
    colors = ['#FF9999', '#66B2FF']
    
    fig = go.Figure(data=[go.Bar(x=x, y=y, text=[f'{val:.2f}' for val in y], 
                                 textposition='auto', marker_color=colors)])
    fig.update_layout(
        title={
            'text': f'Bernoulli Distribution (p={p:.2f})',
            'font': {'size': 24, 'color': '#1F77B4'}
        },
        xaxis_title='Outcome',
        yaxis_title='Probability',
        font={'family': 'Arial', 'size': 14},
        plot_bgcolor='rgba(240,240,240,0.8)',
        width=700,
        height=500
    )
    fig.update_xaxes(tickvals=[0, 1], ticktext=['Failure', 'Success'])
    return fig

st.set_page_config(layout="wide", page_title="Bernoulli Distribution Demo")

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
.stTabs [data-baseweb="tab-list"] {
    gap: 24px;
}
.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: pre-wrap;
    background-color: #F0F8FF;
    border-radius: 4px;
    color: #1E90FF;
    font-size: 16px;
}
.stTabs [aria-selected="true"] {
    background-color: #1E90FF;
    color: white;
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
}
.quiz-container {
    background-color: #f0f8ff;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.quiz-question {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}
.stButton>button {
    background-color: #1E90FF;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title('🎲 Bernoulli Distribution Interactive Demo')

tabs = st.tabs(["📚 Introduction", "📊 Visualization", "🧮 Examples", "🧠 Quiz", "📈 Properties"])

with tabs[0]:
    st.markdown('<p class="big-font">The Bernoulli distribution is a discrete probability distribution for a random variable that has only two possible outcomes: success (usually denoted as 1) or failure (usually denoted as 0).</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>Key points:</b><br>
    1. It models a single trial of a random experiment with two possible outcomes.<br>
    2. The probability of success is denoted by p, and the probability of failure is 1-p.<br>
    3. It's non-judgmental: "success" and "failure" are just labels, not value judgments.
    </div>
    """, unsafe_allow_html=True)

    st.subheader('Probability Mass Function (PMF)')
    st.latex(r'''
    P(X = x) = \begin{cases}
        p, & \text{if } x = 1 \\
        1-p, & \text{if } x = 0
    \end{cases}
    ''')

with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        p = st.slider('Probability of Success (p)', 0.0, 1.0, 0.5, 0.01)
    with col2:
        st.plotly_chart(create_bernoulli_plot(p), use_container_width=True)

with tabs[2]:
    st.subheader('Real-world Examples')
    examples = {
        "Manufacturing": "Success (1): Part is defective\nFailure (0): Part is not defective",
        "Medical Test": "Success (1): Test is positive\nFailure (0): Test is negative",
        "Coin Flip": "Success (1): Heads\nFailure (0): Tails",
        "Customer Purchase": "Success (1): Customer makes a purchase\nFailure (0): Customer doesn't make a purchase"
    }
    
    selected_example = st.selectbox("Choose an example", list(examples.keys()))
    st.code(examples[selected_example])

    st.subheader('Interactive Numerical Example')
    custom_p = st.number_input("Enter probability of success (p)", 0.0, 1.0, 0.3, 0.01)
    st.markdown(f"""
    <div class="info-box">
    We're modeling the probability of a customer making a purchase, with p = {custom_p:.2f}.<br><br>
    Probability of success (making a purchase): {custom_p:.2f} = {custom_p*100:.1f}%<br>
    Probability of failure (not making a purchase): {1-custom_p:.2f} = {(1-custom_p)*100:.1f}%
    </div>
    """, unsafe_allow_html=True)

with tabs[3]:
    st.subheader('Quiz')
    
    questions = [
        {
            "question": "In a Bernoulli distribution, how many possible outcomes are there?",
            "options": ["1", "2", "3", "4"],
            "correct": "2",
            "explanation": "A Bernoulli distribution has exactly two possible outcomes: success (1) and failure (0)."
        },
        {
            "question": "If the probability of success (p) is 0.7, what is the probability of failure?",
            "options": ["0.3", "0.7", "1.0", "1.3"],
            "correct": "0.3",
            "explanation": "The probability of failure is 1 - p. So if p = 0.7, the probability of failure is 1 - 0.7 = 0.3."
        },
        {
            "question": "Which of these is NOT an example of a Bernoulli trial?",
            "options": ["Coin flip", "Die roll", "Yes/No survey question", "Pass/Fail test"],
            "correct": "Die roll",
            "explanation": "A die roll has six possible outcomes, not two, so it's not a Bernoulli trial. All other options have only two possible outcomes."
        }
    ]

    for i, q in enumerate(questions):
        st.markdown(f"""
        <div class="quiz-container">
        <p class="quiz-question">{i+1}. {q['question']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        answer = st.radio("Select your answer:", q['options'], key=f"q{i}")
        
        if st.button(f"Check Answer {i+1}"):
            if answer == q['correct']:
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect. Try again!")
            
            st.info(f"Explanation: {q['explanation']}")
        
        st.markdown("---")

with tabs[4]:
    st.subheader('Additional Properties')
    st.write("""
    1. Expected Value: E(X) = p
    2. Variance: Var(X) = p(1-p)
    3. Standard Deviation: σ = √(p(1-p))
    """)

    prop_p = st.slider('Choose p value', 0.0, 1.0, 0.5, 0.01, key='prop_slider')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Expected Value", f"{prop_p:.4f}")
    with col2:
        st.metric("Variance", f"{prop_p*(1-prop_p):.4f}")
    with col3:
        st.metric("Standard Deviation", f"{np.sqrt(prop_p*(1-prop_p)):.4f}")

    # Visualize how properties change with p
    p_range = np.linspace(0, 1, 100)
    expected_value = p_range
    variance = p_range * (1 - p_range)
    std_dev = np.sqrt(variance)

    fig = px.line(x=p_range, y=[expected_value, variance, std_dev], 
                  labels={'x': 'p', 'value': 'Value'},
                  title='Bernoulli Distribution Properties')
    fig.update_layout(legend_title_text='Property')
    fig.data[0].name = 'Expected Value'
    fig.data[1].name = 'Variance'
    fig.data[2].name = 'Standard Deviation'
    st.plotly_chart(fig, use_container_width=True)

st.sidebar.title("About")
st.sidebar.info("This interactive demo helps you understand the Bernoulli distribution, its properties, and applications.")
st.sidebar.title("Navigation")
st.sidebar.info("Use the tabs above to explore different aspects of the Bernoulli distribution.")