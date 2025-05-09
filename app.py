# A streamlit app to showcase my projects
import streamlit as st


def main():
    st.set_page_config(
        page_title="My Projects",
        page_icon=":rocket:",
        layout="wide",
    )

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
            "title": "Horoscope",
            "description": "A simple horoscope app that provides daily horoscope readings.",
            "link": "https://horoscope-ayush2991.streamlit.app/"
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
            "title": "Project 6",
            "description": "Description of project 6.",
            "link": "https://example.com/project6"
        },

    ]
    # Display projects in a grid layout
    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i % 3]:
            st.subheader(project["title"])
            st.write(project["description"])
            st.markdown(f"[View Project]({project['link']})")

    # Show more projects in a collapsible section in a grid layout
    st.write("### More Projects")
    st.write("Click below to see more projects.")
    # Create a button to expand/collapse more projects
    # This is a simple way to show/hide content in Streamlit
    # You can also use st.expander for a more interactive approach
    # Here we use st.expander to create a collapsible section
    with st.expander("Show more projects"):
        for i in range(7, 13):
            st.subheader(f"Project {i}")
            st.write(f"Description of project {i}.")
            st.markdown(f"[View Project](https://example.com/project{i})")
            st.write("Additional details about project {i} can be added here.")
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