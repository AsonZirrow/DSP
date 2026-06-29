

from decision_record import DecisionRecord


def print_decision(record: DecisionRecord):

    event = record.event

    print("\n🧠 ENGINE RESULT")
    print(f"INPUT: {event.payload}")
    print(f"TYPE: {event.type} | INTENT: {getattr(event, 'intent', 'unknown')}")

    print("\n🏆 WINNER:")
    print(f"{record.winner_rule} (score={record.winner_score})")

    print("\n💬 OUTPUT:")
    print(record.output)

    print("\n📊 RULES EVALUATED:")

    for r in record.evaluated_rules:
        status = "✔ MATCH" if r["matched"] else "✘ NO MATCH"
        print(f"{r['name']:<20} → {status} ({r['score']})")

    if record.trace:
        print("\n🧠 TRACE:")
        for t in record.trace:
            print(f"- {t}")