
UNIFORM = {
    1 : "black",
    2 : "blue",
    3 : "green",
}


def ai_2_worker(report:dict):
    # 이름 변경 및 숫자를 문자로 변경
    report['uniform'] = UNIFORM[report.pop('dress_kind')]

    return report
    