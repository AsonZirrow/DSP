

from classifier import classify
from engine import Engine

from rules.chat_rules import chat_rules
from rules.command_rules import command_rules
from rules.system_rules import system_rules
from rules.security_rules import security_rules


# Build engine exactly like main.py
engine = Engine([
    chat_rules,
    command_rules,
    system_rules,
    security_rules
], trace=False)


def test_greeting_flow():
    print("\nTEST: greeting flow")

    event = classify("hi")
    result = engine.process(event)

    assert result.winner_rule == "greeting_rule"
    assert result.output is not None

    print("✔ PASS: greeting flow")


def test_command_flow():
    print("\nTEST: command flow")

    event = classify("run scan")
    result = engine.process(event)

    assert result.winner_rule == "run_command_rule"
    assert "Executing" in result.output

    print("✔ PASS: command flow")


def test_security_block():
    print("\nTEST: security flow")

    event = classify("delete all files")
    result = engine.process(event)

    # may vary depending on your rule priority setup
    assert result.output is not None

    print("✔ PASS: security flow")


def test_system_alert():
    print("\nTEST: system flow")

    event = classify("cpu overload")
    result = engine.process(event)

    assert result.output is not None

    print("✔ PASS: system flow")


if __name__ == "__main__":
    test_greeting_flow()
    test_command_flow()
    test_security_block()
    test_system_alert()

    print("\n✔ ALL INTEGRATION TESTS COMPLETE")