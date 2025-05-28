import streamlit as st
import mysql.connector

st.subheader("অধ্যায় ৭: ডেটাবেস ও ব্যাকএন্ড সংযোগ — বিস্তারিত গাইড (SQLite & MySQL, ফর্ম থেকে ডেটা সেভ, রিয়েল টাইম ডেটা দেখানো)")

st.subheader("""ভূমিকা
ডেটাবেস হলো তোমার অ্যাপের ‘মেমরি’ যেখানে ইউজারের ইনপুট, তথ্য, ডেটা সব সংরক্ষণ করা হয়।
Python প্রজেক্টে SQLite বা MySQL ব্যবহার করে ডেটাবেস সংযোগ ও CRUD (Create, Read, Update, Delete) অপারেশন করা হয়।

এই পোস্টে তুমি শিখবে —

SQLite ও MySQL সংযোগ কীভাবে করে

Streamlit বা Python ফর্ম থেকে কিভাবে ডেটা ডেটাবেসে সেভ করে

ডেটাবেস থেকে ডেটা রিয়েল টাইমে কিভাবে দেখানো যায়

কোথায় কোন কোড রাখবে, প্রজেক্ট স্ট্রাকচার কেমন হবে

""")

st.subheader("""প্রয়োজনীয়তা
             
Python (৩.৭+ ভার্সন)

Streamlit (যদি Streamlit ব্যবহার করো)

SQLite3 (Python এর বিল্ট-ইন)

MySQL Server (যদি MySQL ব্যবহার করো)

MySQL Connector/Python লাইব্রেরি (MySQL এর জন্য)

সাধারণ Python/IDE (VS Code, PyCharm, Jupyter ইত্যাদি)""")



st.code('''প্রজেক্ট স্ট্রাকচার

my_project/
│
├── app.py                 # মেইন Streamlit অ্যাপ যেখানে UI এবং ডেটাবেস সংযোগ থাকবে
├── database.py            # (Optional) ডেটাবেস কানেকশন এবং ফাংশনগুলো আলাদা ফাইলে রাখতে পারো
├── student.db             # SQLite ডেটাবেস ফাইল (SQLite এর জন্য)
└── requirements.txt       # প্রয়োজনীয় প্যাকেজগুলো লিখে রাখবে''', language="bash")

st.subheader("""১. SQLite সংযোগ ও CRUD অপারেশন
             
১.১ ডেটাবেস সংযোগ ও টেবিল তৈরি""")

st.text('নিচের কোডগুলো কপি করো')

st.code('''import sqlite3

# ডেটাবেস সংযোগ (অথবা তৈরি)
conn = sqlite3.connect('students.db', check_same_thread=False)
cursor = conn.cursor()

# টেবিল তৈরি (যদি না থাকে আগে থেকে)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()

''', language="bash")
st.write("বিঃদ্রঃ check_same_thread=False Streamlit এর জন্য দরকার (মাল্টিপল থ্রেড হ্যান্ডেল করার জন্য)।")

with st.expander("বিস্তারিত দেখুন"):
    
    st.subheader("উপরের কোডগুলোর ব্যাখ্যা")
    
    st.subheader(""" ১. import sqlite3

    import sqlite3
                 
    👉 এই লাইন দিয়ে Python এর মধ্যে sqlite3 লাইব্রেরি ইমপোর্ট করা হয়।
    sqlite3 হল একটি বিল্ট-ইন লাইব্রেরি, যা দিয়ে Python প্রোগ্রাম থেকে সরাসরি SQLite ডেটাবেসের সাথে কাজ করা যায়।

    ✅ অতিরিক্ত কিছু ইনস্টল করতে হয় না, কারণ এটি Python এর সাথে আগে থেকেই থাকে।""")

    st.subheader("""🔹 ২. ডেটাবেস সংযোগ তৈরি

    conn = sqlite3.connect('students.db', check_same_thread=False)
                 
    ব্যাখ্যা:
                 
    sqlite3.connect('students.db'): এটি students.db নামে একটি SQLite ফাইল তৈরি করে (যদি আগে থেকে না থাকে) এবং তার সাথে সংযোগ স্থাপন করে।

    এই ডেটাবেস ফাইলটি তোমার প্রজেক্ট ফোল্ডারে সংরক্ষিত থাকবে।

    check_same_thread=False: এটি Streamlit-এর জন্য দরকার হয়, কারণ Streamlit বিভিন্ন থ্রেড (thread) এ কাজ করতে পারে। এটি না দিলে কখনো কখনো ত্রুটি (error) দেখা দিতে পারে।

    📁 সংক্ষেপে: conn হচ্ছে তোমার ডেটাবেস সংযোগ, যেটা পরবর্তী সময়ে ডেটা ইনসার্ট, রিড, আপডেট, ডিলিট করার কাজে ব্যবহার হবে।""")

    st.subheader("""🔹 ৩. Cursor তৈরি

    cursor = conn.cursor()
                 
    ব্যাখ্যা:
                 
    cursor হলো একটি মিডিয়েটর/মিডলম্যান, যেটা দিয়ে তুমি ডেটাবেসে SQL কমান্ড চালাতে পারো।

    তুমি cursor.execute() দিয়ে SQL কমান্ড চালাবে যেমন: INSERT, SELECT, UPDATE, DELETE, ইত্যাদি।
    """)

    st.subheader("""🔹 ৪. টেবিল তৈরি (যদি না থাকে)

    cursor.execute(
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
    )
    ব্যাখ্যা:
  | কলাম   | টাইপ                           | ব্যাখ্যা                                                           |
|--------|--------------------------------|--------------------------------------------------------------------|
| id     | INTEGER PRIMARY KEY AUTOINCREMENT | এটি স্বয়ংক্রিয়ভাবে প্রতিটি ছাত্রের জন্য ইউনিক আইডি তৈরি করে (1, 2, 3...) |
| name   | TEXT                           | ছাত্রের নাম                                                        |
| age    | INTEGER                        | ছাত্রের বয়স                                                       |
| grade  | TEXT                           | ছাত্রের গ্রেড যেমন A+, B ইত্যাদি                                 |


    ✅ IF NOT EXISTS মানে টেবিলটা আগে থেকে না থাকলে তৈরি করবে — একই টেবিল বারবার তৈরি করার চেষ্টা করলে যেন error না দেয়।""")

    st.subheader("""🔹 ৫. conn.commit()

    conn.commit()
    👉 এই লাইনটি হলো সবশেষে করা কাজগুলোকে ডেটাবেসে স্থায়ীভাবে সেভ করার কমান্ড।
    যদি তুমি commit() না লেখো, তাহলে SQL কমান্ডগুলো কেবল মেমোরিতে থাকবে — ডেটাবেস ফাইলে সেভ হবে না।""")

    st.subheader("""✅ সংক্ষেপে পুরো কাজের ধাপগুলো:
                 
        | ধাপ              | কাজ                                           |
    |------------------|-----------------------------------------------|
    | import sqlite3 | লাইব্রেরি ইমপোর্ট                             |
    | connect()      | ডেটাবেস সংযোগ বা তৈরি                         |
    | cursor()       | SQL চালানোর মাধ্যম তৈরি                      |
    | CREATE TABLE   | টেবিল তৈরি                                     |
    | commit()       | টেবিল তৈরি বা ডেটা পরিবর্তন সেভ করা           |
    """)


import sqlite3

# ডেটাবেস সংযোগ (অথবা তৈরি)
conn = sqlite3.connect('students.db', check_same_thread=False)
cursor = conn.cursor()

# টেবিল তৈরি (যদি না থাকে আগে থেকে)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()





st.subheader("১.২ ফর্ম থেকে ডেটা সেভ করা (Insert)")

st.text('নিচের কোডগুলো কপি করো')

st.code('''import streamlit as st

st.title("🎓 ছাত্র ব্যবস্থাপনা অ্যাপ")

with st.form("insert_form"):
    st.subheader("➕ নতুন ছাত্র যোগ করুন")
    name = st.text_input("নাম")
    age = st.number_input("বয়স", min_value=1, max_value=100)
    grade = st.text_input("গ্রেড (A+/B/C...)")
    insert_btn = st.form_submit_button("✅ যুক্ত করুন")

    if insert_btn:
        if name and grade:
            cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
            conn.commit()
            st.success(f"🎉 {name} কে সফলভাবে যুক্ত করা হয়েছে!")
        else:
            st.error("❌ নাম ও গ্রেড অবশ্যই পূরণ করুন!")

''', language="bash")

with st.expander("বিস্তারিত দেখুন"):
    st.subheader("উপরের কোডগুলো ব্যাখ্যা")

    st.write("""🔹 ১. with st.form("insert_form"):
             
        👉 এটি একটি ফর্ম তৈরি করে যার আইডি "insert_form"।
        👉 এই ফর্মের মধ্যে থাকা ইনপুট ফিল্ড ও বাটন একসাথে সাবমিট হয়।

    🔹 ২. st.subheader("➕ নতুন ছাত্র যোগ করুন")
        👉 ফর্মের উপরে একটি সাবহেডার দেখায়: "➕ নতুন ছাত্র যোগ করুন"।

    🔹 ৩. name = st.text_input("নাম")
        👉 ছাত্রের নাম ইনপুট নেওয়ার জন্য একটি টেক্সট ইনপুট ফিল্ড দেখায়।

    🔹 ৪. age = st.number_input("বয়স", min_value=1, max_value=100)
        👉 বয়স ইনপুট নেওয়ার জন্য একটি নাম্বার ইনপুট ফিল্ড দেখায়।
        👉 বয়সের মান অবশ্যই ১ থেকে ১০০ এর মধ্যে হতে হবে।

    🔹 ৫. grade = st.text_input("গ্রেড (A+/B/C...)")
        👉 ছাত্রের গ্রেড ইনপুট নেওয়ার জন্য আরেকটি টেক্সট ইনপুট ফিল্ড।

    🔹 ৬. insert_btn = st.form_submit_button("✅ যুক্ত করুন")
        👉 ফর্ম সাবমিট করার জন্য একটি সাবমিট বাটন দেখায়।
        👉 ক্লিক করলে ফর্মের ডেটা প্রক্রিয়া হয়।

    🔹 ৭. if insert_btn:
        👉 চেক করে সাবমিট বাটন ক্লিক করা হয়েছে কিনা।

    🔹 ৮. if name and grade:
        👉 নিশ্চিত করে যে নাম ও গ্রেড ফাঁকা নয়।
        👉 বয়স বাধ্যতামূলক না, কারণ তা number_input থেকেই মিনিমাম ১ হয়।

    🔹 ৯. cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        👉 ডেটাবেসে ছাত্রের তথ্য insert (যোগ) করে।
        👉 ? ব্যবহার করা হয় SQL injection থেকে নিরাপদ থাকার জন্য।

    🔹 ১০. conn.commit()
        👉 ডেটা স্থায়ীভাবে সংরক্ষণ (save) করে ডেটাবেসে।

    🔹 ১১. st.success(f"🎉 {name} কে সফলভাবে যুক্ত করা হয়েছে!")
        👉 সফল হলে স্ক্রিনে সবুজ ✅ বার্তা দেখায়।

    🔹 ১২. else: st.error("❌ নাম ও গ্রেড অবশ্যই পূরণ করুন!")
        👉 যদি নাম বা গ্রেড ফাঁকা থাকে, তাহলে ত্রুটি বার্তা দেখায়।""")
  


st.title("🎓 ছাত্র ব্যবস্থাপনা অ্যাপ")

with st.form("insert_form"):
    st.subheader("➕ নতুন ছাত্র যোগ করুন")
    name = st.text_input("নাম")
    age = st.number_input("বয়স", min_value=1, max_value=100)
    grade = st.text_input("গ্রেড (A+/B/C...)")
    insert_btn = st.form_submit_button("✅ যুক্ত করুন")

    if insert_btn:
        if name and grade:
            cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
            conn.commit()
            st.success(f"🎉 {name} কে সফলভাবে যুক্ত করা হয়েছে!")
        else:
            st.error("❌ নাম ও গ্রেড অবশ্যই পূরণ করুন!")



#ডেটা পড়া (Read)
st.subheader("১.৩ ডেটা পড়া (Read)")

st.text('নিচের কোডগুলো কপি করো')

st.code('''st.subheader("📋 ছাত্র তালিকা")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

if rows:
    for row in rows:
        st.markdown(f"🧑‍🎓 **{row[0]} | {row[1]} | বয়স: {row[2]} | গ্রেড: {row[3]}**")
else:
    st.info("🙁 কোনো ছাত্র পাওয়া যায়নি।")

''', language="bash")

with st.expander("বিস্তারিত দেখুন"):
    st.subheader("উপরের কোডগুলো ব্যাখ্যা")

    st.write("""
    🔹 ১. cursor.execute("SELECT * FROM students") 
              
        👉 SQLite ডেটাবেস থেকে students টেবিলের সমস্ত রেকর্ড (সারি) নির্বাচন করার জন্য SQL কমান্ড চালানো হয়।
        👉 SELECT * মানে সব কলামসহ সব ডেটা আনা হবে।

    🔹 ২. rows = cursor.fetchall()  
               
        👉 উপরের SQL কমান্ডের ফলাফল সব সারি নিয়ে আসে এবং rows ভেরিয়েবলে একটি তালিকা হিসেবে সংরক্ষণ করে।
        👉 প্রতিটি row একটি টাপল, যেখানে প্রথম মান id, দ্বিতীয় name, তৃতীয় age এবং চতুর্থ grade।

    🔹 ৩. if rows: 
             
        👉 চেক করে যে ডেটাবেস থেকে কোনো রেকর্ড পাওয়া গেছে কিনা।
        👉 যদি rows খালি না হয়, তাহলে সত্য (True) হবে।

    🔹 ৪. for row in rows:  
             
        👉 পাওয়া সমস্ত রেকর্ডের মধ্যে লুপ চালিয়ে এক এক করে প্রতিটি ছাত্রের তথ্য নিয়ে আসে।

    🔹 ৫. st.markdown(f"🧑‍🎓 **{row[0]} | {row[1]} | বয়স: {row[2]} | গ্রেড: {row[3]}**")
             
        👉 প্রতিটি ছাত্রের তথ্য Markdown ফরম্যাটে স্ট্রিমলিট অ্যাপে প্রদর্শন করে।
        👉 {row[0]} → ছাত্রের id
        👉 {row[1]} → ছাত্রের name
        👉 {row[2]} → ছাত্রের age
        👉 {row[3]} → ছাত্রের grade
        👉 উদাহরণ: 🧑‍🎓 1 | রাকিব | বয়স: 15 | গ্রেড: A+

    🔹 ৬. else:
             
        👉 যদি rows খালি হয়, অর্থাৎ কোনো ছাত্রের তথ্য না পাওয়া যায়, তাহলে নিচের বার্তা দেখাবে।

    🔹৭. st.info("🙁 কোনো ছাত্র পাওয়া যায়নি।")
             
        👉 তথ্য জানাতে একটি নীল রঙের তথ্যবার্তা দেখায়, যেখানে লেখা থাকবে "🙁 কোনো ছাত্র পাওয়া যায়নি।"
        👉 ব্যবহারকারীকে জানায় যে ডাটাবেসে কোনো ছাত্রের তথ্য নেই।

""")

st.subheader("📋 ছাত্র তালিকা")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

if rows:
    for row in rows:
        st.markdown(f"🧑‍🎓 **{row[0]} | {row[1]} | বয়স: {row[2]} | গ্রেড: {row[3]}**")
else:
    st.info("🙁 কোনো ছাত্র পাওয়া যায়নি।")




st.subheader("১.৪ ডেটা আপডেট (Update) ও ডিলিট (Delete)")
st.text('নিচের কোডগুলো কপি করো')

st.code(''' # Session state দিয়ে আপডেট ID ধরে রাখো
if "update_id" not in st.session_state:
    st.session_state.update_id = None

for row in rows:
    st.markdown(f"🧑‍🎓 **{row[0]} | {row[1]} | বয়স: {row[2]} | গ্রেড: {row[3]}**")
    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"✏️ আপডেট করুন (ID: {row[0]})", key=f"update_btn_{row[0]}"):
            st.session_state.update_id = row[0]  # কোন ID আপডেট হবে, সেটি রাখো

    with col2:
        if st.button(f"🗑️ ডিলিট করুন (ID: {row[0]})", key=f"delete_btn_{row[0]}"):
            cursor.execute("DELETE FROM students WHERE id = ?", (row[0],))
            conn.commit()
            st.warning(f"⚠️ ID {row[0]} ডিলিট হয়েছে!")
            st.rerun()

    # যদি এই ID আপডেট মোডে থাকে, তাহলে text input দেখাও
    if st.session_state.update_id == row[0]:
        new_grade = st.text_input(f"🔁 নতুন গ্রেড (ID: {row[0]})", key=f"new_grade_{row[0]}")
        if st.button(f"💾 গ্রেড সেভ করুন (ID: {row[0]})", key=f"save_grade_{row[0]}"):
            if new_grade:
                cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, row[0]))
                conn.commit()
                st.success(f"✅ ID {row[0]} এর গ্রেড আপডেট হয়েছে!")
                st.session_state.update_id = None  # আপডেট মোড বন্ধ করো
                st.rerun()

''', language="bash")

with st.expander("বিস্তারিত দেখুন"):
    st.subheader("উপরের কোডগুলো ব্যাখ্যা")
    st.write("""✅ session_state দিয়ে আপডেট ID ধরে রাখা
                 
    🔹 ১. if "update_id" not in st.session_state:
                 
        👉 চেক করে update_id নামে কোনো কী session-এ আছে কিনা।
        👉 না থাকলে নতুন করে তৈরি করে নিচের লাইনে।

    🔹 ২. st.session_state.update_id = None
                 
        👉 আপডেট করার জন্য যে student-এর ID ধরতে হবে তা শুরুতে None করে দেওয়া হয়।

    ✅ প্রতিটি ছাত্রের তথ্য দেখানো এবং আপডেট/ডিলিট অপশন যুক্ত করা
    🔹 ৩. for row in rows:
                 
        👉 প্রতিটি ছাত্রের জন্য লুপ চালানো হচ্ছে।

    🔹 ৪. st.markdown(...)
                 
        👉 ছাত্রের ID, নাম, বয়স, এবং গ্রেড দেখায়।
        👉 উদাহরণ: 🧑‍🎓 1 | রাহুল | বয়স: 17 | গ্রেড: A+

    🔹 ৫. col1, col2 = st.columns(2)
                 
        👉 দুইটি কলাম তৈরি করা হয়—একটিতে আপডেট বাটন, অন্যটিতে ডিলিট বাটন থাকবে।

    ✅ আপডেট বাটনের কার্যক্রম
                 
    🔹 ৬. if st.button(..., key=f"update_btn_{row[0]}"):
                 
        👉 যদি আপডেট বাটনে ক্লিক করা হয়, তাহলে সেই ছাত্রের ID session_state.update_id এ রাখা হয়।

    ✅ ডিলিট বাটনের কার্যক্রম
                 
    🔹 ৭. if st.button(..., key=f"delete_btn_{row[0]}"):
             
            👉 যদি ডিলিট বাটনে ক্লিক হয়:
            ✅ সেই ছাত্রের ID অনুযায়ী DELETE FROM students চালানো হয়।
            ✅ conn.commit() দিয়ে চিরতরে মুছে ফেলা হয়।
            ✅ ব্যবহারকারীকে দেখানো হয় যে এই ID ডিলিট হয়েছে।
            ✅ st.rerun() দিয়ে অ্যাপটি আবার চালানো হয় যাতে পরিবর্তন সঙ্গে সঙ্গে দেখা যায়।

    ✅ আপডেট মোডে ইনপুট ফিল্ড দেখানো
                 
    🔹 ৮. if st.session_state.update_id == row[0]:
        👉 যদি এই ছাত্রটির ID বর্তমানে আপডেট মোডে থাকে, তখন ইনপুট বক্স দেখানো হয়।

    🔹 ৯. new_grade = st.text_input(...)
                 
        👉 ছাত্রের জন্য নতুন গ্রেড ইনপুট নেওয়ার বক্স।

    🔹 ১০. if st.button(...):
                 
        👉 "গ্রেড সেভ করুন" বাটনে ক্লিক করলে:
        ✅ UPDATE students SET grade = ? WHERE id = ? SQL চালানো হয়।
        ✅ নতুন গ্রেড সংরক্ষণ হয়।
        ✅ সফল বার্তা দেখানো হয়।
        ✅ update_id আবার None করে দেওয়া হয় (অর্থাৎ আপডেট মোড থেকে বের হওয়া)।
        ✅ st.rerun() দিয়ে পেজ রিফ্রেশ হয় যাতে আপডেট দেখা যায়।
    """)
    
    

# Session state দিয়ে আপডেট ID ধরে রাখো
if "update_id" not in st.session_state:
    st.session_state.update_id = None

for row in rows:
    st.markdown(f"🧑‍🎓 **{row[0]} | {row[1]} | বয়স: {row[2]} | গ্রেড: {row[3]}**")
    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"✏️ আপডেট করুন (ID: {row[0]})", key=f"update_btn_{row[0]}"):
            st.session_state.update_id = row[0]  # কোন ID আপডেট হবে, সেটি রাখো

    with col2:
        if st.button(f"🗑️ ডিলিট করুন (ID: {row[0]})", key=f"delete_btn_{row[0]}"):
            cursor.execute("DELETE FROM students WHERE id = ?", (row[0],))
            conn.commit()
            st.warning(f"⚠️ ID {row[0]} ডিলিট হয়েছে!")
            st.rerun()

    # যদি এই ID আপডেট মোডে থাকে, তাহলে text input দেখাও
    if st.session_state.update_id == row[0]:
        new_grade = st.text_input(f"🔁 নতুন গ্রেড (ID: {row[0]})", key=f"new_grade_{row[0]}")
        if st.button(f"💾 গ্রেড সেভ করুন (ID: {row[0]})", key=f"save_grade_{row[0]}"):
            if new_grade:
                cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, row[0]))
                conn.commit()
                st.success(f"✅ ID {row[0]} এর গ্রেড আপডেট হয়েছে!")
                st.session_state.update_id = None  # আপডেট মোড বন্ধ করো
                st.rerun()

st.subheader("""আজ আমরা শিখবো কিভাবে Python দিয়ে MySQL ডেটাবেসে সংযোগ করতে হয়, ডেটা যোগ, পড়া, আপডেট এবং ডিলিট (CRUD অপারেশন) করতে হয়। 
             একদম শুরু থেকে, ইনস্টলেশন থেকে কোড উদাহরণ পর্যন্ত বিস্তারিতভাবে!""")

st.subheader("""ধাপ ১: কী কী লাগবে?
তোমার প্রয়োজন হবে:
             
| জিনিস                         | উদ্দেশ্য                                             |
|------------------------------|------------------------------------------------------|
| Python                       | প্রোগ্রামিং ভাষা                                     |
| MySQL Server                 | ডেটাবেস চালানোর জন্য                                |
| `mysql-connector-python` লাইব্রেরি | Python আর MySQL-এর মধ্যে সংযোগ স্থাপনের জন্য        |
""")

st.subheader("""✅ ধাপ ২: ইনস্টলেশন
             
🔸 MySQL Server ইনস্টল করো (যেমনঃ XAMPP)
             
XAMPP ডাউনলোড করো

XAMPP ইনস্টল করে চালাও

XAMPP Control Panel থেকে MySQL চালু করো

phpMyAdmin খুলো: http://localhost/phpmyadmin""")

st.subheader("🔸 Python লাইব্রেরি ইনস্টল করো")

st.code("""
টার্মিনালে নিচের কমান্ড চালাও:


pip install mysql-connector-python
""", language="bash")


st.write("এটি mysql.connector নামে একটি লাইব্রেরি ইনস্টল করবে যা দিয়ে Python MySQL-এ সংযোগ করতে পারে।")


st.subheader("""ধাপ ৩: ডেটাবেস তৈরি (phpMyAdmin)
             
phpMyAdmin এ যাও (http://localhost/phpmyadmin)

বাম পাশে "New" এ ক্লিক করো

ডেটাবেসের নাম দাও: students_db

এরপর নিচের SQL কমান্ডটি চালাও:""")


st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
);
""", language="bash")
st.markdown('<p style="font-size:12px;">এটি একটি students নামে টেবিল তৈরি করবে যেখানে id, name, age, ও grade থাকবে।</p>', unsafe_allow_html=True)



st.subheader("""ধাপ ৪: ডেটাবেস সংযোগ ফাংশন
             
🔹 connect_mysql.py নামে একটি ফাইল তৈরি করো:""")


st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="students_db"
    )
    return conn

""", language="bash")


st.subheader("ধাপ ৫: নতুন ছাত্র যোগ করার ফাংশন (Insert)")

st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""def add_student(name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    cursor.close()
    conn.close()
""", language="bash")


st.subheader("ধাপ ৬: সব ছাত্র দেখানোর ফাংশন (Select)")

st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

""", language="bash")


st.subheader("ধাপ ৭: ছাত্রের গ্রেড আপডেট করার ফাংশন (Update)")

st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""def update_student_grade(student_id, new_grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE students SET grade = %s WHERE id = %s"
    cursor.execute(query, (new_grade, student_id))
    conn.commit()
    cursor.close()
    conn.close()

""", language="bash")



st.subheader("ধাপ ৮: ছাত্র মুছে ফেলার ফাংশন (Delete)")

st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    cursor.close()
    conn.close()


""", language="bash")


st.subheader("পুরো কোড (সংক্ষেপে)")

st.markdown('<p style="font-size:12px;">নিচের কোডগুলো কপি করো</p>', unsafe_allow_html=True)
st.code("""import streamlit as st
import mysql.connector

# ✅ ডেটাবেস সংযোগ
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="students_db"
)
cursor = conn.cursor()

st.title("📚 ছাত্র ব্যবস্থাপনা সিস্টেম")

menu = st.selectbox("📌 অপশন বেছে নাও", ["নতুন ছাত্র যোগ করো", "সব ছাত্র দেখাও", "ছাত্রের গ্রেড আপডেট করো", "ছাত্র মুছে ফেলো"])

# ✅ ১. নতুন ছাত্র যোগ করো
if menu == "নতুন ছাত্র যোগ করো":
    st.subheader("➕ নতুন ছাত্র যোগ করো")
    with st.form("add_form"):
        name = st.text_input("👤 নাম")
        age = st.number_input("📅 বয়স", min_value=1, step=1)
        grade = st.selectbox("🎓 গ্রেড", ["A", "B", "C", "D", "F"])
        submit = st.form_submit_button("✅ যোগ করো")
    if submit:
        if name:
            cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
            conn.commit()
            st.success("✅ ছাত্র সফলভাবে যোগ হয়েছে!")
        else:
            st.error("❗ নাম লিখতে হবে।")

# ✅ ২. সব ছাত্র দেখাও
elif menu == "সব ছাত্র দেখাও":
    st.subheader("📄 ছাত্র তালিকা")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        st.table(rows)
    else:
        st.info("⚠️ কোনো ছাত্র পাওয়া যায়নি।")

# ✅ ৩. ছাত্রের গ্রেড আপডেট করো
elif menu == "ছাত্রের গ্রেড আপডেট করো":
    st.subheader("🔁 ছাত্রের গ্রেড আপডেট করো")
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    student_dict = {f"{name} (ID: {sid})": sid for sid, name in students}
    selected_student = st.selectbox("👤 ছাত্র নির্বাচন করো", list(student_dict.keys()))
    new_grade = st.selectbox("🆕 নতুন গ্রেড", ["A", "B", "C", "D", "F"])
    if st.button("✅ আপডেট করো"):
        sid = student_dict[selected_student]
        cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, sid))
        conn.commit()
        st.success("🎉 গ্রেড আপডেট হয়েছে!")

# ✅ ৪. ছাত্র মুছে ফেলো
elif menu == "ছাত্র মুছে ফেলো":
    st.subheader("🗑️ ছাত্র ডিলিট করো")
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    student_dict = {f"{name} (ID: {sid})": sid for sid, name in students}
    selected_student = st.selectbox("❌ যেই ছাত্র মুছতে চাও", list(student_dict.keys()))
    if st.button("⚠️ ছাত্র মুছে ফেলো"):
        sid = student_dict[selected_student]
        cursor.execute("DELETE FROM students WHERE id = %s", (sid,))
        conn.commit()
        st.warning("🗑️ ছাত্র ডিলিট হয়েছে!")

# ✅ সংযোগ বন্ধ
cursor.close()
conn.close()


""", language="bash")


st.subheader("এখানে Error দেখাচ্ছে কারণ, আমার xampp file active করা নাই এখন, তবে দূচিন্তার কারণ নাাই তুমি কোডগুলো কপি করে রান করো এবং তোমার xampp file active করো.")





# ✅ ডেটাবেস সংযোগ
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="students_db"
)
cursor = conn.cursor()

st.title("📚 ছাত্র ব্যবস্থাপনা সিস্টেম")

menu = st.selectbox("📌 অপশন বেছে নাও", ["নতুন ছাত্র যোগ করো", "সব ছাত্র দেখাও", "ছাত্রের গ্রেড আপডেট করো", "ছাত্র মুছে ফেলো"])

# ✅ ১. নতুন ছাত্র যোগ করো
if menu == "নতুন ছাত্র যোগ করো":
    st.subheader("➕ নতুন ছাত্র যোগ করো")
    with st.form("add_form"):
        name = st.text_input("👤 নাম")
        age = st.number_input("📅 বয়স", min_value=1, step=1)
        grade = st.selectbox("🎓 গ্রেড", ["A", "B", "C", "D", "F"])
        submit = st.form_submit_button("✅ যোগ করো")
    if submit:
        if name:
            cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
            conn.commit()
            st.success("✅ ছাত্র সফলভাবে যোগ হয়েছে!")
        else:
            st.error("❗ নাম লিখতে হবে।")

# ✅ ২. সব ছাত্র দেখাও
elif menu == "সব ছাত্র দেখাও":
    st.subheader("📄 ছাত্র তালিকা")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        st.table(rows)
    else:
        st.info("⚠️ কোনো ছাত্র পাওয়া যায়নি।")

# ✅ ৩. ছাত্রের গ্রেড আপডেট করো
elif menu == "ছাত্রের গ্রেড আপডেট করো":
    st.subheader("🔁 ছাত্রের গ্রেড আপডেট করো")
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    student_dict = {f"{name} (ID: {sid})": sid for sid, name in students}
    selected_student = st.selectbox("👤 ছাত্র নির্বাচন করো", list(student_dict.keys()))
    new_grade = st.selectbox("🆕 নতুন গ্রেড", ["A", "B", "C", "D", "F"])
    if st.button("✅ আপডেট করো"):
        sid = student_dict[selected_student]
        cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, sid))
        conn.commit()
        st.success("🎉 গ্রেড আপডেট হয়েছে!")

# ✅ ৪. ছাত্র মুছে ফেলো
elif menu == "ছাত্র মুছে ফেলো":
    st.subheader("🗑️ ছাত্র ডিলিট করো")
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    student_dict = {f"{name} (ID: {sid})": sid for sid, name in students}
    selected_student = st.selectbox("❌ যেই ছাত্র মুছতে চাও", list(student_dict.keys()))
    if st.button("⚠️ ছাত্র মুছে ফেলো"):
        sid = student_dict[selected_student]
        cursor.execute("DELETE FROM students WHERE id = %s", (sid,))
        conn.commit()
        st.warning("🗑️ ছাত্র ডিলিট হয়েছে!")

# ✅ সংযোগ বন্ধ
cursor.close()
conn.close()


