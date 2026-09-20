#20260917
#遇到(e + 8) * (e - 8)怎么用stack计算？
import collections
import re
class Polynomial:

    def __init__(self, count=None):
        # count: Dict[Tuple[str, ...], int]
        # key 是排序后的变量元组，如 ("a", "b")；value 是对应的系数
        self.count = collections.Counter(count)

    @staticmethod
    def from_term(symbol, val=1):
        # 构造单个变量或常数的多项式
        p = Polynomial()
        if symbol.isdigit() or (symbol.startswith("-") and symbol[1:].isdigit()):
            p.count[()] += int(symbol)
        else:
            p.count[(symbol,)] += val
        return p

    def __add__(self, other):
        res = Polynomial(self.count)
        res.count.update(other.count)
        return res

    def __sub__(self, other):
        res = Polynomial(self.count)
        for term, coeff in other.count.items():
            res.count[term] -= coeff
        return res

    def __mul__(self, other):
        res = Polynomial()
        for t1, c1 in self.count.items():
            for t2, c2 in other.count.items():
                # 合并变量并重新按字典序排序
                merged_term = tuple(sorted(t1 + t2))
                res.count[merged_term] += c1 * c2
        return res

    def to_list(self):
        # 过滤系数为 0 的项
        terms = [t for t in self.count if self.count[t] != 0]

        # 按照题目要求的规则排序：
        # 1. 自由变量数量（次数/Degree）从大到小 (-len(t))
        # 2. 字典序从小到大 (t)
        terms.sort(key=lambda t: (-len(t), t))

        res = []
        for t in terms:
            coeff = self.count[t]
            if not t:  # 常数项
                res.append(str(coeff))
            else:  # 变量项，格式为 "系数*var1*var2"
                res.append(f"{coeff}*" + "*".join(t))
        return res


class Solution:

    def basicCalculatorIV(
        self, expression: str, evalvars: list[str], evalints: list[int]
    ) -> list[str]:
        # 1. 构建变量替换映射
        eval_map = dict(zip(evalvars, evalints))

        # 2. 词法分析 (Tokenizer)
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

        #双栈法，一个栈用于存变量/数，一个用来存运算符
        operands = []  # 存储 Polynomial 对象
        operators = []  # 存储运算符 '+', '-', '*', '('

        # 运算符优先级
        priority = {"+": 1, "-": 1, "*": 2}

        def compute():
            op = operators.pop()
            right = operands.pop()
            left = operands.pop()
            if op == "+":
                operands.append(left + right)
            elif op == "-":
                operands.append(left - right)
            elif op == "*":
                operands.append(left * right)

        for token in tokens:
            if token.isdigit() or token.islower():
                # 如果是评估变量，直接替换为常数
                if token in eval_map:
                    token = str(eval_map[token])
                operands.append(Polynomial.from_term(token))

            elif token == "(":
                operators.append(token)

            elif token == ")":
                while operators and operators[-1] != "(":
                    compute()
                operators.pop()  # 弹出 '('

            elif token in priority:
                # 栈顶运算符优先级高于或等于当前运算符时，先计算栈顶
                while (
                    operators
                    and operators[-1] != "("
                    and priority[operators[-1]] >= priority[token]
                ):
                    compute()
                operators.append(token)

        # 清空剩余运算符
        while operators:
            compute()

        return operands[0].to_list() if operands else []