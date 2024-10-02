import streamlit as st
import random

# Set page configuration
st.set_page_config(layout="wide", page_title="Logic & Math Explorer", page_icon="🧠")

# Custom CSS
st.markdown("""
<style>
    body {
        background-color: #f0f2f6;
        color: #1e1e1e;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #e0e0e0;
        border-radius: 4px;
        color: #1e1e1e;
        font-size: 18px;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50;
        color: white;
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
    .topic-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .fun-fact {
        background-color: #e8f5e9;
        border-left: 5px solid #4CAF50;
        padding: 10px;
        margin: 20px 0;
    }
    .quiz-container {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("Logic & Math Explorer: An Interactive Learning Journey")
st.markdown("""
Welcome to this interactive learning experience! Explore the fascinating world of **mathematical notation**, **propositional logic**, and **predicate logic**. 
This guide offers clear explanations, engaging examples, and quiz questions to help you master these fundamental concepts.

Let's begin our exploration! 🚀
""")

# Create tabs for each topic
tab1, tab2, tab3 = st.tabs(["📐 Mathematical Notation", "🤔 Propositional Logic", "🔍 Predicate Logic"])

# Tab 1: Mathematical Notation
with tab1:
    st.header("Mathematical Notation")
    
    st.markdown("""
    Mathematical notation is a symbolic language used to represent mathematical concepts. It includes symbols for numbers, operations, functions, and relationships, helping us express complex ideas concisely.
    
    ### Basic Notations:
    1. **Numbers**: 
       - Natural numbers: $\\mathbb{N} = \\{0, 1, 2, 3, \\dots\\}$
       - Integers: $\\mathbb{Z} = \\{\\dots, -2, -1, 0, 1, 2, \\dots\\}$
       - Real numbers: $\\mathbb{R}$
    2. **Operations**:
       - Addition: $a + b$
       - Subtraction: $a - b$
       - Multiplication: $a \\cdot b$ or $ab$
       - Division: $\\frac{a}{b}$
    3. **Sets and Relations**:
       - Set notation: $A = \\{1, 2, 3\\}$
       - Belongs to: $2 \\in A$
       - Does not belong to: $5 \\notin A$
       - Subset: $B \\subseteq A$
    4. **Common Symbols**:
       - $\\forall$: For all
       - $\\exists$: There exists
       - $\\Rightarrow$: Implies
       - $\\Leftrightarrow$: If and only if
    """)

    st.markdown("""
    <div class='fun-fact'>
        <h3>🎨 Fun Fact</h3>
        <p>Did you know that mathematical symbols we use today, like = (equals sign) and + (plus sign), were only standardized in the 16th and 17th centuries?</p>
    </div>
    """, unsafe_allow_html=True)

    # Quiz for Mathematical Notation
    st.subheader("Quiz: Mathematical Notation")
    math_questions = [
        {
            "question": "What does the symbol $\\mathbb{N}$ represent?",
            "options": ["Natural numbers", "Negative numbers", "Rational numbers", "Real numbers"],
            "correct": 0,
            "explanation": "The symbol $\\mathbb{N}$ represents Natural numbers, which are positive integers including zero (0, 1, 2, 3, ...). For example, 5 is a natural number, but -3 or 2.5 are not."
        },
        {
            "question": "Which symbol represents 'belongs to' in set notation?",
            "options": ["$\\subset$", "$\\in$", "$\\notin$", "$\\supset$"],
            "correct": 1,
            "explanation": "The symbol $\\in$ represents 'belongs to' in set notation. For example, if A = {1, 2, 3}, we can say 2 $\\in$ A, which means 2 belongs to the set A."
        },
        {
            "question": "What does the symbol $\\forall$ mean?",
            "options": ["There exists", "For all", "Such that", "If and only if"],
            "correct": 1,
            "explanation": "The symbol $\\forall$ means 'For all' or 'For every'. It's used in statements that apply to all elements in a set. For example, $\\forall x \\in \\mathbb{R}, x + 0 = x$ means 'For all real numbers x, adding 0 to x equals x'."
        }
    ]

    for i, q in enumerate(math_questions):
        st.markdown(f"**Question {i+1}: {q['question']}**")
        user_answer = st.radio(f"Select your answer for Question {i+1}:", q['options'], key=f"math_q{i}")
        if st.button(f"Check Answer for Question {i+1}", key=f"math_check{i}"):
            if user_answer == q['options'][q['correct']]:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
            st.info(f"Explanation: {q['explanation']}")
        st.markdown("---")

# Tab 2: Propositional Logic
with tab2:
    st.header("Propositional Logic")
    
    st.markdown("""
    **Propositional logic** is a branch of logic that deals with statements that are either true or false. These statements, called **propositions**, are connected using logical connectives like AND, OR, and NOT.

    ### Basic Components:
    1. **Propositions**: Statements that can be true or false. Examples:
       - $p$: "It is raining."
       - $q$: "I have an umbrella."
    2. **Logical Connectives**:
       - **AND** ($\\land$): True if both propositions are true. Example: $p \\land q$ ("It is raining AND I have an umbrella").
       - **OR** ($\\lor$): True if at least one proposition is true. Example: $p \\lor q$ ("It is raining OR I have an umbrella").
       - **NOT** ($\\neg$): Inverts the truth value of a proposition. Example: $\\neg p$ ("It is NOT raining").
       - **Implication** ($\\rightarrow$): $p \\rightarrow q$ means "If $p$ is true, then $q$ is true".
       - **Biconditional** ($\\leftrightarrow$): $p \\leftrightarrow q$ means "$p$ is true if and only if $q$ is true".
    """)

    st.markdown("""
    <div class='fun-fact'>
        <h3>🕰️ Fun Fact</h3>
        <p>The concept of logic dates back to ancient Greece, but it was George Boole in the 19th century who formalized the laws of Boolean logic that we use in computer science today.</p>
    </div>
    """, unsafe_allow_html=True)

    # Quiz for Propositional Logic
    st.subheader("Quiz: Propositional Logic")
    prop_questions = [
        {
            "question": "What does the symbol $\\land$ represent in propositional logic?",
            "options": ["AND", "OR", "NOT", "IMPLIES"],
            "correct": 0,
            "explanation": "The symbol $\\land$ represents AND in propositional logic. It's true only when both of its inputs are true. For example, if p: 'It's sunny' and q: 'It's warm', then p $\\land$ q means 'It's sunny AND warm', which is only true when both conditions are met."
        },
        {
            "question": "If $p$ is true and $q$ is false, what is the truth value of $p \\lor q$?",
            "options": ["False", "True", "Cannot be determined", "Both true and false"],
            "correct": 1,
            "explanation": "The symbol $\\lor$ represents OR, which is true if at least one of its inputs is true. In this case, since p is true, p $\\lor$ q is true regardless of the value of q. For example, if p: 'I like pizza' (true) and q: 'I like broccoli' (false), then 'I like pizza OR broccoli' is true."
        },
        {
            "question": "What is the negation of the statement 'It is raining' ($p$)?",
            "options": ["$p \\land q$", "$\\neg p$", "$p \\lor q$", "$p \\rightarrow q$"],
            "correct": 1,
            "explanation": "The negation of a statement p is represented by $\\neg p$. It means 'not p' or the opposite of p. So if p is 'It is raining', then $\\neg p$ means 'It is not raining'."
        }
    ]

    for i, q in enumerate(prop_questions):
        st.markdown(f"**Question {i+1}: {q['question']}**")
        user_answer = st.radio(f"Select your answer for Question {i+1}:", q['options'], key=f"prop_q{i}")
        if st.button(f"Check Answer for Question {i+1}", key=f"prop_check{i}"):
            if user_answer == q['options'][q['correct']]:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
            st.info(f"Explanation: {q['explanation']}")
        st.markdown("---")

# Tab 3: Predicate Logic
with tab3:
    st.header("Predicate Logic")
    
    st.markdown("""
    **Predicate logic** extends propositional logic by dealing with predicates and quantifiers. A **predicate** is a statement that contains variables and becomes a proposition when the variables are given specific values.

    ### Basic Components:
    1. **Predicates**: Functions that return true or false. Example: $P(x)$ can represent "$x$ is greater than 5".
    2. **Quantifiers**:
       - **Universal Quantifier** ($\\forall$): Indicates that a statement applies to all elements in a set. Example: $\\forall x \\in \\mathbb{N}, x + 1 > x$ ("For all natural numbers $x$, $x + 1$ is greater than $x$").
       - **Existential Quantifier** ($\\exists$): Indicates that there exists at least one element in a set for which the statement is true. Example: $\\exists x \\in \\mathbb{R}, x^2 = 4$ ("There exists a real number $x$ such that $x^2 = 4$").

    ### Example: Prime Numbers
    Let's use predicate logic to express "All prime numbers greater than 2 are odd."
    - Predicate: $P(x)$ = "$x$ is prime."
    - Statement: $\\forall x \\in \\mathbb{N}, (P(x) \\land x > 2) \\rightarrow \\text{Odd}(x)$
    """)

    st.markdown("""
    <div class='fun-fact'>
        <h3>💻 Fun Fact</h3>
        <p>Predicate logic forms the foundation of programming languages and artificial intelligence, allowing machines to process and infer complex information.</p>
    </div>
    """, unsafe_allow_html=True)

    # Quiz for Predicate Logic
    st.subheader("Quiz: Predicate Logic")
    pred_questions = [
        {
            "question": "What does the symbol $\\forall$ mean in predicate logic?",
            "options": ["There exists", "For all", "Such that", "If and only if"],
            "correct": 1,
            "explanation": "The symbol $\\forall$ means 'For all' or 'For every' in predicate logic. It's used to make statements about all elements in a set. For example, $\\forall x \\in \\mathbb{R}, x = x$ means 'For all real numbers x, x equals itself'."
        },
        {
            "question": "In the statement $\\exists x \\in \\mathbb{R}, x^2 = 4$, what does $\\exists$ represent?",
            "options": ["For all", "There exists", "Does not exist", "If and only if"],
            "correct": 1,
            "explanation": "The symbol $\\exists$ means 'There exists' or 'There is at least one'. In this statement, it means 'There exists a real number x such that x squared equals 4'. This is true because both 2 and -2 satisfy this condition."
        },
        {
            "question": "Which of the following is a predicate?",
            "options": ["$p$: It is raining", "$q \\land r$", "$\\neg p$", "$P(x)$: $x$ is greater than 5"],
            "correct": 3,
            "explanation": "A predicate is a statement that contains variables and becomes a proposition when the variables are given specific values. $P(x)$: '$x$ is greater than 5' is a predicate because it becomes true or false depending on the value of x. For example, P(6) is true, while P(4) is false."
        }
    ]

    for i, q in enumerate(pred_questions):
        st.markdown(f"**Question {i+1}: {q['question']}**")
        user_answer = st.radio(f"Select your answer for Question {i+1}:", q['options'], key=f"pred_q{i}")
        if st.button(f"Check Answer for Question {i+1}", key=f"pred_check{i}"):
            if user_answer == q['options'][q['correct']]:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")
            st.info(f"Explanation: {q['explanation']}")
        st.markdown("---")


