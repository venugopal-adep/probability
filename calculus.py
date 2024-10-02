import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Set page configuration
st.set_page_config(layout="wide", page_title="Calculus Explorer", page_icon="📈")

# Custom CSS (unchanged)
st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

# Title
st.title("Calculus Explorer: An Interactive Journey")

# Create tabs for each topic
tabs = st.tabs(["Limits", "Derivatives", "Integrals"])

# Helper function to convert SymPy expressions to Python functions
def sympy_to_function(expr):
    return sp.lambdify(x, expr, "numpy")

# Limits
with tabs[0]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Limits")
        st.markdown(r"""
        A limit describes the behavior of a function as its input approaches a particular value.
        
        $\lim_{x \to a} f(x) = L$
        
        This means that as $x$ gets arbitrarily close to $a$, $f(x)$ gets arbitrarily close to $L$.
        """)
        function = st.text_input("Enter a function f(x)", value="1 / (x - 2)")
        limit_point = st.number_input("Limit point (a)", value=2.0)
    
    with col2:
        x = sp.Symbol('x')
        f = sp.sympify(function)
        
        try:
            limit = sp.limit(f, x, limit_point)
            
            x_vals = np.linspace(limit_point - 2, limit_point + 2, 1000)
            x_vals = x_vals[x_vals != limit_point]  # Remove the limit point to avoid division by zero
            f_numpy = sympy_to_function(f)
            y_vals = f_numpy(x_vals)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'))
            fig.add_trace(go.Scatter(x=[limit_point], y=[float(limit)], mode='markers', name='Limit',
                                     marker=dict(size=10, color='red')))
            
            fig.update_layout(title='Limit Visualization', xaxis_title='x', yaxis_title='f(x)',
                              width=700, height=400, showlegend=True)
            st.plotly_chart(fig)
            
            st.markdown(f"**Limit:** {limit}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Derivatives
with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Derivatives")
        st.markdown(r"""
        The derivative of a function represents its rate of change. It's defined as:
        
        $f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$
        
        Geometrically, it represents the slope of the tangent line to the function at a given point.
        """)
        function_d = st.text_input("Enter a function f(x)", value="x**2", key="derivative_function")
        point = st.number_input("Point of interest", value=1.0)
    
    with col2:
        x = sp.Symbol('x')
        f = sp.sympify(function_d)
        
        try:
            derivative = sp.diff(f, x)
            derivative_at_point = derivative.subs(x, point)
            
            x_vals = np.linspace(point - 2, point + 2, 100)
            f_numpy = sympy_to_function(f)
            y_vals = f_numpy(x_vals)
            
            # Tangent line
            tangent_b = f.subs(x, point) - derivative_at_point * point
            tangent_y = [float(derivative_at_point) * val + float(tangent_b) for val in x_vals]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'))
            fig.add_trace(go.Scatter(x=x_vals, y=tangent_y, mode='lines', name='Tangent line'))
            fig.add_trace(go.Scatter(x=[point], y=[float(f.subs(x, point))], mode='markers', name='Point',
                                     marker=dict(size=10, color='red')))
            
            fig.update_layout(title='Derivative Visualization', xaxis_title='x', yaxis_title='f(x)',
                              width=700, height=400, showlegend=True)
            st.plotly_chart(fig)
            
            st.markdown(f"**Derivative:** {derivative}")
            st.markdown(f"**Derivative at x = {point}:** {derivative_at_point}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Integrals
with tabs[2]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Integrals")
        st.markdown(r"""
        An integral represents the area under a curve. The definite integral is defined as:
        
        $\int_{a}^{b} f(x) dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x$
        
        where $\Delta x = \frac{b - a}{n}$ and $x_i$ is a sample point in the i-th subinterval.
        """)
        function_i = st.text_input("Enter a function f(x)", value="x**2", key="integral_function")
        a = st.number_input("Lower bound (a)", value=0.0)
        b = st.number_input("Upper bound (b)", value=1.0)
    
    with col2:
        x = sp.Symbol('x')
        f = sp.sympify(function_i)
        
        try:
            integral = sp.integrate(f, (x, a, b))
            
            x_vals = np.linspace(a, b, 100)
            f_numpy = sympy_to_function(f)
            y_vals = f_numpy(x_vals)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)', fill='tozeroy'))
            
            fig.update_layout(title='Integral Visualization', xaxis_title='x', yaxis_title='f(x)',
                              width=700, height=400, showlegend=True)
            st.plotly_chart(fig)
            
            st.markdown(f"**Definite Integral from {a} to {b}:** {integral}")
            
            # Visualize Riemann sum
            n_rectangles = st.slider("Number of rectangles for Riemann sum", 1, 50, 10)
            dx = (b - a) / n_rectangles
            x_riemann = np.linspace(a, b, n_rectangles + 1)
            y_riemann = f_numpy(x_riemann)
            
            fig_riemann = go.Figure()
            fig_riemann.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'))
            for i in range(n_rectangles):
                fig_riemann.add_shape(type="rect",
                    x0=x_riemann[i], y0=0, x1=x_riemann[i+1], y1=y_riemann[i],
                    line=dict(color="RoyalBlue", width=2),
                    fillcolor="LightSkyBlue", opacity=0.5)
            
            fig_riemann.update_layout(title=f'Riemann Sum Approximation (n={n_rectangles})',
                                      xaxis_title='x', yaxis_title='f(x)',
                                      width=700, height=400, showlegend=True)
            st.plotly_chart(fig_riemann)
            
            riemann_sum = float(sum(f.subs(x, x_riemann[i]) * dx for i in range(n_rectangles)))
            st.markdown(f"**Riemann Sum Approximation:** {riemann_sum}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
