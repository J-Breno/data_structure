import json
from dateutil import parser

with open('file.json', 'r') as f:
    data = json.load(f)

def parse_timestamp(timestamp):
    return parser.isoparse(timestamp)

for course in data:
    print(f"Curso: {course['title']}")

    for lesson in course['lessons']:
        print(f"      Aula {lesson['id']}: {lesson['title']}")
        print(f"          Media: {lesson['media']}")
        print(f"                Timestamp: {parse_timestamp(lesson['timestamp'])}")
    print()