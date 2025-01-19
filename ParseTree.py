import operator

class Node:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
    
    def getRootVal(self):
        return self.value

    def getLeftChild(self):
        return self.leftchild
    
    def getRightChild(self):
        return self.rightchild
    
    def setLeftChild(self, leftchild):
        self.leftchild = leftchild    
    def setRightChild(self, rightchild):
        self.rightchild =rightchild

def parse(expression):
    return parse_expression(expression.split())

def parse_expression(tokens): #                     1 + root =>     + left 1 right                                               
    if len(tokens) == 1:
        return tokens[0] if isinstance(tokens[0], Node) else Node(tokens[0]) # 1 + node

    # parse all paranthesised blocks as subtrees  then return the root of the subtree
    while '(' in tokens:
        open_idx = tokens.index('(')
        close_idx = find_matching_parenthesis(tokens, open_idx)   
        sub_tree = parse_expression(tokens[open_idx + 1:close_idx])
        tokens = tokens[:open_idx] + [sub_tree] + tokens[close_idx + 1:]

    op_idx = find_lowest_precedence_operator(tokens)
    if(op_idx == -1):
        return tokens[0] if isinstance(tokens[0], Node) else Node(tokens[0])
    
    root = Node(tokens[op_idx])
    root.setLeftChild(parse_expression(tokens[:op_idx]))
    root.setRightChild(parse_expression(tokens[op_idx + 1:]))

    return root

def find_matching_parenthesis(tokens, open_idx): #(())
    stack = 1
    for i in range(open_idx + 1, len(tokens)):
        if tokens[i] == '(':
            stack += 1
        elif tokens[i] == ')':
            stack -= 1
        if stack == 0:
            return i
    raise ValueError("Mismatched parentheses")

def find_lowest_precedence_operator(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    lowest = float('inf')
    index = -1
    for i, token in enumerate(tokens):        # 1/3/2  example => will find the second / operator and return the index
        if isinstance(token, Node):
            continue
        if token in precedence and precedence[token] <= lowest:
            lowest = precedence[token]
            index = i
    return index

def evaluate(parseTree):    # + 1 root
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(float(evaluate(leftC)), float(evaluate(rightC)))   
    else:
        root_val = parseTree.getRootVal()
        return float(root_val)

print(evaluate(parse("1 + 2 * 3"))) # 7.0
print(evaluate(parse("1 + 2 * 3 + 4"))) # 11.0
print(evaluate(parse("1 + 2 * 3 + 4 * 5"))) # 27.0
print(evaluate(parse("1 + 2 * 3 + 4 * 5 + 6"))) # 33.0