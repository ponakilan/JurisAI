from search import VectorDB

db = VectorDB()

query = """
The case involves a dispute regarding the jurisdiction of the Payment of Wages Authority, whose order is challenged through a writ petition before the Bombay High Court under Article 226 of the Indian Constitution. The petitioner, Shri Balwantrai Chimanlal Trivedi, contends that the authority lacks jurisdiction to pass the order in question. After the Bombay High Court upholds the decision, the petitioner files a special leave petition under Article 136 before the Supreme Court, arguing that the tribunal's lack of jurisdiction invalidates the order. The Supreme Court considers whether the issue of jurisdiction has led to any failure of justice, which would warrant interference under its discretionary powers. The case raises important questions about the limits of judicial review, the role of special leave jurisdiction, and the conditions under which a court should intervene when jurisdictional concerns are raised.
"""

docs = db.search(query, 2)