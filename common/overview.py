import os

import pandas as pd
import requests
from aocd.models import default_user


class Member:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.local_score = data['local_score']
        self.global_score = data['global_score']
        # add stars
        self.stars = 0
        self.progress = {}
        for day, day_data in data['completion_day_level'].items():
            self.progress[day] = 0
            for _, _ in day_data.items():
                self.progress[day] += 1
                self.stars += 1

    def progress_str(self):
        return "".join([str(self.progress.get(str(x), '0')) for x in range(1, 26)])

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "local_score": self.local_score,
            "global_score": self.global_score,
            "stars": self.stars,
            "progress": self.progress_str()
        }


def get_personal_overview():
    user = default_user()
    stats = user.get_stats(2024)
    results = []

    class Part:
        def __init__(self, data):
            self.time = data['time'].total_seconds()
            self.rank = data['rank']
            self.score = data['score']

    for date, data in stats.items():
        for key, value in data.items():
            results.append({'day': date,
                            'part': key.upper(),
                            'time': value['time'],
                            'rank': value['rank'],
                            'score': value['score']
                            })

    # create dataframe from results
    df = pd.DataFrame(results)

    display(df)


def print_leaderboard(id):
    url = f"https://adventofcode.com/2024/leaderboard/private/view/{id}.json"
    # AOC_SESSION variable from environment
    session_id = os.getenv("AOC_SESSION")

    response = requests.get(url, cookies={"session": session_id})
    data = response.json()
    members = data['members']

    board = []

    for member_id, member_data in members.items():
        member = Member(member_data)
        board.append(member)

    # sort board by local score
    board.sort(key=lambda x: x.local_score, reverse=True)
    # remove people with 0 points
    board = [x for x in board if x.local_score > 0]
    # convert to dict
    board = [x.to_dict() for x in board]

    # convert to dataframe
    df = pd.DataFrame(board)
    display(df[['name', 'local_score', 'stars', 'progress']])
