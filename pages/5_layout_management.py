import streamlit as st
st.subheader("""Layout Management (লেআউট ব্যবস্থাপনা)
         
Streamlit-এ layout মানে কীভাবে content গুলো স্ক্রিনে সাজানো হয়। নিচে প্রতিটি layout ফিচার সহজভাবে ব্যাখ্যা করছি:""")

st.subheader(""" 1. Columns: st.columns()
👉 এটি ব্যবহার করে তুমি একাধিক কলাম (দুইটি বা তার বেশি) এক লাইনে পাশাপাশি রাখতে পারো।


col1, col2 = st.columns(2)
             
col1.write("আমি বাম পাশে")
             
col2.write("আমি ডান পাশে")
             
🖼️ আউটপুট: স্ক্রিনে দুটি অংশে বিভক্ত হবে, এক পাশে "আমি বাম পাশে", অন্য পাশে "আমি ডান পাশে"।

""")

col1, col2 = st.columns(2)
col1.write("আমি বাম পাশে")
col2.write("আমি ডান পাশে")

st.write("নিচের কোডগুলো কপি করো")

st.code('''col1, col2 = st.columns(2)
col1.write("আমি বাম পাশে")
col2.write("আমি ডান পাশে")''',language="bash")

st.divider()

st.subheader("""2. Sidebar: st.sidebar
             
👉 এইটা ব্যবহার করে তুমি একটা সাইডবারে (বাম পাশের দিকের লেআউট) কনটেন্ট রাখতে পারো। ফর্ম, ইনপুট, বাটন — সব রাখতে পারো।

🔹 উদাহরণ:

name = st.sidebar.text_input("তোমার নাম লেখো")
             
st.write("তোমার নাম:", name)
             
🖼️ আউটপুট: বাম পাশে ইনপুট বক্স আসবে, যেখানে ইউজার নাম লিখতে পারবে।""")

st.write("নিচের কোডগুলো কপি করো")

st.code('''name = st.sidebar.text_input("তোমার নাম লেখো")
             
st.write("তোমার নাম:", name)''', language="bash")

st.divider()

st.subheader("""3. Expander: st.expander()
👉 এটি ব্যবহার করলে তোমার কনটেন্ট ভেতরে লুকানো থাকবে, ইউজার চাইলে এক্সপ্যান্ড করে দেখতে পারবে।

🔹 উদাহরণ:
with st.expander("বিস্তারিত দেখুন"):
    st.write("এখানে অতিরিক্ত তথ্য আছে।")
🖼️ আউটপুট: একটা বক্স থাকবে "বিস্তারিত দেখুন", ক্লিক করলে ভিতরের লেখা দেখাবে।""")

with st.expander("বিস্তারিত দেখুন"):
    st.write("হ্যালো, আসসালামু আলাইকুম")

st.write("নিচের কোডগুলো কপি করো")

st.code('''with st.expander("বিস্তারিত দেখুন"):
    st.write("হ্যালো, আসসালামু আলাইকুম")''', language="bashe")
st.divider()

st.subheader("""4. Tabs: st.tabs()
             
👉 Tabs দিয়ে তুমি আলাদা আলাদা ট্যাবে আলাদা কনটেন্ট দেখাতে পারো।

🔹 উদাহরণ:

tab1, tab2 = st.tabs(["👨 ছাত্র", "👩 ছাত্রী"])

with tab1:
             
    st.write("এখানে ছাত্রদের তথ্য")

with tab2:
             
    st.write("এখানে ছাত্রীদের তথ্য")
             
🖼️ আউটপুট: উপরে দুটি ট্যাব থাকবে। ক্লিক করলে ট্যাব অনুযায়ী আলাদা লেখা দেখা যাবে।""")

tab1, tab2 = st.tabs(["👨 ছাত্র", "👩 ছাত্রী"])

with tab1:
             
    st.write("এখানে ছাত্রদের তথ্য")

with tab2:
             
    st.write("এখানে ছাত্রীদের তথ্য")
st.divider()

st.write("নিচের কোডগুলো কপি করো")

st.code('''tab1, tab2 = st.tabs(["👨 ছাত্র", "👩 ছাত্রী"])

with tab1:
             
    st.write("এখানে ছাত্রদের তথ্য")

with tab2:
             
    st.write("এখানে ছাত্রীদের তথ্য")''', language="bash")
st.divider()

st.subheader("""5. Page Configuration: st.set_page_config()
             
👉 এটি দিয়ে তুমি তোমার অ্যাপের title, icon, layout, menu ইত্যাদি শুরুতেই সেট করতে পারো।

🔹 উদাহরণ:

st.set_page_config(
             
    page_title="আমার অ্যাপ",
             
    page_icon="🚀",
             
    layout="wide"
)
             
🖼️ আউটপুট: ব্রাউজারে ট্যাবের নাম হবে "আমার অ্যাপ", আইকন হবে 🚀, এবং পুরো স্ক্রিনজুড়ে wide layout হবে।""")
st.divider()

st.code('''st.set_page_config(
             
    page_title="আমার অ্যাপ",
             
    page_icon="🚀",
             
    layout="wide"
)''', language="bash")



