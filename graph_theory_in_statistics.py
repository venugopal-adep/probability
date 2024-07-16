import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import networkx.algorithms.community as nx_comm

@st.cache_data
def load_data():
    G = nx.karate_club_graph()
    return G

def main():
    st.set_page_config(page_title="Graph Theory in Statistics Demo", layout="wide")
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #1e3d59;
    }
    .stButton>button {
        background-color: #ff6e40;
        color: white !important;
    }
    .stButton>button:hover {
        background-color: #ff9e80;
        color: white !important;
    }
    .info-box {
        background-color: #e6f3ff;
        border-left: 5px solid #3366cc;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff6e40;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🕸️ Graph Theory in Statistics")
    
    tabs = st.tabs(["📚 Introduction", "🔍 Network Visualization", "📊 Network Metrics", "🔗 Community Detection", "🧠 Quiz"])
    
    with tabs[0]:
        introduction_section()
    
    with tabs[1]:
        network_visualization_section()
    
    with tabs[2]:
        network_metrics_section()
    
    with tabs[3]:
        community_detection_section()
    
    with tabs[4]:
        quiz_section()

def introduction_section():
    st.header("Introduction to Graph Theory in Statistics")
    
    st.markdown("""
    <div class="info-box">
    Graph Theory in Statistics is the study of graphs, which are mathematical structures used to model pairwise relations between objects. 
    A graph in this context is made up of vertices (also called nodes or points) which are connected by edges (also called links or lines). 
    In statistics, graph theory is often applied to network analysis, studying relationships and flows between people, groups, organizations, or other entities.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Key Concepts")
    concepts = {
        "Node": "An entity in the network, such as a person or organization",
        "Edge": "A connection or relationship between two nodes",
        "Degree": "The number of edges connected to a node",
        "Path": "A sequence of nodes connected by edges",
        "Centrality": "Measures of the importance of nodes in a network",
        "Community": "A group of nodes that are more densely connected to each other than to the rest of the network"
    }

    for concept, description in concepts.items():
        st.markdown(f"**{concept}**: {description}")

    st.subheader("Importance of Graph Theory in Statistics")
    st.markdown("""
    - Provides a framework for analyzing complex systems of relationships
    - Helps identify important actors or components in a network
    - Allows for the study of information or resource flow through a system
    - Useful in detecting communities or clusters within data
    - Applicable in various fields such as social network analysis, biology, transportation, and more
    """)

def network_visualization_section():
    st.header("Network Visualization")

    G = load_data()

    st.markdown("""
    <div class="info-box">
    Network visualization is a powerful tool for understanding the structure and properties of a graph. 
    It can reveal patterns, clusters, and key nodes that might not be apparent from raw data alone.
    </div>
    """, unsafe_allow_html=True)

    # Visualization options
    layout = st.selectbox("Choose a layout", ["spring", "circular", "random", "shell"])
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G) if layout == "spring" else \
          nx.circular_layout(G) if layout == "circular" else \
          nx.random_layout(G) if layout == "random" else \
          nx.shell_layout(G)
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500, font_size=10, font_weight='bold', ax=ax)
    
    st.pyplot(fig)

    st.markdown("""
    This visualization shows the Zachary's Karate Club network. Each node represents a member of the karate club, 
    and edges represent interactions between members outside of the club. The network captures the fission of a 
    karate club into two separate clubs, led by the instructor (node 0) and the club president (node 33).
    
    Try different layouts to see how they affect the visualization of the network structure.
    """)

def network_metrics_section():
    st.header("Network Metrics")

    G = load_data()

    st.markdown("""
    <div class="info-box">
    Network metrics provide quantitative measures of the structure and properties of a graph. 
    These metrics can reveal important characteristics of the network and its components.
    </div>
    """, unsafe_allow_html=True)

    # Calculate metrics
    degrees = dict(G.degree())
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    eigenvector = nx.eigenvector_centrality(G)

    metrics_df = pd.DataFrame({
        'Degree': degrees,
        'Betweenness Centrality': betweenness,
        'Closeness Centrality': closeness,
        'Eigenvector Centrality': eigenvector
    })

    st.subheader("Node-level Metrics")
    st.write(metrics_df)

    # Visualize distributions
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Degree Distribution", "Betweenness Centrality", 
                                                        "Closeness Centrality", "Eigenvector Centrality"))
    fig.add_trace(go.Histogram(x=list(degrees.values()), name="Degree"), row=1, col=1)
    fig.add_trace(go.Histogram(x=list(betweenness.values()), name="Betweenness"), row=1, col=2)
    fig.add_trace(go.Histogram(x=list(closeness.values()), name="Closeness"), row=2, col=1)
    fig.add_trace(go.Histogram(x=list(eigenvector.values()), name="Eigenvector"), row=2, col=2)
    fig.update_layout(height=600, width=800, title_text="Distribution of Centrality Measures")
    st.plotly_chart(fig)

    st.markdown("""
    These distributions show how centrality measures vary across nodes in the network:
    - **Degree**: The number of connections a node has.
    - **Betweenness Centrality**: Measures the extent to which a node lies on paths between other nodes.
    - **Closeness Centrality**: Measures how close a node is to all other nodes in the network.
    - **Eigenvector Centrality**: Measures the influence of a node in the network.
    """)

    # Network-level metrics
    st.subheader("Network-level Metrics")
    st.write(f"Number of Nodes: {G.number_of_nodes()}")
    st.write(f"Number of Edges: {G.number_of_edges()}")
    st.write(f"Average Clustering Coefficient: {nx.average_clustering(G):.4f}")
    st.write(f"Network Density: {nx.density(G):.4f}")
    st.write(f"Network Diameter: {nx.diameter(G)}")

def community_detection_section():
    st.header("Community Detection")

    G = load_data()

    st.markdown("""
    <div class="info-box">
    Community detection algorithms aim to find groups of nodes that are more densely connected to each other 
    than to the rest of the network. These communities can reveal important substructures within the network.
    </div>
    """, unsafe_allow_html=True)

    # Louvain community detection
    communities = nx_comm.louvain_communities(G)

    # Create a dictionary mapping each node to its community
    partition = {}
    for i, community in enumerate(communities):
        for node in community:
            partition[node] = i

    # Visualization with communities
    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=[partition[node] for node in G.nodes()], with_labels=True, 
            node_size=500, font_size=10, font_weight='bold', cmap=plt.cm.Set3, ax=ax)
    
    st.pyplot(fig)

    st.markdown("""
    This visualization shows the network with nodes colored by their detected communities. 
    The Louvain algorithm has been used for community detection, which aims to optimize modularity.
    
    Communities in this context represent groups of club members who interact more frequently with each other.
    """)

    # Community statistics
    community_sizes = pd.Series(partition).value_counts().sort_index()
    st.subheader("Community Sizes")
    st.bar_chart(community_sizes)

    st.markdown("""
    This bar chart shows the size of each detected community. 
    Larger communities might represent more influential subgroups within the karate club.
    """)

def quiz_section():
    st.header("Test Your Knowledge")
    
    questions = [
        {
            "question": "What does the 'degree' of a node represent in a graph?",
            "options": [
                "The age of the node",
                "The number of connections the node has",
                "The importance of the node",
                "The color of the node in visualization"
            ],
            "correct": "The number of connections the node has",
            "explanation": "In graph theory, the degree of a node is the number of edges connected to it, representing the number of direct connections or relationships the node has in the network."
        },
        {
            "question": "What is the purpose of community detection in network analysis?",
            "options": [
                "To count the number of nodes",
                "To visualize the network",
                "To find groups of densely connected nodes",
                "To calculate the average degree"
            ],
            "correct": "To find groups of densely connected nodes",
            "explanation": "Community detection algorithms aim to identify groups of nodes in a network that are more densely connected to each other than to the rest of the network. This can reveal important substructures or clusters within the data."
        },
        {
            "question": "What does a high betweenness centrality for a node indicate?",
            "options": [
                "The node has many direct connections",
                "The node is close to all other nodes",
                "The node frequently lies on paths between other nodes",
                "The node is not well connected"
            ],
            "correct": "The node frequently lies on paths between other nodes",
            "explanation": "Betweenness centrality measures the extent to which a node lies on paths between other nodes. A high betweenness centrality indicates that the node acts as a bridge between different parts of the network and is important for information flow."
        },
        {
            "question": "What does the network density measure?",
            "options": [
                "The total weight of all edges",
                "The ratio of existing edges to all possible edges",
                "The number of communities in the network",
                "The average degree of nodes"
            ],
            "correct": "The ratio of existing edges to all possible edges",
            "explanation": "Network density is a measure of how many edges are in the graph compared to the maximum possible number of edges. It ranges from 0 (no edges) to 1 (all possible edges exist), indicating how interconnected the network is."
        }
    ]
    
    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}")
        with st.container():
            st.write(q["question"])
            answer = st.radio("Select your answer:", q["options"], key=f"q{i}")
            if st.button("Check Answer", key=f"check{i}"):
                if answer == q["correct"]:
                    st.success("Correct! 🎉")
                else:
                    st.error(f"Incorrect. The correct answer is: {q['correct']}")
                st.info(f"Explanation: {q['explanation']}")
            st.write("---")

if __name__ == "__main__":
    main()