from pathlib import Path


def split_text(text):
    """
    按完整知识段落切分
    """

    paragraphs = text.split("\n\n")

    chunks = []

    current_chunk = ""

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue


        if current_chunk:

            current_chunk += "\n\n" + paragraph

        else:

            current_chunk = paragraph


        # 一个完整模块作为一个chunk
        if len(current_chunk) > 300:

            chunks.append(current_chunk)

            current_chunk = ""


    if current_chunk:

        chunks.append(current_chunk)


    return chunks



file_path = Path("knowledge/agent_notes.txt")


text = file_path.read_text(
    encoding="utf-8"
)


chunks = split_text(text)


print("原始文本长度：", len(text))

print("切分后的文档数量：", len(chunks))


for i, chunk in enumerate(chunks):

    print(f"\n===== 文档块 {i + 1} =====")

    print(chunk)