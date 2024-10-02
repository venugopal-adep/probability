import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Probability Mastery Quiz", layout="wide")

# Custom CSS for improved aesthetics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #f0f4f8;
        color: #1e1e1e;
    }
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #2c3e50;
        text-align: center;
    }
    .stTabs {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
    }
    .question-box {
        background-color: #e0f2fe;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-weight: 600;
        padding: 10px 20px;
        border-radius: 30px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .score-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        background-color: #d5f5e3;
        color: #27ae60;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feedback-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feedback-correct {
        background-color: #d4edda;
        color: #155724;
    }
    .feedback-incorrect {
        background-color: #f8d7da;
        color: #721c24;
    }
    .explanation-box {
        background-color: #e9ecef;
        border-left: 5px solid #3498db;
        padding: 15px;
        margin-top: 20px;
        border-radius: 5px;
    }
    .topic-header {
        background-color: #3498db;
        color: white;
        padding: 10px;
        border-radius: 10px 10px 0 0;
        text-align: center;
        font-weight: bold;
    }
    .quiz-container {
        background-color: white;
        border-radius: 0 0 10px 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🎲 Probability Mastery Quiz")
st.markdown("""
Welcome to the Probability Mastery Quiz! Test your knowledge on various probability concepts and sharpen your statistical skills. 
Choose a topic below to get started. Good luck! 🍀
""")

# Define quiz topics and their respective questions
quiz_topics = {
    "Random Variables": [
        {
            "question": "What does a random variable do in an experiment?",
            "correct_answer": "Assigns a numerical value to each outcome",
            "incorrect_answer": "Determines the outcome of the experiment",
            "explanation": "A random variable is like a special label maker. In an experiment, it gives each possible result a number tag. For example, in a coin toss, it might label 'heads' as 1 and 'tails' as 0. This way, we can do math with the results!"
        },
        {
            "question": "In a fair coin toss experiment (two tosses), what's the chance of getting two heads?",
            "correct_answer": "1/4",
            "incorrect_answer": "1/2",
            "explanation": "Imagine you're flipping a coin twice. To get two heads, you need 'heads' on the first flip AND 'heads' on the second flip. The chance of each is 1/2, so together it's 1/2 × 1/2 = 1/4. It's like rolling a four-sided die and hoping for a specific number!"
        },
        {
            "question": "Which type of random variable can take on any value within a range?",
            "correct_answer": "Continuous",
            "incorrect_answer": "Discrete",
            "explanation": "A continuous random variable is like measuring something with a super-precise ruler. It can be any value in a range, even tiny fractions. Think of your height - it's not just 5 or 6 feet, but could be 5.7231... feet. Discrete variables, on the other hand, are like counting whole things, like the number of cars in a parking lot."
        }
    ],
    "Probability Distributions": [
        {
            "question": "What does a probability distribution describe?",
            "correct_answer": "Values a random variable can take and their probabilities",
            "incorrect_answer": "Only the possible outcomes of an experiment",
            "explanation": "A probability distribution is like a recipe for chance. It tells you not just what ingredients (values) you might get, but also how likely each one is. It's your roadmap to understanding all the possible outcomes and their chances of happening."
        },
        {
            "question": "What does a probability mass function provide for a discrete random variable?",
            "correct_answer": "The probability for each value of the random variable",
            "incorrect_answer": "The range of values the random variable can take",
            "explanation": "Think of a probability mass function as a menu of chances. For each item (value) on the menu, it tells you exactly how likely you are to 'order' it. It's like knowing the odds of rolling each number on a die."
        },
        {
            "question": "What does a probability density function determine for a continuous random variable?",
            "correct_answer": "The probability with which the variable lies in a given interval",
            "incorrect_answer": "The exact probability of any single value",
            "explanation": "Imagine a probability density function as a weather map for chances. It doesn't tell you the exact chance of a specific temperature (because there are infinitely many!), but it shows you how likely temperatures are in different ranges. It's like saying it's more likely to be 70-80°F than 90-100°F tomorrow."
        }
    ],
    "Binomial Distribution": [
        {
            "question": "What is the main characteristic of a binomial distribution?",
            "correct_answer": "It models the number of successes in fixed trials with two outcomes",
            "incorrect_answer": "It models continuous data with equal probability",
            "explanation": "The binomial distribution is perfect for scenarios where you're counting successes (like winning lottery tickets) in a fixed number of trials (like 10 tickets), each with only two possible outcomes (win or lose)."
        },
        {
            "question": "Which of these is NOT an assumption of the binomial distribution?",
            "correct_answer": "The probability of success changes for each trial",
            "incorrect_answer": "The trials are independent",
            "explanation": "In a binomial distribution, the probability of success must remain constant for each trial. The other assumptions are: two possible outcomes, fixed number of trials, and independent trials."
        },
        {
            "question": "When does a binomial distribution become a Bernoulli distribution?",
            "correct_answer": "When the number of trials is equal to 1",
            "incorrect_answer": "When the probability of success is 0.5",
            "explanation": "A Bernoulli distribution is a special case of the binomial distribution where there's only one trial. It's like a single coin flip instead of multiple flips."
        }
    ],
    "Uniform Distribution": [
        {
            "question": "What is the key characteristic of a uniform distribution?",
            "correct_answer": "All outcomes are equally likely",
            "incorrect_answer": "Outcomes cluster around a central value",
            "explanation": "In a uniform distribution, every possible outcome has the same probability. It's like a perfectly fair die where each number has an equal chance of being rolled."
        },
        {
            "question": "Which is an example of a discrete uniform distribution?",
            "correct_answer": "Rolling a single die",
            "incorrect_answer": "Weight gained over 2 months",
            "explanation": "Rolling a single die is a perfect example of a discrete uniform distribution. Each number (1 to 6) has an equal probability of being rolled, and there are a finite number of possible outcomes."
        },
        {
            "question": "In a continuous uniform distribution, what can the random variable be?",
            "correct_answer": "Any value within a given range",
            "incorrect_answer": "Only whole numbers within a range",
            "explanation": "A continuous uniform distribution allows the random variable to be any value within a specified range. For example, a person's weight gain could be any value between 2 and 5 kg, including fractional values."
        }
    ],
    "Normal Distribution": [
        {
            "question": "What shape does the graph of a normal distribution resemble?",
            "correct_answer": "A bell curve",
            "incorrect_answer": "A straight line",
            "explanation": "The normal distribution graph looks like a symmetrical bell-shaped curve. This is why it's often called the 'bell curve'."
        },
        {
            "question": "In a normal distribution, which of these is true?",
            "correct_answer": "Mean = Median = Mode",
            "incorrect_answer": "Mean > Median > Mode",
            "explanation": "In a normal distribution, the mean, median, and mode are all equal. This is due to the perfect symmetry of the distribution."
        },
        {
            "question": "What is a characteristic of the standard normal distribution?",
            "correct_answer": "It has a mean of 0 and a standard deviation of 1",
            "incorrect_answer": "It has a mean of 1 and a standard deviation of 0",
            "explanation": "A standard normal distribution is a special case where the mean is centered at 0 and the standard deviation is exactly 1. This standardization makes it easier to compare different normal distributions."
        }
    ],
    "Sampling Distributions": [
        {
            "question": "Why do we use sampling in statistics?",
            "correct_answer": "To make inferences about a population when studying the entire population is not feasible",
            "incorrect_answer": "To increase the complexity of a study",
            "explanation": "Sampling allows us to study a smaller, manageable subset of a population and make educated guesses about the entire population. It's like tasting a spoonful of soup to judge the flavor of the whole pot."
        },
        {
            "question": "What is a sampling distribution?",
            "correct_answer": "A distribution of a sample statistic from all possible samples of a population",
            "incorrect_answer": "The distribution of the entire population",
            "explanation": "A sampling distribution shows how a particular statistic (like the mean) would vary if we took many different samples from the same population. It's like seeing all possible 'snapshots' of the population."
        },
        {
            "question": "In the example of testing a new drug, why is sampling used?",
            "correct_answer": "It's almost impossible to test the drug on an entire country's population",
            "incorrect_answer": "To make the study more expensive",
            "explanation": "Testing a new drug on an entire population would be impractical, time-consuming, and extremely costly. Sampling allows researchers to draw conclusions about the drug's effects using a smaller, representative group of people."
        }
    ],
    "Central Limit Theorem": [
        {
            "question": "What does the Central Limit Theorem state about sampling distributions?",
            "correct_answer": "They approach a normal distribution as sample size increases",
            "incorrect_answer": "They always match the population distribution",
            "explanation": "The Central Limit Theorem says that no matter what shape the population distribution has, the sampling distribution of the means will become more normal as we increase the sample size. It's like magic that turns any distribution into a bell curve!"
        },
        {
            "question": "What is a key assumption of the Central Limit Theorem?",
            "correct_answer": "Samples should be randomly selected",
            "incorrect_answer": "The population must be normally distributed",
            "explanation": "Random sampling is crucial for the Central Limit Theorem to work. It ensures that each sample is representative of the population. The beauty of CLT is that it works regardless of the population's distribution shape."
        },
        {
            "question": "What is the recommended minimum sample size for the Central Limit Theorem to apply?",
            "correct_answer": "30",
            "incorrect_answer": "10",
            "explanation": "Generally, a sample size of at least 30 is recommended for the Central Limit Theorem to take effect. This is often referred to as the 'magic number' in statistics, though larger samples are even better!"
        }
    ],
    "Estimation": [
        {
            "question": "What is the main purpose of estimation in statistics?",
            "correct_answer": "To make inferences about a population parameter based on a sample statistic",
            "incorrect_answer": "To calculate the exact value of a population parameter",
            "explanation": "Estimation allows us to make educated guesses about population characteristics using sample data. It's like estimating the average height of all students in a school by measuring just a few of them."
        },
        {
            "question": "What is point estimation?",
            "correct_answer": "A single value estimate of a population parameter",
            "incorrect_answer": "A range of possible values for a population parameter",
            "explanation": "Point estimation gives us a single 'best guess' for a population parameter. For example, saying the average income in a city is $50,000 based on a sample is a point estimate."
        },
        {
            "question": "What does interval estimation provide?",
            "correct_answer": "A range of values within which the population parameter lies with some confidence",
            "incorrect_answer": "The exact value of the population parameter",
            "explanation": "Interval estimation gives us a range where we believe the true population parameter lies, with a certain level of confidence. It's like saying, 'We're 95% sure the average income is between $48,000 and $52,000.'"
        }
    ]
}

# Function to run the quiz
def run_quiz(topic):
    if f'game_state_{topic}' not in st.session_state:
        st.session_state[f'game_state_{topic}'] = {
            'questions': quiz_topics[topic].copy(),
            'score': 0,
            'total_questions': len(quiz_topics[topic]),
            'current_question': None,
            'feedback': None,
            'explanation': None,
            'show_next': False
        }

    game_state = st.session_state[f'game_state_{topic}']

    if game_state['questions']:
        if not game_state['current_question']:
            game_state['current_question'] = random.choice(game_state['questions'])
            game_state['feedback'] = None
            game_state['explanation'] = None
            game_state['show_next'] = False

        # Display live score
        st.markdown(f"""
        <div class="score-box">
            🏆 Score: {game_state['score']} / {game_state['total_questions']}
        </div>
        """, unsafe_allow_html=True)

        # Display the question
        st.markdown(f"""
        <div class="question-box">
            <h3>📊 Question:</h3>
            <p style="font-size: 18px; font-weight: 600;">{game_state['current_question']['question']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Buttons for selection
        if not game_state['show_next']:
            col1, col2 = st.columns(2)
            with col1:
                option1 = st.button(game_state['current_question']['correct_answer'], key=f"{topic}_option1", use_container_width=True)
            with col2:
                option2 = st.button(game_state['current_question']['incorrect_answer'], key=f"{topic}_option2", use_container_width=True)

            # Check answer and provide feedback
            if option1 or option2:
                selected_answer = game_state['current_question']['correct_answer'] if option1 else game_state['current_question']['incorrect_answer']
                correct_answer = game_state['current_question']['correct_answer']
                
                if selected_answer == correct_answer:
                    game_state['score'] += 1
                    game_state['feedback'] = f"✅ Correct! Well done!"
                else:
                    game_state['feedback'] = f"❌ Oops! The correct answer is '{correct_answer}'."
                
                game_state['explanation'] = game_state['current_question']['explanation']
                game_state['show_next'] = True
                st.rerun()

        # Display feedback, explanation, and next button
        if game_state['feedback']:
            st.markdown(f"""
            <div class="feedback-box {'feedback-correct' if '✅' in game_state['feedback'] else 'feedback-incorrect'}">
                {game_state['feedback']}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="explanation-box">
                <h3>💡 Explanation:</h3>
                <p>{game_state['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Next Question", key=f"{topic}_next_question"):
                game_state['questions'].remove(game_state['current_question'])
                game_state['current_question'] = None
                game_state['feedback'] = None
                game_state['explanation'] = None
                game_state['show_next'] = False
                st.rerun()

    else:
        final_score = game_state['score']
        total_questions = game_state['total_questions']
        percentage = (final_score / total_questions) * 100

        st.markdown(f"""
        <div style="text-align: center; padding: 30px; background-color: #ffffff; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h2>🎉 Congratulations! You've completed the {topic} Quiz! 🎉</h2>
            <p style="font-size: 24px; font-weight: 600; color: #2c3e50;">Your final score: {final_score} / {total_questions}</p>
            <p style="font-size: 20px; color: #3498db;">Accuracy: {percentage:.1f}%</p>
            <p style="font-size: 18px; font-style: italic; color: #7f8c8d; margin-top: 20px;">
                "In the grand casino of life, understanding probability is like knowing the odds. You've just improved your chances of success!"
            </p>
        </div>
        """, unsafe_allow_html=True)

        if percentage == 100:
            st.balloons()

        if st.button("Play Again", key=f"{topic}_play_again"):
            st.session_state[f'game_state_{topic}'] = {
                'questions': quiz_topics[topic].copy(),
                'score': 0,
                'total_questions': len(quiz_topics[topic]),
                'current_question': None,
                'feedback': None,
                'explanation': None,
                'show_next': False
            }
            st.rerun()

# Create topic selection
selected_topic = st.selectbox("Choose a topic:", list(quiz_topics.keys()))

# Display the selected quiz
st.markdown(f"""
<div class="topic-header">
    {selected_topic}
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
run_quiz(selected_topic)
st.markdown('</div>', unsafe_allow_html=True)

# Brief explanation
st.markdown("""
---
<div style="text-align: center; font-style: italic; color: #3498db; padding: 20px; background-color: #e8f4f8; border-radius: 10px; margin-top: 30px;">
    Dive into the world of Probability! 🌟<br>
    This quiz covers various topics in probability and statistics, from basic concepts to more advanced theories.<br>
    Remember, understanding probability is key to making informed decisions in an uncertain world! Good luck! 🍀
</div>
""", unsafe_allow_html=True)