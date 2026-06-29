

from rule_types import Rule

def command_rules():
    return [
        Rule(
            name="run_command_rule",
            match=lambda e: e["type"] == "command",
            score=lambda e: 0.8,
            action="run_command"
        )
    ]