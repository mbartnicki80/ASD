class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, val):
        if self.val==None:
            self.val = val
            return
        while self.next!=None:
            self = self.next
        self.next = Node(val)

    def __str__(self):
        res = ""
        while self!=None:
            res += str(self.val) + " "
            self = self.next
        return res

def merge(list1, list2):
    if list1==None:
        return list2
    if list2==None:
        return list1
    
    if list1.val<list2.val:
        list1.next = merge(list1.next, list2)
        return list1
    else:
        list2.next = merge(list1, list2.next)
        return list2

def msort(list):
    
    return merge(list1, list2)

if __name__=="__main__":

    list1 = Node()
    list1.append(5); list1.append(5); list1.append(6)
    list2 = Node()
    list2.append(3); list2.append(6); list2.append(7)
    print(merge(list1, list2))
