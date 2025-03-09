streamlit run temp.py --server.port 8000 &
streamlit run ui/format.py --server.port 8001 &
streamlit run ui/doc.py --server.port 8002 &
streamlit run ui/guide.py --server.port 8003 &
cd core && streamlit run similar_cases.py --server.port 8004 &