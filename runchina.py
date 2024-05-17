#!/usr/bin/env python

import argparse
import requests

raceDistances = {
    "10K": 10000.0,
    "Half Marathon": 21097.5,
    "Marathon": 42195.0,
}

standardLevels = ["未达标", "大众精英级", "大众一级", "大众二级"]

parser = argparse.ArgumentParser(description="Show running race results in runchina.")
parser.add_argument("--cardNo", help="ID card number", required=True)
parser.add_argument("--userName", help="Name on ID card", required=True)
parser.add_argument("--timesToken", help="Token to query results", required=True)
args = parser.parse_args()

def query_results():
    url = "https://api-changzheng.chinaath.com/changzheng-score-center-api/api/app/score/offline/mineRaceScoreWithToken"
    data = {
        "cardNo": args.cardNo,
        "userName": args.userName,
        "timesToken": args.timesToken,
        "competitionName":"",
        "offlineScoreType":None,
        "pageNo":1,
        "pageQueryFlag":False,
        "pageSize":9999
    }
    response = requests.post(url, json=data)
    if response.ok:
        resp = response.json()
        if resp["success"] and resp["data"] is not None:
            return resp["data"]["results"]
        else:
            print("Failed to query results: " + resp["msg"])
    else:
        print("Failed to query results: " + response.text)
    return []

def print_results(results):
    if not results:
        return
    for raceItem in raceDistances:
        has_result = False
        for result in results:
            if result["raceDistance"] == raceDistances[raceItem]:
                if not has_result:
                    has_result = True
                    print(f"\n# {raceItem}\n")
                    print("|Race|Date|Race Level|Number|Chip Time|Gun Time|Time Level|Split Time|")
                    print("|---|---|---|---|---|---|---|---|")
                print(f"|{result['raceName']}|{result['scoreTime']}|{result['competitionType']}|{result['entryNumber']}|{result['scoreChip']}|{result['scoreShot']}|{standardLevels[result['standardLevel']+1]}|{'<br>'.join([x['paragraphName'] + '<br>' + x['paragraphScore'] for x in result['paragraphScoreList']])}|")

if __name__ == "__main__":
    print("[Home Page](https://laqieer.github.io/running.html){:btn} [Running Page](https://laqieer.github.io/running_page){:btn}")
    print_results(query_results())
