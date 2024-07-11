import streamlit as st
import plotly.graph_objects as go
import numpy as np
import random

def set_page_config():
    st.set_page_config(page_title="Uniform Distribution in Real Life", layout="wide")
    st.title("🌟 Uniform Distribution: Real-Life Applications")
    st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: white;
    }
    h1, h2, h3, p {
        color: #1f1f1f;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #4682B4;
        border-radius: 4px 4px 0px 0px;
        gap: 12px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

def dice_roll_simulation():
    st.header("🎲 Fair Dice Roll")
    st.write("In a fair dice, each number has an equal probability of being rolled.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Roll the Dice!"):
            result = random.randint(1, 6)
            st.success(f"You rolled a {result}!")
            st.balloons()
    with col2:
        rolls = st.slider("Number of rolls", 100, 10000, 1000)
        results = [random.randint(1, 6) for _ in range(rolls)]
        fig = go.Figure(data=[go.Histogram(x=results, nbinsx=6)])
        fig.update_layout(title=f"Distribution of {rolls} Dice Rolls", xaxis_title="Dice Value", yaxis_title="Frequency")
        st.plotly_chart(fig)

def roulette_wheel():
    st.header("🎰 Roulette Wheel")
    st.write("In a roulette wheel, each number has an equal chance of being selected.")
    
    numbers = list(range(0, 37))  # 0 to 36
    colors = ['green'] + ['red' if n % 2 else 'black' for n in range(1, 37)]
    
    if st.button("Spin the Wheel!"):
        result = random.choice(numbers)
        color = colors[numbers.index(result)]
        st.success(f"The ball landed on {result} ({color})!")
        
        fig = go.Figure(go.Pie(labels=numbers, values=[1]*37, marker_colors=colors, textinfo='label', hole=.3))
        fig.update_layout(title="Roulette Wheel", annotations=[dict(text='Spin Result', x=0.5, y=0.5, font_size=20, showarrow=False)])
        fig.add_annotation(x=0.5, y=0.5, text=str(result), font=dict(size=40, color="white"), showarrow=False)
        st.plotly_chart(fig)

def random_number_generator():
    st.header("🔢 Random Number Generator")
    st.write("A uniform distribution is often used in random number generators.")
    
    min_val = st.number_input("Minimum value", value=1)
    max_val = st.number_input("Maximum value", value=100)
    
    if st.button("Generate Random Number"):
        result = random.randint(min_val, max_val)
        st.success(f"Your random number is: {result}")
        
        x = list(range(min_val, max_val+1))
        y = [1/(max_val-min_val+1)] * len(x)
        fig = go.Figure(go.Bar(x=x, y=y, marker_color='lightblue'))
        fig.add_vline(x=result, line_width=3, line_dash="dash", line_color="red")
        fig.update_layout(title="Uniform Distribution of Random Numbers", xaxis_title="Number", yaxis_title="Probability")
        st.plotly_chart(fig)

def waiting_time():
    st.header("⏰ Waiting Time at a Bus Stop")
    st.write("If buses arrive every 15 minutes, your waiting time is uniformly distributed between 0 and 15 minutes.")
    
    if st.button("Simulate Arrival"):
        wait_time = random.uniform(0, 15)
        st.success(f"You waited for {wait_time:.2f} minutes.")
        
        x = np.linspace(0, 15, 100)
        y = [1/15] * 100
        fig = go.Figure(go.Scatter(x=x, y=y, fill='tozeroy'))
        fig.add_vline(x=wait_time, line_width=3, line_dash="dash", line_color="red")
        fig.update_layout(title="Uniform Distribution of Waiting Times", xaxis_title="Time (minutes)", yaxis_title="Probability Density")
        st.plotly_chart(fig)

def lottery_simulation():
    st.header("🎟️ Lottery Ticket")
    st.write("In a lottery, each ticket has an equal chance of winning.")
    
    total_tickets = st.number_input("Total number of tickets", min_value=1, value=1000)
    num_simulations = st.slider("Number of simulations", 1, 10000, 1000)
    
    if st.button("Run Lottery Simulation"):
        wins = [random.randint(1, total_tickets) for _ in range(num_simulations)]
        your_ticket = random.randint(1, total_tickets)
        your_wins = wins.count(your_ticket)
        
        st.success(f"Your ticket number: {your_ticket}")
        st.info(f"You won {your_wins} times out of {num_simulations} draws!")
        
        fig = go.Figure(data=[go.Histogram(x=wins, nbinsx=50)])
        fig.add_vline(x=your_ticket, line_width=3, line_dash="dash", line_color="red")
        fig.update_layout(title=f"Distribution of Winning Tickets in {num_simulations} Draws", xaxis_title="Ticket Number", yaxis_title="Frequency")
        st.plotly_chart(fig)

def main():
    set_page_config()
    
    tabs = st.tabs([
        "🎲 Dice Roll",
        "🎰 Roulette Wheel",
        "🔢 Random Number Generator",
        "⏰ Bus Stop Waiting Time",
        "🎟️ Lottery Simulation"
    ])
    
    with tabs[0]:
        dice_roll_simulation()
    with tabs[1]:
        roulette_wheel()
    with tabs[2]:
        random_number_generator()
    with tabs[3]:
        waiting_time()
    with tabs[4]:
        lottery_simulation()

if __name__ == "__main__":
    main()