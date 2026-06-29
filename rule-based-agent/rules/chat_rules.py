from rule_types import Rule

def chat_rules():
    return [
        Rule(
            name="greeting_rule",
            match=lambda e: e["type"] == "chat" and any(
                w in e["payload"].lower()
                for w in ["hi", "hello", "hey"]
            ),
            score=lambda e: 0.9,
            action="respond_greeting"
        )
    ]







# from rule_types import Rule

# def chat_rules():
#     return [
#         Rule(
#             name="greeting_rule",
#             match=lambda e: e["type"] == "chat" and e["payload"] in ["hi", "hello", "hey"],
#             score=lambda e: 0.9,
#             action="respond_greeting"
#         )
#     ]