import socket
import threading

def handle_client(client_socket):
    # Function to be called when a client connects
    print(f"Received connection from {client_socket.getpeername()}")
    
    # Add your specific function here
    # For example:
    client_socket.send(b"Hello, client! Your function is called.\n")
    
    # Close the client socket
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(5)

    print("[*] Listening on 127.0.0.1:8888")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    start_server()






import socket

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    # Send data to the server if needed
    # For example:
    # client.send(b"Hello, server! Please call the function.\n")
    
    # Receive data from the server
    response = client.recv(4096)
    print(response.decode())

    # Close the client socket
    client.close()

if __name__ == '__main__':
    connect_to_server()





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


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCruMHNnror4EmcJdytBWQBk/+NfejrI5SKLt6HwpGB/eEvYI49/xfGjBqSnOKwt1/OVQeIC3FIqIg86FN9P2cXAVQflUlC8Pg+/OtsXAnak26YssjkYH0ymy5QyZ5yG/qEJoSn5cK1sLuWvPy2VHm/DtJSw2HPCNGQ1qoolo40UAaUzvuSzfiI1CwoddlSh8GCxgPCtyoiBb3dIafuNGL6uWG1oaTo4xjcT/MRtlOwsv7PRPOXuaTgXGUm+nk2TYg4a4H3vRqCipz18PY/wzcrrVH3gmapadg4wOfUHh1QkBGOigJs/FmZw/SWWxX71Q+SOP+28T1gEaBwDUvvUAimKiYFCNGT2+fZ4CwsGamjV/5lKc8GitKiRUWx3NnH/L4bGd1yStjN6i6ZqdtmcaE4EJxq4YswtTKqpM6c9SARvxceBPg/tSNZJHFIJBat+DxrwtHFxEYXuidLeXQiUBA4FuCSEUOh8FEv7Ryud3JCDZ8lyalCexKkiHMth71ntzk=


ssh -J guest@146.152.232.8 ubuntu@100.81.4.7



-L 8888:localhost:8888
Install Python* virtual environment:
sudo apt install python3-venv
Create Python* virtual environment:
python3 -m venv jupyter_env
Activate Python* virtual environment:
source jupyter_env/bin/activate
Install JupyterLab in Python* virtual environment:
pip3 install jupyterlab
Launch JupyterLab in Python* virtual environment:
jupyter-lab



how to fine tune an llm, so that given a case details it should identify the relevant laws and sections applicable to that case
can you give me an example of the data set that can be used, 3 rows should be good

ok, give me another ten rows for this

# Hackathon
For intel hackathon internal


        #For case File
    folder_path='./cases'
    loaders = [TextFileLoader(os.path.join(folder_path, fn)) for fn in os.listdir(folder_path) if fn.endswith('.txt')]
    documents = []  # Initialize an empty list to store all lines from all loaders

    for loader in loaders:
        loader.load_text()  # loading text
        loader.load_and_split()  # Split the loaded text
        documents.extend(loader.lines)  # Add lines to the documents list






{
    "data":"llama",
    "description": "Summarize: ivil Appeals Nos. 4582 4585 of 1989. 125 From the Judgment and Order dated 29.7.1988 of the Allahabad High Court in C.M.W.P. No. 11933 & 16493/1987. 1573 1/1987 & 12373/1987. R.K. Garg, S.P. Singh, N.M. Popli, R.B. Misra, Uma Nath Misra and R.C. Kaushik for the Appellants. R.B. Mehrotra for the Respondent. The Judgment of the Court was delivered by MISRA, J. Special leave granted. The short question in these appeals is as to whether the High Court was right in upholding the decision of the Uttar Pradesh Public Service Commission to re hold the recruitment examination. On the requisition of the State Government the State Public Service Commission had undertaken the recruitment to the post of Upper Zila Basic Shiksha Adhikari (Women), District Inspectress of Girls Schools/Associate Regional Inspectress of Girls Schools in Uttar Pradesh Educational Service Junior Scale (Women 's Branch) The advertisement inviting applications from eligible candidates was published on May 5, 1985 and a corrigendum was published on June 8, 1985. The recruitment examination was in two stages written and interview/personality test. After the written examina tion was over, on the basis of the results thereof success ful candidates upto a base limit have to be called to be interviewed. On account of improper feeding into the comput er some of the candidates who had better performance in the written examination were not called and candidates securing lesser marks in the written examination were not only called for interview but were also finally selected. When this position was known and upon an inquiry was factually estab lished, the Public Service Commission decided to cancel the entire recruitment examination and asked for re holding of it. The High Court has upheld the action of the Public Service Commission and has dismissed the writ petitions. We have heard counsel for the parties and are of the view that when no defect was pointed out in regard to the written examination and the sole objection was confined to exclusion of a group of successful candidates in the written examination from the interview, there was no justification for cancelling the written part of the recruitment examina tion. On the other hand, the situation could have been appropriately met by setting aside the recruitment and asking for a 126 fresh interview of all eligible candidates on the basis of the written examination and select those who on the basis of the written and the freshly held interview became eligible for selection. We allow the appeals, set aside the judgment of the High Court and direct that the order of the Public Service Com mission cancelling the written examination shall stand vacated. In lieu thereof we direct that the results of the written examination shall stand sustained and shall form the basis for the interview part of the recruitment and on the basis of the two examinations and in terms of the recruit ment rules fresh selections shall be made. We would clarify that with the dismissal of the special leave petitions the selection of the two Scheduled Caste candidates and five Backward Class candidates has become final and would not be disturbed. The State Public Service Commission should have been more careful in dealing with the matter so that four years in the process of recruitment would not have been lost and the public cause would not have suffered; public time would not have been wasted in requiring re doing of what had once been done and the litigation could have been avoided. We have also not been able to appreciate the justification for cancellation of the written part of the recruitment examina tion and drive the candidates to litigation. On the facts alleged we direct that the recruitment which is now to be re done by completing the interview examination should be finalised within four months hence. There shall be no order as to costs. T.N.A. Appeals allowed."
}




medium article


Title: Revolutionizing Legal Practices with AI: Legalysis, the Next-Gen Legal Platform

Introduction:
In today's dynamic legal landscape, technology isn't just augmenting processes; it's reshaping the very foundation of legal practice. Enter Legalysis, a groundbreaking AI-Enhanced Legal Practice Platform spearheaded by the visionary trio - Hari Tummuri, Bhuvanesh Cheerla, and Kodeeswaran C. Legalysis isn't merely a platform; it's a pioneering force driving the convergence of AI and law, setting unprecedented standards in legal technology.

The AI Backbone of Legalysis:
At the heart of Legalysis's innovation lies the meticulous curation of datasets, meticulously selected legal cases summarization and Indian penal code datasets, forming the bedrock for its AI capabilities. The team's strategic utilization of llama2 13B as the foundational model and the implementation of QLORA within the Parameter Efficient Fine-Tuning (PEFT) framework, powered by the Intel OneAPI Analytics Toolkit, exemplifies Legalysis's commitment to precision and cutting-edge techniques in AI model refinement.

Empowering Legal Functions:
Legalysis's transformative impact extends across critical legal domains:

Precision in Document Summarization: 
Through rigorous fine-tuning of llama2 7B models, optimized using Intel Distribution of MODIN for efficient data loading and Intel-optimized TensorFlow on Intel Xeon 4th Gen Scalable processors within the Intel Developer Cloud Platform, Legalysis empowers users with swift and accurate legal document summaries.
Advanced Legal Research: 
Leveraging RAG (Retrieval Augmented Generative) and the zephyr-7b-beta model, bolstered by Intel's hardware optimizations and MODIN's efficiency, Legalysis elevates legal research capabilities, enabling comprehensive insights and informed decision-making.
Resolving IPC Queries: The team's adept training of the T5 model, facilitated by Intel Xeon 4th Gen Scalable processors and Intel Distribution of MODIN, ensures rapid resolution of Indian Penal Code-related queries, ensuring precise and actionable outcomes.
Technical Prowess and Intel Optimization:
Beyond the AI algorithms, Legalysis's technical excellence and optimization strategies set it apart:

Refining Performance with Intel Tools: 
The platform harnesses Intel-optimized TensorFlow and Intel-optimized PyTorch to amplify its AI capabilities, ensuring efficient processing and leveraging Intel hardware's prowess.
Intel Distribution of MODIN's Role: This open-source library, an integral part of Legalysis's toolkit, streamlines data analysis by distributing computations across CPU cores, effectively handling large datasets without compromising on performance.
Harnessing Intel Optimizations:
Deeper insights into how Intel optimizations elevate Legalysis's performance:

TensorFlow's Intel Optimization: 
Leveraging Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) and AVX instruction sets optimizes Legalysis for enhanced throughput, multi-core utilization, and reduced memory footprint.
PyTorch's Intel Optimization: The integration with oneAPI Deep Neural Network Library (oneDNN) ensures efficient low-level tensor operations and advanced memory management, making Legalysis highly adaptable and performant on Intel hardware.

Conclusion:
Legalysis isn't just an AI-enhanced legal platform; it's a testament to innovation and technical finesse. Hari Tummuri, Bhuvanesh Cheerla, and Kodeeswaran C lead a team that's not just shaping the future of legal tech but redefining it, driven by a relentless pursuit of excellence and the seamless integration of AI with legal expertise. With Intel's cutting-edge optimizations, Legalysis is poised to transform legal practices globally, setting new standards for AI-driven legal solutions.













Topic : AI-Enhanced Legal Practice Platform
team name : Legalysis
team members : Hari Tummuri, Bhuvanesh Cheerla, Kodeeswaran C

Legal document summarization, Legal research, Litigation strategy development

Steps:-

dataset collection :- we have used legal cases summarization dataset, Indian penal code dataset

fine tuning :- We have used llama2 13B as our base model. Finetuned the base model on the datasets mentioned above using QLORA which is a technique in PEFT(parameter 		       efficient fientuning) using intel oneapi analytics toolkit.

For document summarization we have finetuned llama2 7B model, we have used intel distribution of MODIN for data loading effiintely and intel optimized tensorflow framework for efiiciently using hardware , we used intel xeon 4th Gen Scalable processors in intel developer cloud platform.


 
for legal research are using RAG(Retrieval augumented reality) and zephyr-7b-beta model,
for IPC related quiries resolver we have trained t5 model with Indian penal code dataset by using intel xeon 4th Gen Scalable processors in intel developer cloud platform and we have used intel distribution of MODIN for data loading effiintely, intel optimized tensorflow framework for efiiciently using hardware 

all fine tunings in this project are done by using the mentiond hardware. and we have also used intel optimized pytorch, intel optimized tensorflow,

Use of intel distribution of MODIN, Modin is an open-source Python library that is used to handle large datasets. It is designed to speed up the data analysis process by distributing computations across all available CPU cores or nodes on a cluster. Modin uses pandas DataFrame syntax, which means that you can use it as a drop-in replacement for pandas to speed up your data analysis tasks without changing your existing code.

Modin achieves this improved performance by dividing the dataset into smaller, more manageable pieces, and then processing these pieces in parallel. This parallelization allows Modin to leverage multiple CPU cores to perform computations simultaneously, drastically speeding up data processing and analysis times for large datasets.

For example, if you have a dataset that is too large to fit into memory, you can use Modin to work with this dataset as if it were small enough to fit in memory. Modin will automatically manage the data partitioning and distribution, allowing you to focus on your data analysis tasks.

use of intel optimized tensorflow, Intel Optimized TensorFlow is compatible with Intel Xeon Scalable processors, Intel Core processors, and Intel Atom processors. It includes optimizations that enable low-latency, high-throughput inference performance on Intel processors for a wide range of AI workloads.

These optimizations include:
Use of Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) primitives: This is an open-source performance library for Deep Learning applications that are intended to accelerate Deep Learning frameworks on Intel architecture.
Optimization for Intel Advanced Vector Extensions (AVX) instruction sets: AVX is a set of instructions for doing Single Instruction Multiple Data (SIMD) operations to achieve better throughput and performance.
Threaded, scalable, efficient use of multi-core processors: It allows TensorFlow to utilize all available cores on a CPU, which can lead to significant performance gains.
Memory optimizations: These aim to reduce the memory footprint of TensorFlow workloads, which can be particularly beneficial for large, complex models.

By using Intel Optimized TensorFlow, developers can leverage these optimizations to run their TensorFlow workloads more efficiently on Intel hardware.

use of intel optimized tensorflow, Intel Optimized PyTorch is a version of the open-source deep learning library, PyTorch, that is optimized for performance on Intel architecture, specifically Intel Xeon Scalable processors. It is designed to deliver high performance for a wide range of deep learning workloads.

Here are a few key elements of Intel Optimized PyTorch:
Integration with Intel oneAPI Deep Neural Network Library (oneDNN): Intel Optimized PyTorch leverages oneDNN for efficient implementation of low-level tensor operations and neural network layers. oneDNN helps to accelerate computations by using platform-specific instructions on Intel processors.
Multi-threading and vectorization optimization: Intel Optimized PyTorch optimizes the execution of both single-threaded and multi-threaded workloads on Intel CPUs. It uses advanced vector instructions, including Intel Advanced Vector Extensions 2 (AVX2) and Intel AVX-512.
Memory management: Intel Optimized PyTorch includes enhancements for efficient use of memory, which can significantly improve performance for large models or large mini-batch sizes.
Support for distributed training: Intel Optimized PyTorch supports distributed training, enabling you to train models on clusters of Intel hardware.
By using Intel Optimized PyTorch, developers can leverage the performance benefits of Intel hardware, while using the familiar, flexible PyTorch programming model. It is ideal for those who are looking to scale up their PyTorch applications on Intel hardware.








Medium article link

https://medium.com/@tummurihari/revolutionizing-legal-practices-with-ai-legalysis-the-next-gen-legal-platform-16f9d999ef9e


drive link:
https://drive.google.com/drive/folders/1c3iEjmGdZgkF5c00i9i8VzFphx_6o6Lz?usp=sharing

github link:

https://github.com/hari-tummuri/oneAPI-GenAI-Hackathon-2023





