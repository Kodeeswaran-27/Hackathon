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



