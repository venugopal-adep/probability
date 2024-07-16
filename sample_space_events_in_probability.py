import streamlit as st
import plotly.graph_objects as go
import random
import pandas as pd
from PIL import Image
import io
import base64

# Set page config
st.set_page_config(layout="wide", page_title="Probability Playground", page_icon="🎲")

# Custom CSS with more aesthetically pleasing design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #FFFFFF;
    }
    
    .big-font {
        font-size: 34px !important;
        font-weight: 600;
        color: #FFF176;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .medium-font {
        font-size: 28px !important;
        font-weight: 600;
        color: #81C784;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .small-font {
        font-size: 18px !important;
        color: #E0E0E0;
    }
    
    .stButton>button {
        color: #4A4A4A;
        background-color: #FFD54F;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #FFC107;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        color: #FFFFFF;
        border-radius: 10px;
    }
    
    .stRadio>div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to create animated dice
def create_dice_animation(result):
    frames = []
    for _ in range(10):  # Create 10 frames
        img = Image.new('RGB', (100, 100), color='white')
        d = Image.new('RGB', (80, 80), color='red')
        img.paste(d, (10, 10))
        frames.append(img)
    
    # Final frame with the result
    img = Image.new('RGB', (100, 100), color='white')
    d = Image.new('RGB', (80, 80), color='red')
    img.paste(d, (10, 10))
    frames.append(img)
    
    # Save frames to a byte stream
    byte_stream = io.BytesIO()
    frames[0].save(byte_stream, format='GIF', save_all=True, append_images=frames[1:], duration=100, loop=0)
    return byte_stream.getvalue()

# Title
st.markdown("<h1 style='text-align: center; color: #FFF176; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>🎲 Probability Playground: Sample Spaces & Events 🃏</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("<p class='big-font'>Welcome to the exciting world of probability!</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>Let's dive into the fundamental concepts of sample spaces and events through interactive examples and games.</p>", unsafe_allow_html=True)

# Explanation
st.markdown("<p class='medium-font'>What are Sample Spaces and Events?</p>", unsafe_allow_html=True)
st.markdown("""
<p class='small-font'>
- <strong>Sample Space:</strong> The set of all possible outcomes in an experiment.<br>
- <strong>Event:</strong> A subset of the sample space that we're interested in.
</p>
""", unsafe_allow_html=True)

# Tabs with custom styling
tab1, tab2, tab3, tab4 = st.tabs(["🎲 Dice Roll", "🃏 Card Draw", "🧮 Probability Calculator", "🧠 Quiz"])

with tab1:
    st.markdown("<p class='medium-font'>Roll the Dice!</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='small-font'>Sample Space: {1, 2, 3, 4, 5, 6}</p>", unsafe_allow_html=True)
        st.markdown("<p class='small-font'>Events we're watching:</p>", unsafe_allow_html=True)
        st.markdown("• Even number: {2, 4, 6}", unsafe_allow_html=True)
        st.markdown("• Greater than 3: {4, 5, 6}", unsafe_allow_html=True)

    with col2:
        if st.button("Roll Dice 🎲"):
            result = random.randint(1, 6)
            dice_animation = create_dice_animation(result)
            st.image(dice_animation, use_column_width=True)
            st.markdown(f"<p class='big-font'>You rolled: {result}</p>", unsafe_allow_html=True)
            
            events = []
            if result % 2 == 0:
                events.append("even number")
            if result > 3:
                events.append("greater than 3")
            
            if events:
                st.markdown(f"<p class='small-font'>This roll is an example of: {', '.join(events)}</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='small-font'>This roll doesn't match our example events.</p>", unsafe_allow_html=True)

with tab2:
    st.markdown("<p class='medium-font'>Draw a Card!</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='small-font'>Sample Space: 52 cards (4 suits, 13 ranks each)</p>", unsafe_allow_html=True)
        st.markdown("<p class='small-font'>Events we're watching:</p>", unsafe_allow_html=True)
        st.markdown("• Red card (Hearts or Diamonds)", unsafe_allow_html=True)
        st.markdown("• Face card (Jack, Queen, or King)", unsafe_allow_html=True)

    with col2:
        suits = ['♥️', '♦️', '♣️', '♠️']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        if st.button("Draw Card 🃏"):
            card_suit = random.choice(suits)
            card_rank = random.choice(ranks)
            st.markdown(f"<p class='big-font' style='font-size: 72px !important;'>{card_rank}{card_suit}</p>", unsafe_allow_html=True)
            
            events = []
            if card_suit in ['♥️', '♦️']:
                events.append("red card")
            if card_rank in ['J', 'Q', 'K']:
                events.append("face card")
            
            if events:
                st.markdown(f"<p class='small-font'>This draw is an example of: {', '.join(events)}</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='small-font'>This draw doesn't match our example events.</p>", unsafe_allow_html=True)

with tab3:
    st.markdown("<p class='medium-font'>Probability Calculator</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='small-font'>Enter the number of favorable outcomes and total outcomes:</p>", unsafe_allow_html=True)
        favorable = st.number_input("Favorable outcomes", min_value=0, max_value=1000, value=1)
        total = st.number_input("Total outcomes", min_value=1, max_value=1000, value=2)

    with col2:
        if st.button("Calculate Probability"):
            probability = favorable / total
            st.markdown(f"<p class='big-font'>Probability: {probability:.4f}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='small-font'>Or approximately 1 in {round(1/probability)}</p>", unsafe_allow_html=True)

    # Interactive Visualization
    st.markdown("<p class='medium-font'>Interactive Probability Visualization</p>", unsafe_allow_html=True)
    
    events = st.multiselect("Select events to visualize:", ['Even', 'Odd', '> 3', '≤ 3'], default=['Even', 'Odd'])
    probabilities = [0.5 if event in ['Even', 'Odd'] else (0.5 if event == '> 3' else 0.5) for event in events]

    fig = go.Figure(data=[go.Bar(
        x=events, 
        y=probabilities,
        marker_color=['#FF9800', '#2196F3', '#4CAF50', '#F44336'][:len(events)]
    )])
    fig.update_layout(
        title="Probability of Selected Events in Die Rolls",
        xaxis_title="Events",
        yaxis_title="Probability",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white")
    )
    st.plotly_chart(fig)

with tab4:
    st.markdown("<p class='medium-font'>Test Your Knowledge!</p>", unsafe_allow_html=True)

    questions = [
        {
            "question": "What is the sample space when flipping a coin twice?",
            "options": ["HH, HT, TH, TT", "H, T", "HHH, HHT, HTH, HTT, THH, THT, TTH, TTT", "0, 1, 2"],
            "correct": 0,
            "explanation": """When we flip a coin twice, we're performing two separate coin flips. For each flip, we have two possible outcomes: Heads (H) or Tails (T). To find all possible combinations, we consider what can happen on the first flip and then what can happen on the second flip:

1. First flip H, second flip H: HH
2. First flip H, second flip T: HT
3. First flip T, second flip H: TH
4. First flip T, second flip T: TT

This gives us the complete sample space: {HH, HT, TH, TT}

Think of it like choosing an ice cream flavor (chocolate or vanilla) for two scoops. You have four possibilities: chocolate-chocolate, chocolate-vanilla, vanilla-chocolate, and vanilla-vanilla."""
        },
        {
            "question": "In a standard deck of 52 cards, what is the probability of drawing a red ace?",
            "options": ["1/26", "1/13", "1/4", "2/52"],
            "correct": 3,
            "explanation": """Let's break this down step by step:

1. In a standard deck, we have 52 cards total.
2. There are four aces in the deck (one for each suit).
3. Two of these aces are red (the Ace of Hearts and the Ace of Diamonds).

To calculate the probability, we use the formula:
Probability = (Number of favorable outcomes) / (Total number of possible outcomes)

In this case:
- Favorable outcomes: 2 (the two red aces)
- Total possible outcomes: 52 (all cards in the deck)

So, the probability is 2/52, which simplifies to 1/26.

To put this in perspective, imagine you have a bag with 52 marbles, and only 2 of them are red. The chance of picking a red marble on your first try would be the same as drawing a red ace from a deck of cards."""
        },
        {
            "question": "If you roll two dice, what is the probability of getting a sum of 7?",
            "options": ["1/6", "1/12", "1/36", "7/36"],
            "correct": 0,
            "explanation": """Let's visualize this:

1. First, consider all possible outcomes when rolling two dice. We have 6 choices for the first die and 6 for the second, giving us 6 x 6 = 36 total possible outcomes.

2. Now, let's list all the ways to get a sum of 7:
   - 1 on first die and 6 on second: (1,6)
   - 2 on first die and 5 on second: (2,5)
   - 3 on first die and 4 on second: (3,4)
   - 4 on first die and 3 on second: (4,3)
   - 5 on first die and 2 on second: (5,2)
   - 6 on first die and 1 on second: (6,1)

We have 6 favorable outcomes out of 36 total outcomes.

Using our probability formula:
Probability = (Favorable outcomes) / (Total outcomes) = 6/36 = 1/6

To visualize this, imagine a 6x6 grid representing all possible dice roll combinations. The sum of 7 would form a diagonal line across this grid, touching 6 squares out of the total 36."""
        }
    ]

    for i, q in enumerate(questions):
        st.markdown(f"<p class='small-font'><strong>Question {i+1}:</strong> {q['question']}</p>", unsafe_allow_html=True)
        user_answer = st.radio("Select your answer:", q['options'], key=f"q{i}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Check Answer", key=f"check{i}"):
                if q['options'].index(user_answer) == q['correct']:
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect. Try again! 🤔")
        with col2:
            if st.button("Show Explanation", key=f"explain{i}"):
                st.info(q['explanation'])
        st.markdown("---")

# Conclusion
st.markdown("<p class='big-font'>Congratulations! 🎊</p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'>You've explored the exciting world of sample spaces and events in probability. Keep practicing and exploring – probability is everywhere around us!</p>", unsafe_allow_html=True)