

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classifier import classify
from decision_record import DecisionRecord


def test_decision_structure():
    print("\nTEST: decision record structure")

    event = classify("hi")

    record = DecisionRecord(
        event=event,
        evaluated_rules=[],
        winner_rule="test",
        winner_score=0.5,
        output="hello",
        trace=[]
    )

    assert record.winner_rule == "test"
    assert record.output == "hello"

    print("✔ PASS")


if __name__ == "__main__":
    test_decision_structure()
    print("\n✔ DECISION RECORD TESTS COMPLETE")









# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from decision_record import DecisionRecord
# from event import Event


# def test_decision_structure():
#     print("\nTEST: decision record structure")

#     event = Event(type="chat", payload="hi", context={})

#     record = DecisionRecord(
#         event=event,
#         evaluated_rules=[],
#         winner_rule="test",
#         winner_score=0.5,
#         output="hello",
#         trace=[]
#     )

#     assert record.winner_rule == "test"
#     assert record.output == "hello"

#     print("✔ PASS")


# if __name__ == "__main__":
#     test_decision_structure()
#     print("\n✔ DECISION RECORD TESTS COMPLETE")