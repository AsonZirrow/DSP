

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classifier import classify
from actions import ACTIONS


def test_greeting_action():
    print("\nTEST: greeting action")

    event = classify("hi")
    result = ACTIONS["respond_greeting"](event)

    assert "Hello" in result
    print("✔ PASS")


def test_command_action():
    print("\nTEST: command action")

    event = classify("run scan")
    result = ACTIONS["run_command"](event)

    assert "Executing" in result
    print("✔ PASS")


if __name__ == "__main__":
    test_greeting_action()
    test_command_action()
    print("\n✔ ACTIONS TESTS COMPLETE")
















# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from actions import ACTIONS
# from event import Event
# from classifier import classify


# def test_greeting_action():
#     print("\nTEST: greeting action")

#     event = Event(type="chat", payload="hi", context={})
#     result = ACTIONS["respond_greeting"](event)

#     assert "Hello" in result
#     print("✔ PASS")


# def test_command_action():
#     print("\nTEST: command action")

#     # event = Event(type="command", payload="run scan", context={})
#     event = classify("hi")
#     result = ACTIONS["run_command"](event)

#     assert "Executing" in result
#     print("✔ PASS")


# if __name__ == "__main__":
#     test_greeting_action()
#     test_command_action()
#     print("\n✔ ACTIONS TESTS COMPLETE")