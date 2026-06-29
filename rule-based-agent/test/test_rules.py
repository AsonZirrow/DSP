

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from rules.chat_rules import chat_rules


def test_chat_rules_exist():
    print("\nTEST: chat rules load")

    rules = chat_rules()
    assert len(rules) > 0

    print("✔ PASS")


if __name__ == "__main__":
    test_chat_rules_exist()
    print("\n✔ RULES TESTS COMPLETE")