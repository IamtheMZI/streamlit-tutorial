import streamlit as st

st.title("অধ্যায় ৯: অ্যাডভান্সড ফিচার")

st.subheader("Streamlit ওয়েব অ্যাপকে আরও শক্তিশালী ও ইউজার ফ্রেন্ডলি করার জন্য প্রয়োজনীয় ফিচার")

st.subheader("""ভূমিকা
             
এই অধ্যায়ে তুমি শিখবে:

Custom Components কিভাবে বানাতে হয়

Session State দিয়ে তথ্য কীভাবে ধরে রাখা হয়

কিভাবে Caching ব্যবহার করে অ্যাপ দ্রুত করা যায়

কিভাবে অ্যাপ সিকিউর করা যায় Authentication দিয়ে

কীভাবে ফাইল আপলোড → প্রিভিউ → ডাউনলোড ওয়ার্কফ্লো বানানো যায়""")


st.subheader("""ধাপ ১: কী কী লাগবে?
তোমার প্রয়োজন হবে:
             
| জিনিস                         | উদ্দেশ্য                                             |
|------------------------------|------------------------------------------------------|
✅ Streamlit              | ওয়েব অ্যাপ তৈরির লাইব্রেরি       |
| ✅ GitHub Account         | কোড স্টোর ও শেয়ার করার জন্য     |
| ✅ Streamlit Cloud Account | অ্যাপ হোস্ট করার জন্য           |
""")

st.subheader("""ধাপ ২: Custom Components (streamlit.components.v1)
             
🔍 এটি কী?
             
Streamlit নিজে অনেক UI কম্পোনেন্ট দেয়। কিন্তু আপনি চাইলে নিজের HTML, CSS, JavaScript বা React দিয়ে তৈরি করা কম্পোনেন্ট যুক্ত করতে পারেন।""")

st.write("লাইব্রেরি:")

st.write("নিচের কোড কপি করো:")

st.code('''import streamlit.components.v1 as components
''', language="bash")

st.code('''উদাহরণ:

components.html(
    """
    <h2 style='color:green;'>এটি একটি কাস্টম HTML কম্পোনেন্ট</h2>
    <p>Streamlit এর ভিতরে HTML ব্যবহার করা যাচ্ছে!</p>
    """,
    height=150
)''', language="bash")

with st.expander("বিস্তারিত দেখুন"):
    st.subheader("""import streamlit.components.v1 as components
                 
    এই লাইনের মানে, কারণ, আর ব্যবহারের পদ্ধতি আমি নিচে খুব সহজভাবে ব্যাখ্যা করছি:""")

    st.subheader("""এটা কী?
    streamlit.components.v1 হলো Streamlit-এর একটি মডিউল, যা দিয়ে আপনি Custom Components (নিজের তৈরি HTML, CSS, JavaScript/React UI) আপনার Streamlit অ্যাপে যুক্ত করতে পারেন।

    as components মানে হলো —
                 
    এই লম্বা নামটার (streamlit.components.v1) বদলে আমরা সংক্ষেপে components লিখে ব্যবহার করবো।""")
    

    st.subheader("""কেন ব্যবহার করবো?
                 
    Streamlit নিজে কিছু নির্দিষ্ট কম্পোনেন্ট দেয় যেমন st.button(), st.text_input() ইত্যাদি।

    কিন্তু যদি আপনি চাইছেন এমন কিছু করতে, যেটা Streamlit ডিফল্টভাবে দেয় না — যেমন:

    সুন্দর ডিজাইনের HTML UI

    কাস্টম ভিডিও প্লেয়ার

    React ভিত্তিক চার্ট

    Special animation, iframe embed, custom JS ইত্যাদি

    তখন আপনি Custom Component বানিয়ে বা HTML/JS ইনপুট দিয়ে সেটা অ্যাপে দেখাতে পারবেন streamlit.components.v1 দিয়ে।""")

    st.subheader("""কিভাবে ব্যবহার করবো?
                 
    👉 উদাহরণ ১: HTML কোড দেখানো""")

    st.write("নিচের কোড কপি করো:")

    st.code('''import streamlit as st
    import streamlit.components.v1 as components

    st.title("আমার অ্যাপ")

    components.html(
        """
        <h2 style='color:blue;'>এইটা একটা কাস্টম HTML হেডিং!</h2>
        <p>এখানে আপনি নিজের HTML, CSS কোড ব্যবহার করতে পারবেন।</p>
        """,
        height=150,
    )
    ''', language="bash")

    import streamlit as st
    import streamlit.components.v1 as components

    st.title("আমার অ্যাপ")

    components.html(
        """
        <h2 style='color:blue;'>এইটা একটা কাস্টম HTML হেডিং!</h2>
        <p>এখানে আপনি নিজের HTML, CSS কোড ব্যবহার করতে পারবেন।</p>
        """,
        height=150,
    )

    st.write(" এখানে components.html() ব্যবহার করে HTML কোড Streamlit অ্যাপে দেখানো হয়েছে।")

    st.subheader("উদাহরণ ২: YouTube ভিডিও এমবেড করা")

    st.write("নিচের কোড কপি করো:")

    st.code('''
    components.html(
    """
    <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/B2iAodr0fOo" 
    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    height=315,
    )

    ''', language="bash")

    components.html(
    """
    <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/B2iAodr0fOo" 
    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    height=315,
    )

    st.write("এখানে আমরা iframe ব্যবহার করে ইউটিউব ভিডিও দেখিয়েছি Streamlit অ্যাপের ভেতরে।")


st.subheader("""ধাপ ৩: Session State
             
এটি কী?
             
যখন তুমি চাইছো ইউজারের ইনপুট, ক্লিক, বা অ্যাপের অবস্থা মনে রাখতে, তখন st.session_state ব্যবহার করা হয়।

💡 উদাহরণ:""")

st.write("নিচের কোড কপি করো:")

st.code('''

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("➕ বাড়াও"):
    st.session_state.count += 1

st.write("বর্তমান মান:", st.session_state.count)

    ''', language="bash")


#Session State
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("➕ বাড়াও"):
    st.session_state.count += 1

st.write("বর্তমান মান:", st.session_state.count)

st.write("➡️ এখানে বোতাম ক্লিক করলে মান বাড়ে এবং সেটা মনে রাখে।")


st.subheader("""ধাপ ৪: Caching with @st.cache_data
🔍 এটি কী?
কোনো ফাংশনের রেজাল্ট যদি একই থাকে, তাহলে তা বারবার না করে একবার করে Cache এ রেখে দেয়, ফলে অ্যাপ দ্রুত চলে।

💡 উদাহরণ:""")

st.write("নিচের কোড কপি করো:")

st.code('''import streamlit as st
import time

@st.cache_data
def slow_function():
    time.sleep(3)
    return "ডেটা লোড সম্পন্ন ✅"

st.write(slow_function())


''', language="bash")

#Caching with @st.cache_data
import time

@st.cache_data
def slow_function():
    time.sleep(3)
    return "ডেটা লোড সম্পন্ন ✅"

st.write(slow_function())

st.write("➡️ প্রথমবার ৩ সেকেন্ড সময় নেবে, তারপরের বার একদম দ্রুত চলে যাবে।")


st.subheader("""ধাপ ৫: Authentication / Password Protection
             
Streamlit এ বিল্ট-ইন Authentication না থাকলেও, আপনি নিজে st.text_input দিয়ে ইউজারনেম/পাসওয়ার্ড চেক করতে পারেন।

💡 উদাহরণ:""")

st.write("নিচের কোড কপি করো:")

st.code('''

username = st.text_input("ইউজারনেম")
password = st.text_input("পাসওয়ার্ড", type="password")

if st.button("লগইন"):
    if username == "admin" and password == "1234":
        st.success("লগইন সফল ✅")
    else:
        st.error("ভুল ইউজারনেম অথবা পাসওয়ার্ড ❌")

''', language="bash")



#Authentication / Password Protection
username = st.text_input("ইউজারনেম")
password = st.text_input("পাসওয়ার্ড", type="password")

if st.button("লগইন"):
    if username == "admin" and password == "1234":
        st.success("লগইন সফল ✅")
    else:
        st.error("ভুল ইউজারনেম অথবা পাসওয়ার্ড ❌")


st.subheader("""ধাপ ৬: Upload → Preview → Download Workflow
             
🔍 এটি কী?
             
ইউজার ফাইল আপলোড করবে → আপনি সেটা প্রিভিউ দেখাবেন → এরপর সেই ডেটা প্রসেস করে ডাউনলোড লিংক দিবেন।

💡 উদাহরণ:""")


st.code('''
import pandas as pd

uploaded_file = st.file_uploader("CSV ফাইল আপলোড করুন", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 প্রিভিউ:", df.head())

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 ডাউনলোড করুন",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )


''', language="bash")


#Upload → Preview → Download Workflow
import pandas as pd

uploaded_file = st.file_uploader("CSV ফাইল আপলোড করুন", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 প্রিভিউ:", df.head())

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 ডাউনলোড করুন",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )


st.subheader("""উপসংহার
             
এই অধ্যায়ে তুমি শিখেছো কীভাবে Streamlit অ্যাপে:

কাস্টম কম্পোনেন্ট যুক্ত করা যায়

ইউজারের তথ্য স্মরণ রাখা যায়

অ্যাপ পারফরম্যান্স বাড়ানো যায় কেশিং দিয়ে

অ্যাপ সিকিউর করা যায় লগইন পদ্ধতিতে

ফাইল আপলোড, প্রিভিউ ও ডাউনলোড করা যায়

🔔 এই ফিচারগুলো ব্যবহার করে তুমি এখন আরও প্রফেশনাল Streamlit অ্যাপ বানাতে পারবে।""")






