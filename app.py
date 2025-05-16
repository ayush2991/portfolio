# A streamlit app to showcase my projects
import streamlit as st


def main():
    st.set_page_config(
        page_title="My Projects",
        page_icon=":rocket:",
        layout="wide",
    )

    # Inject custom CSS for project cards
    # This CSS aims to make cards in the same row have equal height
    # and ensures a consistent internal layout for each card.
    card_style = """
    <style>
    /* Target the Streamlit column's internal wrapper to make it a flex container
       and ensure it takes up full height. This allows the .project-card
       with height: 100% to expand correctly. */
    div[data-testid="column"] > div {
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .project-card {
        border: 1px solid var(--lines, #e0e0e0); /* Theme-aware border */
        border-radius: 8px;             /* Rounded corners */
        padding: 16px;                  /* Inner spacing */
        margin-bottom: 16px;            /* Space below card (for stacked cards) */
        
        /* Default shadow, suitable for light theme or if data-theme attribute isn't picked up */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06); 
        display: flex;                  /* Enable flexbox for internal layout */
        flex-direction: column;         /* Stack content (title, desc, link) vertically */
        justify-content: space-between; /* Push link to the bottom */
        height: 100%;                   /* Crucial: Card takes full height of its column cell */
        width: 100%;                    /* Card takes full width of its column cell */
        min-height: 280px;              /* Increased minimum height for better content fit and consistency */
    }

    .project-card-content { /* Wrapper for title and description */
        flex-grow: 1; /* Allows this section to expand, pushing badges/link down */
    }

    .project-card h3 {
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 0.75rem;
    }

    .project-card p {
        font-size: 0.95rem;
        line-height: 1.5;
        margin-bottom: 1rem; /* Space before badges or link */
    }
    .badges {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 12px 0;
    }

    .badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
        color: white;
        opacity: 0.9;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        transition: opacity 0.2s ease;
    }

    .badge:hover {
        opacity: 1;
    }

    .project-card a, .project-card a:visited {
        color: var(--primary-color, #FF4B4B); /* Theme-aware link color */
        text-decoration: none;
    }
    .project-card a:hover {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    st.title("My Projects")
    st.write("Welcome to my projects showcase! Here are some of the projects I've worked on:")

    # Define your featured projects here (now a list)
    featured_projects = [
        {
            "title": "Grounding LLMs with Web Search",
            "description": "LLMs are great at generating text, but they can make mistakes. This project leverages web search to locate sources that can corroborate claims made by LLMs.",
            # Updated badge colors for better harmony and readability
            "badges": [
                {"text": "LLM", "color": "#FF4B4B"},
                {"text": "Search API", "color": "#17A2B8"},
                {"text": "Embeddings", "color": "#28A745"},
                {"text": "Pandas", "color": "#6C757D"}
            ],
            "link": "https://ayush2991-grounding-llms-with-web-search.streamlit.app/"
        },
        {
            "title": "Agentic RAG",
            "description": "An agentic RAG (Retrieval-Augmented Generation) system that can answer any question about Harry Potter! It even cites its sources and rewrites queries if necessary.",
            "badges": [
                {"text": "LLM", "color": "#FF4B4B"},
                {"text": "Agents", "color": "#17A2B8"},
                {"text": "Embeddings", "color": "#28A745"},
                {"text": "Retrieval Augmented Generation", "color": "#6C757D"},
                {"text": "Vector DB", "color": "#FF8C00"}
            ],
            "link": "https://ayush2991-agentic-rag.streamlit.app/"
        }
    ]

    if featured_projects:
        st.subheader("✨ Featured Projects") # Changed to plural
        
        # Display featured projects in two columns
        cols_featured = st.columns(2,)
        for i, project in enumerate(featured_projects):
            with cols_featured[i % 2]: # Distribute projects into the two columns
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-card-content">
                        <h3>{project['title']}</h3>
                        <p>{project['description']}</p>
                    </div>
                    <div class="badges">
                        {"".join([f'<span class="badge" style="background-color: {badge["color"]};">{badge["text"]}</span>' for badge in project.get("badges", [])])}
                    </div>
                    <a href="{project['link']}" target="_blank">View Project</a>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---") # Add a separator

    # Add your other project details here
    projects = [
        {
            "title": "Some Good News",
            "description": "Your daily news, but with a dose of positivity! This app uses a sentiment analysis model to prioritize positive news articles over anxiety-inducing ones. Filter by topic and country.",
            "badges": [
                {"text": "Sentiment Analysis", "color": "#6A0DAD"}, # Purple
                {"text": "News API", "color": "#0DCAF0"},           # Light Blue/Cyan
                {"text": "Embeddings", "color": "#28A745"}
            ],
            "link": "https://some-good-news-ayush2991.streamlit.app/"
        },
        {
            "title": "Pytorch Playground",
            "description": "An interactive dashboard for visualizing the training of a neural network using Pytorch. You can play with the hyperparameters and see how they affect the training process.",
            "badges": [
                {"text": "Streamlit", "color": "#FF8C00"},      # Dark Orange
                {"text": "Pytorch", "color": "#007BFF"},        # Bright Blue
                {"text": "Neural Networks", "color": "#20C997"} # Tealish Green
            ],
            "link": "https://ayush2991-pytorch-playground-app-rimmmd.streamlit.app/"
        },
        {
            "title": "Flagging Toxic Comments",
            "description": "Live train a Pytorch model for various labels such as 'toxic', 'obscene' and 'threat' (or just use a pre-trained model). Then enter your own comment to get a live toxicity score!",
            "badges": [
                {"text": "Pytorch", "color": "#007BFF"},        # Bright Blue
                {"text": "Neural Networks", "color": "#20C997"}, # Tealish Green
                {"text": "Streamlit", "color": "#FF8C00"},      # Dark Orange
            ],
            "link": "https://jigsaw-comment-toxicity-challenge-ayush2991.streamlit.app/"
        },
        {
            "title": "Nutrition in Indian Meals",
            "description": "It's not easy to guess the nutritional value of Indian dishes you want to eat. This app helps you predict the nutritional value of a dish based on the closest match from a database of Indian meals. Or compare two dishes easily with visualizations.",
            "badges": [
                {"text": "Pandas", "color": "#6C757D"},
                {"text": "Streamlit", "color": "#FF8C00"},      # Dark Orange
                {"text": "Data Visualization", "color": "#FFC107"}
            ],
            "link": "https://nutrition-in-indian-meals-ayush2991.streamlit.app/"
        }
    ]
    # Display projects in a grid layout
    st.subheader("More Projects")
    cols = st.columns(2)
    
    # Get titles of featured projects to avoid duplicating them in the "More Projects" grid
    featured_project_titles = [fp["title"] for fp in featured_projects]
    
    for i, project in enumerate(projects):
        if project["title"] in featured_project_titles:
            continue # Skip if this project was already featured
        with cols[i % 2]:
            st.markdown(f"""
            <div class="project-card">
                <div class="project-card-content">
                    <h3>{project['title']}</h3>
                    <p>{project['description']}</p>
                </div>
                <div class="badges">
                    {"".join([f'<span class="badge" style="background-color: {badge["color"]};">{badge["text"]}</span>' for badge in project.get("badges", [])])}
                </div>
                <a href="{project['link']}" target="_blank">View Project</a>
            </div>
            """, unsafe_allow_html=True)

    
    # Add a footer
    st.write("---")
    st.write("Thank you for visiting my projects showcase!")
    st.write("Feel free to reach out if you have any questions or feedback.")

    # Add a sidebar with navigation
    st.sidebar.image("./data/profile.png", caption="Aayush Agarwal")
    st.sidebar.title("About Me")
    st.sidebar.write("I'm a *Machine Learning Engineer* with a passion for solving real-world problems using AI and data science. In my free time I write intuitive explanations for foundational data science concepts in my blog.")

    st.sidebar.subheader("Links")
    st.sidebar.markdown(":link: https://medium.com/@ayush2991")
    st.sidebar.markdown(":link: https://linkedin.com/in/ayush2991")
    st.sidebar.markdown(":link: https://github.com/ayush2991")
    st.sidebar.subheader(":email: Contact")
    st.sidebar.write("You can reach me at ayush2991@gmail.com")

if __name__ == "__main__":
    main()

# To run the app, use the command:
# streamlit run app.py