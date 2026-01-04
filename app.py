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
        
        # --- NEW: Progress Bar ---
        max_days = 30 
        progress_value = max(0, min(100, (1 - (days / max_days)) * 100))
        st.progress(int(progress_value))
        
        #create a visual separator
        st.divider()

        # --- NEW: Smart Phasing Logic ---
        if days > 20:
            #1. long term preparation
            with st.expander("📅 PHASE 1: Deep Preparation (Slow Pace)"):
                st.info("Since the exam is far away, focus on understanding the core concepts.")
                st.write("- Read all materials and organize your index.")
                st.write("- Create mind maps and summaries.")
                st.write("- Don't stress yet, just keep a steady rhythm.")

            #2. the final 15 days countdown
            st.subheader("🏁 The Final 15 Days Countdown")
            for i in range(1, 16):
                current_day = today + datetime.timedelta(days=i)
                day_text = current_day.strftime("%d %b")
                
                with st.expander(f"Final Sprint - Day {i} ({day_text})"):
                    if i % 2 == 0:
                        st.warning("🧠 **Focus on the topics you struggle with the most.**")
                    else:
                        st.write("🔁 **Review** your summaries and watch research videos.")
        else:
            #3. if exam is in a little amount of days
            for i in range(1, days + 1):
                current_day = today + datetime.timedelta(days=i)
                day_text = current_day.strftime("%d %b")
                
                with st.expander(f"Session {i} - {day_text}"):
                    if i == days:
                        st.success("🏁 **Final review** and relax before the exam day.")
                    elif i == 1:
                        st.info("📖 **Organize** your notes and do a quick summary.")
                    elif i % 2 == 0:
                        st.warning("🧠 **Focus on the topics you struggle with the most.**")
                    else:
                        st.write("🔁 **Review** what you did last lesson.")

#instructions for user
st.sidebar.info("Fill the details and click 'Generate Plan' to start studying.")
