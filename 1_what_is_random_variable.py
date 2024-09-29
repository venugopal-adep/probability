import streamlit as st
import plotly.graph_objs as go
import numpy as np
from scipy import stats
import plotly.express as px

st.set_page_config(layout="wide", page_title="Random Variables Explained")

# Custom CSS for better visual appeal
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
    .stRadio [data-testid="stMarkdownContainer"] > p {
        font-size: 16px;
    }
    .formula {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 5px;
        font-family: monospace;
    }
    .st-emotion-cache-16idsys p {
        font-size: 18px;
        line-height: 1.6;
    }
    .sidebar .sidebar-content {
        background-color: #f0f8ff;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎲 Understanding Random Variables 📊")
st.write("**Developed by : Venugopal Adep**")

tab1, tab2, tab3, tab4 = st.tabs(["📚 Introduction", "🎲 Discrete Random Variables", "📈 Continuous Random Variables", "🧠 Quiz"])

with tab1:
    st.header("What is a Random Variable?")
    st.write("""
    A random variable is a mathematical concept that assigns a numerical value to each outcome of an uncertain event or experiment. It's a way to quantify and analyze uncertainty in various situations.
    """)
    
    st.subheader("Types of Random Variables")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Discrete Random Variable**: Takes on distinct, countable values.\n\n🎭 Example: Number of people in a theater (0, 1, 2, 3, ...)")
    with col2:
        st.info("**Continuous Random Variable**: Can take any value within a range.\n\n🌡️ Example: Temperature outside (20.1°C, 20.15°C, 20.153°C, ...)")

    st.subheader("🪙 Interactive Example: Coin Toss")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("Let's toss a coin twice and count the number of heads!")
        if st.button("🪙 Toss Coins"):
            toss1 = "Heads" if np.random.rand() > 0.5 else "Tails"
            toss2 = "Heads" if np.random.rand() > 0.5 else "Tails"
            result = f"{toss1} and {toss2}"
            heads_count = result.count("Heads")
            st.success(f"Result: {result}")
            st.info(f"Number of Heads: {heads_count}")
    
    with col2:
        outcomes = ['0 Heads (TT)', '1 Head (HT or TH)', '2 Heads (HH)']
        probabilities = [0.25, 0.5, 0.25]
        
        fig = px.bar(x=outcomes, y=probabilities, labels={'x':'Outcome', 'y':'Probability'})
        fig.update_layout(title="Probability Distribution of Coin Toss Outcomes")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Discrete Random Variables")
    st.write("""
    A discrete random variable takes on a countable number of distinct values. It's often used when counting occurrences or items.
    """)
    
    st.subheader("🎲 Interactive Example: Rolling Dice")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("Adjust the number of dice and roll them!")
        num_dice = st.slider("Number of dice to roll", 1, 5, 2)
        
        if st.button(f"🎲 Roll {num_dice} Dice"):
            results = [np.random.randint(1, 7) for _ in range(num_dice)]
            total = sum(results)
            st.success(f"You rolled: {results}")
            st.info(f"Total sum: {total}")

    with col2:
        possible_sums = range(num_dice, 6*num_dice + 1)
        probabilities = [sum(1 for dice in range(1, 7) for _ in range(num_dice) 
                             if sum(dice for _ in range(num_dice)) == s) / (6**num_dice) 
                         for s in possible_sums]

        fig = px.bar(x=possible_sums, y=probabilities, labels={'x':'Sum of Dice', 'y':'Probability'})
        fig.update_layout(title=f"Probability Distribution for Sum of {num_dice} Dice")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Continuous Random Variables")
    st.write("""
    A continuous random variable can take any value within a range, including fractional values. It's often used for measurements like height, weight, or time.
    """)
    
    st.subheader("📏 Interactive Example: Height Distribution")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("Adjust the parameters to see how they affect the height distribution:")
        mean = st.slider("Average height (cm)", 150, 190, 170)
        std = st.slider("Standard deviation (cm)", 5, 20, 10)
        
        user_height = st.number_input("Enter a height to check its percentile:", min_value=120, max_value=220, value=170)
        percentile = stats.norm.cdf(user_height, mean, std) * 100
        st.write(f"A height of {user_height} cm is at the {percentile:.2f}th percentile.")
    
    with col2:
        x = np.linspace(120, 220, 1000)
        y = stats.norm.pdf(x, mean, std)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='PDF'))
        fig.update_layout(
            title="Probability Density Function of Adult Heights",
            xaxis_title="Height (cm)",
            yaxis_title="Probability Density"
        )

        fig.add_trace(go.Scatter(x=[mean, mean], y=[0, max(y)], mode='lines', name='Mean', line=dict(color='red', dash='dash')))
        
        percentiles = [2.5, 16, 50, 84, 97.5]
        colors = ['rgba(255,0,0,0.1)', 'rgba(0,255,0,0.1)', 'rgba(0,0,255,0.1)']
        for i, (lower, upper) in enumerate(zip(percentiles[:-1], percentiles[1:])):
            lower_val = stats.norm.ppf(lower/100, mean, std)
            upper_val = stats.norm.ppf(upper/100, mean, std)
            fig.add_trace(go.Scatter(
                x=[lower_val, lower_val, upper_val, upper_val],
                y=[0, max(y), max(y), 0],
                fill='toself',
                fillcolor=colors[i % len(colors)],
                line=dict(color='rgba(255,255,255,0)'),
                name=f'{lower}th to {upper}th percentile'
            ))

        st.plotly_chart(fig, use_container_width=True)

        st.write("🔍 Hover over the chart to see exact values. The colored areas represent different percentile ranges. The red dashed line shows the mean height.")

with tab4:
    st.header("📝 Random Variables Quiz")
    
    questions = [
        {
            "question": "What type of random variable can only take whole number values?",
            "options": ["Discrete", "Continuous", "Both", "Neither"],
            "correct": 0,
            "explanation": "Discrete random variables can only take specific, countable values like whole numbers."
        },
        {
            "question": "Which of these is an example of a continuous random variable?",
            "options": ["Number of cars", "Temperature", "Coin flips", "Dice rolls"],
            "correct": 1,
            "explanation": "Temperature can be any value within a range and can be measured to arbitrary precision, making it a continuous random variable."
        },
        {
            "question": "In a fair coin toss, what's the probability of getting heads?",
            "options": ["1/4", "1/3", "1/2", "3/4"],
            "correct": 2,
            "explanation": "In a fair coin toss, the probability of getting heads is 1/2 or 50%, as there are two equally likely outcomes."
        }
    ]
    
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(q["question"])
            answer = st.radio("Choose your answer:", q["options"], key=f"q{i}")
        with col2:
            if st.button(f"Submit Answer for Question {i+1}"):
                if q["options"].index(answer) == q["correct"]:
                    st.success("🎉 Correct! Well done!")
                else:
                    st.error("❌ Incorrect. Try again!")
                st.info(f"Explanation: {q['explanation']}")
        st.write("---")

st.sidebar.title("📚 Learning Guide")
st.sidebar.info("""
1. Start with the Introduction to grasp the basic concept.
2. Explore Discrete Random Variables with the dice rolling example.
3. Dive into Continuous Random Variables and experiment with the height distribution.
4. Test your knowledge with the Quiz!
""")
st.sidebar.success("Happy learning! 🚀")
