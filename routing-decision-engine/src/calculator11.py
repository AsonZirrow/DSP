

class RouteCalculator:
    def compute_time(self, distance_km, speed_kmh):
        """
        PURE CALCULATOR:
        Only does math. No rules. No decisions.
        """

        if speed_kmh <= 0:
            return None

        return distance_km / speed_kmh

    def compute_distance_with_penalty(self, distance_km, multiplier):
        """
        Applies external multiplier (from config)
        """
        return distance_km * multiplier
















# class RouteCalculator:
#     def compute(self, distance_km, speed_kmh):
#         """
#         PURE CALCULATION ONLY
#         No routing logic. No decisions.
#         """

#         if speed_kmh <= 0:
#             return None

#         time_hours = distance_km / speed_kmh

#         return {
#             "distance_km": distance_km,
#             "speed_kmh": speed_kmh,
#             "time_hours": time_hours
#         }















# # from collections import deque

# # def find_path(graph, start, goal):
# #     queue = deque([[start]])
# #     visited = set()

# #     while queue:
# #         path = queue.popleft()
# #         node = path[-1]

# #         if node == goal:
# #             return path

# #         if node not in visited:
# #             visited.add(node)

# #             for neighbor in graph[node]:
# #                 new_path = path + [neighbor]
# #                 queue.append(new_path)

# #     return None


# # graph = {
# #     "A": ["B", "C"],
# #     "B": ["A", "D", "E"],
# #     "C": ["A", "E"],
# #     "D": ["B"],
# #     "E": ["B", "C"]
# # }

# # print(find_path(graph, "A", "D"))