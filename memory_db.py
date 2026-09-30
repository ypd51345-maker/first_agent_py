import chromadb


client = chromadb.PersistentClient(
    path="./memory_database"
)


collection = client.get_or_create_collection(
    name="user_memory"
)



def save_memory(text):

    count = collection.count()


    collection.add(
        documents=[text],
        ids=[str(count)]
    )



def search_memory(question):

    result = collection.query(
        query_texts=[question],
        n_results=3
    )


    return result["documents"]