import streamlit as st
import random

st.set_page_config(page_title="Hypothesis Testing Quiz", layout="wide")

# Custom CSS (same as before)
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
</style>
""", unsafe_allow_html=True)

# Quiz questions based on the slides
quiz_topics = {
    "Introduction to Hypothesis Testing": [
        {
            "question": "What does the null hypothesis (H₀) represent in hypothesis testing?",
            "correct_answer": "The status quo",
            "incorrect_answer": "The research hypothesis",
            "explanation": "The null hypothesis (H₀) represents the status quo or the current assumption about the population parameter."
        },
        {
            "question": "What does the alternative hypothesis (Ha) represent?",
            "correct_answer": "The research hypothesis",
            "incorrect_answer": "The status quo",
            "explanation": "The alternative hypothesis (Ha) represents the research hypothesis or the claim to be tested."
        },
        {
            "question": "In the example given, what is the question of interest?",
            "correct_answer": "Has the new online Ad increased the conversion rates for an E-commerce website?",
            "incorrect_answer": "Has the new online Ad decreased the conversion rates for an E-commerce website?",
            "explanation": "The question of interest is whether the new online Ad has increased the conversion rates for an E-commerce website."
        }
    ],
    "Key Terms in Hypothesis Testing": [
        {
            "question": "What does a smaller p-value indicate in hypothesis testing?",
            "correct_answer": "Stronger evidence against the null hypothesis",
            "incorrect_answer": "Weaker evidence against the null hypothesis",
            "explanation": "A smaller p-value indicates stronger evidence against the null hypothesis."
        },
        {
            "question": "What does the level of significance (α) represent?",
            "correct_answer": "The probability of rejecting the null hypothesis when it is true",
            "incorrect_answer": "The probability of accepting the null hypothesis when it is false",
            "explanation": "The level of significance (α) represents the probability of rejecting the null hypothesis when it is true."
        },
        {
            "question": "What determines the acceptance or rejection of the null hypothesis?",
            "correct_answer": "The test statistic lying in the rejection region",
            "incorrect_answer": "The p-value being greater than the significance level",
            "explanation": "We reject the null hypothesis when the test statistic lies in the rejection region."
        }
    ],
    "Type I and Type II Errors": [
        {
            "question": "What is a Type I error in hypothesis testing?",
            "correct_answer": "Rejecting the null hypothesis when it is true",
            "incorrect_answer": "Failing to reject the null hypothesis when it is false",
            "explanation": "A Type I error occurs when we reject the null hypothesis when it is actually true."
        },
        {
            "question": "What is a Type II error in hypothesis testing?",
            "correct_answer": "Failing to reject the null hypothesis when it is false",
            "incorrect_answer": "Rejecting the null hypothesis when it is true",
            "explanation": "A Type II error occurs when we fail to reject the null hypothesis when it is actually false."
        },
        {
            "question": "What is the relationship between the significance level (α) and the confidence level?",
            "correct_answer": "Confidence Level = 1 - α",
            "incorrect_answer": "Confidence Level = α",
            "explanation": "The confidence level is calculated as 1 minus the significance level (α)."
        }
    ],
    "Hypothesis Testing Example": [
        {
            "question": "In the store manager example, what is the null hypothesis (H₀)?",
            "correct_answer": "The average waiting time at checkouts is less than or equal to 15 minutes",
            "incorrect_answer": "The average waiting time at checkouts is more than 15 minutes",
            "explanation": "The null hypothesis states that the average waiting time is less than or equal to 15 minutes, representing the status quo."
        },
        {
            "question": "What would be a Type I error in this example?",
            "correct_answer": "Concluding the average waiting time is more than 15 minutes when it is actually less than or equal to 15 minutes",
            "incorrect_answer": "Concluding the average waiting time is less than or equal to 15 minutes when it is actually more than 15 minutes",
            "explanation": "A Type I error would be rejecting the null hypothesis (average waiting time ≤ 15 minutes) when it is actually true."
        },
        {
            "question": "What would be a Type II error in this example?",
            "correct_answer": "Concluding the average waiting time is less than or equal to 15 minutes when it is actually more than 15 minutes",
            "incorrect_answer": "Concluding the average waiting time is more than 15 minutes when it is actually less than or equal to 15 minutes",
            "explanation": "A Type II error would be failing to reject the null hypothesis (average waiting time ≤ 15 minutes) when it is actually false."
        }
    ],
    "One-tailed vs Two-tailed Test": [
        {
            "question": "Which type of test would you use if you want to detect a difference in either direction from the null hypothesis?",
            "correct_answer": "Two-tailed test",
            "incorrect_answer": "One-tailed test",
            "explanation": "A two-tailed test is used when you want to detect a difference in either direction from the null hypothesis."
        },
        {
            "question": "In a lower tail test, what is the form of the alternative hypothesis?",
            "correct_answer": "Ha: μ < ...",
            "incorrect_answer": "Ha: μ > ...",
            "explanation": "In a lower tail test, the alternative hypothesis is of the form Ha: μ < ... , indicating we're testing if the parameter is less than a certain value."
        },
        {
            "question": "When would you use an upper tail test?",
            "correct_answer": "When you want to test if a parameter is greater than a certain value",
            "incorrect_answer": "When you want to test if a parameter is less than a certain value",
            "explanation": "An upper tail test is used when you want to test if a parameter is greater than a certain value, with the alternative hypothesis of the form Ha: μ > ..."
        }
    ],


    "Hypothesis Testing Steps": [
        {
            "question": "What is the first step in hypothesis testing according to the image?",
            "correct_answer": "Formulate H₀ and Ha",
            "incorrect_answer": "Select Appropriate Test",
            "explanation": "The first step in hypothesis testing is to formulate the null hypothesis (H₀) and alternative hypothesis (Ha)."
        },
        {
            "question": "After collecting data and calculating the test statistic, what are the two parallel steps shown?",
            "correct_answer": "Determine p-value and Determine Critical Value",
            "incorrect_answer": "Compare with α and Compare with Test Statistic",
            "explanation": "After calculating the test statistic, the next steps are to determine the p-value and determine the critical value."
        },
        {
            "question": "What is the final step in the hypothesis testing process according to the image?",
            "correct_answer": "Draw Conclusion",
            "incorrect_answer": "Reject or Do Not Reject H₀",
            "explanation": "The final step in the hypothesis testing process is to draw a conclusion based on the decision to reject or not reject the null hypothesis."
        }
    ]



}

# Function to run the quiz (modified to handle topic selection)
def run_quiz(topic, questions):
    if f'game_state_{topic}' not in st.session_state:
        st.session_state[f'game_state_{topic}'] = {
            'questions': questions.copy(),
            'score': 0,
            'total_questions': len(questions),
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
            <h3>Question:</h3>
            <p style="font-size: 18px; font-weight: 600;">{game_state['current_question']['question']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Buttons for selection
        if not game_state['show_next']:
            col1, col2 = st.columns(2)
            with col1:
                option1 = st.button(game_state['current_question']['correct_answer'], key=f"{topic}_option1")
            with col2:
                option2 = st.button(game_state['current_question']['incorrect_answer'], key=f"{topic}_option2")

            # Check answer and provide feedback
            if option1 or option2:
                selected_answer = game_state['current_question']['correct_answer'] if option1 else game_state['current_question']['incorrect_answer']
                correct_answer = game_state['current_question']['correct_answer']
                
                if selected_answer == correct_answer:
                    game_state['score'] += 1
                    game_state['feedback'] = "✅ Correct! Well done!"
                else:
                    game_state['feedback'] = f"❌ Oops! The correct answer is: {correct_answer}"
                
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
                <h4>Explanation:</h4>
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
                "Understanding hypothesis testing is crucial for making informed decisions in statistics and research!"
            </p>
        </div>
        """, unsafe_allow_html=True)

        if percentage == 100:
            st.balloons()

        if st.button("Play Again", key=f"{topic}_play_again"):
            st.session_state[f'game_state_{topic}'] = {
                'questions': questions.copy(),
                'score': 0,
                'total_questions': len(questions),
                'current_question': None,
                'feedback': None,
                'explanation': None,
                'show_next': False
            }
            st.rerun()

# Main app
st.title("🧪 Hypothesis Testing Quiz")
st.markdown("""
Welcome to the Hypothesis Testing Quiz! Select a topic and test your knowledge on various concepts related to hypothesis testing in statistics. 
Good luck! 🍀
""")

# Topic selection dropdown
selected_topic = st.selectbox("Choose a topic:", list(quiz_topics.keys()))

# Run the quiz for the selected topic
run_quiz(selected_topic, quiz_topics[selected_topic])