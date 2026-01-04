import streamlit as st
import datetime

#title for the page and emoji setup
st.set_page_config(page_title="Study Planner for 2026", page_icon="📅")
#sub title
st.title("📚 Smart Study Planner")
st.subheader("Your assistant for exam preparation created Ian")

#sidebar for inputs
with st.sidebar:
    st.header("Exam Details")
    subject = st.text_input("What is the subject?", value="Computer Science")
    # Date picker: No more typing errors!
    exam_date = st.date_input("When is the exam?", datetime.date.today() + datetime.timedelta(days=7))
    difficulty = st.slider("Difficulty Level (1-10):", 1, 10, 5)

#study logic
today = datetime.date.today()
difference = exam_date - today
days = difference.days + 1

if st.button("Generate Plan"):
    if days < 1:
        st.error("Please select a date in the future!")
    else:
        st.success(f"Plan created for {subject}!")
        st.write(f"**Days left:** {days}")
        
        #create a visual separator
        st.divider()

        #loop with logic tips
        for i in range(1, days + 1):
            current_day = today + datetime.timedelta(days=i)
            day_text = current_day.strftime("%d %b")
            
            #use 'expander' to make it look like a modern app
            with st.expander(f"Session {i} - {day_text}"):
                if i == days:
                    st.write("🏁 **Final review** and relax before the exam day.")
                elif i == 1:
                    st.write("📖 **Organize** your notes and do a quick summary.")
                elif i % 2 == 0:
                    st.warning("🧠 **Focus on the topics you struggle with the most.**")
                else:
                    st.write("🔁 **Review** what you did last lesson.")

#instructions for user
st.sidebar.info("Fill the details and click 'Generate Plan' to start studying.")
