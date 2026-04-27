<<<<<<< HEAD
import streamlit as st
from openai import OpenAI

client = OpenAI()

# Page config
st.set_page_config(page_title="CopyGenie", page_icon="🧠", layout="centered")

# Header
st.title("🧠 CopyGenie")
st.caption("AI-powered product description generator for Jumia sellers")

# Sidebar (inputs)
st.sidebar.header("🛠️ Product Details")

product_name = st.sidebar.text_input("Product Name")
features = st.sidebar.text_area("Key Features (one per line)")
target = st.sidebar.text_input("Target Audience")
tone = st.sidebar.selectbox("Tone", ["Persuasive", "Professional", "Casual"])

generate = st.sidebar.button("🚀 Generate")

# Main area
if generate:
    if not product_name or not features:
        st.warning("Please fill in product name and features")
    else:
        prompt = f"""
Write a high-converting Jumia product description.

Product: {product_name}
Features:
{features}
Target Audience: {target}
Tone: {tone}

Return:
- Short Description
- Bullet Benefits
- Full Description

Make it persuasive, clear, and benefit-driven.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        output = response.choices[0].message.content

        st.subheader("✨ Generated Copy")
        st.markdown(output)

        # Copy box
        st.text_area("📋 Copy your text below:", value=output, height=200)

else:
=======
import streamlit as st
from openai import OpenAI

client = OpenAI()

# Page config
st.set_page_config(page_title="CopyGenie", page_icon="🧠", layout="centered")

# Header
st.title("🧠 CopyGenie")
st.caption("AI-powered product description generator for Jumia sellers")

# Sidebar (inputs)
st.sidebar.header("🛠️ Product Details")

product_name = st.sidebar.text_input("Product Name")
features = st.sidebar.text_area("Key Features (one per line)")
target = st.sidebar.text_input("Target Audience")
tone = st.sidebar.selectbox("Tone", ["Persuasive", "Professional", "Casual"])

generate = st.sidebar.button("🚀 Generate")

# Main area
if generate:
    if not product_name or not features:
        st.warning("Please fill in product name and features")
    else:
        prompt = f"""
Write a high-converting Jumia product description.

Product: {product_name}
Features:
{features}
Target Audience: {target}
Tone: {tone}

Return:
- Short Description
- Bullet Benefits
- Full Description

Make it persuasive, clear, and benefit-driven.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        output = response.choices[0].message.content

        st.subheader("✨ Generated Copy")
        st.markdown(output)

        # Copy box
        st.text_area("📋 Copy your text below:", value=output, height=200)

else:
>>>>>>> 884196ee5af31de36ca53e75c993c8b3b5efbae9
    st.info("Fill in product details on the left and click Generate 🚀")