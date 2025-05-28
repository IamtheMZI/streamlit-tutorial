import streamlit as st
st.subheader(""" অধ্যায় ৬: ফর্ম ও ইউজার ইনপুট–এর সম্পূর্ণ ব্যাখ্যা দিয়েছি, যেখানে থাকছে:

st.form() ও form_submit_button() কীভাবে কাজ করে

ইউজার ইনপুট Validate করার কৌশল

Success/Error মেসেজ দেখানোর পদ্ধতি""")

st.subheader(""" উদ্দেশ্য:
             
Streamlit-এ ইউজার ইনপুট নেওয়া, যাচাই (validation) করা এবং ফলাফল দেখানো।

""")

st.subheader("Step 1: ফর্ম তৈরি করা") 

st.write("নিচের কোডগুলো কপি করো")

st.code('''import streamlit as st

st.title("📋 ইউজার ইনপুট ফর্ম")

# ফর্ম শুরু
with st.form("my_form"):
    name = st.text_input("তোমার নাম লিখো:")
    age = st.number_input("তোমার বয়স কত?", min_value=0, max_value=120)
    submitted = st.form_submit_button("জমা দাও")

    # যখন ফর্ম সাবমিট হবে
    if submitted:
        if name.strip() == "":
            st.error("❌ নাম খালি রাখা যাবে না!")
        elif age < 18:
            st.warning("⚠️ তুমি এখনো প্রাপ্তবয়স্ক না!")
        else:
            st.success(f"✅ ধন্যবাদ {name}, তোমার বয়স {age} বছর।")
''', language="bashe")


st.title("📋 ইউজার ইনপুট ফর্ম")

# ফর্ম শুরু
with st.form("my_form"):
    name = st.text_input("তোমার নাম লিখো:")
    age = st.number_input("তোমার বয়স কত?", min_value=0, max_value=120)
    submitted = st.form_submit_button("জমা দাও")

    # যখন ফর্ম সাবমিট হবে
    if submitted:
        if name.strip() == "":
            st.error("❌ নাম খালি রাখা যাবে না!")
        elif age < 18:
            st.warning("⚠️ তুমি এখনো প্রাপ্তবয়স্ক না!")
        else:
            st.success(f"✅ ধন্যবাদ {name}, তোমার বয়স {age} বছর।")
st.subheader("""ব্যাখ্যা:
             

             
st.form("my_form")	                        এটি একটি ফর্ম ব্লক তৈরি করে, যেখানে একসাথে ইনপুট নেওয়া যায়।
             
st.text_input()	                            ইউজার থেকে নাম নেওয়ার জন্য।
             
st.number_input()	                        বয়স নেওয়ার জন্য, নিচের ও উপরের সীমা দেওয়া যায়।
             
form_submit_button()	                    ফর্ম সাবমিট করার বাটন। সাবমিট না করলে ভেতরের কিছুই চলবে না।
             
st.success(), st.error(), st.warning()	    বিভিন্ন রকম মেসেজ দেখানোর জন্য ব্যবহৃত হয়।""")


with st.expander("📘 ফর্ম ও ইনপুট ব্যাখ্যা"):
    st.markdown("""
### st.form()
- এটি একটি ফর্ম ব্লক তৈরি করে।
- সব ইনপুট একসাথে নেওয়া হয় এবং `form_submit_button()` ক্লিক না করা পর্যন্ত সেগুলো কাজ করে না।

### ইনপুট যাচাই (Validation)
- খালি ইনপুট, ভুল ইনপুট ব্লক করতে `if-else` ব্যবহার করা হয়।

### st.success(), st.error(), st.warning()
- বিভিন্ন অবস্থায় ইউজারকে Feedback দেওয়ার জন্য ব্যবহৃত হয়।

💡 উদাহরণ: ভুল ইনপুটে লাল রঙের Error, সঠিক ইনপুটে সবুজ Success।
""")

