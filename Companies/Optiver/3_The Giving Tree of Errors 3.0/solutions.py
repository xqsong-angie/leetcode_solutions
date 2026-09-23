from collections import defaultdict
def solution(pairs:str):
    def isInvalidFormat(pairs):
        if "\n" in pairs:
            return True
        elif pairs.startswith(" ") or pairs.endswith(" "):
            return True
        else:
            pairs_list=pairs.split()
            #🔥这里可以check 能不能转成tuple?
            all_tuple=True
            for pair in pairs_list:
                #if pair not tuple:
                all_tuple=False
            if all_tuple==False:
                return True
        return False
    
    if isInvalidFormat(pairs):
        return "E1 Invalid Input Format"
    #这里假设validformat
    else:
        pairs_list=pairs.split()
        pair_set=set()
        for pair in pairs_list:
            if pair not in pair_set and (pair[1],pair[0]) not in pair_set:
                pair_set.add(pair)
            else:
                return "E2 Duplicate Pair"
            
        parents=defaultdict(list)
        children=defaultdict(list)
        for pair in pairs_list:
            parents[pair[0]].append(pair[1])
            children[pair[1]].append(pair[0])
        for _,v in parents.items():
            if len(v)>2:
                return "E3 Parent Has More than Two Children"
        for _,v in children.items():
            if len(v)>1:
                return "E4 Multiple Roots"
        
        nodes=set()
        for pair in pairs_list:
            if pair[0] not in nodes:
                nodes.add(pair[0])
            else:
                return "E5 Input Contains Cycle"
            if pair[1] not in nodes:
                nodes.add(pair[1])
            else:
                return "E5 Input Contains Cycle"
            
        res=["("]
        def dfs(node):
            for node,v in parents.items():
                res.append(node+"(")
                for n in v:
                    dfs(n)
        #🔥(A(B(D(E(G))))(C(F)))这里不知道怎么一边加括号还要一边排序
        dfs(parents.keys()[0])

        return ("").join(res)


from collections import defaultdict

def solution(input_str: str) -> str:
    # -------------------------------------------------------------
    # 1. 检测 E1: Invalid Input Format (纯字符串法，无需正则)
    # -------------------------------------------------------------
    # 检查换行、首尾空格
    if '\n' in input_str or input_str.startswith(' ') or input_str.endswith(' '):
        return "E1"
    
    # 按照单个空格切分
    tokens = input_str.split(' ')
    parsed_pairs = []

    for token in tokens:
        # 每个格式必须形如 (X,Y)，长度严格为 5
        if len(token) != 5:
            return "E1"
        if token[0] != '(' or token[2] != ',' or token[4] != ')':
            return "E1"
        
        parent, child = token[1], token[3]
        # 必须都是大写字母
        if not ('A' <= parent <= 'Z') or not ('A' <= child <= 'Z'):
            return "E1"
        
        parsed_pairs.append((parent, child))

    # -------------------------------------------------------------
    # 2. 检测 E2: Duplicate Pair (出现了完全相同的 Parent-Child 对)
    # -------------------------------------------------------------
    seen_pairs = set()
    for parent, child in parsed_pairs:
        if (parent, child) in seen_pairs:
            return "E2"
        seen_pairs.add((parent, child))

    # 建图：邻接表（为图中的每一个节点，建立一个列表（List））与度数统计
    parent_to_children = defaultdict(list)
    child_to_parents = defaultdict(list)
    all_nodes = set()

    for parent, child in parsed_pairs:
        parent_to_children[parent].append(child)
        child_to_parents[child].append(parent)
        all_nodes.add(parent)
        all_nodes.add(child)

    # -------------------------------------------------------------
    # 3. 检测 E3: Parent Has More than Two Children
    # -------------------------------------------------------------
    for parent, children in parent_to_children.items():
        if len(children) > 2:
            return "E3"

    # -------------------------------------------------------------
    # 4. 检测 E4: Multiple Roots (查找入度为 0 的节点)
    # -------------------------------------------------------------
    roots = []
    for node in all_nodes:
        if len(child_to_parents[node]) == 0:
            roots.append(node)

    # 没有入度为 0 的节点说明全图成环（E5）；有多个根节点说明不是单棵树（E4）
    if len(roots) > 1:
        return "E4"
    if len(roots) == 0:
        return "E5"


    root = roots[0]

    # -------------------------------------------------------------
    # 5. 检测 E5 (Cycle) & E4 (孤立节点/森林检测)
    # -------------------------------------------------------------
    visited = set()
    
    def has_cycle(node):
        visited.add(node)
        for child in parent_to_children[node]:
            # 如果访问到了递归栈/已访问集合中的节点，说明有环
            if child in visited:
                return True
            if has_cycle(child):
                return True
        return False

    if has_cycle(root):
        return "E5"

    # 如果根节点遍历完后，还有节点没访问到，说明图不连通（有独立森林/孤立环），报 E4
    if len(visited) != len(all_nodes):
        return "E4"

    # -------------------------------------------------------------
    # 6. 生成字典序最小的 S-Expression
    # -------------------------------------------------------------
    def get_s_expr(node):
        # 遍历前先对 child 按字母排序，确保字典序最小
        children = sorted(parent_to_children[node])
        
        res = f"({node}"
        for child in children:
            res += get_s_expr(child)
        res += ")"
        return res

    return get_s_expr(root)


# -------------------------------------------------------------
# 测试验证
# -------------------------------------------------------------
print(solution("(A,B) (B,D) (D,E) (A,C) (C,F) (E,G)"))  # 输出: (A(B(D(E(G))))(C(F)))
print(solution("(A,B) (A,C) (B,D) (D,C)"))              # 输出: E5