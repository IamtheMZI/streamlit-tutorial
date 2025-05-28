import streamlit as st

st.title("📦 অধ্যায় ২: সেটআপ ও ইনস্টলেশন")

st.header("🔹 Python ইনস্টলেশন")

st.markdown("""
1. প্রথমে [https://www.python.org/downloads/](https://www.python.org/downloads/) লিংকে যাও  
2. আপনার OS অনুযায়ী (Windows/Mac/Linux) **Python 3.10+** ভার্সন ডাউনলোড করে ইনস্টল করো  
3. **"Add Python to PATH"** অপশনটা অবশ্যই টিক দাও ✅  
""")

st.success("✅ টার্মিনালে `python --version` কমান্ড দিয়ে ইনস্টল হয়েছে কিনা চেক করো")

st.header("🔹 Virtual Environment তৈরি")

st.code("""
# টার্মিনালে নিচের কমান্ডগুলো দাও:
python -m venv venv
venv\\Scripts\\activate   # Windows এর জন্য
source venv/bin/activate  # Linux/Mac এর জন্য
""", language='bash')

st.success("✅ এখন তোমার ভার্চুয়াল এনভায়রনমেন্ট অ্যাক্টিভ!")

st.header("🔹 Streamlit ইনস্টলেশন")

st.code("pip install streamlit", language='bash')

st.success("✅ Streamlit ইনস্টল হয়ে গেছে!")

st.header("🔹 প্রথম অ্যাপ ফাইল তৈরি")

st.markdown("""
✅ `app.py` নামে একটি Python ফাইল তৈরি করো এবং নিচের কোডটি লিখো:
""")

st.code("""
import streamlit as st

st.title("👋 হ্যালো, Streamlit!")
st.write("Streamlit অ্যাপে তোমাকে স্বাগতম!")
""")

st.header("🔹 Streamlit অ্যাপ রান করা")

st.code("streamlit run app.py", language='bash')

st.markdown("""
➡️ ব্রাউজারে অ্যাপ খুলবে এই লিংকে: `http://localhost:8501`

💡 যদি অ্যাপ আপডেট করো, তাহলে ব্রাউজারে **auto-refresh** হয়ে যাবে।
""")

st.header("🔹 Common Errors ও সমাধান")

st.markdown("""
❌ `streamlit: command not found`  
👉 সমাধান: ভার্চুয়াল এনভায়রনমেন্ট অ্যাক্টিভ করো

❌ ব্রাউজারে লিংক ওপেন হচ্ছে না  
👉 সমাধান: টার্মিনালে `streamlit run app.py` দিয়ে আবার চালাও

❌ ModuleNotFoundError: streamlit  
👉 সমাধান: `pip install streamlit` দিয়ে লাইব্রেরি ইনস্টল করো
""")

st.info("🎉 অভিনন্দন! তুমি Streamlit এর সেটআপ সফলভাবে শিখে ফেলেছো।")



st.title("""এখন করণীয়:
pages ফোল্ডারে 2_Installation.py নামে এই কোডটি সংরক্ষণ করো

তারপর আবার streamlit run app.py দিয়ে চালাও

সাইডবারে অধ্যায় ২: সেটআপ ও ইনস্টলেশন নামে একটি অপশন দেখাবে

ওখানে ক্লিক করলে উপরের টিউটোরিয়ালটি সুন্দরভাবে দেখাবে
         
""")


st.title("ফোল্ডার স্ট্রাকচার হওয়া উচিত:")

st.code('''your-project/
│
├── app.py                 👈 শুধু টাইটেল ও হোমপেজ থাকবে
├── requirements.txt
└── pages/
    ├── 1_Intro.py         👈 অধ্যায় ১
    ├── 2_Installation.py  👈 অধ্যায় ২
    └── 3_Widgets.py       👈 অধ্যায় ৩ (যখন তৈরি করবে)''', language='bash')



    

