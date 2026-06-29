

from rule_types import Rule

def system_rules():
    return [
        Rule(
            name="system_alert_rule",
            match=lambda e: e["type"] == "system",
            score=lambda e: 0.85,
            action="system_alert"
        )
    ]