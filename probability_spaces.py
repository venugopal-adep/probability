import streamlit as st

# Set page layout to wide
st.set_page_config(layout="wide")

# Title and Introduction
st.title("Understanding Probability Spaces: An Interactive Learning Experience")
st.markdown("""
## Introduction to Probability Spaces
In probability theory, a **probability space** is a mathematical framework that models random experiments. It consists of three key components:
- **Sample Space (S)**: The set of all possible outcomes. For example, flipping a coin gives us a sample space of {Heads, Tails}.
- **Events (E)**: Specific outcomes or sets of outcomes within the sample space. For instance, rolling an even number on a die.
- **Probability (P)**: A numerical value representing the likelihood of an event occurring. It is calculated as the ratio of favorable outcomes to total possible outcomes.

Let's explore different scenarios to understand how probability spaces work in the real world.
""")

# Tabs for Examples
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Coin Toss", "Dice Roll", "Card Draw", "Weather Forecasting", "Frequently Asked Questions"])

# Tab 1: Coin Toss Example
with tab1:
    st.header("Coin Toss")
    st.image("https://example.com/coin_image.jpg", caption="Flipping a Coin", use_column_width=True)
    st.markdown("""
    A simple coin toss is one of the most basic examples of a probability space. When you flip a fair coin:
    - **Sample Space (S)**: {Heads, Tails}
    - **Event (E)**: Let's say the event is "getting heads".
    - **Probability (P)**: Since there are 2 possible outcomes and only 1 favorable outcome (heads), the probability is:
      \[
      P(\text{Heads}) = \frac{1}{2} = 0.5
      \]

    ### Fun Fact:
    Did you know that ancient Greeks used to flip coins to resolve disputes? This practice is known as "Heads or Tails."

    ### Quick Quiz
    What is the probability of getting tails in a fair coin toss?
    """)
    if st.button("Show Answer for Coin Toss"):
        st.write("The probability of getting tails is also 0.5, since the sample space has 2 outcomes and 1 favorable outcome (tails).")

# Tab 2: Dice Roll Example
with tab2:
    st.header("Dice Roll")
    st.image("https://example.com/dice_image.jpg", caption="Rolling a Die", use_column_width=True)
    st.markdown("""
    Rolling a fair six-sided die gives us a sample space with six outcomes:
    - **Sample Space (S)**: {1, 2, 3, 4, 5, 6}
    - **Event (E)**: Let's say the event is "rolling an even number".
    - **Probability (P)**: There are 3 favorable outcomes (2, 4, 6) out of 6 possible outcomes:
      \[
      P(\text{Even}) = \frac{3}{6} = 0.5
      \]

    ### Fun Fact:
    The oldest known dice were excavated from Mesopotamia and are believed to be around 5,000 years old!

    ### Quick Quiz
    What is the probability of rolling a 4 on a fair six-sided die?
    """)
    if st.button("Show Answer for Dice Roll"):
        st.write("The probability of rolling a 4 is 1/6, as there is only 1 favorable outcome out of 6 possible outcomes.")

# Tab 3: Card Draw Example
with tab3:
    st.header("Card Draw")
    st.image("https://example.com/cards_image.jpg", caption="Drawing a Card from a Deck", use_column_width=True)
    st.markdown("""
    A standard deck of cards contains 52 cards. If we draw a card at random:
    - **Sample Space (S)**: All 52 cards.
    - **Event (E)**: Let's say the event is "drawing an Ace".
    - **Probability (P)**: There are 4 Aces in the deck, so:
      \[
      P(\text{Ace}) = \frac{4}{52} = \frac{1}{13} \approx 0.077
      \]

    ### Fun Fact:
    The four suits in a deck of cards (hearts, diamonds, clubs, and spades) originated in France around the 15th century.

    ### Quick Quiz
    What is the probability of drawing a Queen from a standard deck of 52 cards?
    """)
    if st.button("Show Answer for Card Draw"):
        st.write("The probability of drawing a Queen is 4/52, as there are 4 Queens in the deck. This simplifies to 1/13 or approximately 0.077.")

# Tab 4: Weather Forecasting Example
with tab4:
    st.header("Weather Forecasting")
    st.image("https://example.com/weather_image.jpg", caption="Weather Prediction", use_column_width=True)
    st.markdown("""
    Weather forecasting involves predicting different weather conditions:
    - **Sample Space (S)**: {Sunny, Rainy, Cloudy, Snowy}.
    - **Event (E)**: Let's say the event is "Rainy".
    - **Probability (P)**: Based on historical data, if 100 days were observed and it rained on 30 of them:
      \[
      P(\text{Rainy}) = \frac{30}{100} = 0.3
      \]

    ### Fun Fact:
    Modern weather forecasting uses complex computer models that simulate the atmosphere's dynamics to predict weather patterns.

    ### Quick Quiz
    If it snowed on 20 out of 100 days, what would be the probability of a snowy day?
    """)
    if st.button("Show Answer for Weather Forecasting"):
        st.write("The probability of a snowy day would be 20/100 = 0.2.")

# Tab 5: Frequently Asked Questions
with tab5:
    st.header("Frequently Asked Questions")
    st.markdown("""
    **Q1: What is a sample space?**  
    A sample space is the set of all possible outcomes of a random experiment.

    **Q2: Can probabilities be greater than 1?**  
    No, probabilities range from 0 to 1, where 0 means an event is impossible, and 1 means an event is certain.

    **Q3: What is the difference between an event and an outcome?**  
    An outcome is a single possible result of an experiment, while an event is a set of one or more outcomes.

    **Q4: Why do we use probability spaces?**  
    Probability spaces help us model and understand random phenomena in a structured way.
    """)

    st.markdown("### Have more questions? Feel free to reach out in the comments section!")
