import requests

# Define the base URL and your access key
base_url = "http://api.exchangeratesapi.io/v1/latest"
access_key = "8d33b72224d5396cbf4aa532d86051a8"  # Replace with your actual access key

# Construct the full URL
url = f"{base_url}?access_key={access_key}"

# Send a GET request to the API
response = requests.get(url)

# Check the HTTP status code
if response.status_code == 200:
    # Request was successful, print the JSON response
    data = response.json()
    print(data)
else:
    # Request failed, print an error message
    print(f"Request failed with status code: {response.status_code}")
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
# testing
