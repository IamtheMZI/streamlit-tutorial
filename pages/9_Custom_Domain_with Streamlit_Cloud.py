import streamlit as st

st.subheader("অধ্যায় ৯: কাস্টম ডোমেইন যুক্ত করা (Custom Domain with Streamlit Cloud)")

st.subheader("""ভূমিকা
             
Streamlit Cloud সাধারণত তোমার অ্যাপকে https://your-app-name.streamlit.app এই ধরনের সাব-ডোমেইনে চালায়।
কিন্তু প্রফেশনাল অ্যাপের জন্য অনেক সময় তোমার নিজের ডোমেইন যেমন:""")

st.subheader("https://www.myawesomeapp.com")

st.write("এই রকম কাস্টম ডোমেইন ব্যবহার করতে চাইবে। এখন আমরা শিখবো কীভাবে Streamlit অ্যাপে কাস্টম ডোমেইন যুক্ত করা যায়।")

st.subheader("""ধাপ ১: তোমার নিজের ডোমেইন কিনে নাও (যদি না থাকে)
             
তুমি ডোমেইন কিনতে পারো নিচের যেকোনো ওয়েবসাইট থেকে:

Namecheap

Google Domains

GoDaddy

⏳ সাধারণত .com, .net, .xyz টাইপ ডোমেইন ৮০০–১৫০০ টাকার মধ্যে পাওয়া যায়।""")

st.subheader("""ধাপ ২: Streamlit অ্যাপ ডেপলয় করো
             
Streamlit Cloud-এ তোমার অ্যাপ আগে থেকেই থাকতে হবে। না থাকলে প্রথমে GitHub + Streamlit Cloud দিয়ে ডেপলয় করো:

✅ উদাহরণ:
             
https://your-username-your-repo-name.streamlit.app""")



st.subheader("""ধাপ ৩: কাস্টম ডোমেইন সেটআপ (Streamlit Cloud থেকে)
             
১. Streamlit Cloud এ গিয়ে অ্যাপ ওপেন করো
             
২. ⚙️ Settings > Domains এ যাও
             
৩. নিচের মতো একটি অপশন দেখবে:

🔗 Add Custom Domain
             
৪. সেখানে তোমার ডোমেইন লিখো, যেমন:


www.myawesomeapp.com
             

৫. Submit করার পর, Streamlit তোমাকে কিছু DNS রেকর্ড দেবে (A Record বা CNAME)""")

st.subheader("""ধাপ ৪: DNS রেকর্ড কনফিগার করো (Domain Provider থেকে)
             
১. ডোমেইন যেখান থেকে কিনেছো, সেখানে DNS Management প্যানেলে যাও
             
২. Streamlit-এ যেই রেকর্ডগুলো বলা হয়েছে সেগুলো হুবহু কপি করে DNS-এ পেস্ট করো

যেমন:

Name: @
             
Type: CNAME
             
Value: cname.streamlit.io
             
TTL: 3600
             
৩. সেভ করো ✅

⏳ এটা লাইভ হতে ১ ঘণ্টা পর্যন্ত সময় নিতে পারে""")

st.subheader("""ধাপ ৫: চেক করো
             
১. ১–২৪ ঘণ্টা পরে https://www.myawesomeapp.com ওপেন করো
             
২. দেখবে তোমার Streamlit অ্যাপ সেই ডোমেইনে রান করছে 🎉

""")