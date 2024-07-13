import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import binom
import plotly.express as px

def main():
    st.set_page_config(page_title="Rainfall Explorer", page_icon="🌧️", layout="wide")
    st.write("**Developed by : Venugopal Adep**")
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1E90FF;
    }
    .medium-font {
        font-size:20px !important;
        color: #4682B4;
    }
    .small-font {
        font-size:14px !important;
        color: #708090;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page title with custom styling
    st.markdown('<p class="big-font">🌧️ Rainfall Probability Explorer</p>', unsafe_allow_html=True)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📚 Introduction", "🧮 Calculator", "📊 Visualizations", "🧠 Quiz", "💡 Real-world Insights", "🌍 Applications"])
    
    with tab1:
        display_introduction()
    
    with tab2:
        display_interactive_calculator()
    
    with tab3:
        display_visualizations()
    
    with tab4:
        display_quiz()
    
    with tab5:
        display_real_world_considerations()
    
    with tab6:
        display_applications()

def display_introduction():
    st.markdown('<p class="medium-font">Understanding Rainfall Patterns</p>', unsafe_allow_html=True)
    st.write("""
    Welcome to the Rainfall Probability Explorer! This interactive app helps you understand
    the fascinating world of rainfall patterns and probability distributions. We'll use the
    binomial distribution to model rainfall occurrences and explore how different factors
    affect the likelihood of rainy days.
    """)
    
    st.info("Did you know? The binomial distribution is not just for rainfall. It's used in many fields, including genetics, quality control, and even predicting election outcomes!")
    
    st.subheader("The Scenario")
    st.write("""
    Imagine you're planning an outdoor event next month. You want to know the chances of
    having more than a certain number of rainy days. Let's dive in and calculate these
    probabilities!
    """)

def display_interactive_calculator():
    st.markdown('<p class="medium-font">Interactive Probability Calculator</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        n_days = st.slider("Number of days in the month", 28, 31, 30)
        rain_prob = st.slider("Daily probability of rain", 0.0, 1.0, 0.2, 0.01)
        threshold = st.slider("Threshold (more than X days of rain)", 0, n_days-1, 10)

    with col2:
        st.markdown('<p class="small-font">Binomial Distribution Formula:</p>', unsafe_allow_html=True)
        st.latex(r"""
        P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
        """)
        st.markdown('<p class="small-font">Where:</p>', unsafe_allow_html=True)
        st.write("""
        - n is the number of trials (days in the month)
        - k is the number of successes (rainy days)
        - p is the probability of success on each trial (daily rain probability)
        """)

    # Calculate probabilities
    x = np.arange(0, n_days + 1)
    pmf = binom.pmf(x, n_days, rain_prob)
    cdf = binom.cdf(x, n_days, rain_prob)

    # Create and display plot
    fig = create_distribution_plot(x, pmf, cdf, threshold)
    st.plotly_chart(fig, use_container_width=True)

    # Display calculated probability
    probability = 1 - binom.cdf(threshold, n_days, rain_prob)
    st.success(f"The probability of having more than {threshold} rainy days: {probability:.4f}")

    # Solved numerical example
    st.markdown('<p class="small-font">Solved Example:</p>', unsafe_allow_html=True)
    st.write(f"""
    Given:
    - Number of days (n) = {n_days}
    - Daily rain probability (p) = {rain_prob:.2f}
    - Threshold (k) = {threshold}

    Step 1: Calculate the probability of having exactly {threshold+1} rainy days
    P(X = {threshold+1}) = C({n_days}, {threshold+1}) * {rain_prob:.2f}^{threshold+1} * (1-{rain_prob:.2f})^{n_days-(threshold+1)}
    = {binom.pmf(threshold+1, n_days, rain_prob):.6f}

    Step 2: Sum the probabilities for all values above the threshold
    P(X > {threshold}) = P(X = {threshold+1}) + P(X = {threshold+2}) + ... + P(X = {n_days})
    = {probability:.6f}
    """)

def create_distribution_plot(x, pmf, cdf, threshold):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=pmf, name="Probability Mass Function", marker_color='lightblue'))
    fig.add_trace(go.Scatter(x=x, y=cdf, mode="lines", name="Cumulative Distribution Function", line=dict(color='darkblue')))
    
    # Add a vertical line for the threshold
    fig.add_vline(x=threshold, line_dash="dash", line_color="red", annotation_text=f"Threshold: {threshold}", annotation_position="top right")
    
    fig.update_layout(
        title="Binomial Distribution of Rainy Days",
        xaxis_title="Number of Rainy Days",
        yaxis_title="Probability",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    return fig

def display_visualizations():
    st.markdown('<p class="medium-font">Rainfall Pattern Visualizations</p>', unsafe_allow_html=True)
    
    # Seasonal rainfall pattern
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    rainfall = [50, 40, 60, 80, 100, 120, 140, 130, 110, 90, 70, 60]
    
    fig_seasonal = px.line(x=months, y=rainfall, labels={'x': 'Month', 'y': 'Average Rainfall (mm)'}, title='Seasonal Rainfall Pattern')
    st.plotly_chart(fig_seasonal, use_container_width=True)
    
    st.write("This chart shows a typical seasonal rainfall pattern. Notice how rainfall varies throughout the year, violating our assumption of constant probability.")

    # Rainy day clustering
    days = list(range(1, 31))
    rain_status = [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]
    
    fig_clustering = px.bar(x=days, y=rain_status, labels={'x': 'Day of Month', 'y': 'Rain Status (1=Rain, 0=No Rain)'}, title='Rainy Day Clustering')
    st.plotly_chart(fig_clustering, use_container_width=True)
    
    st.write("This chart illustrates how rainy days often cluster together, violating our assumption of independence between days.")

def display_quiz():
    st.markdown('<p class="medium-font">Test Your Knowledge</p>', unsafe_allow_html=True)
    
    questions = [
        {
            "question": "If the daily probability of rain is 0.3 and we're considering a 30-day month, what's the expected number of rainy days?",
            "options": ["5 days", "9 days", "15 days", "21 days"],
            "correct": 1,
            "explanation": """
            The expected number of rainy days is calculated by multiplying the number of days by the daily probability of rain.

            In this case: 30 days * 0.3 = 9 days

            Think of it like this: If you flip a coin that lands heads 30% of the time, and you flip it 100 times, you'd expect to get heads about 30 times. Similarly, if it rains 30% of the time, in 30 days, you'd expect about 9 rainy days.

            Remember, this is an average. In reality, you might get more or fewer rainy days, but over many months, it would average out to about 9 days per month.
            """
        },
        {
            "question": "Which of the following violates the assumptions of our binomial distribution model for rainfall?",
            "options": ["The chance of rain is constant throughout the month", "Rainy days occur independently of each other", "The probability of rain increases during certain seasons", "There are exactly two outcomes: rain or no rain"],
            "correct": 2,
            "explanation": """
            The binomial distribution model for rainfall assumes that the probability of rain is constant and that each day's weather is independent of other days. The option that violates these assumptions is:

            "The probability of rain increases during certain seasons"

            This violates the assumption of constant probability. In reality, seasons do affect rainfall:

            1. Constant probability (assumption): Imagine a game where you roll a die, and it rains if you roll a 6. The chance is always 1/6, regardless of when you play.

            2. Seasonal changes (reality): It's more like playing different games depending on the season. In the rainy season, you might rain if you roll 4, 5, or 6 (higher chance), while in the dry season, it might only rain on a 6 (lower chance).

            The other options align with the binomial model's assumptions:
            - Constant chance throughout the month (assumed in the model)
            - Independent occurrences (assumed in the model)
            - Two outcomes: rain or no rain (part of the binomial model definition)
            """
        },
        {
            "question": "If rainy days tend to cluster together, how does this affect the probability of having long dry spells compared to our binomial model?",
            "options": ["Increases the probability", "Decreases the probability", "Has no effect on the probability", "Cannot be determined"],
            "correct": 0,
            "explanation": """
            When rainy days cluster together, it increases the probability of having long dry spells compared to our binomial model.

            Binomial model (independent events):
            Imagine flipping a coin where heads = rain, tails = no rain. Each flip is independent, so you might get a random mix like:
            HTHTHTHTHT (H = rain, T = no rain)

            Reality (clustered events):
            Rainy days often come together, so you might see a pattern more like:
            HHHHTTTTTHHHHTTTTT

            In the clustered pattern, you're more likely to see longer streaks of both rainy and dry days. This means:
            1. When it rains, it's more likely to keep raining for a while.
            2. When it's dry, it's more likely to stay dry for a longer period.

            So, compared to the binomial model, clustering increases the chances of both long rainy periods and long dry spells. This is why weather forecasts often talk about "rainy seasons" or "dry spells" rather than predicting each day independently.
            """
        }
    ]
    
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer {i+1}"):
            if q["options"].index(answer) == q["correct"]:
                st.success("Correct! Well done!")
            else:
                st.error(f"Not quite. The correct answer is: {q['options'][q['correct']]}")
            
            st.markdown("### Explanation")
            st.write(q["explanation"])
            st.write("---")

def display_real_world_considerations():
    st.markdown('<p class="medium-font">Real-world Insights</p>', unsafe_allow_html=True)
    st.write("""
    While our binomial distribution model provides a useful approximation, real-world weather patterns are far more complex. Here are some factors that challenge our assumptions:
    """)
    
    factors = [
        ("🌡️ Climate Change", "Long-term shifts in weather patterns can affect rainfall probabilities over time."),
        ("🌪️ Extreme Weather Events", "Unusual weather phenomena can drastically alter expected rainfall patterns."),
        ("🏞️ Geographic Variations", "Local topography and proximity to water bodies can influence rainfall probabilities."),
        ("🌍 Global Weather Systems", "Large-scale atmospheric patterns like El Niño can affect rainfall across entire regions.")
    ]
    
    for emoji, factor in factors:
        st.markdown(f"**{emoji} {factor}**")
    
    st.info("Remember: While probability models are useful tools, always consult professional meteorologists and climate scientists for accurate weather predictions and climate insights!")

def display_applications():
    st.markdown('<p class="medium-font">Real-Life Applications of Binomial Distribution</p>', unsafe_allow_html=True)
    st.write("""
    The binomial distribution is a powerful tool that finds applications in various fields. 
    Let's explore five real-life scenarios where this distribution proves invaluable.
    """)

    applications = [
        {
            "title": "1. Quality Control in Manufacturing",
            "description": """
            Imagine you're running a lightbulb factory. You want to ensure that no more than 5% of the bulbs are defective. 
            To check this, you randomly select 100 bulbs from a large batch and test them.

            How it works:
            - Each bulb is either defective (failure) or not (success).
            - You're performing 100 independent trials (testing 100 bulbs).
            - The probability of a defective bulb should be 5% or less.

            Using the binomial distribution, you can calculate the probability of finding different numbers of defective bulbs in your sample. 
            If you find too many defectives, it might indicate a problem in the manufacturing process.

            Example: If 8 out of 100 tested bulbs are defective, is this within acceptable limits?
            You can use the binomial distribution to determine how likely it is to get 8 or more defectives if the true defect rate is 5%. 
            If this probability is very low, it might suggest your manufacturing process needs adjustment.
            """
        },
        {
            "title": "2. Clinical Trials in Medicine",
            "description": """
            Clinical trials often use the binomial distribution to analyze the effectiveness of new treatments.

            Scenario: A new drug is being tested to see if it's better than the current standard treatment. 
            200 patients are randomly assigned to either the new drug or the standard treatment (100 each).

            How it works:
            - Each patient either responds positively to the treatment (success) or doesn't (failure).
            - You have 100 independent trials for each treatment.
            - You compare the number of successes between the two groups.

            The binomial distribution helps determine if the difference in success rates between the two groups is statistically significant 
            or if it could have occurred by chance.



            Example: If 60 patients respond positively to the new drug, compared to 45 for the standard treatment, 
            is this difference significant enough to conclude the new drug is better?
            """
        },
        {
            "title": "3. Election Predictions",
            "description": """
            Political analysts often use the binomial distribution to model election outcomes and create predictions.

            Scenario: In an upcoming election, candidate A is polling at 52% support. 
            A news organization wants to predict the likelihood of candidate A winning.

            How it works:
            - Each voter either votes for candidate A (success) or doesn't (failure).
            - There are millions of independent "trials" (voters).
            - The probability of "success" (voting for A) is estimated at 52%.

            Using the binomial distribution (or its normal approximation for large numbers), analysts can calculate 
            the probability of candidate A getting more than 50% of the votes.

            Example: In a state with 1,000,000 voters, what's the probability that candidate A will get at least 510,000 votes (51%)?
            This calculation helps in predicting the election outcome and understanding the uncertainty in the prediction.
            """
        },
        {
            "title": "4. Genetics and Inheritance",
            "description": """
            The binomial distribution is crucial in genetics for understanding how traits are inherited.

            Scenario: In pea plants, the allele for purple flowers (P) is dominant over white flowers (p). 
            If both parent plants are heterozygous (Pp), what's the likelihood of their offspring having purple flowers?

            How it works:
            - Each offspring either inherits the dominant allele (success) or doesn't (failure).
            - Each birth is an independent trial.
            - The probability of inheriting at least one P allele is 75% (PP, Pp, or pP, but not pp).

            Geneticists use the binomial distribution to predict the distribution of traits in a population and to analyze 
            the results of breeding experiments.

            Example: If these plants have 20 offspring, what's the probability that 18 or more will have purple flowers?
            This helps geneticists understand if their observed results match theoretical expectations.
            """
        },
        {
            "title": "5. Customer Behavior Analysis",
            "description": """
            Businesses use the binomial distribution to analyze and predict customer behavior.

            Scenario: An online store finds that historically, 30% of visitors to their site make a purchase. 
            They want to use this information for planning and analysis.

            How it works:
            - Each visitor either makes a purchase (success) or doesn't (failure).
            - Each visit is considered an independent event.
            - The probability of a purchase is 30%.

            The binomial distribution can help answer questions like:
            - What's the probability of getting 15 or more sales from the next 40 visitors?
            - How likely is it to have a day with no sales if they average 50 visitors per day?

            Example: If the store gets 100 visitors in a day, what's the probability of having at least 40 sales?
            This information can be used for inventory planning, staffing decisions, and setting realistic sales targets.
            """
        }
    ]

    for app in applications:
        st.subheader(app["title"])
        st.write(app["description"])
        st.write("---")

if __name__ == "__main__":
    main()
