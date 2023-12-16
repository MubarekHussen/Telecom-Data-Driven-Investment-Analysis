import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D


def display_handsets():
    """
    This function reads the 'top_10_handsets.csv' file, creates a bar plot using Plotly Express with 'Handset Type' on the x-axis and 'count' on the y-axis, and displays the plot in a Streamlit app.
    """
    df = pd.read_csv("../data/top_10_handsets.csv")
    fig = px.bar(df, x="Handset Type", y="count")
    fig.update_traces(marker_color="orange")
    fig.update_layout(font=dict(size=14))
    fig.update_layout(title_text="Top 10 Handset Types", font=dict(size=14))

    st.plotly_chart(fig)


def display_manufacturers():
    """
    This function reads the 'top_3_manufacturers.csv' file, creates a pie chart using Plotly Express with 'count' as values and 'Handset Manufacturer' as names, and displays the plot in a Streamlit app.
    """
    df = pd.read_csv("../data/top_3_manufacturers.csv")
    fig = px.pie(df, values="count", names="Handset Manufacturer", hole=0.5)
    fig.update_layout(title_text="Top 3 Handset Manufacturers")
    st.plotly_chart(fig)


def display_clusters():
    """
    This function reads the 'engagement_clusters.csv' file, creates a 3D scatter plot using Matplotlib with 'Number of Sessions', 'Total Session Duration', and 'Total Traffic' as axes, and displays the plot in a Streamlit app.
    """
    df = pd.read_csv("../data/engagement_clusters.csv")
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    scatter = ax.scatter(
        df["Number of Sessions"],
        df["Total Session Duration"],
        df["Total Traffic"],
        c=df["Engagement Cluster"],
        cmap="viridis",
    )

    ax.set_title("Customer Engagement Clusters")
    ax.set_xlabel("Number of Sessions")
    ax.set_ylabel("Total Session Duration")
    ax.set_zlabel("Total Traffic")

    cbar = plt.colorbar(scatter)
    cbar.set_label("Cluster")

    plt.savefig("engagement_clusters.png")
    st.title("Engagement Clusters")
    st.image("engagement_clusters.png")
    st.title("Experience Clusters")
    st.image("experience_clusters.png")


def display_top_3_apps():
    """
    This function reads the 'engagement_clusters.csv' file, creates a bar plot using Matplotlib with 'Total Traffic' on the x-axis and 'Application' on the y-axis, and displays the plot in a Streamlit app.
    """
    top_3_data = {}
    applications = {
        "Google": ["Google Download Data", "Google Upload Data"],
        "Email": ["Email Download Data", "Email Upload Data"],
        "Youtube": ["Youtube Download Data", "Youtube Upload Data"],
        "Netflix": ["Netflix Download Data", "Netflix Upload Data"],
    }

    data_df = pd.read_csv("../data/engagement_clusters.csv")

    for app, columns in applications.items():
        total_traffic = data_df[columns].sum().sum()
        top_3_data[app] = total_traffic

    top_3_apps = pd.Series(top_3_data).nlargest(3)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_3_apps.index, top_3_apps.values, color="skyblue")
    ax.set_xlabel("Total Traffic")
    ax.set_ylabel("Application")
    ax.set_title("Top 3 Most Used Applications")
    ax.invert_yaxis()

    st.pyplot(fig)


def display_histograms():
    """
    This function reads a CSV file, creates two histograms for 'Total Upload Data' and 'Total Download Data', and displays them side by side in a Streamlit app.
    """
    df = pd.read_csv("../data/df.csv")
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].hist(df["Total Upload Data"], bins=20)
    axs[0].set_xlabel("Total Uploaded Data")
    axs[0].set_ylabel("Frequency")
    axs[0].set_title("Total Uploaded Data")
    axs[1].hist(df["Total Download Data"], bins=20)
    axs[1].set_xlabel("Total Download Data")
    axs[1].set_ylabel("Frequency")
    axs[1].set_title("Total Download Data")
    fig.suptitle("Total Download and Upload Grouped by User")
    st.pyplot(fig)


display_manufacturers()
display_handsets()
display_clusters()
display_top_3_apps()
display_histograms()
