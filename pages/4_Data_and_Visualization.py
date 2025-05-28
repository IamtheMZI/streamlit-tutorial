import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt

st.title("📊 অধ্যায় ৪: ডেটা হ্যান্ডলিং ও Visualization")

st.title("""
         এখানে তুমি শিখবে:

st.table(), st.dataframe(), st.json() দিয়ে ডেটা দেখানো

লাইন চার্ট, বার চার্ট, এরিয়া চার্ট

Plotly, Matplotlib, Altair দিয়ে কাস্টম ভিজুয়ালাইজেশন
""")

st.subheader("📋 Table ও DataFrame")

data = {
    "নাম": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
    "স্কোর": [85, 92, 78, 88],
    "গ্রেড": ["A", "A+", "B", "A"]
}
df = pd.DataFrame(data)

st.write("👉 `st.table()` (static table)")
st.table(df)

st.write("👉 `st.dataframe()` (interactive)")
st.dataframe(df)

st.divider()
st.write("নিচে কোডগুলো কপি করে রান কর.")

st.code('''st.subheader("📋 Table ও DataFrame")

data = {
    "নাম": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
    "স্কোর": [85, 92, 78, 88],
    "গ্রেড": ["A", "A+", "B", "A"]
}
df = pd.DataFrame(data)

st.write("👉 `st.table()` (static table)")
st.table(df)

st.write("👉 `st.dataframe()` (interactive)")
st.dataframe(df)''', language='bash')

with st.expander("বিস্তারিত দেখুন"):
    
    st.subheader("এই কোডগুলোর ব্যাখ্যা")
    st.write("""
    তুমি একটি DataFrame (টেবিল) বানাচ্ছো এবং সেটা Streamlit-এর মাধ্যমে দুইভাবে দেখাচ্ছো:

    ✅ `st.table()` → একটি সাধারণ (static) টেবিল

    ✅ `st.dataframe()` → একটি ইন্টার‌্যাকটিভ (interactive) টেবিল
    """)

    st.subheader("প্রতিটি লাইন ব্যাখ্যা:")

    st.write("""
    data = {
        "নাম": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
        "স্কোর": [85, 92, 78, 88],
        "গ্রেড": ["A", "A+", "B", "A"]
    }

    🔹 তুমি একটা dictionary বানিয়েছো যেটাতে ৩টি কলাম আছে:
    - "নাম" → শিক্ষার্থীদের নাম
    - "স্কোর" → তাদের নম্বর
    - "গ্রেড" → তাদের গ্রেড
    """)

    st.write("""
    df = pd.DataFrame(data)

    🔸 তুমি ওই dictionary-কে pandas এর DataFrame এ রূপান্তর করেছো — এটা আসলে একটি টেবিল ফরম্যাটে ডেটা।
    """)

    st.write("""
    st.write("👉 st.table() (static table)")
    st.table(df)

    🔸 এখানে তুমি `st.table(df)` ব্যবহার করে একটি static table দেখিয়েছো।
    Static মানে: শুধু দেখতে পারবে, কিন্তু কিছু করা যাবে না (যেমন স্ক্রল, ফিল্টার, রিসাইজ ইত্যাদি না)।
    """)

    st.write("""
    st.write("👉 st.dataframe() (interactive)")
    st.dataframe(df)

    🔸 এখানে `st.dataframe(df)` ব্যবহার করেছো।
    Interactive মানে:
    - কলামগুলো রিসাইজ করতে পারবে
    - টেবিলটা স্ক্রল করা যাবে
    - স্লাইডিং করে ডেটা দেখা যাবে
    """)


st.divider()






st.subheader("📦 JSON ডেটা")
st.json({
    "name": "Streamlit App",
    "version": "1.0",
    "features": ["simple", "fast", "interactive"]
})

st.divider()

st.write("এই কোডগুলো কপি করে রান কর.")

st.code('''st.subheader("📦 JSON ডেটা")
st.json({
    "name": "Streamlit App",
    "version": "1.0",
    "features": ["simple", "fast", "interactive"]
})

''', language='bash')

st.subheader("""এই কোডগুলো ব্যাখ্যা:
             
st.json({
             
    "name": "Streamlit App",
             
    "version": "1.0",
             
    "features": ["simple", "fast", "interactive"]
})
🔹 এই লাইনে তুমি একটা JSON format এর ডেটা দেখাচ্ছো।""")

st.subheader(""" 
             JSON মানে কী?
JSON (JavaScript Object Notation) হলো ডেটা সংরক্ষণের ও আদান-প্রদানের একটি জনপ্রিয় ফরম্যাট।
             
{
             
    "name": "Streamlit App",           # অ্যাপের নাম
             
    "version": "1.0",                  # ভার্সন নম্বর
             
    "features": ["simple", "fast", "interactive"]  # বৈশিষ্ট্যসমূহ
}
🔸 st.json() ফাংশন এই JSON ডেটাকে সুন্দরভাবে দেখায় —
ব্রাউজারে এটা দেখতে খুব সাজানো ও রঙিন হয়, যাতে বোঝা সহজ হয়।

""")

st.write("আমি তোমাকে একটি live উদাহরণ সহ demo কোড দিচ্ছি, যেটা তুমি নিজের Streamlit অ্যাপে চালিয়ে দেখতে পারো। এতে তুমি দেখবে কীভাবে st.json() কাজ করে এবং JSON ডেটা কেমনভাবে দেখায়।")


st.title("📦 JSON ডেটার লাইভ ডেমো")

# সাবহেডিং
st.subheader("🎓 শিক্ষার্থীর তথ্য")

# JSON ডেটা তৈরি
student_data = {
    "নাম": "রাহুল ইসলাম",
    "শ্রেণি": "১০ম",
    "রোল": 5,
    "বিষয়ভিত্তিক নম্বর": {
        "গণিত": 85,
        "বিজ্ঞান": 90,
        "ইংরেজি": 82
    },
    "পাস": True
}


# JSON দেখানো
st.json(student_data) 

st.divider()





st.subheader("📈 Built-in Chart API")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.write("👉 `st.line_chart()`")
st.line_chart(chart_data)

st.write("👉 `st.bar_chart()`")
st.bar_chart(chart_data)

st.write("👉 `st.area_chart()`")
st.area_chart(chart_data)

st.divider()
st.write("এই কোডগুলো কপি করে রান কর.")

st.code('''st.subheader("📈 Built-in Chart API")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.write("👉 `st.line_chart()`")
st.line_chart(chart_data)

st.write("👉 `st.bar_chart()`")
st.bar_chart(chart_data)

st.write("👉 `st.area_chart()`")
st.area_chart(chart_data)''', language="bash")

st.subheader("এই কোডগুলো ব্যাখ্যা:")

st.subheader("""ডেটা তৈরি:

chart_data = pd.DataFrame(
             
    np.random.randn(20, 3),
             
    columns=["A", "B", "C"]
)
             
 ব্যাখ্যা:

np.random.randn(20, 3) → এটা ২০টি সারি (row) এবং ৩টি কলাম (column) সহ একা-একা random সংখ্যা তৈরি করে।

columns=["A", "B", "C"] → এই ডেটার কলামগুলোর নাম রাখা হয়েছে A, B, ও C।

🎯 তুমি ধরে নিতে পারো এটা ২০ দিনের তথ্য, যেখানে ৩টা আলাদা ফিচার (A, B, C) এর ভ্যালু আছে।""")

st.subheader("""লাইন চার্ট:

st.write("👉 `st.line_chart()`")
             
st.line_chart(chart_data)
             
➡️ এখানে লাইন চার্ট তৈরি হবে।
             
প্রতিটি কলাম (A, B, C) এর জন্য আলাদা লাইন আঁকা হবে।
             
এটি সময় বা সিরিজ ডেটা দেখাতে ভালো কাজ করে।""")

st.subheader("""বার চার্ট:

st.write("👉 `st.bar_chart()`")
             
st.bar_chart(chart_data)
             
➡️ এটা bar chart দেখায়, যেখানে প্রতিটি সারির জন্য কলাম (A, B, C) এর মান বার (দণ্ড) আকারে দেখানো হয়।""")

st.subheader("""এরিয়া চার্ট:

st.write("👉 `st.area_chart()`")
             
st.area_chart(chart_data)
             
➡️ এটি লাইন চার্টের মতো, তবে নিচের অংশটা রঙ দিয়ে ভরাট করা থাকে।
             
এটা তুলনামূলকভাবে ভিজ্যুয়াল ডিফারেন্স আরও ভালোভাবে দেখায়।""")

st.write("চলো আমরা একটা লাইভ ইন্টার‍্যাকটিভ ডেমো বানাই যেখানে ইউজার স্লাইডার ব্যবহার করে নির্ধারণ করতে পারবে কয়টা সারি ডেটা চার্টে দেখাবে")

st.title("লাইভ ডেমো কোড")

st.code('''import streamlit as st
import pandas as pd
import numpy as np

# টাইটেল
st.title("📊 ইন্টার‍্যাকটিভ চার্ট ডেমো")

# সাবহেডিং
st.subheader("🔢 আপনি কয়টা সারি (row) দেখতে চান?")

# স্লাইডার
rows = st.slider("ডেটার পরিমাণ নির্বাচন করুন", min_value=5, max_value=100, value=20, step=5)

# ডেটা তৈরি
chart_data = pd.DataFrame(
    np.random.randn(rows, 3),
    columns=["A", "B", "C"]
)

st.write("🔍 নির্বাচিত সারি সংখ্যা:", rows)

# লাইন চার্ট
st.subheader("📈 লাইন চার্ট")
st.line_chart(chart_data)

# বার চার্ট
st.subheader("📊 বার চার্ট")
st.bar_chart(chart_data)

# এরিয়া চার্ট
st.subheader("📉 এরিয়া চার্ট")
st.area_chart(chart_data)
''', language="bash")

st.write("কোড রান করার পর:")

import streamlit as st
import pandas as pd
import numpy as np

# টাইটেল
st.title("📊 ইন্টার‍্যাকটিভ চার্ট ডেমো")

# সাবহেডিং
st.subheader("🔢 আপনি কয়টা সারি (row) দেখতে চান?")

# স্লাইডার
rows = st.slider("ডেটার পরিমাণ নির্বাচন করুন", min_value=5, max_value=100, value=20, step=5)

# ডেটা তৈরি
chart_data = pd.DataFrame(
    np.random.randn(rows, 3),
    columns=["A", "B", "C"]
)

st.write("🔍 নির্বাচিত সারি সংখ্যা:", rows)

# লাইন চার্ট
st.subheader("📈 লাইন চার্ট")
st.line_chart(chart_data)

# বার চার্ট
st.subheader("📊 বার চার্ট")
st.bar_chart(chart_data)

# এরিয়া চার্ট
st.subheader("📉 এরিয়া চার্ট")
st.area_chart(chart_data)
st.divider()

st.subheader("📊 Custom Chart: Plotly")

plot_data = pd.DataFrame({
    "শিক্ষার্থী": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
    "স্কোর": [85, 92, 78, 88]
})

fig = px.bar(plot_data, x="শিক্ষার্থী", y="স্কোর", title="Plotly Bar Chart")
st.plotly_chart(fig)

st.divider()

st.write("নিচের কোডগুলো কপি করো")

st.code('''st.subheader("📊 Custom Chart: Plotly")

plot_data = pd.DataFrame({
    "শিক্ষার্থী": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
    "স্কোর": [85, 92, 78, 88]
})

fig = px.bar(plot_data, x="শিক্ষার্থী", y="স্কোর", title="Plotly Bar Chart")
st.plotly_chart(fig)''', language="bash")



st.subheader("""এই কোডগুলোর ব্যাখ্যা:

plot_data = pd.DataFrame({
             
    "শিক্ষার্থী": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
             
    "স্কোর": [85, 92, 78, 88]
})
             
🔸 এখানে আমরা একটি DataFrame তৈরি করছি
             
🔸 এতে ২টি কলাম আছে:

শিক্ষার্থী	  স্কোর
             
রাহুল	  85
             
সুমনা	  92
             
জোবায়ের	  78
             
তৃষা	  88


fig = px.bar(plot_data, x="শিক্ষার্থী", y="স্কোর", title="Plotly Bar Chart")
             
🔹 এখানে আমরা plotly.express.bar() ফাংশন দিয়ে একটি Bar Chart বানাচ্ছি।

x="শিক্ষার্থী" → এক্স-অক্সিসে থাকবে নামগুলো (রাহুল, সুমনা...)

y="স্কোর" → ওয়াই-অক্সিসে থাকবে নাম অনুযায়ী তাদের স্কোর
             
title="Plotly Bar Chart" → চার্টের উপরে এই শিরোনাম দেখাবে

st.plotly_chart(fig)
🔸 এই লাইনে আমরা Streamlit দিয়ে চার্টটা ওয়েবপেজে দেখাচ্ছি।
             

✅ আউটপুট কেমন হয়?
             
একটা সুন্দর Bar Chart আসবে যেখানে:

এক্স-অক্সিসে থাকবে ৪ জন শিক্ষার্থীর নাম

ওয়াই-অক্সিসে থাকবে তাদের স্কোর

প্রতিটি শিক্ষার্থীর জন্য একটি বার দেখাবে (যত বেশি স্কোর, তত উঁচু বার)""")
st.divider()

st.subheader("📉 Custom Chart: Matplotlib")

fig2, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 5])
ax.set_title("Matplotlib Line Plot")
st.pyplot(fig2)

st.divider()

st.write("নিচের কোডগুলো কপি করো")

st.code('''st.subheader("📉 Custom Chart: Matplotlib")

fig2, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 5])
ax.set_title("Matplotlib Line Plot")
st.pyplot(fig2)''', language="bash")

st.subheader("""কোডগুলোর ব্যাখ্যা:
             
st.subheader("📉 Custom Chart: Matplotlib")

fig2, ax = plt.subplots()                    # একটি ফিগার ও অ্যাক্সিস (Graph এর খালি ক্যানভাস) তৈরি

ax.plot([1, 2, 3], [10, 20, 5])              # X = 1,2,3 আর Y = 10,20,5 ব্যবহার করে একটি লাইনের চার্ট আঁকা

ax.set_title("Matplotlib Line Plot")        # চার্টের উপরে একটা টাইটেল দেয়া হচ্ছে

st.pyplot(fig2)                              # Streamlit এ চার্টটি দেখানো হচ্ছে
""")
st.divider()





st.subheader("🎨 Custom Chart: Altair")

alt_chart = alt.Chart(plot_data).mark_bar().encode(
    x="শিক্ষার্থী",
    y="স্কোর",
    color="শিক্ষার্থী"
).properties(title="Altair Bar Chart")

st.altair_chart(alt_chart, use_container_width=True)

st.divider()

st.write("নিচের কোডগুলো কপি করো")
st.code('''st.subheader("🎨 Custom Chart: Altair")

alt_chart = alt.Chart(plot_data).mark_bar().encode(
    x="শিক্ষার্থী",
    y="স্কোর",
    color="শিক্ষার্থী"
).properties(title="Altair Bar Chart")

st.altair_chart(alt_chart, use_container_width=True)''', language="bash")

st.subheader(""" এই কোডগুলো ধাপে ধাপে ব্যাখ্যা:
             
🔹 plot_data কী?
             
এটি একটি DataFrame যেটিতে শিক্ষার্থীদের নাম এবং তাদের স্কোর আছে:


plot_data = pd.DataFrame({
             
    "শিক্ষার্থী": ["রাহুল", "সুমনা", "জোবায়ের", "তৃষা"],
             
    "স্কোর": [85, 92, 78, 88]
})
             
🔸 1. alt.Chart(plot_data)
             
👉 Altair লাইব্রেরি দিয়ে একটি চার্ট তৈরি করা হচ্ছে, যার ডেটা হচ্ছে plot_data।

🔸 2. .mark_bar()
             
👉 এই লাইনে বলা হচ্ছে, “আমি একটা বার চার্ট (Bar Chart) বানাতে চাই।”

🔸 3. .encode(...)
             
👉 এই অংশে বলা হচ্ছে, চার্টে কোন তথ্য কোন অক্ষ (axis) ও রঙে দেখাবে:

x="শিক্ষার্থী" → X-অক্ষে থাকবে শিক্ষার্থীদের নাম।

y="স্কোর" → Y-অক্ষে থাকবে তাদের স্কোর।

color="শিক্ষার্থী" → প্রতিটি শিক্ষার্থীর বার-এর রঙ আলাদা হবে।

🔸 4. .properties(title="Altair Bar Chart")
             
👉 চার্টের উপরে Altair Bar Chart টাইটেল দেখাবে।

🔸 5. st.altair_chart(...)
             
👉 এই লাইন দিয়ে Streamlit-এ চার্টটি দেখানো হচ্ছে।

use_container_width=True মানে চার্টটি পুরো প্রস্থ জুড়ে (responsive) দেখাবে।

""")
st.divider()




st.subheader("""
✅ রান করার পর তুমি যা দেখতে পাবে:
🔸 JSON, DataFrame, Table সহ ডেটা
🔸 Random চার্ট
🔸 Plotly, Matplotlib, Altair — ৩ ধরনের কাস্টম চার্ট         
""")

st.subheader("""
         
✍️ কী করে এখন:
এই কোড কপি করে pages/4_Data_and_Visualization.py ফাইলে রাখো

streamlit run app.py চালাও

সাইডবার থেকে অধ্যায় ৪: ডেটা হ্যান্ডলিং ও Visualization সিলেক্ট করো

নিজেই চার্ট চেক করো, টেস্ট করো, পরিবর্তন করো
""")






