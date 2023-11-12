class Prompts(object):
    generate_medical_report_template="""Generate a detailed medical report based on the following input:
    {
        "conversation": [list of patient-doctor dialogue],
        "past_reports": [list of previous medical reports] or null,
        "real_time_doctor_notes": "string of notes taken during the consultation"
    }
    Provide a comprehensive report summarizing the doctor visitation/consultation, incorporating relevant details from the conversation, any past reports, and the real-time notes. The report should be clear, concise, and structured for easy understanding.
    {
        "text": "Generated medical report text here.",
        "report_title": "Title summarizing the medical visit"
    }
    Ensure accuracy and coherence in presenting the medical information.
    """
    generate_ehr_template="""Create an Electronic Health Record (EHR) based on the provided input:
    {
        "all_consultation_reports": [list of doctor consultation reports],
        "new_report": "string of the latest consultation report",
        "old_ehr_record": "string of the existing EHR record" or null
    }
    Generate a comprehensive Electronic Health Record by integrating information from all previous consultation reports, the latest report, and the existing EHR record (if available). Organize the data in a structured format that is easily accessible and understandable.
    {
        "ehr_text": "Generated EHR text here.",
        "ehr_title": "Title summarizing the Electronic Health Record"
    }
    Ensure accuracy and coherence in presenting the medical history and updates in the EHR.
    """