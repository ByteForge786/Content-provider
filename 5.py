import streamlit as st
import streamlit.components.v1 as components

# Streamlit app
st.title("URL Content Fetcher")

# Input for URL
url = st.text_input("Enter the URL:", "")

# JavaScript code
js_code = f"""
<script>
async function fetchData() {{
    try {{
        const response = await fetch('{url}');
        const data = await response.text();
        document.getElementById('content').innerText = data;
    }} catch (error) {{
        document.getElementById('content').innerText = 'Error: ' + error.message;
    }}
}}

fetchData();
</script>
<div id="content"></div>
"""

if st.button("Fetch Content"):
    if url:
        # Render the JavaScript component
        components.html(js_code, height=600)
    else:
        st.error("Please enter a URL")

# Display raw JSON if successfully fetched
if st.checkbox("Display Raw JSON"):
    components.html(f"""
    <script>
    async function fetchJSON() {{
        try {{
            const response = await fetch('{url}');
            const data = await response.json();
            document.getElementById('json-content').innerText = JSON.stringify(data, null, 2);
        }} catch (error) {{
            document.getElementById('json-content').innerText = 'Error: ' + error.message;
        }}
    }}

    fetchJSON();
    </script>
    <pre id="json-content"></pre>
    """, height=600)
