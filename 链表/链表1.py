# 节点类：就是单颗珠子
class Node:
        #class:类，一种可以批量制造的模板
        #Node:节点，链表中最小单元，存着数据和下一节点的线索
    def __init__(self, data):   
        #init：初始化方法，新建时自动执行的函数
        # self：当前这个珠子自己
        # data：珠子存的数据
        self.data = data
        # next：记录下一颗珠子是谁，默认是空None
        self.next = None

    # getter 获取数据：读出珠子里面存的值
    def get_data(self):
        return self.data
    # setter 设置数据：修改珠子里面的值
    def set_data(self, new_data):
        self.data = new_data

    # getter 获取下一个珠子
    def get_next(self):
        return self.next
    # setter 设置下一个珠子（改连线）
    def set_next(self, new_next):
        self.next = new_next


# 链表类：一整串珠子
class LinkedList: 
        #LinkedList:链表
    def __init__(self):
        # head 头指针：链表的第一颗珠子，刚创建链表时是空
        self.head = None

    # 判断链表是不是空的
    def is_empty(self):
        return self.head is None

    # 增：在链表最前面加珠子
    def add(self, data):   #add：增加在链表的最前面
        new_node = Node(data)       # 造一颗新珠子
        new_node.set_next(self.head)# 新珠子连上原来第一颗珠子
        self.head = new_node        # 把头换成这颗新珠子

    # 增：在链表最后面加珠子
    def append(self, data):   #append：增加在链表的最后面
        new_node = Node(data)
        if self.is_empty():         # 如果链表是空，新珠子直接当头
            self.head = new_node
            return
        current = self.head         # current 当前正在查看的珠子，从头开始
        while current.get_next() is not None: # 当前珠子后面还有珠子，就继续往后走
            current = current.get_next()
        current.set_next(new_node)  # 走到最后一颗，接上新珠子

    # 访问：根据下标index拿到对应的珠子 index:索引
    def get_at_index(self, index):
        if self.is_empty():
            return None
        current = self.head
        count = 0
        while current and count < index:
            current = current.get_next()
            count += 1
        return current

    # 改：修改指定下标珠子的数据
    def modify_at_index(self, index, new_data):
        target = self.get_at_index(index)
        if target:
            target.set_data(new_data)
            return True
        return False

    # 删：删除指定下标的节点（一次只删除一个）
    def remove_at_index(self, index):
        if self.is_empty():
            return False
        if index == 0:              # 如果要删第一个节点
            self.head = self.head.get_next()
            return True        #第一个节点删除后其余的顺位往上排
        prev = self.get_at_index(index - 1) # prev:前一个值  
        if not prev or not prev.get_next():
            return False
        prev.set_next(prev.get_next().get_next()) 
        # 前一颗直接跳过目标，连后面的节点
        return True

    
    # 增：在指定下标位置插入节点（中间插入）
    def insert_at_index(self, index, data):
        # 第一步：如果链表是空的，或者要插在最前面(index=0)，直接复用之前写好的add
        if self.is_empty() or index == 0:
            self.add(data)
            return True
        
        # index-1：要插入位置的【前一个节点的下标】
        # prev = previous 前节点
        prev = self.get_at_index(index - 1)
        # 情况：找不到这个前节点 → 输入的index太大，超出链表范围，插入失败
        if not prev:
            return False
        
        # 1. 造一颗新珠子（新节点）
        new_node = Node(data)
        # 2. 新珠子的连线，先接上【原来prev后面的那个节点】
        new_node.set_next(prev.get_next())
        # 3. 前节点prev的连线，改成连上这个new_node
        prev.set_next(new_node)
        # 插入成功
        return True


    # 辅助：打印整条链表，方便我们看结果
    def print_list(self):
        res = []
        current = self.head
        while current:
            res.append(str(current.get_data()))
            current = current.get_next()
        print(" -> ".join(res))


