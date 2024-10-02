import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(layout="wide", page_title="Number Representation Explorer", page_icon="🔢")

# Custom CSS
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
st.title("Number Representation Explorer: An Interactive Journey")

# Create tabs for each topic
tabs = st.tabs(["Number Bases", "Fixed/Floating Point", "AI Mathematics"])

# Number Bases and Binary Arithmetic
with tabs[0]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Number Bases and Binary Arithmetic")
        st.markdown("""
        Number bases are systems for representing numbers. The most common bases are:
        - Base 2 (Binary): Uses 0 and 1
        - Base 10 (Decimal): Uses 0-9
        - Base 16 (Hexadecimal): Uses 0-9 and A-F
        """)
        decimal_num = st.number_input("Enter a decimal number", value=42, step=1)
    
    with col2:
        binary = bin(decimal_num)[2:]
        hex_num = hex(decimal_num)[2:]
        
        fig = go.Figure(data=[
            go.Bar(name='Binary', x=['Binary'], y=[len(binary)], text=[binary], textposition='auto'),
            go.Bar(name='Decimal', x=['Decimal'], y=[len(str(decimal_num))], text=[decimal_num], textposition='auto'),
            go.Bar(name='Hexadecimal', x=['Hexadecimal'], y=[len(hex_num)], text=[hex_num], textposition='auto')
        ])
        fig.update_layout(title='Number Representation in Different Bases', 
                          xaxis_title='Base', yaxis_title='Number of Digits',
                          width=700, height=500)
        st.plotly_chart(fig)

# Fixed/Floating Point
with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Fixed/Floating Point Representation")
        st.markdown("""
        Fixed-point and floating-point are two ways to represent real numbers in digital systems:
        - Fixed-point: The decimal point is in a fixed position
        - Floating-point: The decimal point can "float" relative to the significant digits
        """)
        number = st.number_input("Enter a real number", value=3.14159, format="%.5f")
        precision = st.slider("Select precision (decimal places)", 0, 10, 5)
    
    with col2:
        fixed_point = format(number, f'.{precision}f')
        float_repr = f'{number:.{precision}e}'
        
        fig = go.Figure(data=[
            go.Table(
                header=dict(values=['Representation', 'Value']),
                cells=dict(values=[
                    ['Original', 'Fixed-point', 'Floating-point'],
                    [number, fixed_point, float_repr]
                ])
            )
        ])
        fig.update_layout(width=700, height=200)
        st.plotly_chart(fig)
        
        # Visualize precision loss
        x = np.linspace(number - 0.1, number + 0.1, 1000)
        y = np.sin(x)
        y_fixed = np.sin(np.round(x, precision))
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Actual'))
        fig.add_trace(go.Scatter(x=x, y=y_fixed, mode='lines', name=f'Fixed-point ({precision} decimals)'))
        fig.update_layout(title='Precision Comparison', xaxis_title='x', yaxis_title='sin(x)',
                          width=700, height=400)
        st.plotly_chart(fig)

# Mathematics in Research-level AI
with tabs[2]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Mathematics in Research-level AI")
        st.markdown("""
        Advanced AI research often involves complex mathematical concepts, including:
        - Linear Algebra
        - Calculus
        - Probability Theory
        - Information Theory
        """)
        dimension = st.slider("Select dimension for vector visualization", 2, 5, 3)
    
    with col2:
        # Generate random vectors
        vectors = np.random.randn(10, dimension)
        
        # Perform dimensionality reduction for visualization
        if dimension > 3:
            from sklearn.decomposition import PCA
            pca = PCA(n_components=3)
            vectors_3d = pca.fit_transform(vectors)
        else:
            vectors_3d = vectors[:, :3]
        
        # Create 3D scatter plot
        fig = go.Figure(data=[go.Scatter3d(
            x=vectors_3d[:, 0],
            y=vectors_3d[:, 1],
            z=vectors_3d[:, 2],
            mode='markers',
            marker=dict(
                size=12,
                color=vectors_3d[:, 2],
                colorscale='Viridis',
                opacity=0.8
            )
        )])
        fig.update_layout(title=f'{dimension}-D Vectors in 3D Space', 
                          scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                          width=700, height=700)
        st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by AI Educators | © 2024 Number Representation Explorer")