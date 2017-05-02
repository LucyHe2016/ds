
# string-based patricia tree

def lcp(str1, str2):
    i = 0
    while i<len(str1) and i<len(str2) and str1[i] == str2[i]:
        i += 1
    return (str1[:i], str1[i:], str2[i:])

def branch(key1, tree1, key2, tree2):
    if key1 == "":
        tree1.children[key2] = tree2
        return tree1
    t = PatriciaNode()
    t.children[key1] = tree1
    t.children[key2] = tree2
    return t

class PatriciaNode:
    
    def __init__(self, value = 0):
        self.value = 0
        self.children = {}

class PatriciaTree:

    def __init__(self, root = None):
        self.root = root

    def insert(self, key, value = 1):
        if self.root is None:
            self.root = PatriciaNode()

        node = self.root
        while True:
            match = False
            for k, tr in node.children.items():
                if key == k:
                    tr.value = value  # update value
                    return
                (prefix, k1, k2) = lcp(key, k)
                if prefix != '':
                    match = True
                    if k2 == '': # k is sub-string of key
                        node = tr
                        key = k1
                        break
                    else:
                        node.children[prefix] = branch(k1, PatriciaNode(value), k2, tr)
                        del node.children[k]
                        return
            if not match:
                node.children[key] = PatriciaNode(value)

    def lookup(self, key):
        node = self.root
        if node is None:
            return False
        while True:
            match = False
            for k, tr in node.children.items():
                if key == k:
                    return True
                index = key.find(k)
                if index == 0:
                    match = True
                    node = tr
                    key = key[len(k):]
                    break
            if not match:
                return False

    def lookup_prefix(self, prefix):
        node = self.root
        retlist = []
        if node is None:
            return retlist
        key = prefix
        while True:
            match = False
            for k, tr in node.children.items():
                if k.startswith(key):
                    if tr.value == 1:
                        retlist += [prefix]
                    rest = getall(tr)
                    retlist.extend([prefix+s for s in rest])
                    return retlist
                index = key.find(k)
                if index == 0:
                    match = True
                    node = tr
                    key = key[len(k):]
                    break
            if not match:
                return retlist

def getall(tr):
    stack = []
    stack.append(("", tr))
    retlist = []
    while len(stack) > 0:
        (prefix, pnode) = stack.pop(0)
        if len(pnode.children) == 0:
            retlist += [prefix]
        else:
            for k, ctr in pnode.children.items():
                stack.append((prefix+k, ctr))

    return retlist 

if __name__ == '__main__':
    t = PatriciaTree()
    for cmdstr in ['macerror', 'macbinary', 'm4', 'sample', 'sampleproc', 'mine']:
        t.insert(cmdstr)
    print(t.lookup_prefix('mac'))
    print(t.lookup_prefix('m'))
    print(t.lookup_prefix('sample'))
