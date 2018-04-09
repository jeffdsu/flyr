

class Node():
    '''
    Node Class that have many child nodes
    '''

    def __init__(self, node_id):
        self.node_id = node_id
        self.child_nodes = []

    def add_child(self, node):
        '''
        Add a node to a another node's children
        :param node:
        :return:
        '''

        if not isinstance(node, Node):
            raise Exception("Can only add a node to a node's children.  Object given was a {}".format(type(node)))

        if self.node_id == node.node_id:
            raise Exception("cannot a child node that it is itself: id {}".format(self.node_id))

        if self.will_have_circular_dependency(node):
            raise Exception("cannot have a circular dependency")

        self.child_nodes.append(node)

    def will_have_circular_dependency(self, node):
        '''
        Check if there will circular dependency if adding a node to children
        :param node:
        :return:
        '''

        if has_path(node, self):
            return True
        return False

    def get_children(self):
        '''
        get all children for this node
        :return:
        '''
        return self.child_nodes


def has_path(node_start, node_end):
    '''
        check if there is a pthc from node start to node end
        :return:
    '''

    visited, stack = set(), [node_start]

    while stack:
        curent_node = stack.pop()
        if curent_node not in visited:
            visited.add(curent_node)
            stack.extend(list(filter(lambda x: x.node_id not in list(map(lambda node: node.node_id, visited)), curent_node.get_children())))


    if node_end.node_id in list(map(lambda node: node.node_id, visited)):
        return True

    return False




class Graph():
    '''
    Graph class
    '''

    def __init__(self):
        self.nodes = dict()

    def create_node(self, node_id):
        '''
        create node and place in current graph object
        :param node_id:
        :return:
        '''

        if node_id in self.nodes:
            raise Exception("cannot create node using same id: {}".format(node_id))

        self.nodes[node_id] = Node(node_id)

        return self.nodes[node_id]

    def get_node(self, node_id):
        '''
        get a specific node by id
        :param node_id:
        :return:
        '''
        return self.nodes[node_id] if node_id in self.nodes else None


    def print_graph(self):
        '''
        print the graph
        :return:
        '''
        for node_id, node in self.nodes.items():
            children = node.get_children()
            children_str = ', '.join(list(map(lambda x: str(x.node_id), children))) if len(children) > 0 else 'No Children'
            print("{}-> {}".format(node.node_id, children_str))


if __name__ == '__main__':

    graph = Graph()

    # node1 = graph.create_node(1)
    # node2 = graph.create_node(2)
    # node3 = graph.create_node(3)
    # node4 = graph.create_node(4)
    # node5 = graph.create_node(5)
    # node6 = graph.create_node(6)
    #
    # node1.add_child(node2)
    # node1.add_child(node3)

    #
    # node2.add_child(node5)
    #
    # node3.add_child(node6)
    #
    # node4.add_child(node3)
    # node4.add_child(node6)
    #
    # node5.add_child(node6)
    #
    # graph.print_graph()


    node1 = graph.create_node(1)
    node2 = graph.create_node(2)
    node3 = graph.create_node(3)

    # node1.add_child(3)

    node1.add_child(node2)

    node2.add_child(node3)

    node3.add_child(node1)









