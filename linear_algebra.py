import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(layout="wide", page_title="Linear Algebra Explorer", page_icon="📐")

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
st.title("Linear Algebra Explorer: An Interactive Journey")

# Create tabs for each topic
tabs = st.tabs(["Vector Spaces", "Matrix Multiplication", "Matrix Inversion (2x2)", "Change of Basis", "Eigenvectors & Eigenvalues"])

# Vector Spaces
with tabs[0]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Vector Spaces")
        st.markdown("""
        A vector space is a collection of objects called vectors, which may be added together and multiplied by scalars.
        
        Key properties:
        1. Closure under addition and scalar multiplication
        2. Commutativity and associativity of addition
        3. Existence of zero vector and additive inverses
        4. Distributivity of scalar multiplication over vector addition
        """)
        x1 = st.slider("Vector 1 x-component", -5.0, 5.0, 1.0, 0.1)
        y1 = st.slider("Vector 1 y-component", -5.0, 5.0, 2.0, 0.1)
        x2 = st.slider("Vector 2 x-component", -5.0, 5.0, -3.0, 0.1)
        y2 = st.slider("Vector 2 y-component", -5.0, 5.0, 1.0, 0.1)
    
    with col2:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[0, x1], y=[0, y1], mode='lines+markers', name='Vector 1', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=[0, x2], y=[0, y2], mode='lines+markers', name='Vector 2', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=[0, x1+x2], y=[0, y1+y2], mode='lines+markers', name='Sum', line=dict(color='green')))
        fig.update_layout(title='2D Vector Addition', xaxis_title='X', yaxis_title='Y', 
                          xaxis=dict(range=[-6, 6]), yaxis=dict(range=[-6, 6]), 
                          width=700, height=500, showlegend=True)
        st.plotly_chart(fig)

# Matrix Multiplication
with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Matrix Multiplication")
        st.markdown("""
        Matrix multiplication is a fundamental operation in linear algebra. For two matrices A and B to be multiplied, 
        the number of columns in A must equal the number of rows in B.
        """)
        st.subheader("Matrix A")
        a11 = st.number_input("A[1,1]", value=1)
        a12 = st.number_input("A[1,2]", value=2)
        a21 = st.number_input("A[2,1]", value=3)
        a22 = st.number_input("A[2,2]", value=4)
        
        st.subheader("Matrix B")
        b11 = st.number_input("B[1,1]", value=5)
        b12 = st.number_input("B[1,2]", value=6)
        b21 = st.number_input("B[2,1]", value=7)
        b22 = st.number_input("B[2,2]", value=8)
    
    with col2:
        A = np.array([[a11, a12], [a21, a22]])
        B = np.array([[b11, b12], [b21, b22]])
        C = np.dot(A, B)
        
        fig = make_subplots(rows=1, cols=3, subplot_titles=("Matrix A", "Matrix B", "Result A * B"))
        fig.add_trace(go.Heatmap(z=A, text=A, texttemplate="%{text}", colorscale="Viridis"), row=1, col=1)
        fig.add_trace(go.Heatmap(z=B, text=B, texttemplate="%{text}", colorscale="Viridis"), row=1, col=2)
        fig.add_trace(go.Heatmap(z=C, text=C, texttemplate="%{text}", colorscale="Viridis"), row=1, col=3)
        fig.update_layout(height=400, width=700)
        st.plotly_chart(fig)

# Matrix Inversion (2x2)
with tabs[2]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Matrix Inversion (2x2)")
        st.markdown("""
        The inverse of a square matrix A is denoted A^(-1) and satisfies the equation AA^(-1) = A^(-1)A = I, 
        where I is the identity matrix. Not all matrices have inverses.
        """)
        st.subheader("Matrix A")
        a11 = st.number_input("A[1,1]", value=1, key="inv11")
        a12 = st.number_input("A[1,2]", value=2, key="inv12")
        a21 = st.number_input("A[2,1]", value=3, key="inv21")
        a22 = st.number_input("A[2,2]", value=4, key="inv22")
    
    with col2:
        A = np.array([[a11, a12], [a21, a22]])
        det = np.linalg.det(A)
        
        if abs(det) < 1e-10:
            st.error("This matrix is not invertible (determinant is zero)")
        else:
            A_inv = np.linalg.inv(A)
            fig = make_subplots(rows=1, cols=2, subplot_titles=("Matrix A", "Inverse of A"))
            fig.add_trace(go.Heatmap(z=A, text=A, texttemplate="%{text}", colorscale="Viridis"), row=1, col=1)
            fig.add_trace(go.Heatmap(z=A_inv, text=A_inv, texttemplate="%{text:.3f}", colorscale="Viridis"), row=1, col=2)
            fig.update_layout(height=400, width=700)
            st.plotly_chart(fig)

# Change of Basis
with tabs[3]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Change of Basis")
        st.markdown("""
        A change of basis is a conversion from one coordinate system to another. It's represented by a matrix 
        that transforms vectors from one basis to another.
        """)
        theta = st.slider("Rotation angle (degrees)", 0, 360, 45)
    
    with col2:
        theta_rad = np.radians(theta)
        
        # Original basis vectors
        e1 = np.array([1, 0])
        e2 = np.array([0, 1])
        
        # New basis vectors (rotated)
        e1_new = np.array([np.cos(theta_rad), np.sin(theta_rad)])
        e2_new = np.array([-np.sin(theta_rad), np.cos(theta_rad)])
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Original Basis", "New Basis"))
        
        # Original basis
        fig.add_trace(go.Scatter(x=[0, e1[0]], y=[0, e1[1]], mode='lines+markers', name='e1', line=dict(color='red')), row=1, col=1)
        fig.add_trace(go.Scatter(x=[0, e2[0]], y=[0, e2[1]], mode='lines+markers', name='e2', line=dict(color='blue')), row=1, col=1)
        
        # New basis
        fig.add_trace(go.Scatter(x=[0, e1_new[0]], y=[0, e1_new[1]], mode='lines+markers', name='e1_new', line=dict(color='red')), row=1, col=2)
        fig.add_trace(go.Scatter(x=[0, e2_new[0]], y=[0, e2_new[1]], mode='lines+markers', name='e2_new', line=dict(color='blue')), row=1, col=2)
        
        fig.update_layout(height=400, width=700)
        fig.update_xaxes(range=[-1.5, 1.5])
        fig.update_yaxes(range=[-1.5, 1.5])
        st.plotly_chart(fig)

# Eigenvectors & Eigenvalues
with tabs[4]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Eigenvectors & Eigenvalues")
        st.markdown("""
        An eigenvector of a square matrix A is a non-zero vector v that, when multiplied by A, yields a scalar 
        multiple of itself. This scalar is called an eigenvalue.

        Av = λv

        where v is an eigenvector and λ is the corresponding eigenvalue.
        """)
        st.subheader("Matrix A")
        a11 = st.number_input("A[1,1]", value=1, key="eig11")
        a12 = st.number_input("A[1,2]", value=2, key="eig12")
        a21 = st.number_input("A[2,1]", value=3, key="eig21")
        a22 = st.number_input("A[2,2]", value=4, key="eig22")
    
    with col2:
        A = np.array([[a11, a12], [a21, a22]])
        eigenvalues, eigenvectors = np.linalg.eig(A)
        
        st.markdown("Eigenvalues:")
        st.write(eigenvalues)
        st.markdown("Eigenvectors:")
        st.write(eigenvectors)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[0, eigenvectors[0,0]], y=[0, eigenvectors[1,0]], mode='lines+markers', name='Eigenvector 1', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=[0, eigenvectors[0,1]], y=[0, eigenvectors[1,1]], mode='lines+markers', name='Eigenvector 2', line=dict(color='blue')))
        fig.update_layout(title='Eigenvectors', xaxis_title='X', yaxis_title='Y', 
                          xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1]), 
                          width=700, height=400, showlegend=True)
        st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by AI Educators | © 2024 Linear Algebra Explorer")