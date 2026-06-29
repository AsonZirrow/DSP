

# models.py

class Node:
    """
    Represents a location.
    """

    def __init__(self, node_id, name):
        self.node_id = node_id
        self.name = name

    def __str__(self):
        return f"Node({self.node_id}, {self.name})"


class Connection:
    """
    Represents travel between two nodes.
    """

    def __init__(self, start_node, end_node, distance):
        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance

    def __str__(self):
        return (
            f"Connection("
            f"{self.start_node.name} -> "
            f"{self.end_node.name}, "
            f"{self.distance} km)"
        )


class Cost:
    """
    Represents calculated route cost.
    """

    def __init__(
        self,
        distance=0,
        time=0,
        score=0
    ):
        self.distance = distance
        self.time = time
        self.score = score

    def __str__(self):
        return (
            f"Cost("
            f"distance={self.distance}, "
            f"time={self.time}, "
            f"score={self.score})"
        )
    



class Route:
    """
    Represents a full route composed of a connection and its cost.
    """

    def __init__(self, connection, cost):
        self.connection = connection
        self.cost = cost

    def __str__(self):
        return (
            f"Route(\n"
            f"  {self.connection},\n"
            f"  {self.cost}\n"
            f")"
        )