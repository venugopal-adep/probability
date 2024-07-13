import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy import stats

# Set page config
st.set_page_config(page_title="Normal Distribution in Real Life", layout="wide", initial_sidebar_state="expanded")

# Custom CSS to improve visual appeal
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #4e7dd1;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2c5282;
    }
    .stButton>button {
        background-color: #4e7dd1;
        color: white;
    }
    .stButton>button:hover {
        background-color: #2c5282;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("📊 Normal Distribution in Real Life")
st.write("**Developed by : Venugopal Adep**")
st.write("""
The normal distribution, also known as the Gaussian distribution, is a fundamental concept in statistics and probability theory. 
It's characterized by its distinctive "bell curve" shape and is defined by two parameters: the mean (μ) and the standard deviation (σ).

Explore real-life applications of the normal distribution in the interactive tabs below!
""")

# Function to create a bell curve
def create_bell_curve(mean, std_dev, title, x_label, highlight_value=None):
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    
    fig = go.Figure()
    
    # Add main curve
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution',
                             line=dict(color='#4e7dd1', width=2)))
    
    # Add mean line
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, max(y)], mode='lines', name='Mean',
                             line=dict(color='#2c5282', width=2, dash='dash')))
    
    # Highlight area if a value is provided
    if highlight_value is not None:
        highlight_y = stats.norm.pdf(highlight_value, mean, std_dev)
        fig.add_trace(go.Scatter(x=[highlight_value, highlight_value], y=[0, highlight_y], 
                                 mode='lines', name='Selected Value',
                                 line=dict(color='#e53e3e', width=2)))
        
        # Shade area
        x_fill = x[x <= highlight_value]
        y_fill = stats.norm.pdf(x_fill, mean, std_dev)
        fig.add_trace(go.Scatter(x=x_fill, y=y_fill, fill='tozeroy', 
                                 fillcolor='rgba(229, 62, 62, 0.3)', 
                                 line=dict(color='rgba(255, 255, 255, 0)'),
                                 name='Highlighted Area'))

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center'),
        xaxis_title=x_label,
        yaxis_title="Probability Density",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=40, t=40, b=40),
        hovermode="x unified"
    )
    return fig

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧠 IQ Scores", "📏 Human Height", "🏭 Manufacturing", "💹 Finance", "🐘 Natural Phenomena"])

with tab1:
    st.header("IQ Scores")
    st.write("IQ scores are designed to follow a normal distribution with a mean of 100 and a standard deviation of 15.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        iq_score = st.slider("Enter an IQ score:", min_value=40, max_value=160, value=100, step=1, key="iq")
    with col2:
        if st.button("Calculate IQ Percentile", key="iq_button"):
            percentile = stats.norm.cdf(iq_score, loc=100, scale=15)
            st.metric("Percentile", f"{percentile*100:.2f}%")
    
    st.plotly_chart(create_bell_curve(100, 15, "IQ Score Distribution", "IQ Score", iq_score), use_container_width=True)
    
    st.write(f"""
    **Explanation:**
    
    You've selected an IQ score of {iq_score}. Here's what this means:

    1. The average IQ score is 100. This is represented by the dashed line in the middle of the curve.
    2. About 68% of people have an IQ score between 85 and 115 (within one standard deviation of the mean).
    3. Your selected score of {iq_score} is {'above' if iq_score > 100 else 'below' if iq_score < 100 else 'exactly at'} the average.
    4. The red line on the graph shows where your selected IQ score falls on the distribution.
    5. The shaded area represents the percentage of people who have an IQ score at or below {iq_score}.

    For example, if you selected an IQ of 115:
    - This is one standard deviation above the mean.
    - About 84% of people would have an IQ score at or below this level.
    - This would be considered "above average" intelligence.

    Remember, IQ is just one measure of cognitive ability and doesn't capture all aspects of intelligence or potential.
    """)

with tab2:
    st.header("Human Height")
    st.write("Adult human heights within a population are normally distributed.")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        gender = st.radio("Select Gender:", ["Male", "Female"])
    with col2:
        height = st.number_input("Enter height (cm):", min_value=130, max_value=220, value=170, step=1, key="height")
    with col3:
        if st.button("Calculate Height Percentile", key="height_button"):
            mean = 175 if gender == "Male" else 162
            std_dev = 7
            percentile = stats.norm.cdf(height, loc=mean, scale=std_dev)
            st.metric("Percentile", f"{percentile*100:.2f}%")
    
    mean = 175 if gender == "Male" else 162
    st.plotly_chart(create_bell_curve(mean, 7, f"{gender} Height Distribution", "Height (cm)", height), use_container_width=True)
    
    st.write(f"""
    **Explanation:**
    
    You've selected a height of {height} cm for a {gender.lower()}. Here's what this means:

    1. The average height for {'men' if gender == 'Male' else 'women'} is about {mean} cm. This is represented by the dashed line in the middle of the curve.
    2. About 68% of {'men' if gender == 'Male' else 'women'} have a height between {mean-7} cm and {mean+7} cm (within one standard deviation of the mean).
    3. Your selected height of {height} cm is {'above' if height > mean else 'below' if height < mean else 'exactly at'} the average.
    4. The red line on the graph shows where your selected height falls on the distribution.
    5. The shaded area represents the percentage of {'men' if gender == 'Male' else 'women'} who are this height or shorter.

    For example, if you selected a height of 182 cm for a male:
    - This is one standard deviation above the mean for men.
    - About 84% of men would be this height or shorter.
    - This would be considered "tall" for a man.

    Remember, height varies across different populations and can be influenced by factors like nutrition and genetics.
    """)

with tab3:
    st.header("Manufacturing Tolerances")
    st.write("In manufacturing, product dimensions often follow a normal distribution around the target size.")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        target_size = st.number_input("Target Size (mm):", min_value=1, max_value=1000, value=100, step=1, key="target")
    with col2:
        tolerance = st.number_input("Tolerance (±mm):", min_value=0.1, max_value=10.0, value=0.5, step=0.1, key="tolerance")
    with col3:
        if st.button("Calculate Defect Rate", key="manufacturing_button"):
            defect_rate = 2 * (1 - stats.norm.cdf(tolerance / (target_size * 0.01)))
            st.metric("Defect Rate", f"{defect_rate*100:.2f}%")
    
    st.plotly_chart(create_bell_curve(target_size, target_size*0.01, "Product Size Distribution", "Size (mm)", target_size + tolerance), use_container_width=True)
    
    st.write(f"""
    **Explanation:**
    
    You've set a target size of {target_size} mm with a tolerance of ±{tolerance} mm. Here's what this means:

    1. The ideal product size is {target_size} mm. This is represented by the dashed line in the middle of the curve.
    2. Products are considered acceptable if they are within {target_size - tolerance} mm to {target_size + tolerance} mm.
    3. The red line on the graph shows the upper tolerance limit ({target_size + tolerance} mm).
    4. The shaded area represents the percentage of products that fall within the acceptable range.
    5. Products outside this range are considered defective.

    For example, if you set a target size of 100 mm with a tolerance of ±0.5 mm:
    - Acceptable products would be between 99.5 mm and 100.5 mm.
    - If the defect rate is 5%, it means that 95% of products fall within this range.
    - This implies that 5% of products are either smaller than 99.5 mm or larger than 100.5 mm.

    In manufacturing, tighter tolerances (smaller tolerance values) generally result in higher quality but may increase production costs and defect rates.
    """)

with tab4:
    st.header("Financial Returns")
    st.write("Short-term financial returns are often modeled using a normal distribution.")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        daily_return = st.slider("Enter daily return (%):", min_value=-10.0, max_value=10.0, value=0.5, step=0.1, key="return")
    with col2:
        volatility = st.slider("Market Volatility (%):", min_value=0.1, max_value=5.0, value=1.0, step=0.1, key="volatility")
    with col3:
        if st.button("Calculate Return Probability", key="finance_button"):
            probability = 1 - stats.norm.cdf(abs(daily_return) / volatility)
            st.metric("Probability of more extreme return", f"{probability*100:.2f}%")
    
    st.plotly_chart(create_bell_curve(0, volatility, "Daily Return Distribution", "Return (%)", daily_return), use_container_width=True)
    
    st.write(f"""
    **Explanation:**
    
    You've set a daily return of {daily_return}% with a market volatility of {volatility}%. Here's what this means:

    1. The average daily return is assumed to be 0% (neither gain nor loss). This is represented by the dashed line in the middle of the curve.
    2. The volatility ({volatility}%) represents the standard deviation of daily returns. Higher volatility means more unpredictable returns.
    3. About 68% of daily returns fall between -{volatility}% and +{volatility}% (within one standard deviation of the mean).
    4. The red line on the graph shows your selected daily return of {daily_return}%.
    5. The shaded area represents the probability of getting a return less than or equal to {daily_return}%.

    For example, if you set a daily return of 2% with a volatility of 1%:
    - This return is 2 standard deviations above the mean.
    - There's about a 2.3% chance of getting a return this high or higher on any given day.
    - Conversely, there's about a 97.7% chance of getting a return lower than this.

    Remember, in finance, higher potential returns often come with higher risk (volatility). Past performance doesn't guarantee future results.
    """)

with tab5:
    st.header("Natural Phenomena")
    st.write("Many natural phenomena, such as birth weights of a species, follow a normal distribution.")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        species = st.selectbox("Select Species:", ["Human", "Elephant", "Penguin"])
    with col2:
        if species == "Human":
            birth_weight = st.slider("Enter birth weight (kg):", min_value=1.0, max_value=6.0, value=3.5, step=0.1, key="weight")
            mean, std_dev = 3.5, 0.5
        elif species == "Elephant":
            birth_weight = st.slider("Enter birth weight (kg):", min_value=50.0, max_value=190.0, value=120.0, step=1.0, key="weight")
            mean, std_dev = 120, 15
        else:  # Penguin
            birth_weight = st.slider("Enter birth weight (kg):", min_value=0.05, max_value=0.15, value=0.1, step=0.01, key="weight")
            mean, std_dev = 0.1, 0.02
    with col3:
        if st.button("Calculate Birth Weight Percentile", key="nature_button"):
            percentile = stats.norm.cdf(birth_weight, loc=mean, scale=std_dev)
            st.metric("Percentile", f"{percentile*100:.2f}%")
    
    st.plotly_chart(create_bell_curve(mean, std_dev, f"{species} Birth Weight Distribution", "Weight (kg)", birth_weight), use_container_width=True)
    
    st.write(f"""
    **Explanation:**
    
    You've selected a birth weight of {birth_weight} kg for a {species.lower()}. Here's what this means:

    1. The average birth weight for a {species.lower()} is about {mean} kg. This is represented by the dashed line in the middle of the curve.
    2. About 68% of {species.lower()}s have a birth weight between {mean-std_dev:.2f} kg and {mean+std_dev:.2f} kg (within one standard deviation of the mean).
    3. Your selected birth weight of {birth_weight} kg is {'above' if birth_weight > mean else 'below' if birth_weight < mean else 'exactly at'} the average.
    4. The red line on the graph shows where your selected birth weight falls on the distribution.
    5. The shaded area represents the percentage of {species.lower()}s that have this birth weight or less.

    For example, if you selected a birth weight of 4 kg for a human baby:
    - This is one standard deviation above the mean.
    - About 84% of human babies would have a birth weight at or below this level.
    - This would be considered a "large" baby, but still within a normal range.

    Remember, while birth weights tend to follow a normal distribution, factors like genetics, nutrition, and environmental conditions can influence individual cases.
    """)

# Add an explanation about the application
st.sidebar.title("About this app")
st.sidebar.write("""
This interactive application demonstrates five real-life applications of the normal distribution:

1. 🧠 IQ Scores
2. 📏 Human Height
3. 🏭 Manufacturing Tolerances
4. 💹 Financial Returns
5. 🐘 Natural Phenomena (Birth Weights)

Each tab allows you to interact with the normal distribution in a different context. 
Enter values using the sliders and input fields, then see how they relate to the normal distribution for each scenario.

The visualizations update in real-time as you change the inputs!
""")

# Add a fun fact section
st.sidebar.title("📚 Fun Fact")
fun_facts = [
    "The normal distribution is also known as the 'bell curve' due to its shape.",
    "About 68% of the data falls within one standard deviation of the mean in a normal distribution.",
    "The normal distribution was first introduced by Abraham de Moivre in 1733.",
    "The Central Limit Theorem states that the sampling distribution of the mean approaches a normal distribution as the sample size gets larger.",
    "Many natural phenomena, such as human height and IQ scores, closely follow a normal distribution.",
    "The normal distribution is symmetric, meaning it's the same on both sides of the center.",
    "In a normal distribution, the mean, median, and mode are all equal.",
    "The 'empirical rule' states that 68%, 95%, and 99.7% of the data fall within 1, 2, and 3 standard deviations of the mean, respectively.",
    "The normal distribution is used in many fields, including psychology, biology, and finance.",
    "The standard normal distribution has a mean of 0 and a standard deviation of 1."
]
st.sidebar.info(np.random.choice(fun_facts))

# Add a footer
st.markdown("""
---
Created with ❤️ using Streamlit | Data is for demonstration purposes only
""")
