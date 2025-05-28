import streamlit as st

st.subheader("অধ্যায় ৮: Streamlit অ্যাপ অনলাইনে প্রকাশ")

st.subheader("""ভূমিকা
             
তুমি কি চাও তোমার বানানো Streamlit অ্যাপটি সবাই অনলাইনে দেখতে ও ব্যবহার করতে পারুক?
এই অধ্যায়ে তুমি শিখবে কীভাবে তোমার লোকাল কম্পিউটারে বানানো অ্যাপটি GitHub এ আপলোড করে Streamlit Cloud ব্যবহার করে একদম ফ্রি-তে হোস্ট করতে পারো।""")

st.subheader(""" এই পোস্টে তুমি শিখবে —
             
✅ কীভাবে requirements.txt ফাইল তৈরি করতে হয়
             
✅ কীভাবে প্রজেক্ট GitHub এ আপলোড করতে হয়
             
✅ কীভাবে Streamlit Cloud-এ অ্যাপ হোস্ট করতে হয়
             
✅ কীভাবে একটি শেয়ারযোগ্য URL তৈরি হয়""")


st.subheader("""ধাপ ১: কী কী লাগবে?
তোমার প্রয়োজন হবে:
             
| জিনিস                         | উদ্দেশ্য                                             |
|------------------------------|------------------------------------------------------|
✅ Streamlit              | ওয়েব অ্যাপ তৈরির লাইব্রেরি       |
| ✅ GitHub Account         | কোড স্টোর ও শেয়ার করার জন্য     |
| ✅ Streamlit Cloud Account | অ্যাপ হোস্ট করার জন্য           |
| ✅ requirements.txt       | লাইব্রেরি ইনস্টল করার জন্য দরকার |
""")

st.subheader("""ধাপ ১: requirements.txt ফাইল তৈরি করা
             
🔹 VS Code-এ তোমার প্রজেক্ট ফোল্ডারে একটি ফাইল তৈরি করো requirements.txt নামে।

🔹 নিচের মতো লাইব্রেরিগুলোর নাম লিখে রাখো (তোমার অ্যাপে যেগুলা ইউজ করছো):""")


st.code('requirements.txt', language="bash")

st.write(" ফাইলের ভিতরের কন্টেন্ট হবে এমন:")

st.code('''streamlit
pandas
numpy
plotly
matplotlib
altair
mysql-connector-python
''',language="bash")

st.subheader("""Step 2: requirements.txt ফাইল কীভাবে বানাবে?
             
পদ্ধতি ১: VS Code বা Notepad দিয়ে
             
১. নতুন ফাইল তৈরি করো।

২. নিচের লাইন লিখো:""")

st.code('''streamlit
pandas
numpy
plotly
matplotlib
altair
mysql-connector-python
''',language="bash")

st.write("৩. ফাইলটি save করো এই নামে:")

st.code('requirements.txt', language="bash")

st.markdown('<p style="font-size:12px;">⚠️ .txt টাইপ নিশ্চিত হও (না হলে Streamlit Cloud বুঝবে না)।</p>', unsafe_allow_html=True)

st.subheader("""ধাপ ২: GitHub এ প্রজেক্ট আপলোড
             
🔹 https://github.com এ গিয়ে একটা নতুন Repository তৈরি করো।
             
🔹 তারপর VS Code থেকে Git দিয়ে Push করো:।""")


st.write("এই রকম তোমার GitHub এ দেখা যাবে:")

st.code('''git init
git remote add origin https://github.com/your-username/your-repo-name.git
git add .
git commit -m "Initial Commit"
git push -u origin main
''', language="bash")


st.subheader("""ধাপ ৩: Streamlit Cloud-এ হোস্টিং
             
🔗 Visit: https://streamlit.io/cloud

🔹 লগইন করো (GitHub দিয়ে)।
             
🔹 “Deploy an app” বাটনে ক্লিক করো।
             
🔹 তোমার GitHub Repo এর লিংক দাও।
             
🔹 main file path হিসেবে your_app.py ফাইলের নাম দাও।
             
🔹 Deploy বাটনে ক্লিক করো।

🟢 কিছুক্ষণের মধ্যে তোমার অ্যাপ অনলাইনে লাইভ হয়ে যাবে!""")

st.subheader("""ধাপ ৪: শেয়ারযোগ্য URL
             
Streamlit Cloud তোমাকে একটি লিংক দেবে, যেমন:""")

st.code('''https://your-app-name.streamlit.app
''', language="bash")

st.write("এই লিংক তুমি বন্ধুদের, ইউজারদের বা ভিডিওর নিচে শেয়ার করতে পারো।")

st.subheader("""উপসংহার
             
এখন তুমি শিখে গেছো কীভাবে লোকালি বানানো Streamlit অ্যাপ GitHub এ আপলোড করে অনলাইনে ফ্রি হোস্ট করতে হয়।

এটা তোমার প্রজেক্টকে অনেক মানুষের কাছে পৌঁছানোর সুযোগ করে দেয়।

""")