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

