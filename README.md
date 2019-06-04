# sCake
Python (v 2.7) scripts for implementing sCAKE method for single document Keyword Extraction. Also includes script for keyphrase generation.

sCAKE: semantic Connectivity Aware Keyword Extraction

Authors: [Surbhi Mittal](https://github.com/surbhim18/), [Shivani Kumar](https://github.com/shivanik96)

Acknowledgement: [Swagata Duari](https://github.com/SDuari/)

Article DOI: https://doi.org/10.1016/j.ins.2018.10.034

Article Link: http://www.sciencedirect.com/science/article/pii/S0020025518308521, https://arxiv.org/pdf/1811.10831.pdf

R Scripts for implementing sCAKE and LAKE method for single document keyword Extraction:
https://github.com/SDuari/sCAKE-and-LAKE

Citation:
=========
```tex
@article{DUARI2019100,
        title = "sCAKE: Semantic Connectivity Aware Keyword Extraction",
        journal = "Information Sciences",
        volume = "477",
        pages = "100 - 117",
        year = "2019",
        issn = "0020-0255",
        doi = "https://doi.org/10.1016/j.ins.2018.10.034",
        url = "http://www.sciencedirect.com/science/article/pii/S0020025518308521",
        author = "Swagata Duari and Vasudha Bhatnagar",
        keywords = "Automatic Keyword Extraction, Text Graph, Semantic Connectivity, Parameterless, Language Agnostic"
}
```

Description:
============

The algorithms rank all the candidate keywords and present the output in descending order of SCScore. and does not define the number of candidates to be extracted as keywords.
Thus the user has to decide on the number of extracted keywords. sCAKE is designed for languages with support of sohisticated NLP tools, like English. This impementation of sCAKE is aimed for English language only. However, interested users may apply the appropriate NLP tools, if available, for the language of their interest.

Pipeline:
=========
1. Run 'Create-position-info-sCAKE.py'.
2. Run 'Create-graph-sCAKE.py'.
3. Run 'InfluenceEvaluation.py'.
4. Run 'Word-score-with-PositionWeight-sCAKE.py'.
5. Run 'Construct-keyphrases-sCAKE.py' (for keyphrase generation).
