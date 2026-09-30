
import chromadb
import re


# 连接 Chroma 数据库
client = chromadb.PersistentClient(path="./database")

collection = client.get_collection(name="knowledge")


# 通用词
STOP_WORDS = {
    "AI",
    "Agent",
    "什么",
    "哪些",
    "通常",
    "核心",
    "如何",
    "怎么",
    "介绍",
    "一下",
    "有",
    "是",

    "架构",
    "相关",
    "概念",
    "内容",
    "主要",
    "定义",
    }





def extract_keywords(text):
    """
    提取关键词
    """

    english_words = re.findall(
        r"[a-zA-Z0-9]+",
        text
    )


    chinese_text = "".join(
        re.findall(
            r"[\u4e00-\u9fff]",
            text
        )
    )


    chinese_words = []


    for i in range(len(chinese_text)-1):

        word = chinese_text[i:i+2]

        if word not in STOP_WORDS:

            chinese_words.append(word)



    keywords = english_words + chinese_words


    keywords = [
        word
        for word in keywords
        if word.lower()
        not in {
            item.lower()
            for item in STOP_WORDS
        }
    ]


    return list(set(keywords))


def has_keyword_relevance(question, document):
    question_lower = question.lower()
    document_lower = document.lower()

    important_topics = {
        "agent": [
            "agent",
            "智能体",
            "自主",
            "任务",
            "工具调用"
        ],

        "rag": [
            "rag",
            "检索增强",
            "知识库",
            "向量"
        ],

        "react": [
            "react",
            "推理",
            "行动",
            "思考"
        ],

        "reflection": [
            "reflection",
            "反思",
            "评价"
        ],

        "memory": [
            "memory",
            "记忆",
            "历史"
        ],

        "tool": [
            "tool",
            "工具",
            "调用"
        ],

        "planner": [
            "planner",
            "规划",
            "计划"
        ],

        "transformer": [
            "transformer",
            "attention",
            "注意力机制",
            "encoder",
            "decoder"
        ]
    }

    # 第一部分：检查重要主题
    for topic, related_words in important_topics.items():

        if topic in question_lower:

            for word in related_words:

                if word.lower() in document_lower:

                    return True

    # 第二部分：提取关键词
    keywords = extract_keywords(question)

    matched_keywords = []

    for keyword in keywords:

        if keyword.lower() in document_lower:

            matched_keywords.append(keyword)

    if matched_keywords:

        print(
            "匹配关键词：",
            matched_keywords
        )

        return True

    return False







def rag_search(question):

    """
    从知识库中检索
    """

    print(
        "当前检索数量设置为：3"
    )


    results = collection.query(

        query_texts=[question],

        n_results=3

    )


    print(
        "完整距离:",
        results["distances"]
    )



    documents = results["documents"][0]

    distances = results["distances"][0]



    final_results = []



    for i, (document, distance) in enumerate(
        zip(documents, distances)
    ):


        print(
            f"\n第 {i+1} 个检索结果"
        )

        print(
            f"检索距离：{distance}"
        )



        # 距离过滤

        if distance >= 999:

            print(
                "距离过大，跳过该结果"
            )

            continue




        # 关键词检查

        if not has_keyword_relevance(
            question,
            document
        ):


            print(
                "关键词不匹配，但保留向量结果"
            )



        else:


            print(
                "关键词匹配成功，保留该结果"
            )



        final_results.append({

            "content": document,

            "score": distance

        })




    final_results.sort(

        key=lambda item:item["score"]

    )



    if not final_results:

        return [{

            "content":
            "知识库中没有找到相关信息",

            "score":999

        }]



    return final_results