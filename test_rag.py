from rag import rag_search


while True:

    question = input(
        "\n请输入问题:"
    )


    if question=="exit":
        break


    result = rag_search(
        question
    )


    print("\n查询结果:")

    for r in result:
        print(
            r
        )