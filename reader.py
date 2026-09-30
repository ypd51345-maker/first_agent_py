import requests
from bs4 import BeautifulSoup


def read_webpage(url):

    try:

        headers = {
            "User-Agent": 
            "Mozilla/5.0"
        }


        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        # 删除无用标签
        for tag in soup(
            ["script", "style"]
        ):
            tag.decompose()


        text = soup.get_text(
            "\n"
        )


        # 去掉空行
        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]


        content = "\n".join(lines)


        return content[:5000]


    except Exception as e:

        return "网页读取失败：" + str(e)