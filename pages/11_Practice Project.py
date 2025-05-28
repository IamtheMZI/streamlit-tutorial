import streamlit as st
import pandas as pd
import requests
import plotly.express as px


st.title("""অধ্যায় ১০: প্র্যাকটিস প্রজেক্ট""")

st.subheader("""ভূমিকা
             
এই অধ্যায়ে আমরা কিছু প্র্যাকটিক্যাল প্রজেক্ট বানাবো যেগুলো প্রফেশনাল Streamlit অ্যাপ্লিকেশন তৈরির পথে তোমার দক্ষতা আরও বাড়াবে। প্রতিটি প্রজেক্টে থাকবে রিয়েল ডেটা, ইউজার ইনপুট, এবং ডেটা ভিজ্যুয়ালাইজেশন। ধাপে ধাপে শেখা হবে যেন তুমি নিজের মতো করে ফিচার অ্যাড করতে পারো।""")

st.subheader("""প্রজেক্ট তালিকা:
             
📊 COVID Dashboard

📦 ইনভেন্টরি ম্যানেজমেন্ট

📁 ফাইল আপলোড সিস্টেম

🎓 অনলাইন কুইজ প্ল্যাটফর্ম""")

st.subheader("""ই পোস্টে তুমি শিখবে —
             
API থেকে কিভাবে ডেটা আনা যায়

JSON ডেটা কীভাবে DataFrame-এ রূপান্তর করো

ডেটা ফিল্টার করো দেশ অনুসারে

চার্ট তৈরি করো Plotly দিয়ে

Streamlit অ্যাপে সুন্দরভাবে দেখাও""")

st.subheader("""ধাপ ১: কী কী লাগবে?
তোমার প্রয়োজন হবে:
             
| নাম                 | উদ্দেশ্য                           |
|---------------------|-------------------------------------|
| **Python**          | মূল প্রোগ্রামিং ভাষা                |
| **Streamlit**       | UI তৈরি করতে                       |
| **Pandas**          | ডেটা প্রসেসিং                      |
| **Matplotlib / Plotly** | চার্ট ও গ্রাফ তৈরি করতে        |
| **SQLite / CSV**    | ডেটা স্টোর করার জন্য               |
| **OS / Pathlib**    | ফাইল হ্যান্ডলিং (ফাইল আপলোড সিস্টেমে) |

""")

st.write("ইনস্টল করতে পারো এইভাবে:")
st.code('''pip install streamlit pandas matplotlib plotly
''', language="bash")

st.subheader("""প্রজেক্ট ১: COVID Dashboard
             
📊 Objective: API থেকে COVID-19 এর রিয়েলটাইম ডেটা নিয়ে Streamlit অ্যাপে প্রেজেন্ট করা।
""")

st.write("চল আমরা Step-by-Step দেখি কীভাবে COVID Dashboard বানানো যায় Streamlit দিয়ে, যেখানে API থেকে COVID ডেটা এনে সেটাকে টেবিল ও গ্রাফ আকারে দেখাবো।")



st.subheader("""এই পোস্টে তুমি শিখবে —
             
API থেকে কিভাবে ডেটা আনা যায়

JSON ডেটা কীভাবে DataFrame-এ রূপান্তর করো

ডেটা ফিল্টার করো দেশ অনুসারে

চার্ট তৈরি করো Plotly দিয়ে

Streamlit অ্যাপে সুন্দরভাবে দেখাও""")

st.subheader("ধাপ ১: কী কী লাগবে")
st.code('''pip install streamlit pandas matplotlib plotly
''', language="bash")


st.subheader("ফোল্ডার স্ট্রাকচার:")
st.code('''Streamlit/
├── covid_dashboard.py
''', language="bash")


st.subheader("ধাপ ২: কোড লিখো (covid_dashboard.py)")
st.write("নিচের কোডগুলো কপি করো")
st.code('''# covid_dashboard.py

import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# ✅ Page config
st.set_page_config(page_title="COVID Dashboard", layout="wide")

# ✅ Title
st.title("🦠 Global COVID-19 Dashboard")
st.markdown("Real-time COVID-19 data powered by disease.sh API.")

# ✅ Step 1: Fetch data from API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data)
    
    # ✅ Step 2: Select specific columns
    df = df[["country", "cases", "todayCases", "deaths", "todayDeaths", "recovered", "active", "population"]]
    
    # ✅ Step 3: Sidebar Filter
    countries = df["country"].sort_values().unique()
    selected_countries = st.sidebar.multiselect("🌍 Select Countries", countries, default=["India", "USA", "Brazil"])
    
    filtered_df = df[df["country"].isin(selected_countries)]

    # ✅ Step 4: Show Table
    st.subheader("📋 COVID-19 Data Table")
    st.dataframe(filtered_df.set_index("country"))

    # ✅ Step 5: Show Graphs
    st.subheader("📊 Total Cases per Country")
    fig = px.bar(filtered_df, x="country", y="cases", color="country", title="Total Cases")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Today's Cases per Country")
    fig2 = px.bar(filtered_df, x="country", y="todayCases", color="country", title="Today's Cases")
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.error("❌ Failed to fetch data from the API.")
''', language="bash")

with st.expander("বিস্তারিত দেখুন:"):
    st.write("উপরের কোডগুলোর ব্যাখ্যা করা হলো:")

    #Library Import
    st.subheader(""" 1. লাইব্রেরি ইমপোর্ট করা
                 
    import streamlit as st          
    import pandas as pd          
    import requests           
    import plotly.express as px
                 
    🔹 streamlit: UI তৈরি করতে ব্যবহৃত হয় (ওয়েব অ্যাপ)।    
    🔹 pandas: ডেটা প্রসেসিং/টেবিল ফরম্যাটে কাজ করার জন্য।      
    🔹 requests: API থেকে রিয়েল-টাইম ডেটা আনতে ব্যবহৃত।      
    🔹 plotly.express: গ্রাফ এবং চার্ট আঁকার জন্য।""")

    #Page configuration
    st.subheader("""2. পেজ কনফিগারেশন

    st.set_page_config(page_title="COVID Dashboard", layout="wide")
                 
    🔸 এই লাইনে Streamlit অ্যাপের পেজের নাম COVID Dashboard দেওয়া হয়েছে।      
    🔸 layout="wide" মানে পুরো স্ক্রিন জুড়ে ওয়াইড লেআউট হবে।""")

    #Title and description
    st.subheader("""3. শিরোনাম ও বিবরণ
    st.title("🦠 Global COVID-19 Dashboard")         
    st.markdown("Real-time COVID-19 data powered by disease.sh API.")
                 
    🔹 অ্যাপে একটি বড় টাইটেল দেখানো হচ্ছে।        
    🔹 markdown() দিয়ে নিচে একটি ছোট বিবরণ দেওয়া হয়েছে।""")


    #Fetching data from API
    st.subheader("""4. API থেকে ডেটা আনা
    url = "https://disease.sh/v3/covid-19/countries"         
    response = requests.get(url)
          
    🔸 এখানে disease.sh API থেকে প্রতিটি দেশের COVID-19 ডেটা আনছে।         
    🔸 response হচ্ছে HTTP রিকোয়েস্টের রেজাল্ট।""")


    #Create a DataFrame by checking the data
    st.subheader("""5. ডেটা চেক করে DataFrame তৈরি
    if response.status_code == 200:      
        data = response.json()      
        df = pd.json_normalize(data)
                 
    🔹 যদি API সফলভাবে কাজ করে (status code 200), তাহলে:      
    🔸 .json() দিয়ে JSON ডেটাকে পাইথন ডিকশনারিতে কনভার্ট করা হচ্ছে।       
    🔸 pd.json_normalize() দিয়ে nested JSON কে DataFrame এ রূপান্তর করছে।""")


    #Country name filter in the sidebar
    st.subheader("""সাইডবারে দেশের নাম ফিল্টার
    countries = df["country"].sort_values().unique()            
    selected_countries = st.sidebar.multiselect("🌍 Select Countries", countries, default=["India", "USA", "Brazil"])
                 
    🔹 ইউজার সাইডবার থেকে দেশ বেছে নিতে পারবে।        
    🔹 ডিফল্টভাবে India, USA, Brazil সিলেক্ট করা থাকবে।""")


    #Data filter based on selected country
    st.subheader("""8. নির্বাচিত দেশের উপর ভিত্তি করে ডেটা ফিল্টার
    filtered_df = df[df["country"].isin(selected_countries)]
                 
    🔸 ইউজার যেসব দেশ সিলেক্ট করবে, শুধু সেই দেশগুলোর ডেটা রাখা হবে।""")


    #Showing data table
    st.subheader("""9. ডেটা টেবিল দেখানো
    st.subheader("📋 COVID-19 Data Table")          
    st.dataframe(filtered_df.set_index("country"))
                 
    🔹 subheader() দিয়ে টেবিলের হেডিং দেওয়া হয়েছে।
    🔹 set_index("country") দিয়ে টেবিলের index হিসেবে দেশের নাম ব্যবহার করা হয়েছে।""")


    #Total Cases Graph
    st.subheader("""10. Total Cases গ্রাফ

    st.subheader("📊 Total Cases per Country")
    fig = px.bar(filtered_df, x="country", y="cases", color="country", title="Total Cases")
    st.plotly_chart(fig, use_container_width=True)
                 
    🔹 Bar Chart ব্যবহার করে দেখানো হচ্ছে কোন দেশে মোট কতটি কেস হয়েছে।
    🔹 plotly_chart() দিয়ে Streamlit-এ গ্রাফ রেন্ডার করা হচ্ছে।
    """)

    #Today's Cases Graph
    st.subheader("""11. Today's Cases গ্রাফ

    st.subheader("📊 Today's Cases per Country")
    fig2 = px.bar(filtered_df, x="country", y="todayCases", color="country", title="Today's Cases")
    st.plotly_chart(fig2, use_container_width=True)
                 
    🔹 আরেকটি Bar Chart – এইবার দেখানো হচ্ছে আজকের নতুন কেসের সংখ্যা প্রতি দেশে।""")

    #API Error Handling
    st.subheader(""" 12. API Error Handling

    else:
        st.error("❌ Failed to fetch data from the API.")
                 
    🔹 যদি API থেকে ডেটা না আসে, তাহলে ব্যবহারকারীকে একটি Error Message দেখানো হবে।""")



st.subheader("উপরের কোডের আউটপুট:")
# covid_dashboard.py


# ✅ Title
st.title("🦠 Global COVID-19 Dashboard")
st.markdown("Real-time COVID-19 data powered by disease.sh API.")

# ✅ Step 1: Fetch data from API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data)
    
    # ✅ Step 2: Select specific columns
    df = df[["country", "cases", "todayCases", "deaths", "todayDeaths", "recovered", "active", "population"]]
    
    # ✅ Step 3: Main page Filter
    countries = df["country"].sort_values().unique()
    selected_countries = st.multiselect("🌍 Select Countries", countries, default=["India", "USA", "Brazil"])
    
    filtered_df = df[df["country"].isin(selected_countries)]

    # ✅ Step 4: Show Table
    st.subheader("📋 COVID-19 Data Table")
    st.dataframe(filtered_df.set_index("country"))

    # ✅ Step 5: Show Graphs
    st.subheader("📊 Total Cases per Country")
    fig = px.bar(filtered_df, x="country", y="cases", color="country", title="Total Cases")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Today's Cases per Country")
    fig2 = px.bar(filtered_df, x="country", y="todayCases", color="country", title="Today's Cases")
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.error("❌ Failed to fetch data from the API.")


#Code Run 
st.subheader(" রান করার নিয়ম")
st.code('''streamlit run covid_dashboard.py
''', language="bash")


#Next step
st.subheader("""পরবর্তী ধাপ কী হতে পারে?
             
Pie Chart বা Line Graph যোগ করো

Historical data নিয়ে টাইমলাইন গ্রাফ বানাও

Dark/Light Mode যুক্ত করো

ইউজারের লোকেশন ধরে অটোদেশ সিলেক্ট করো""")


st.subheader("""প্রজেক্ট ১: ইনভেন্টরি ম্যানেজমেন্ট সিস্টেম
             
🎯 উদ্দেশ্য:
             
এই প্রজেক্টের মাধ্যমে আমরা একটি ছোট ইনভেন্টরি ম্যানেজমেন্ট অ্যাপ তৈরি করব, যেখানে নতুন প্রোডাক্ট যোগ করা যাবে, প্রোডাক্টের তালিকা দেখা যাবে এবং CSV ফাইল থেকে ডেটা লোড করা যাবে।""")


st.subheader("""ধাপ ১: কী কী লাগবে?
তোমার প্রয়োজন হবে:
             
| নাম                 | উদ্দেশ্য                           |
|---------------------|-------------------------------------|
| **Python**          | মূল প্রোগ্রামিং ভাষা                |
| **Streamlit**       | UI তৈরি করতে                       |
| **Pandas**          | ডেটা প্রসেসিং                      |
| **Matplotlib / Plotly** | চার্ট ও গ্রাফ তৈরি করতে        |
| **SQLite / CSV**    | ডেটা স্টোর করার জন্য               |
| **OS / Pathlib**    | ফাইল হ্যান্ডলিং (ফাইল আপলোড সিস্টেমে) |

""")

st.subheader("""ইন্সটল করতে:

pip install streamlit pandas""")

st.subheader("ধাপ ২: প্রজেক্ট ফোল্ডার স্ট্রাকচার")
st.code('''inventory_app/
│
├── app.py
├── data/
│   └── products.csv
├── images/
│   └── product1.png
''', language="basj")

st.write("""app.py → মূল স্ট্রিমলিট অ্যাপ

data/products.csv → প্রোডাক্ট তথ্য

images/ → প্রোডাক্ট ছবি সংরক্ষণের ফোল্ডার""")


st.subheader("ধাপ ৩: প্রাথমিক কোড (Streamlit UI ও CSV লোড)")
st.code('''# app.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Inventory Management", layout="wide")
st.title("📦 ইনভেন্টরি ম্যানেজমেন্ট সিস্টেম")

# ✅ CSV ফাইল থেকে ডেটা লোড করা
DATA_FILE = "data/products.csv"

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Title", "Description", "Image"])

# ✅ টেবিল আকারে প্রোডাক্ট দেখানো
st.subheader("🧾 প্রোডাক্ট তালিকা")
st.dataframe(df)
''', language="bash")




st.subheader("ধাপ ৪: নতুন প্রোডাক্ট যুক্ত করা (ফর্ম ইনপুট সহ)")
st.code('''st.subheader("➕ নতুন প্রোডাক্ট যুক্ত করুন")

with st.form("product_form", clear_on_submit=True):
    title = st.text_input("প্রোডাক্ট নাম")
    description = st.text_area("বর্ণনা")
    image_file = st.file_uploader("ছবি আপলোড করুন", type=["png", "jpg", "jpeg"])
    submit = st.form_submit_button("✅ সংরক্ষণ করুন")

    if submit:
        if title and description and image_file:
            image_path = f"images/{image_file.name}"
            with open(image_path, "wb") as f:
                f.write(image_file.getbuffer())

            new_data = {"Title": title, "Description": description, "Image": image_path}
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("🎉 প্রোডাক্ট সফলভাবে যুক্ত হয়েছে!")
        else:
            st.error("⚠️ সব তথ্য পূরণ করুন।")

''', language="bash")


st.subheader(" ধাপ ৫: প্রতিটি প্রোডাক্ট কার্ড আকারে দেখানো (ছবি সহ)")
st.code('''st.subheader("🖼️ প্রোডাক্ট ভিউ")

for _, row in df.iterrows():
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            if os.path.exists(row["Image"]):
                st.image(row["Image"], width=100)
            else:
                st.warning("📷 ছবি পাওয়া যায়নি")
        with cols[1]:
            st.markdown(f"### {row['Title']}")
            st.write(row["Description"])
        st.markdown("---")
''', language="bash")

st.subheader("""চূড়ান্ত ফলাফল (Output):
             
ইউজার নতুন প্রোডাক্ট যুক্ত করতে পারবে

CSV ফাইলে তথ্য সেভ হবে

সব প্রোডাক্ট একটি কার্ড স্টাইলে ছবিসহ দেখা যাবে""")

st.write("বিঃ দ্রৃঃ তুমি চাইলে তোমার products.csv file এই নিচের csv file টা এড করতে পারো:")
st.code('''Title,Description,Image
Pen,Blue ink pen,images/pen.png
Notebook,100-page notebook,images/notebook.jpg
Camera,High Powerfull Dsler camera,images/old-used-olympus-om-film-camera-olympus-mm-shift-lens-perspective-contr-old-used-brassed-olympus-om-film-camera-201027136.jpg
''')


