

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine import Engine
from rules.chat_rules import chat_rules
from rules.command_rules import command_rules
from rules.system_rules import system_rules
from rules.security_rules import security_rules

from classifier import classify
from decision_record import DecisionRecord

engine = Engine([
    chat_rules,
    command_rules,
    system_rules,
    security_rules
])


def test_greeting_rule():
    print("\nTEST: engine greeting rule")
    event = classify("hi")
    result = engine.process(event)

    assert result.winner_rule == "greeting_rule"
    print("✔ PASS")


def test_command_rule():
    print("\nTEST: engine command rule")
    event = classify("run scan")
    result = engine.process(event)

    assert result.winner_rule == "run_command_rule"
    print("✔ PASS")


if __name__ == "__main__":
    test_greeting_rule()
    test_command_rule()
    print("\n✔ ENGINE TESTS COMPLETE")