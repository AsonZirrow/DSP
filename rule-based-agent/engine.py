

from actions import ACTIONS
from decision_record import DecisionRecord


class Engine:
    def __init__(self, rule_packs, trace=False):
        self.trace = trace
        self.rules = []

        # Flatten rule packs
        for pack in rule_packs:
            self.rules.extend(pack())

    # -------------------------
    # TRACE LOGGER
    # -------------------------
    def log(self, trace_list, message):
        if self.trace:
            trace_list.append(message)

    # -------------------------
    # MAIN PROCESS
    # -------------------------
    def process(self, event):

        event_dict = {
            "type": event.type,
            "intent": getattr(event, "intent", None),
            "payload": event.payload,
            "context": event.context
        }

        trace = []
        evaluated_rules = []

        self.log(trace, "🧠 ENGINE TRACE START")
        self.log(trace, f"Event: type={event.type}, intent={getattr(event, 'intent', None)}")

        # STEP 1: deterministic ordering
        rules = sorted(self.rules, key=lambda r: r.name)

        candidates = []

        # STEP 2: rule evaluation
        for rule in rules:

            matched = rule.match(event_dict)
            score = rule.score(event_dict)

            rule_data = {
                "name": rule.name,
                "matched": matched,
                "score": score,
                "action": rule.action
            }

            evaluated_rules.append(rule_data)

            if matched:
                weight = getattr(rule, "weight", 1.0)
                final_score = score * weight

                candidates.append({
                    "rule": rule,
                    "score": final_score,
                    "base_score": score,
                    "weight": weight,
                    "action": rule.action
                })

                self.log(trace, f"✔ MATCH: {rule.name} | score={score} | weight={weight}")
            else:
                self.log(trace, f"✘ NO MATCH: {rule.name}")

        # STEP 3: no match fallback
        if not candidates:
            self.log(trace, "❌ No matching rules found")

            return DecisionRecord(
                event=event,
                evaluated_rules=evaluated_rules,
                winner_rule="none",
                winner_score=0.0,
                output=None,
                trace=trace,
                status="no_match"
            )

        # STEP 4: conflict resolution (winner selection)
        best = max(candidates, key=lambda x: x["score"])

        self.log(trace, "")
        self.log(trace, "🏆 WINNER SELECTED")
        self.log(trace, f"Rule: {best['rule'].name}")
        self.log(trace, f"Score: {best['score']} (base={best['base_score']}, weight={best['weight']})")

        # STEP 5: execute action
        result = ACTIONS[best["action"]](event)

        # STEP 6: side effects tracking (future expansion)
        side_effects = [
            c["rule"].name for c in candidates
            if c["rule"].name != best["rule"].name
        ]

        # STEP 7: build DecisionRecord (FINAL OUTPUT)
        return DecisionRecord(
            event=event,
            evaluated_rules=evaluated_rules,
            winner_rule=best["rule"].name,
            winner_score=best["score"],
            output=result,
            trace=trace,
            metadata={
                "side_effects": side_effects if side_effects else None
            },
            status="executed"
        )



















# from actions import ACTIONS


# class Engine:
#     def __init__(self, rule_packs, trace=False):
#         self.trace = trace
#         self.rules = []

#         # Flatten rule packs
#         for pack in rule_packs:
#             self.rules.extend(pack())

#     # -------------------------
#     # TRACE LOGGER
#     # -------------------------
#     def log(self, message):
#         if self.trace:
#             print(message)

#     # -------------------------
#     # PRE-FILTER (SCALING)
#     # -------------------------
#     def filter_rules(self, event):
#         """
#         Rule pre-filtering:
#         Only evaluate relevant rules based on event type.
#         """
#         return [r for r in self.rules if r.match(event)]

#     # -------------------------
#     # MAIN PROCESS
#     # -------------------------
#     def process(self, event):

#         event_dict = {
#             "type": event.type,
#             "intent": getattr(event, "intent", None),
#             "payload": event.payload,
#             "context": event.context
#         }

#         self.log("\n🧠 ENGINE TRACE START")
#         self.log(f"Event type: {event.type}, intent: {getattr(event, 'intent', None)}")

#         # STEP 1: deterministic ordering
#         rules = sorted(self.rules, key=lambda r: r.name)

#         # STEP 2: pre-filter (scaling optimization)
#         candidates = []

#         for rule in rules:

#             matched = rule.match(event_dict)

#             if matched:
#                 explanation = f"{rule.name} matched event"
#                 score = rule.score(event_dict)

#                 # RULE WEIGHT SUPPORT (structure improvement)
#                 weight = getattr(rule, "weight", 1.0)
#                 final_score = score * weight

#                 candidates.append({
#                     "rule": rule,
#                     "score": final_score,
#                     "base_score": score,
#                     "weight": weight,
#                     "explanation": explanation,
#                     "action": rule.action
#                 })

#                 self.log(f"✔ MATCH: {rule.name} | score={score} | weight={weight}")

#             else:
#                 self.log(f"✘ NO MATCH: {rule.name}")

#         # STEP 3: no match fallback
#         if not candidates:
#             self.log("❌ No matching rules found")
#             return {
#                 "status": "no_match",
#                 "output": None
#             }

#         # STEP 4: conflict resolution (highest score wins)
#         best = max(candidates, key=lambda x: x["score"])

#         self.log("\n🏆 WINNER SELECTED")
#         self.log(f"Rule: {best['rule'].name}")
#         self.log(f"Final Score: {best['score']} (base={best['base_score']}, weight={best['weight']})")
#         self.log(f"Explanation: {best['explanation']}")

#         # STEP 5: execute action
#         result = ACTIONS[best["action"]](event)

#         # STEP 6: optional multi-rule execution (scaling feature)
#         side_effects = []
#         for c in candidates:
#             if c["rule"].name != best["rule"].name:
#                 # optional lightweight side-effect hook
#                 side_effects.append(c["rule"].name)

#         return {
#             "status": "executed",
#             "rule": best["rule"].name,
#             "score": best["score"],
#             "base_score": best["base_score"],
#             "weight": best["weight"],
#             "output": result,
#             "side_effects": side_effects if side_effects else None
#         }

















# # from actions import ACTIONS

# # class Engine:
# #     def __init__(self, rule_packs):
# #         self.rules = []
# #         for pack in rule_packs:
# #             self.rules.extend(pack())

# #     def process(self, event):
# #         event_dict = {
# #             "type": event.type,
# #             "payload": event.payload,
# #             "context": event.context
# #         }

# #         candidates = []

# #         # STEP 1: match rules
# #         for rule in self.rules:
# #             if rule.match(event_dict):
# #                 candidates.append((rule, rule.score(event_dict)))

# #         if not candidates:
# #             return {
# #                 "status": "no_match",
# #                 "output": None
# #             }

# #         # STEP 2: scoring + selection
# #         best_rule, best_score = max(candidates, key=lambda x: x[1])

# #         # STEP 3: execute action
# #         result = ACTIONS[best_rule.action](event)

# #         return {
# #             "status": "executed",
# #             "rule": best_rule.name,
# #             "score": best_score,
# #             "output": result
# #         }