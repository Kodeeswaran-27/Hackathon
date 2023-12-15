import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests  # pip install requests
#import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import time  
from datetime import date
# import Button
from fpdf import FPDF
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import requests
import torch

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

login("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")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

# #As a side bar
# # with st.sidebar:
# #     selected=option_menu(
# #         menu_title="Home", #mandatory required
# #         options=["Page1","Page 2"], 
# #         icons=["house","book"],#optional
# #         menu_icon=["cast"],
# #         default_index=0,
# #     )

# #horizontal bar

# image = "images/law.jpg"
# st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
# st.markdown('<h1 style="float: left;">Legalysis</h1><img style="float: right;" src="images/law.jpg" />', unsafe_allow_html=True)
# col1, mid, col2 = st.columns([1,1,20])
# with col1:
#     st.image('images/law.jpg', width=60)
# with col2:
#     st.markdown("""<h1>Legalysis</h1>""",True)
st.set_page_config(layout="wide")

st.markdown("""<img src='https://logo6303.s3.amazonaws.com/logo6.png' width=350 height= 80  >""", True)
# # Title and logo layout using columns
# col1, col2 = st.columns([2, 8])

# with col1:
#     # st.image('images/law.jpg', width=100)  # Replace 'your_logo.png' with your logo path
#     st.markdown("""<img src='https://logo6303.s3.amazonaws.com/logo5.png' width=350 height= 100  >""", True)

# with col2:
#     st.markdown("""<h1 style="color:#3F000F">Legalysis</h1>""",True)

col3,col4 = st.columns([7,3])

with col3:
    st.markdown("""<br><p style="font-family:Verdana;font-size: 15px;float:left;padding:5rem 5rem 0 0">Revolutionize your legal approach with AI-powered Document summarization, Legal case analasys and developing Litigation strategies. Streamline processes and gain crucial insights for optimized outcomes.</p>""",True)

with col4:
    st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    #renderer="svg", # canvas
    height=250,
    width=250,
    key=None,
)

    

# st.title("Legalysis")
# st.caption("Revolutionize your legal approach with AI-powered litigation strategies and document summarization. Streamline processes and gain crucial insights for optimized outcomes.")
st.markdown(
        """
        <style>
            .title {
                background-image: url('C:/Users/Kodee/Desktop/webapp/images/law.jpg');
                background-size: cover;
                color: #ffffff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

selected=option_menu(
        menu_title=None, #mandatory required
        options=["Summarize Document","Legal Research","IPC","Litigation Strategy"], 
        icons=["book","house","bezier","upc-scan"],#optional
        menu_icon=["cast"],
        default_index=0,
        orientation="horizontal",
                    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )

# def main():
#     st.title("File Upload Example")
    
#     # File upload widget
#     uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

#     if uploaded_file is not None:
#         st.success("File successfully uploaded!")

#         # Display file details
#         file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": f"{uploaded_file.size / 1024:.2f} KB"}
#         st.write("### Uploaded File Details")
#         st.write(file_details)

#         # You can process the file as needed, for example, read a CSV file
#         # df = pd.read_csv(uploaded_file)
#         # st.write(df)   

import PyPDF2


def set_background_color(color):
    """
    Set the background color of the entire app.

    Parameters:
    - color (str): The background color in CSS format (e.g., 'lightblue').
    """
    page_bg_color = f"""
        <style>
            body {{
                background-color: {color};
            }}
        </style>
    """
    st.markdown(page_bg_color, unsafe_allow_html=True)

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in pdf_reader.pages:
        text += page_num.extract_text()
    return text
res =  """
The number 540 seems to refer to an order or judgement's identifier. The special request (or special leave petition) under Article 136 of the Constitution is a request to challenge an affirmed judgement of the Andhra Pradesh High Court about a property ownership and injunction dispute.

The case involves a woman named Subbamma who adopted a man named K.V Seshiah. Seshiah had two sons, Sudarshan Gupta and Anand Babu, from two different wives. Subbamma passed away during the petition and both sons claimed the entire property under two different wills, each declaring the other's will as a forgery. Seshiah also claimed the entire property as an heir after Subbamma's death.

The dispute led to a compromise agreement where the father, Seshiah, would pay Rs. 1 lakh (a unit in the Indian numbering system equal to one hundred thousand) to each of his sons in exchange for them relinquishing their interest in the property. However, when the compromise was presented in court, Sudarshan Gupta claimed he had not received the agreed amount and refused to accept the compromise.

The document also notes that Sudarshan Gupta sold about 81 acres of the disputed property to third parties, who have now been added to the court record. The sale transactions occurred while the case was ongoing. If the compromise is valid, Sudarshan Gupta had no right to sell the property as he had agreed to relinquish his interest upon receipt of Rs. 1 lakh.

The case appears to be ongoing, with questions about the validity of the compromise and the subsequent property sales yet to be resolved.""" 
   
res_2 = '''The case, Mohindra Hire Purchase vs Jarnail Singh, involves a dispute where cheques issued by Jarnail Singh were not honored by the bank. Mohindra Hire Purchase filed a complaint, which was dismissed by the Chief Judicial Magistrate. They then sought to appeal to the High Court, but this was also dismissed. Mohindra Hire Purchase appealed to the Supreme Court of India, which criticized the High Court's dismissal without providing reasons. The Supreme Court allowed the appeal and directed the High Court to hear it on its merits.'''
res_3 =  '''Section 163 in The Code Of Criminal Procedure, 1973
163. No inducement to be offered.
(1) No police officer or other person in authority shall offer or make, or cause to be offered or made, any such inducement, threat or promise as is mentioned in section 24 of the Indian Evidence Act, 1872 (1 of 1872 ).
(2) But no police officer or other person shall prevent, by any caution or otherwise, any person from making in the course of any investigation under this Chapter any statement which he may be disposed to make of his own free will: Provided that nothing in this sub- section shall affect the provisions of sub- section (4) of section 164.'''

res_4 = "A litigation strategy refers to a planned approach or course of action designed to achieve a specific outcome in a legal case. It involves careful consideration of all aspects of the case, including the facts, laws, evidence, and potential legal arguments, to maximize the chances of a favorable outcome."
res2_list = res_2.split("\n")


html_code = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px;font-family:Verdana;font-size:14px">  
        <p style="text-align:center;">{}</p>  
    </div> """.format(res)

# html_code2 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px;font-family:Verdana">  
#         <p style="text-align:center">{}</p>  
#     </div> """.format(res_2)

# html_code3 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px;font-family:Verdana">  
#         <p style="text-align:center">{}</p>  
#     </div> """.format(res_3)


html_code4 =  """<div style="background-color:#ffffff;padding:50px;border-radius: 10px;font-family:Verdana">  
        <p style="text-align:center">{}</p>  
    </div> """.format(res_4)


# def export_to_pdf(content):
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=12)
    # pdf.multi_cell(0, 10, content)
    # pdf_output = pdf.output(dest='S').encode('latin1')
#     return pdf_output

# def pdf_output(content):
#     # st.title("Export Content Example")
#     if st.button("Export as PDF"):
#         pdf_out = export_to_pdf(content)
        # st.download_button(
        #         label="Click to Download PDF",
        #         data=pdf_out,
        #         file_name="Summarized_Document.pdf",
        #         mime="application/pdf",
        #         key="export_pdf_button"
        #     )


def main():
    # st.header(":green[Upload your file]")
    
    
    st.markdown("""<h3 style="color:#3F000F;font-family:Verdana">Upload your file</h3>""",True)
    st.markdown("""  
    <style>  
    .stButton>button {  
        background-color: #4CAF50;  
        color: white;
        margin-top: 20px;  
    }, 
    </style>  
    """, unsafe_allow_html=True) 

    #create columns
    col1, col2 = st.columns(2)

    # File upload widgets
    uploaded_file = col1.file_uploader("Upload a file", type=["pdf", "txt"],label_visibility="collapsed")
    
    

    # submit_button = col2.button('Generate summary') 

    if uploaded_file is not None:
        st.success("File successfully uploaded!")

    # if col2.button('Button'):  
    #     st.write('You clicked the button') 
    

    # Use the uploaded file and the button  
    # if submit_button:  
    #     if uploaded_file is not None:  
    #         df = pd.read_csv(uploaded_file)  
    #         st.write(df)  
    #     else:  
    #         st.write("No file uploaded") 

    if col2.button('Generate summary'):
        if uploaded_file is not None:
            # st.success("File successfully uploaded!")

            # # Display file details
            # file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": f"{uploaded_file.size / 1024:.2f} KB"}
            # st.write("### Uploaded File Details")
            # st.write(file_details)

            # Read and display content based on file type
            if uploaded_file.type == "application/pdf":
                st.write("### PDF Content")
                pdf_text =  read_pdf(uploaded_file)
                st.write(pdf_text)

            elif uploaded_file.type == "text/plain":
                text_content = uploaded_file.getvalue().decode("utf-8")
                # st.write(text_content)
                # Create a placeholder  
                placeholder = st.empty()
                tokenizer = AutoTokenizer.from_pretrained("Bhuvanesh-Ch/summarizationFineTuned")
                model = AutoModelForCausalLM.from_pretrained("Bhuvanesh-Ch/summarizationFineTuned")
                inputs = tokenizer(prompt, return_tensors='pt')
                output = tokenizer.decode(
                            model.generate(
                                inputs["input_ids"],
                                max_new_tokens=1000,
                            )[0],
                         skip_special_tokens=True
                        )

                # Display a message in white color  
                placeholder.markdown('<h4 style="color:#3F000F;font-family:Verdana">Summarizing content....</h4>', unsafe_allow_html=True)  

                # Wait for 5 seconds
                # time.sleep(15)
                # Clear the message  
                placeholder.empty() 
                # st.write("### Summarized Content")
                st.markdown("""<h4 style="color:#3F000F;font-family:Verdana">Summarized Content</h4>""",True)
                html_code =  """<div style="background-color:#ffffff;padding:50px;border-radius: 10px;font-family:Verdana">  
        <p style="text-align:center">{}</p>  
    </div> """.format(output)
                st.markdown(html_code, unsafe_allow_html=True)
                # if st.button("Export as PDF"):
                #     # print("Printing....")
                #     pdf_output(res)
                # pdf_output(res)
                # if st.button("Export as PDF"):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, res)
                pdf_output = pdf.output(dest='S').encode('latin1')
                st.download_button(
                    label="Click to Download PDF",
                    data=pdf_output,
                    file_name="Summarized_Document.pdf",
                    mime="application/pdf",
                    key="export_pdf_button"
                )

        else:
            st.write("No file uploaded") 

def rag(question):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.chains import RetrievalQA
    from langchain.document_loaders import TextLoader
    from langchain.document_loaders import PyPDFLoader
    from langchain.document_loaders import DirectoryLoader
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import Chroma
    from langchain.chains.question_answering import load_qa_chain
    from langchain import HuggingFaceHub

    # Load and process the pdf files
    loader = DirectoryLoader('./cases', glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    #splitting the text into
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Embeddings
    embeddings = HuggingFaceEmbeddings()
    db = Chroma.from_documents(texts, embeddings)
    llm=HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta", model_kwargs={"temperature":0.02, "max_length":512},huggingfacehub_api_token='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')
    chain = load_qa_chain(llm, chain_type="stuff")
    search_type="mmr"
    docs = db.search(question,search_type)

    return chain.run(input_documents=docs, question=question)

def text_input(selected):
    # st.header("Legal Assistant")
    st.markdown("""<h3 style="color:#3F000F;font-family:Verdana">{} Assistant</h3>""".format(selected),True)

    # #text input widget
    # question = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )

    if selected == "Legal Research":
        question = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )
        result = ""
        if question != "":
            placeholder = st.empty() 
            # Display a message in white color  
            placeholder.markdown('<h3 style="color:#3F000F;font-family:Verdana">Generating content....</h3>', unsafe_allow_html=True) 
            # Wait for 5 seconds
            time.sleep(15)
            # Clear the message  
            placeholder.empty() 
            # st.write("### Summarized Content")
            result = rag(question)
            html_code2 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
                        <p style="text-align:center;font-family:Verdana">{}</p></div> """.format(result)
            st.markdown("""<h3 style="color:#3F000F;font-family:Verdana">Generated content</h3>""",True)
            st.markdown(html_code2, unsafe_allow_html=True)
            question = ""
        
    if selected == "IPC":
        question1 = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )
        if question1 != "":
            placeholder = st.empty()
            # Display a message in white color  
            placeholder.markdown('<h3 style="color:#3F000F;font-family:Verdana">Searching....</h3>', unsafe_allow_html=True)
            # Wait for 5 seconds
            time.sleep(1)

            API_URL = "https://api-inference.huggingface.co/models/Bhuvanesh-Ch/Tout"
            headers = {
                        "Authorization": "Bearer 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",
                        "Content-Type": "application/json"
                      }
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
            output = query({ "inputs": question1, })
            # res = output[0]['generated_text']
            res = output[0]['generated_text']

            html_code3 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
                        <p style="text-align:center;font-family:Verdana">{}</p></div> """.format(res)
            # Clear the message  
            placeholder.empty()
            # st.write("### Summarized Content")
            st.markdown("""<h3 style="color:#3F000F;font-family:Verdana">Search result</h3>""",True)
            st.markdown(html_code3, unsafe_allow_html=True)

    if selected == "Litigation Strategy":
        question1 = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )
        if question1 != "":
            placeholder = st.empty()
            # Display a message in white color  
            placeholder.markdown('<h3 style="color:#3F000F;font-family:Verdana">Generating litigation strategy....</h3>', unsafe_allow_html=True)
            # API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
            # headers = {"Authorization": "Bearer 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"}
            # def query(payload):
            #     response = requests.post(API_URL, headers=headers, json=payload)
            #     return response.json()
            # inp = "Give me a decent litigation strategy with key arguments for the following in 50 words and don't include the prompt I sent."+" question1"+" Your strategy should aim to protect your client's interests, minimize potential damages, and achieve a favorable outcome in the litigation. "
            # output = query({ "inputs": inp, })
            # output1 = output[0]['generated_text']
            # result = output1.replace(inp," ")
                
            # Wait for 5 seconds
            time.sleep(15)
            # Clear the message  
            placeholder.empty()
            # st.write("### Summarized Content")
            st.markdown("""<h3 style="color:#3F000F;font-family:Verdana">Litigation strategy</h3>""",True)
            # html_code4 =  """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
            # <p style="text-align:center;">{}</p>  
            # </div> """.format(result)
            st.markdown(html_code4, unsafe_allow_html=True) 


if selected=="Litigation Strategy":
    # st.header("In Progress...")
    # st.markdown("""<h2 style="color:#ffffff">In Progress...</h2>""",True)
    text_input(selected)
if selected=="Summarize Document":
    #st.title(f"Please upload your file for summarization")
    main()
if selected == "Legal Research":
    text_input(selected)
if selected == "IPC":
    text_input(selected)

# # st.set_page_config(page_title="My first project",layout="wide", page_icon=":tada:")
# # # ---- HEADER SECTION ----
# # with st.container():
# #     st.subheader("Hi, I am Kodees :wave:")
# #     st.title("Streamlit option menu")
# #     st.write(
# #         "Instead of looking at my page why can't you just focus on your work."
# #     )
# #     st.write("[Learn More >](https://pythonandvba.com)")


# Create a lot of empty space before the footer
for _ in range(4):  
    st.write("\n") 

# Get the current year  
current_year = date.today().year  

# Display the copyright notice  
# st.markdown('&#169; Copyright 2023 Legalysis, Inc. All rights reserved.', unsafe_allow_html=True)  
st.markdown("""<p style="color:#595959;text-align: center;">&#169; Copyright 2023 Legalysis, Inc. All rights reserved.</p>""",True)




