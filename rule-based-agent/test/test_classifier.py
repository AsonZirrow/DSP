

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classifier import classify



def test_greeting():
    print("\nTEST: classifier greeting")
    event = classify("hi")
    assert event.type == "chat"
    assert event.intent == "greeting"
    print("✔ PASS")


def test_command():
    print("\nTEST: classifier command")
    event = classify("run scan")
    assert event.type == "command"
    print("✔ PASS")


def test_system():
    print("\nTEST: classifier system")
    event = classify("cpu overload")
    assert event.type == "system"
    print("✔ PASS")


if __name__ == "__main__":
    test_greeting()
    test_command()
    test_system()
    print("\n✔ CLASSIFIER TESTS COMPLETE")