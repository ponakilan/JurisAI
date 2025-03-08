from search import VectorDB

db = VectorDB()

query = """
 HEADNOTE:
 Where  at  the hearing of an appeal filed by  special  leave
 from  a decision of the High Court in a Writ Petition  filed
 there under Art. 226 of the Constitution of India against an
 order   of  the  Payment  of  Wages  Authority,  the   Court
 considered  that  there  was some force  in  the  contention
 relating to the jurisdiction of the Authority concerned  but
 did  not decide that question on the view that as there  had
 been  no  failure of justice the Court would  not  interfere
 under  its powers under Art. 136, and the appellant  applied
 for a review of the judgment
 15
 114
 Held, that wide as are the powers of the Supreme Court under
 Art.  136 of the Constitution, its powers are  discretionary
 and though special leave had been granted the Court was  not
 bound to decide the question of jurisdiction of the inferior
 tribunal  or  court  where  the  decision  of  the  inferior
 tribunal or court had been taken to a higher tribunal  which
 undoubtedly had jurisdiction and from the decision of  which
 the   special  leave  was  granted  if  on  the  facts   and
 circumstances  of  the  case it came to  the  conclusion  in
 dealing with the appeal under that Article that there was no
 failure of justice.
 A. M. Allison v. B.  L. Sen, [1957] S.C.R. 359, relied on
"""

docs = db.search(query, 2)