import csv
from bs4 import BeautifulSoup
import json
import sys
import tqdm


if __name__ == "__main__":
    writer = csv.writer(sys.stdout)
    lines = sys.stdin.readlines()
    for line in tqdm.tqdm(lines):
        data = json.loads(line)
        soup = BeautifulSoup(data["content"], "html.parser")
        divs = soup.find_all("div", class_="theorypass_question")

        for div in divs:
            qid = div.ul["data-question_id"]
            correct = data["json"][qid]["correct"]
            question = div.find("div", class_="theorypass_question_text").text.strip()
            answers = []
            for sub in div.find_all("div", class_="question_text_area"):
                answers.append(sub.text.strip())

            front = question + "\n\n" + "\n".join(answers)
            back = "\n".join(answer for c, answer in zip(correct, answers) if c)
            writer.writerow([front, back])
