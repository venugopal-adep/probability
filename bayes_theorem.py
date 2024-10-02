import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")


# Title of the Streamlit application
st.title("Interactive Application on Bayes' Theorem with Use Case Scenarios")

# Introduction
st.markdown("""
## Understanding Bayes' Theorem
Bayes’ theorem allows us to update our predictions or beliefs based on new information. It calculates the likelihood of an event occurring given prior knowledge or probability.

**General Formula**:
""")

# Displaying the general Bayes' theorem formula
st.latex(r'''P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}''')

st.markdown("""
Where:
- **P(A | B)**: Probability of event A occurring given that B is true (Posterior Probability)
- **P(B | A)**: Probability of event B occurring given that A is true (Likelihood)
- **P(A)**: Probability of event A occurring (Prior)
- **P(B)**: Probability of event B occurring (Evidence)

Let's explore some specific use cases using this formula.
""")

# Creating tabs for each use case
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Medical Diagnosis", "Weather Forecasting", "Spam Filtering", "Search and Rescue", "Predictive Text & Machine Learning", "Flight Incident"])

# Use Case 1: Medical Diagnosis
with tab1:
    st.header("Medical Diagnosis")
    st.markdown("""
    ### Example: Disease Test
    Suppose you want to find out if a student has a sickness based on a test result.

    **Formula Customized for this Case**:
    """)
    st.latex(r'''P(\text{Sickness}|\text{Test Positive}) = \frac{P(\text{Test Positive}|\text{Sickness}) \cdot P(\text{Sickness})}{P(\text{Test Positive})}''')

    st.markdown("""
    - **P(Sickness | Test Positive)**: Probability the student is sick given the test result is positive.
    - **P(Test Positive | Sickness)**: Probability the test is positive if the student is actually sick (True Positive Rate).
    - **P(Sickness)**: Probability the student has the sickness (Prior Probability).
    - **P(Test Positive)**: Probability the test gives a positive result (includes both true and false positives).

    Use the sliders below to explore how changing these values affects the final probability.
    """)

    # Input parameters for the medical diagnosis example
    prior_prob = st.slider("Prior probability of having the sickness (P(Sickness))", min_value=0.0, max_value=1.0, value=0.2, step=0.01, key="med_prior")
    test_sensitivity = st.slider("Test sensitivity (P(Test Positive | Sickness))", min_value=0.0, max_value=1.0, value=0.9, step=0.01, key="med_sensitivity")
    test_specificity = st.slider("Test specificity (P(Test Negative | No Sickness))", min_value=0.0, max_value=1.0, value=0.7, step=0.01, key="med_specificity")

    # Calculating derived parameters for medical diagnosis
    false_positive_rate = 1 - test_specificity
    p_test_positive = (prior_prob * test_sensitivity) + ((1 - prior_prob) * false_positive_rate)
    posterior_prob = (test_sensitivity * prior_prob) / p_test_positive

    # Displaying the result
    st.markdown(f"### Result: Probability of sickness given a positive test result: **{posterior_prob:.2f}**")

# Use Case 2: Weather Forecasting
with tab2:
    st.header("Weather Forecasting")
    st.markdown("""
    ### Example: Rain on a Cloudy Day
    Suppose you want to predict the probability of rain given that the morning is cloudy.

    **Formula Customized for this Case**:
    """)
    st.latex(r'''P(\text{Rain}|\text{Cloudy}) = \frac{P(\text{Cloudy}|\text{Rain}) \cdot P(\text{Rain})}{P(\text{Cloudy})}''')

    st.markdown("""
    - **P(Rain | Cloudy)**: Probability it will rain given that it's cloudy.
    - **P(Cloudy | Rain)**: Probability of a cloudy morning if it rains.
    - **P(Rain)**: Probability it rains (Prior Probability).
    - **P(Cloudy)**: Probability of a cloudy morning.

    Use the sliders below to explore this weather forecasting scenario.
    """)

    # Input parameters for the weather forecasting example
    rain_prob = st.slider("Probability of rain (P(Rain))", min_value=0.0, max_value=1.0, value=0.1, step=0.01, key="weather_rain")
    cloudy_given_rain = st.slider("Probability of cloudy morning given rain (P(Cloudy | Rain))", min_value=0.0, max_value=1.0, value=0.5, step=0.01, key="weather_cloudy_given_rain")
    cloudy_prob = st.slider("Probability of a cloudy morning (P(Cloudy))", min_value=0.0, max_value=1.0, value=0.4, step=0.01, key="weather_cloudy")

    # Calculating posterior probability for weather forecasting
    posterior_prob_weather = (cloudy_given_rain * rain_prob) / cloudy_prob

    # Displaying the result
    st.markdown(f"### Result: Probability of rain given a cloudy morning: **{posterior_prob_weather:.2f}**")

# Use Case 3: Spam Filtering
with tab3:
    st.header("Spam Filtering")
    st.markdown("""
    ### Example: Identifying Spam Emails
    Suppose you want to calculate the probability that an email is spam based on the presence of certain words.

    **Formula Customized for this Case**:
    """)
    st.latex(r'''P(\text{Spam}|\text{Words}) = \frac{P(\text{Words}|\text{Spam}) \cdot P(\text{Spam})}{P(\text{Words})}''')

    st.markdown("""
    - **P(Spam | Words)**: Probability the email is spam given certain words are present.
    - **P(Words | Spam)**: Probability of these words appearing in a spam email.
    - **P(Spam)**: Probability an email is spam (Prior Probability).
    - **P(Words)**: Probability of the words appearing in any email.

    Customize the parameters to understand spam filtering.
    """)

# Use Case 4: Search and Rescue
with tab4:
    st.header("Search and Rescue")
    st.markdown("""
    ### Example: Finding a Lost Object
    Suppose you are trying to find a lost object based on search patterns.

    **Formula Customized for this Case**:
    """)
    st.latex(r'''P(\text{Found}|\text{Search}) = \frac{P(\text{Search}|\text{Found}) \cdot P(\text{Found})}{P(\text{Search})}''')

    st.markdown("""
    - **P(Found | Search)**: Probability the object is found given the search area.
    - **P(Search | Found)**: Probability of searching in a particular area if the object is there.
    - **P(Found)**: Probability the object is in the search area (Prior Probability).
    - **P(Search)**: Probability of choosing the search area.

    Adjust the parameters to simulate a search scenario.
    """)

# Use Case 5: Predictive Text & Machine Learning
with tab5:
    st.header("Predictive Text & Machine Learning")
    st.markdown("""
    ### Example: Predicting the Next Word
    Suppose you want to predict the next word in a sentence based on previous words.

    **Formula Customized for this Case**:
    """)
    st.latex(r'''P(\text{Next Word}|\text{Previous Words}) = \frac{P(\text{Previous Words}|\text{Next Word}) \cdot P(\text{Next Word})}{P(\text{Previous Words})}''')

    st.markdown("""
    - **P(Next Word | Previous Words)**: Probability of the next word given the previous words.
    - **P(Previous Words | Next Word)**: Probability of the previous words given the next word.
    - **P(Next Word)**: Probability of the next word (Prior Probability).
    - **P(Previous Words)**: Probability of the previous words appearing.

    Explore how predictive text applications use Bayes' theorem.
    """)

# Use Case 6: Flight Incident
with tab6:
    st.header("Flight Incident")
    st.markdown("""
    ### Example: Probability of Death Given Boarding a Flight
    Suppose you want to estimate the probability that a person dies given they boarded a flight.

    **Formula Customized for this Case**:
    """)
    st.latex(r'''P(\text{Death}|\text{Boarded Flight}) = \frac{P(\text{Boarded Flight}|\text{Death}) \cdot P(\text{Death})}{P(\text{Boarded Flight})}''')

    st.markdown("""
    - **P(Death | Boarded Flight)**: Probability of death given that the person boarded a flight.
    - **P(Boarded Flight | Death)**: Probability that a person who died had boarded a flight.
    - **P(Death)**: Probability of death (Prior Probability).
    - **P(Boarded Flight)**: Probability of boarding a flight.

    Use the sliders below to explore how the probability changes with different conditions.
    """)

    # Setting the sliders for input values
    death_prob = st.slider("Probability of death (P(Death))", min_value=0.0, max_value=1.0, value=0.0001, step=0.0001, key="flight_death")
    flight_given_death = st.slider("Probability of boarding a flight given death (P(Boarded Flight | Death))", min_value=0.0, max_value=1.0, value=0.01, step=0.01, key="flight_given_death")
    flight_prob = st.slider("Probability of boarding a flight (P(Boarded Flight))", min_value=0.0, max_value=1.0, value=0.1, step=0.01, key="flight_prob")

    # Calculating posterior probability for the flight incident
    if flight_prob > 0:  # Ensure we don't divide by zero
        posterior_prob_flight = (flight_given_death * death_prob) / flight_prob
    else:
        posterior_prob_flight = 0

    # Displaying the result
    st.markdown(f"### Result: Probability of death given that the person boarded a flight: **{posterior_prob_flight:.6f}**")


# Conclusion
st.markdown("### Explore each tab to see how Bayes' theorem is applied in different scenarios using specific examples and simple language.")
