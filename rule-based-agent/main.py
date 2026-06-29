

from engine import Engine
from classifier import classify

from rules.chat_rules import chat_rules
from rules.command_rules import command_rules
from rules.system_rules import system_rules
from rules.security_rules import security_rules
from display import print_decision



engine = Engine([
    chat_rules,
    command_rules,
    system_rules,
    security_rules
])

print("\n🧠 Rule Engine Live (type 'exit' to quit)\n")

while True:
    user_input = input(">> ")

    if user_input.lower() == "exit":
        break

    event = classify(user_input)
    

    result = engine.process(event)

    print(result)
    print_decision(result)


    print("\n[DEBUG EVENT]")
    print(event)
    print("\n")



















# from engine import Engine

# from classifier import build_event

# from rules.chat_rules import chat_rules
# from rules.command_rules import command_rules
# from rules.system_rules import system_rules
# from rules.security_rules import security_rules


# engine = Engine([
#     chat_rules,
#     command_rules,
#     system_rules,
#     security_rules
# ])

# print("\n🧠 Rule Engine Live (type 'exit' to quit)\n")

# while True:

#     user_input = input(">> ")

#     if user_input.lower() == "exit":
#         break

#     event = build_event(user_input)

#     result = engine.process(event)

#     print(result)

















# # from engine import Engine
# # from event import Event

# # from rules.chat_rules import chat_rules
# # from rules.command_rules import command_rules
# # from rules.system_rules import system_rules
# # from rules.security_rules import security_rules


# # def classify_input(text: str) -> str:
# #     text = text.lower().strip()

# #     # VERY simple deterministic classification
# #     if text in ["hi", "hello", "hey", "how are you"]:
# #         return "chat"

# #     if text.startswith("run") or text.startswith("execute"):
# #         return "command"

# #     if "cpu" in text or "system" in text:
# #         return "system"

# #     if "delete" in text:
# #         return "command"

# #     return "chat"  # default fallback


# # engine = Engine([
# #     chat_rules,
# #     command_rules,
# #     system_rules,
# #     security_rules
# # ])


# # print("\n🧠 Rule Engine Live (type 'exit' to quit)\n")

# # while True:
# #     user_input = input(">> ")

# #     if user_input.lower() == "exit":
# #         break

# #     event_type = classify_input(user_input)

# #     event = Event(
# #         type=event_type,
# #         payload=user_input,
# #         context={}
# #     )

# #     result = engine.process(event)

# #     print(result)













# # # from engine import Engine
# # # from event import Event

# # # from rules.chat_rules import chat_rules
# # # from rules.command_rules import command_rules
# # # from rules.system_rules import system_rules
# # # from rules.security_rules import security_rules

# # # engine = Engine([
# # #     chat_rules,
# # #     command_rules,
# # #     system_rules,
# # #     security_rules
# # # ])

# # # tests = [
# # #     Event("chat", "hi", {}),
# # #     Event("command", "run scan", {}),
# # #     Event("system", "cpu overload", {}),
# # #     Event("command", "delete all files", {})
# # # ]

# # # for t in tests:
# # #     result = engine.process(t)
# # #     print("\nINPUT:", t)
# # #     print("OUTPUT:", result)