import streamlit as st

st.title("""3_Basic_Components.py ফাইল তৈরি
এই ফাইলটিতে আমরা নিচের ৪টি ভাগে ভাগ করে শেখাবো:

. টেক্সট এলিমেন্ট

. ইন্টার‌অ্যাকশন উইজেট (ইউজার ইনপুট)

. ফাইল ও মিডিয়া এলিমেন্ট

. তারিখ ও সময় ইনপুট
""")

st.code("""st.title("👉 st.title() - এটা হচ্ছে সবচেয়ে বড় টাইটেল")
st.header("👉 st.header() - এটা একটা হেডার টেক্সট")
st.subheader("👉 st.subheader() - এটা সাব-হেডার")
st.write("👉 st.write() - এটা নরমাল লেখা দেখানোর জন্য")
st.markdown("👉 **st.markdown()** - Markdown দিয়ে লেখা ফরম্যাট করা যায়। যেমন: **Bold**, *Italic*")
st.code("print('Hello Streamlit')", language='python')

st.divider()

st.subheader("🧩 ২. ইউজার ইনপুট উইজেট")

name = st.text_input("তোমার নাম লিখো:")
if st.button("👋 বলো হ্যালো"):
    st.success(f"হ্যালো, {name}! তোমাকে Streamlit এ স্বাগতম!")

agree = st.checkbox("আমি শিখতে আগ্রহী")
if agree:
    st.info("দারুন! চল শেখা শুরু করি 🎓")

gender = st.radio("তোমার লিঙ্গ নির্বাচন করো:", ["পুরুষ", "নারী", "অন্যান্য"])
st.write("তুমি নির্বাচন করেছো:", gender)

option = st.selectbox("তোমার পছন্দের ভাষা:", ["Python", "JavaScript", "C++"])
st.success(f"তোমার পছন্দ: {option}")

level = st.slider("তোমার শেখার আগ্রহের লেভেল (০-১০):", 0, 10)
st.write("তোমার আগ্রহ:", level)

st.divider()

st.subheader("📁 ৩. ফাইল ও মিডিয়া")

st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=250)
video_url = "https://www.youtube.com/watch?v=R2nr1uZ8ffc"
st.video(video_url)

uploaded_file = st.file_uploader("একটি ফাইল আপলোড করো:")
if uploaded_file:
    st.success("✅ ফাইল আপলোড সফল হয়েছে!")

st.divider()

st.subheader("📅 ৪. তারিখ ও সময় ইনপুট")

date = st.date_input("তারিখ নির্বাচন করো:")
time = st.time_input("সময় নির্বাচন করো:")

st.write(f"নির্বাচিত তারিখ: {date} এবং সময়: {time}")
""", language='bash')


# copy text
st.text("এই কোড গুলো কপি করো")









st.title("👉 st.title() - এটা হচ্ছে সবচেয়ে বড় টাইটেল")
st.header("👉 st.header() - এটা একটা হেডার টেক্সট")
st.subheader("👉 st.subheader() - এটা সাব-হেডার")
st.write("👉 st.write() - এটা নরমাল লেখা দেখানোর জন্য")
st.markdown("👉 **st.markdown()** - Markdown দিয়ে লেখা ফরম্যাট করা যায়। যেমন: **Bold**, *Italic*")
st.code("print('Hello Streamlit')", language='python')

st.divider()

st.subheader("🧩 ২. ইউজার ইনপুট উইজেট")

name = st.text_input("তোমার নাম লিখো:")
if st.button("👋 বলো হ্যালো"):
    st.success(f"হ্যালো, {name}! তোমাকে Streamlit এ স্বাগতম!")

agree = st.checkbox("আমি শিখতে আগ্রহী")
if agree:
    st.info("দারুন! চল শেখা শুরু করি 🎓")

gender = st.radio("তোমার লিঙ্গ নির্বাচন করো:", ["পুরুষ", "নারী", "অন্যান্য"])
st.write("তুমি নির্বাচন করেছো:", gender)

option = st.selectbox("তোমার পছন্দের ভাষা:", ["Python", "JavaScript", "C++"])
st.success(f"তোমার পছন্দ: {option}")

level = st.slider("তোমার শেখার আগ্রহের লেভেল (০-১০):", 0, 10)
st.write("তোমার আগ্রহ:", level)

st.divider()

st.subheader("📁 ৩. ফাইল ও মিডিয়া")

st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=250)
video_url = "https://www.youtube.com/watch?v=R2nr1uZ8ffc"
st.video(video_url)

uploaded_file = st.file_uploader("একটি ফাইল আপলোড করো:")
if uploaded_file:
    st.success("✅ ফাইল আপলোড সফল হয়েছে!")

st.divider()

st.subheader("📅 ৪. তারিখ ও সময় ইনপুট")

date = st.date_input("তারিখ নির্বাচন করো:")
time = st.time_input("সময় নির্বাচন করো:")

st.write(f"নির্বাচিত তারিখ: {date} এবং সময়: {time}")


st.title("""✅ রান করার পর তুমি যা দেখতে পাবে:

🔸 সুন্দরভাবে বিভক্ত বিভাগে সবকিছু
🔸 প্রতিটি কম্পোনেন্টে নিজের ইন্টার‌অ্যাকশন করতে পারবে
🔸 সরাসরি ফলাফল দেখতে পাবে স্ক্রিনে
""")

st.title("""✍️ এখন কী করো:
উপরের কোড কপি করে pages/3_Basic_Components.py ফাইলে রাখো

streamlit run app.py চালাও

সাইডবার থেকে অধ্যায় ৩: Basic Components সিলেক্ট করো

শেখো, ইনপুট দাও, ফলাফল দেখো
""")




