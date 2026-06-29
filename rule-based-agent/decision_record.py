

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class DecisionRecord:
    """
    Stores the full reasoning output of the engine.
    This is NOT logic — it is a structured record of what happened.
    """

    # Input event that triggered the decision
    event: Any

    # All rules that were evaluated
    evaluated_rules: List[Dict[str, Any]] = field(default_factory=list)

    # Winning rule name
    winner_rule: str = ""

    # Winning score
    winner_score: float = 0.0

    # Final output from action
    output: Any = None

    # Step-by-step trace (human readable debug info)
    trace: List[str] = field(default_factory=list)

    # Optional metadata (future use)
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Status of decision
    status: str = "executed"