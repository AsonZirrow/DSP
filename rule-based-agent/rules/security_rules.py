

from rule_types import Rule

def security_rules():
    return [
        Rule(
            name="block_bad_command",
            match=lambda e: "delete" in e["payload"],
            score=lambda e: 1.0,
            action="security_block"
        )
    ]