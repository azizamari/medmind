import streamlit as st

def main():
    st.set_page_config(page_title="Electronic Health Record Generator")
    st.title("Electronic Health Record Generator")

    # File uploader for conversation
    st.subheader("New Report")
    conversation_file = st.file_uploader("Upload report file", type=["txt"])
    if conversation_file is not None:
        st.success("Report file uploaded successfully!")

    # File uploader for doctor notes
    st.subheader("Old EHR")
    doctor_notes_file = st.file_uploader("Upload old EHR file", type=["txt"])
    if doctor_notes_file is not None:
        st.success("Patient EHR file uploaded successfully!")

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
