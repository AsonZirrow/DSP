

# main.py

from calculator11 import RouteCalculator
from config import RouteConfig
from models import Node, Connection, Cost, Route


def get_input(prompt, default=None, cast=float):
    value = input(f"{prompt} [{default}]: ")
    return cast(value) if value else default


def main():

    # 1. Initialize core components
    calc = RouteCalculator()
    config = RouteConfig()

    print("\n=== ROUTE CALCULATOR ===\n")

    # 2. Get user inputs
    raw_distance = get_input("Enter distance (km)", 2)
    mode = input("Enter mode (horizontal/vertical/etc.) [horizontal]: ").strip() or "horizontal"
    speed = get_input("Speed (km/h)", config.speed_kmh)

    # 3. Validate / prepare configuration rules
    multiplier = config.get_distance_multiplier(mode)

    # 4. Apply distance adjustments
    adjusted_distance = calc.compute_distance_with_penalty(
        raw_distance,
        multiplier
    )

    # 5. Compute travel time
    time_hours = calc.compute_time(
        adjusted_distance,
        speed
    )

    # 6. Create model objects
    start_node = Node(node_id=1, name="Start")
    end_node = Node(node_id=2, name="End")

    connection = Connection(
        start_node=start_node,
        end_node=end_node,
        distance=adjusted_distance
    )

    cost = Cost(
        distance=adjusted_distance,
        time=time_hours,
        score=(adjusted_distance / speed) if speed else 0
    )

    route = Route(connection, cost)  # ✅ CORRECT PLACE

    # 7. Output raw computation results
    print("\n=== RESULT ===")
    print("Raw Distance:", raw_distance)
    print("Mode:", mode)
    print("Adjusted Distance:", adjusted_distance)
    print("Speed:", speed)
    print("Time (hours):", time_hours)

    # 8. Output structured model objects
    print("\n=== MODEL DEBUG OUTPUT ===")
    print(route)


if __name__ == "__main__":
    main()
























# # main.py

# from calculator11 import RouteCalculator
# from config import RouteConfig
# from models import Node, Connection, Cost, Route
# # from models import Node, Connection, Cost

# route = Route(connection, cost)


# def get_input(prompt, default=None, cast=float):
#     value = input(f"{prompt} [{default}]: ")
#     return cast(value) if value else default


# def main():

#     # 1. Initialize core components
#     calc = RouteCalculator()
#     config = RouteConfig()

#     print("\n=== ROUTE CALCULATOR ===\n")

#     # 2. Get user inputs
#     raw_distance = get_input("Enter distance (km)", 2)
#     mode = input("Enter mode (horizontal/vertical/etc.) [horizontal]: ").strip() or "horizontal"
#     speed = get_input("Speed (km/h)", config.speed_kmh)

#     # 3. Validate / prepare configuration rules
#     multiplier = config.get_distance_multiplier(mode)

#     # 4. Apply distance adjustments (penalties / modifiers)
#     adjusted_distance = calc.compute_distance_with_penalty(
#         raw_distance,
#         multiplier
#     )

#     # 5. Compute travel time
#     time_hours = calc.compute_time(
#         adjusted_distance,
#         speed
#     )

#     # 6. Create model objects (Node / Connection / Cost)
#     start_node = Node(node_id=1, name="Start")
#     end_node = Node(node_id=2, name="End")

#     connection = Connection(
#         start_node=start_node,
#         end_node=end_node,
#         distance=adjusted_distance
#     )

#     cost = Cost(
#         distance=adjusted_distance,
#         time=time_hours,
#         score=(adjusted_distance / speed) if speed else 0
#     )

#     # 7. Output raw computation results
#     print("\n=== RESULT ===")
#     print("Raw Distance:", raw_distance)
#     print("Mode:", mode)
#     print("Adjusted Distance:", adjusted_distance)
#     print("Speed:", speed)
#     print("Time (hours):", time_hours)

#     # 8. Output structured model objects (debug-friendly)
#     print("\n=== MODEL DEBUG OUTPUT ===")
#     print(route)
#     # print(connection)
#     # print(cost)

#     # 9. Future extension area (routing logic, graphs, paths, etc.)
#     # Example: add multiple nodes, pathfinding, route scoring, etc.


# if __name__ == "__main__":
#     main()













# # from calculator11 import RouteCalculator
# # from config import RouteConfig
# # from models import node, Connection, Cost


# # def get_input(prompt, default=None, cast=float):
# #     value = input(f"{prompt} [{default}]: ")
# #     return cast(value) if value else default


# # def main():
# #     calc = RouteCalculator()
# #     config = RouteConfig()

# #     print("\n=== ROUTE CALCULATOR ===\n")

# #     # User inputs
# #     raw_distance = get_input("Enter distance (km)", 2)
# #     mode = input(...).strip() or "horizontal"
# #     speed = get_input("Speed (km/h)", config.speed_kmh)

# #     # Step 1: apply config rules
# #     multiplier = config.get_distance_multiplier(mode)

# #     adjusted_distance = calc.compute_distance_with_penalty(
# #         raw_distance,
# #         multiplier
# #     )

# #     # Step 2: compute result
# #     time_hours = calc.compute_time(
# #         adjusted_distance,
# #         speed
# #     )

# #     # Output
# #     print("\n=== RESULT ===")
# #     print("Raw Distance:", raw_distance)
# #     print("Mode:", mode)
# #     print("Adjusted Distance:", adjusted_distance)
# #     print("Speed:", speed)
# #     print("Time (hours):", time_hours)


# # if __name__ == "__main__":
# #     main()