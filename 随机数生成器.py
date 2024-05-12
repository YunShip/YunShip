import random

def generate_random_number(start=1, end=1000):
    """
    生成一个指定范围内的随机整数。
    
    参数:
    start -- 随机数生成的起始值，默认为1。
    end -- 随机数生成的结束值，默认为100。
    
    返回:
    位于start和end之间的一个随机整数（包括start和end）。
    """
    return random.randint(start, end)

# 示例使用
if __name__ == "__main__":
    random_number = generate_random_number()
    print(f"生成的随机数是: {random_number}")