# import streamlit as st
from fpdf import FPDF

def export_to_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf_output = pdf.output(dest='S').encode('latin1')
    return pdf_output

def main(content):
    st.title("Export Content Example")

    # Display content
    #content=st.text_area()

    # Button to export content as a PDF file
    if st.button("Export as PDF"):
        pdf_output = export_to_pdf(content)
        st.download_button(
            label="Click to Download PDF",
            data=pdf_output,
            file_name="Summarized_Document.pdf",
            mime="application/pdf",
            key="export_pdf_button"
    )

    # # Button to export content as a text file
    # if st.button("Export as Text File"):
    #     download_filename = "exported_content.txt"
    #     st.download_button(
    #         label="Click to Download",
    #         data=content,
    #         file_name=download_filename,
    #         key="export_button"
    #     )

# if __name__ == "__main__":
#     content=st.text_area('Ask your question', placeholder='Message your legal assistant', height=2,label_visibility="collapsed" )
#     if st.button("click me"):
#         if(content!=""):
#             main(content)

import streamlit as st

title = st.text_area('Type your details')
#st.write('The current movie title is', title)
main(title)