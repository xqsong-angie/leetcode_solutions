def solution(data: list[str]) -> str:
    # 直接转 int 比较数值大小
    return max(data, key=lambda x: int(x.split(',')[1])).split(',')[0]