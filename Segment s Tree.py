class MaOperation:

    def operation(self, lval, rval):
        return max(lval, rval)

    def defaultValue(self):
        return float('inf')


class Segment_Tree:
    class node:

        def __init__(self,si,ei):
            self.data = 0
            self.right = None
            self.left = None

            self.si = si
            self.ei = ei

        def __repr__(self):
            return "[" + str(self.si) + ":" + str(self.ei) + "]" + ":" + "[" + str(self.data) + "]"

    def __init__(self, arr):

        self.size = 0
        opt = MaOperation()
        self.root = self.construct(arr, 0, len(arr) - 1, opt)

    def construct(self, arr, si, ei, opt):

        if si == ei:
            nn = self.node(si,ei)
            nn.data = arr[si]
            # self.si = si
            # self.ei = ei
            self.size += 1

            return nn

        mid = (si + ei) // 2

        nn = self.node(si,ei)
        # nn.si = si
        # nn.ei = ei
        self.size += 1

        nn.left = self.construct(arr, si, mid,opt)
        nn.right = self.construct(arr, mid + 1, ei,opt)

        nn.data = opt.operation(nn.left.data, nn.right.data)
        return nn

    def display(self):

        self.displayy(self.root)

    def displayy(self, node):

        if node is None:
            return

        if node.left != None and node.right != None:

            string = str(node.left) + "=>" + str(node.data) + "<=" + str(node.right)
            print(string)
        else:
            string = ".=>" + str(node) + "<= ."
            print(string)

        self.displayy(node.left)
        self.displayy(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
st = Segment_Tree(arr)
st.display()
