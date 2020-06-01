import json
import requests
import time
import tqdm


if __name__ == "__main__":
    data = []
    for quiz_id in tqdm.tqdm(range(1, 46)):
        data = {
            "action": "wp_pro_quiz_admin_ajax",
            "func": "quizLoadData",
            "data[quizId]": quiz_id,
        }
        resp = requests.post(
            "https://lifeintheuktests.co.uk/wp-admin/admin-ajax.php", data=data
        )
        out = json.dumps(resp.json())
        print(out)
        time.sleep(1)
