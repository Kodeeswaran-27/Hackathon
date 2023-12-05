import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests  # pip install requests
#import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import time  
from datetime import date

import requests

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

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


# Title and logo layout using columns
col1, col2, col3 = st.columns([1.5, 11,4])

with col1:
    # st.image('images/law.jpg', width=100)  # Replace 'your_logo.png' with your logo path
    st.markdown("""<img src='https://png.pngtree.com/png-clipart/20200225/original/pngtree-law-logo-vector-with-judicial-balance-symbolic-of-justice-scale-in-png-image_5255566.jpg' width=100 height= 100 style="border-radius: 50%" >""", True)

with col2:
    st.markdown("""<h1 style="color:#E46208">Legalysis</h1>""",True)

with col3:
    st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    #renderer="svg", # canvas
    height=100,
    width=100,
    key=None,
)
    

# st.title("Legalysis")
st.markdown("""<br><p style="color:#FFFFFF;font-family:cursive;font-size: 18px">Revolutionize your legal approach with AI-powered Document summarization, Legal case analasys and developing Litigation strategies. Streamline processes and gain crucial insights for optimized outcomes.</p>""",True)
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
res = "CIVIL APPELLATE JURISDICTION CIVIL APPEAL NO. 12165 OF 1989 From the Judgment and Order dated 20.4.1984 of the Andhra Pradesh High Court in Appeal No. 472 of 1976. K. Mahadeva Reddy, Ms. Manjul Gupta, T.V.S.N. Chari and A. Subba Rao for the Appellant. K. Ram Kumar, S.A. Ahmed, Tanweer Abdul and Mohan Pandey for the Respondents. The Judgment of the Court was delivered by K. JAGANMOHAN, J. The appellant is the adopted son of one Subbamma. The appellant 's adoptive mother died during the pendency of the special leave petition in this Court. The appellant and his brother claimed title to the property of Subbamma. Their claim was opposed by the second respondent who claimed title to the property on the basis of two wills alleged to have been executed by Subbamma. The parties entered into a compromise. The terms of the compromise stipulated payment of Rs.1 lakh by the father to each of his two sons in lieu of relinquishment of their interest. The second respondent maintained that he had not been paid Rs.1 lakh as stipulated and he had no intention to accept the compromise. The question as to recording of the compromise was taken up by this Court and the parties have been heard. The compromise deed signed by the parties stipulated that the petitioner had given to the second and third respondents an amount of Rs.1 lakh each and the second and third respondents had received the same. The second respondent had disputed the fact of payment and had alienated about 81 acres of property which constituted the subject matter of dispute to third parties. The alienees had made an attempt to hold out that there were agreements for sale prior to the compromise for which there was no acceptable evidence. The compromise is not in dispute."

res_2 = "In 1998, the following were established:\n\n1. The International Institute for the Unification of Private Law (UNIDROIT) published Principles of Transnational Civil Procedure, which aimed to provide a set of principles for resolving civil disputes in a transnational context.\n\n2. The United Nations Commission on International Trade Law (UNCITRAL) adopted the Model Law on Electronic Commerce, which aimed to provide a framework for the use of electronic commerce in international transactions.\n\n3. The European Commission established the Expert Group on a Common Frame of Reference in the Area of European Contract Law, which aimed to develop a set of common principles for contract law in the European Union.\n\n4. The International Chamber of Commerce (ICC) published the ICC Rules on the Application of Principles of Law, which aimed to provide a set of principles for resolving disputes in a transnational context.\n\n5. The International Law Commission (ILC) adopted the Draft Convention on International Interests in Mobile Equipment, which aimed to provide a framework for the creation of international interests in mobile equipment, such as aircraft and ships.\n\n6. The International Institute for the Unification of Private Law (UNIDROIT) published the Principles of International Commercial Contracts, which aimed to provide a set of principles for international commercial contracts.\n\n7. The United Nations Commission on International Trade Law (UNCITRAL) adopted the Model Law on Cross-Border Insolvency, which aimed to provide a framework for the resolution of cross-border insolvencies.\n\n8. The International Chamber of Commerce (ICC) published the ICC Rules on the Administration of Evidence in International Arbitration, which aimed to provide a set of rules for the administration of evidence in international arbitration.\n\n9. The International Law Commission (ILC) adopted the Draft Convention on the Law Applicable to Contractual Obligations, which aimed to provide a framework for the determination of the law applicable to contractual obligations in a transnational context.\n\n10. The International Chamber of Commerce (ICC) published the ICC Rules on the Use of Electronic Communications in International Arbitration, which aimed to provide a set of rules for the use of electronic communications in international arbitration.\n\nIn summary, in 1998, several international organizations and commissions published and adopted a number of important legal instruments and conventions related to private law, including principles for transnational civil procedure, electronic commerce, contract law, trusts, succession, and non-contractual obligations, as well as rules for the use of electronic communications and signatures in international arbitration and trade. These instruments aimed to provide a framework for resolving legal disputes and issues in a transnational context, and to promote the harmonization and unification of private law across different legal systems and jurisdictions."

res_3 =  "Section 144 is a provision in the Indian Penal Code that empowers a public servant to issue an order prohibiting an assembly of five or more persons in a public place that has the potential to cause disturbance of public peace. This section is commonly used by authorities to prevent large gatherings during protests, strikes, or other forms of civil disobedience. Violation of this order is a criminal offense punishable under section 188 of the IPC."

# res_4 = "Our litigation strategy will focus on three key arguments:\n\n1. Non-infringement: We will argue that our product does not fall within the scope of the competitor's patent. We will present evidence to show that our product operates differently from the competitor's patented technology and does not infringe upon any of the patent's claims.\n\n2. Invalidity: We will challenge the validity of the competitor's patent. We will present evidence to show that the patent is either obvious or lacks novelty, and therefore should be deemed invalid.\n\n3. Laches: We will argue that the competitor has unreasonably delayed in bringing the lawsuit, and as a result, they should be barred from pursuing their claim. We will present evidence to show that the competitor had knowledge of our product for an extended period before filing the lawsuit.\n\nIn addition to these arguments, we will also consider potential counterclaims against the competitor. If we can identify any instances of the competitor infringing upon our intellectual property, we will pursue counterclaims to strengthen our position in the litigation.\n\nExpert witnesses will play a crucial role in our defense. We will retain experts in the relevant technical fields to provide testimony on the non-infringement, invalidity, and laches arguments. We will also consider retaining experts to provide testimony on the damages, if necessary.\n\nIn terms of legal precedents and statutes, we will review relevant case law and statutes to identify any legal principles that can support our defense. We will also consider any settlement negotiations with the competitor, but only if it is in our client's best interests to do so.\n\nOur pre-trial preparation will involve a thorough review of the discovery process. We will work closely with our client to identify any relevant documents and witnesses, and we will prepare a detailed discovery plan to ensure that we obtain all necessary information.\n\nDuring the motion practice, we will file motions to dismiss the competitor's claims, to exclude certain evidence, and to limit the scope of discovery. We will also consider filing a motion for summary judgment, if appropriate.\n\nAt trial, we will present our arguments in a clear and persuasive manner, using visual aids and demonstrative evidence to support our position. We will also cross-examine the competitor's witnesses and present our own witnesses to testify on our behalf.\n\nIn terms of settlement negotiations, we will only consider settlement if it is in our client's best interests to do so. We will work closely with our client to evaluate the potential benefits and drawbacks of settlement, and we will provide guidance on any settlement proposals that are presented by the competitor.\n\nOverall, our litigation strategy will aim to protect our client's interests, minimize potential damages, and achieve a favorable outcome in the litigation. We will work closely with our client to ensure that we develop a comprehensive plan that is tailored to their specific needs and circumstances."

res2_list = res_2.split("\n")


html_code = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
        <p style="text-align:center;">{}</p>  
    </div> """.format(res)

# html_code2 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
#         <p style="text-align:center;">{}</p>  
#     </div> """.format(res_2)

html_code3 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
        <p style="text-align:center;">{}</p>  
    </div> """.format(res_3)

# html_code4 =  """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
#         <p style="text-align:center;">{}</p>  
#     </div> """.format(res_4)

def main():
    # st.header(":green[Upload your file]")
    st.markdown("""<h2 style="color:#ffffff">Upload your file</h2>""",True)
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

                # Display a message in white color  
                placeholder.markdown('<h3 style="color:white;">Summarizing content....</h3>', unsafe_allow_html=True)  

                # Wait for 5 seconds
                time.sleep(5)
                # Clear the message  
                placeholder.empty() 
                # st.write("### Summarized Content")
                st.markdown("""<h3 style="color:#ffffff">Summarized Content</h3>""",True)
                st.markdown(html_code, unsafe_allow_html=True)
        
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
    st.markdown("""<h2 style="color:#ffffff">{} Assistant</h2>""".format(selected),True)

    # #text input widget
    # question = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )

    if selected == "Legal Research":
        question = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )
        if question != "":
            placeholder = st.empty() 
            # Display a message in white color  
            placeholder.markdown('<h3 style="color:white;">Generating content....</h3>', unsafe_allow_html=True) 
            # Wait for 5 seconds
            time.sleep(5)
            # Clear the message  
            placeholder.empty() 
            # st.write("### Summarized Content")
            result = rag(question)
            html_code2 = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
                        <p style="text-align:center;">{}</p></div> """.format(result)
            st.markdown("""<h3 style="color:#ffffff">Generated content</h3>""",True)
            st.markdown(html_code2, unsafe_allow_html=True)
            question = ""
    if selected == "IPC":
        question1 = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )
        if question1 != "":
            placeholder = st.empty()
            # Display a message in white color  
            placeholder.markdown('<h3 style="color:white;">Searching....</h3>', unsafe_allow_html=True)
            # Wait for 5 seconds
            time.sleep(5)
            # Clear the message  
            placeholder.empty()
            # st.write("### Summarized Content")
            st.markdown("""<h3 style="color:#ffffff">Search result</h3>""",True)
            st.markdown(html_code3, unsafe_allow_html=True) 
    if selected == "Litigation Strategy":
        question1 = st.text_area("Ask your question", placeholder='Message your assistant', height=2,label_visibility="collapsed" )
        if question1 != "":
            placeholder = st.empty()
            # Display a message in white color  
            placeholder.markdown('<h3 style="color:white;">Generating litigation strategy....</h3>', unsafe_allow_html=True)
            API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
            headers = {"Authorization": "Bearer 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"}
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
            inp = "Give me a decent litigation strategy with key arguments for the following in 50 words and don't include the prompt I sent."+" question1"+" Your strategy should aim to protect your client's interests, minimize potential damages, and achieve a favorable outcome in the litigation. "
            output = query({ "inputs": inp, })
            output1 = output[0]['generated_text']
            result = output1.replace(inp," ")
                
            # Wait for 5 seconds
            # Clear the message  
            placeholder.empty()
            # st.write("### Summarized Content")
            st.markdown("""<h3 style="color:#ffffff">Litigation strategy</h3>""",True)
            html_code4 =  """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
            <p style="text-align:center;">{}</p>  
            </div> """.format(result)
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
for _ in range(10):  
    st.write("\n") 

# Get the current year  
current_year = date.today().year  

# Display the copyright notice  
# st.markdown('&#169; Copyright 2023 Legalysis, Inc. All rights reserved.', unsafe_allow_html=True)  
st.markdown("""<p style="color:#d9d9d9;text-align: center;">&#169; Copyright 2023 Legalysis, Inc. All rights reserved.</p>""",True)




