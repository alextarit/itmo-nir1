# Это для simple rag запроса
simple_rag_prompt = """Use the following context to answer the question.
    If the context does not contain enough information for a complete answer, indicate that.
    Respond only in Russian.
    If the request concerns writing code, provide a detailed implementation with comments.

    Context:
    {context}

    Question: {query}

    Answer:"""

# Это для bm25 rag запроса
bm25_rag_prompt = """Use the following context to answer the question.
    If the context does not contain enough information for a complete answer, indicate that.
    Respond only in Russian.
    If the request concerns writing code, provide a detailed implementation with comments.

    Context:
    {context}

    Question: {query}

    Answer:"""

# Это для graph rag запроса
graph_rag_prompt = """Use the following context to answer the question.
    If the context does not contain enough information for a complete answer, indicate that.
    Respond only in Russian.
    If the request concerns writing code, provide a detailed implementation with comments.

    Context:
    {context}

    Question: {query}

    Answer:"""