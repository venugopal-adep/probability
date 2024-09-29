import streamlit as st
import plotly.graph_objs as go
import numpy as np
from scipy import stats

st.set_page_config(layout="wide", page_title="Interactive Probability Distributions")

# Custom CSS for better visual appeal
st.markdown("""
<style>
    .main {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #1E90FF;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Interactive Probability Distributions")

tab1, tab2 = st.tabs(["🪙 Coin Toss", "🎲 Dice Roll"])

with tab1:
    st.header("🪙 Interactive Example: Coin Toss")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("Let's toss coins and count the number of heads!")
        num_coins = st.slider("Number of coins to toss", 1, 10, 2)
        num_tosses = st.number_input("Number of experiments", min_value=100, max_value=10000, value=1000, step=100)
        
        if st.button(f"🪙 Toss {num_coins} Coins {num_tosses} Times"):
            results = np.random.binomial(num_coins, 0.5, num_tosses)
            unique, counts = np.unique(results, return_counts=True)
            experimental_probs = counts / num_tosses
            
            theoretical_probs = [stats.binom.pmf(k, num_coins, 0.5) for k in range(num_coins + 1)]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=list(range(num_coins + 1)), y=experimental_probs, name="Experimental", marker_color='blue'))
            fig.add_trace(go.Scatter(x=list(range(num_coins + 1)), y=theoretical_probs, mode='lines+markers', name="Theoretical", line=dict(color='red')))
            
            fig.update_layout(
                title=f"Probability Distribution of {num_coins} Coin Tosses ({num_tosses} experiments)",
                xaxis_title="Number of Heads",
                yaxis_title="Probability",
                legend_title="Distribution Type"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("Hover over the bars and lines to see exact probabilities!")
    
    with col2:
        st.write("Theoretical Probability Distribution:")
        x = list(range(num_coins + 1))
        y = [stats.binom.pmf(k, num_coins, 0.5) for k in x]
        
        fig = go.Figure(go.Bar(x=x, y=y, marker_color='green'))
        fig.update_layout(
            title=f"Theoretical Probability Distribution for {num_coins} Coin Tosses",
            xaxis_title="Number of Heads",
            yaxis_title="Probability"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("🎲 Interactive Example: Rolling Dice")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("Adjust the number of dice and roll them!")
        num_dice = st.slider("Number of dice to roll", 1, 10, 3)
        num_rolls = st.number_input("Number of rolls", min_value=100, max_value=10000, value=1000, step=100)
        
        if st.button(f"🎲 Roll {num_dice} Dice {num_rolls} Times"):
            results = np.sum(np.random.randint(1, 7, size=(num_rolls, num_dice)), axis=1)
            unique, counts = np.unique(results, return_counts=True)
            experimental_probs = counts / num_rolls
            
            # Calculate theoretical probabilities
            possible_sums = range(num_dice, 6*num_dice + 1)
            theoretical_probs = [sum(1 for dice in np.array(np.meshgrid(*([range(1, 7)] * num_dice))).T.reshape(-1, num_dice)
                                     if sum(dice) == s) / (6**num_dice) for s in possible_sums]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=unique, y=experimental_probs, name="Experimental", marker_color='blue'))
            fig.add_trace(go.Scatter(x=list(possible_sums), y=theoretical_probs, mode='lines+markers', name="Theoretical", line=dict(color='red')))
            
            fig.update_layout(
                title=f"Probability Distribution for Sum of {num_dice} Dice ({num_rolls} rolls)",
                xaxis_title="Sum of Dice",
                yaxis_title="Probability",
                legend_title="Distribution Type"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("Hover over the bars and lines to see exact probabilities!")
    
    with col2:
        st.write("Theoretical Probability Distribution:")
        possible_sums = range(num_dice, 6*num_dice + 1)
        theoretical_probs = [sum(1 for dice in np.array(np.meshgrid(*([range(1, 7)] * num_dice))).T.reshape(-1, num_dice)
                                 if sum(dice) == s) / (6**num_dice) for s in possible_sums]
        
        fig = go.Figure(go.Bar(x=list(possible_sums), y=theoretical_probs, marker_color='green'))
        fig.update_layout(
            title=f"Theoretical Probability Distribution for Sum of {num_dice} Dice",
            xaxis_title="Sum of Dice",
            yaxis_title="Probability"
        )
        st.plotly_chart(fig, use_container_width=True)

st.sidebar.title("📚 Learning Guide")
st.sidebar.info("""
1. Start with the Coin Toss example to understand basic probability concepts.
2. Experiment with different numbers of coins and tosses to see how it affects the distribution.
3. Move on to the Dice Roll example for a more complex probability scenario.
4. Compare the experimental results with theoretical probabilities in both cases.
5. Observe how the distributions change as you increase the number of experiments.
""")
st.sidebar.success("Happy exploring! 🚀")
