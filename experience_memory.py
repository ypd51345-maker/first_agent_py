import chromadb
import time


client = chromadb.PersistentClient(
    path="./experience_memory"
)


collection = client.get_or_create_collection(
    name="agent_experience"
)



def save_experience(
        question,
        action,
        answer
):

    text = f"""
用户问题：
{question}

执行动作：
{action}

最终答案：
{answer}
"""


    collection.add(
        documents=[text],
        ids=[str(time.time())]
    )



def recall_experience(question):

    if collection.count() == 0:
        return []


    result = collection.query(
        query_texts=[question],
        n_results=3
    )


    return result["documents"][0]