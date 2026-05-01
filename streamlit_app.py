import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="CopyGenie", page_icon="🧠", layout="centered")

# ---- SESSION STATE ----
if "output" not in st.session_state:
    st.session_state.output = ""

if "count" not in st.session_state:
    st.session_state.count = 0

# ---- HERO ----
st.title("🧠 CopyGenie")
st.subheader("Turn product features to benefits and convert to sales in seconds")

st.markdown("""
### Write Product Descriptions That Actually Sell  
Stop struggling with words. Enter your product details and get high-converting descriptions for Amazon, eBay, Jumia, or your store—instantly.
""")

st.divider()

# ---- FORM ----
st.header("📦 Product Details")

product_name = st.text_input("Product Name", placeholder="What are you selling?")
features = st.text_area("Key Features", placeholder="List key benefits (one per line)")
audience = st.text_input("Target Audience", placeholder="Who is this for?")
tone = st.selectbox("Tone", ["Persuasive", "Professional", "Casual", "Luxury", "Friendly"])

content_type = st.selectbox(
    "What do you want to generate?",
    ["Full Product Description", "Bullet Points Only", "SEO Product Title", "Facebook Ad Copy"]
)

# ---- FUNCTION ----
def generate_copy():
    if st.session_state.count >= 3:
        st.error("Free limit reached. Upgrade to continue 🚀")
        return

    if not product_name or not features:
        st.warning("Please fill in Product Name and Key Features.")
        return

    with st.spinner("Generating high-converting copy..."):

        if content_type == "Full Product Description":
            instruction = """
            Write a high-converting product description with hook, benefits, bullet points, and CTA.
            """

        elif content_type == "Bullet Points Only":
            instruction = "Convert features into benefit-driven bullet points."

        elif content_type == "SEO Product Title":
            instruction = "Write an SEO-optimized product title."

        else:
            instruction = "Write a Facebook ad with hook, benefits, and CTA."

        prompt = f"""
        You are a professional eCommerce copywriter.

        Product: {product_name}
        Features:
        {features}
        Audience: {audience}
        Tone: {tone}

        Task:
        {instruction}
        """

        response = client.chat.completions.create(
            model="gpt-5.3",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        st.session_state.output = response.choices[0].message.content
        st.session_state.count += 1

# ---- BUTTONS ----
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Generate"):
        generate_copy()

with col2:
    if st.button("🔄 Regenerate"):
        generate_copy()

# ---- OUTPUT ----
if st.session_state.output:
    st.subheader("📝 Generated Copy")
    st.write(st.session_state.output)

    # Copy Button
    st.code(st.session_state.output, language="text")

    # Download Button
    st.download_button(
        label="📥 Download as TXT",
        data=st.session_state.output,
        file_name="copygenie_output.txt",
        mime="text/plain"
    )

# ---- USAGE COUNTER ----
st.caption(f"Free uses left: {3 - st.session_state.count}")