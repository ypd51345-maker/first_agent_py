import os
from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env
load_dotenv()

# 获取 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

# 创建客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


def ask_llm(prompt):

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


def reflection_llm(question, observation):
    """
    使用大模型判断 RAG 检索结果
    是否真正能够回答用户的问题。
    """

    if not observation:
        return False

    context = "\n".join(
        item["content"]
        for item in observation
        if isinstance(item, dict)
    )

    prompt = f"""
你现在是一个 Agent 的 Reflection 模块。

你的任务是判断：
“知识库检索结果是否能够回答用户的问题？”

用户问题：
{question}

知识库检索结果：
{context}

判断规则：

1. 如果检索结果能够直接回答问题，输出 YES。
2. 如果检索结果与问题无关，或者信息不足，输出 NO。
3. 只能输出 YES 或 NO。
4. 不要解释原因。

你的判断：
"""

    result = ask_llm(prompt)

    result = result.strip().upper()

    if "YES" in result:
        return True

    return False


def generate_answer(question, observation):

    if isinstance(observation[0], dict):

        context = "\n".join(
            [
                item["content"]
                for item in observation
            ]
        )

    else:

        context = "\n".join(
            observation
        )

    prompt = f"""
你是一个知识库问答助手。

请严格根据下面的知识库内容回答问题。

如果知识库没有足够的信息，请明确告诉用户。
不要自己编造知识库中没有的内容。

用户问题：
{question}

知识库内容：
{context}
"""

    answer = ask_llm(prompt)

    return answer