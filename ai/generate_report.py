import streamlit as st

def main():
    st.set_page_config(page_title="Medical Report Generator")
    st.title("Medical Report Generator")

    # File uploader for conversation
    st.subheader("Conversation")
    conversation_file = st.file_uploader("Upload conversation file", type=["txt"])
    if conversation_file is not None:
        st.success("Conversation file uploaded successfully!")

    # File uploader for doctor notes
    st.subheader("Doctor Notes")
    doctor_notes_file = st.file_uploader("Upload doctor notes file", type=["txt"])
    if doctor_notes_file is not None:
        st.success("Doctor notes file uploaded successfully!")

    # File uploader for old reports
    st.subheader("Old Reports")
    old_reports_files = st.file_uploader("Upload old reports files", type=["pdf", "docx"], accept_multiple_files=True)
    if old_reports_files is not None:
        st.success(f"{len(old_reports_files)} old reports files uploaded successfully!")

    # Display "hello" on button click
    if st.button("Generate Report"):
        st.write("hello")

if __name__ == "__main__":
    main()
