
import chromadb
from pathlib import Path
from chunking import split_text


# 连接 Chroma 数据库
client = chromadb.PersistentClient(path="./database")


# 删除旧知识库
try:
    client.delete_collection(name="knowledge")
    print("旧知识库已删除")
except Exception:
    print("没有找到旧知识库，直接创建")


# 创建新的知识库
collection = client.get_or_create_collection(
    name="knowledge"
)


# 读取知识文件
file_path = Path("./Knowledge/agent_notes.txt")

text = file_path.read_text(
    encoding="utf-8"
)

# 使用chunking.py中的切片方法
chunks = split_text(text)

# 写入知识库
ids = []

for i, chunk in enumerate(chunks):
    ids.append(f"knowledge_{i}")

    print(f"\n===== 文档块 {i + 1} =====")
    print(chunk)


collection.add(
    documents=chunks,
    ids=ids
)


print("\n知识库创建完成！")
print(f"文档块数量：{len(chunks)}")