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
        border: 1px solid;
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
        min-height: 240px;              /* Minimum height for all cards */
    }
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    st.title("My Projects")
    st.write("Welcome to my projects showcase! Here are some of the projects I've worked on:")

    # Add your project details here
    projects = [
        {
            "title": "Hello World",
            "description": "My first app: Hello, World!",
            "link": "https://ayush2991-hello-world-app-gasriq.streamlit.app/"
        },
        {
            "title": "Nutrition in Indian Meals",
            "description": "A simple app that provides nutritional information about various Indian meals.",
            "link": "https://nutrition-in-indian-meals-ayush2991.streamlit.app/"
        },
        {
            "title": "Some Good News",
            "description": "A simple news app that de-prioritizes anxiety-inducing news and emphasizes source credibility.",
            "link": "https://some-good-news-ayush2991.streamlit.app/"
        },
        {
            "title": "Pytorch Playground",
            "description": "A dashboard for visualizing the training of a neural network using Pytorch.",
            "link": "https://ayush2991-pytorch-playground-app-rimmmd.streamlit.app/"
        },
        {
            "title": "Jigsaw Comment Toxicity Challenge",
            "description": "Detecting toxic comments using a machine learning model.",
            "link": "https://jigsaw-comment-toxicity-challenge-ayush2991.streamlit.app/"
        },
        {
            "title": "Stock Market Dashboard",
            "description": "A dashboard for visualizing stock market data.",
            "link": "https://stock-market-dashboard-ayush2991.streamlit.app/"
        },

    ]
    # Display projects in a grid layout
    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="project-card">
                <div class="project-card-content">
                    <h4>{project['title']}</h4>
                    <p>{project['description']}</p>
                </div>
                <a href="{project['link']}" target="_blank">View Project</a>
            </div>
            """, unsafe_allow_html=True)

    
    # Add a footer
    st.write("---")
    st.write("Thank you for visiting my projects showcase!")
    st.write("Feel free to reach out if you have any questions or feedback.")

    # Add a sidebar with navigation
    st.sidebar.image("https://placehold.co/600x400", caption="Aayush Agarwal")
    st.sidebar.write("I am a software developer with a passion for building web applications.")
    st.sidebar.markdown("## Links")
    st.sidebar.markdown("https://linkedin.com/in/ayush2991")
    st.sidebar.markdown("https://medium.com/@ayush2991")
    st.sidebar.markdown("https://github.com/ayush2991")
    st.sidebar.markdown("## Contact")
    st.sidebar.write("You can reach me at ayush2991@gmail.com")

if __name__ == "__main__":
    main()

# To run the app, use the command:
# streamlit run app.py