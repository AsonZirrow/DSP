

from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class Event:

    # Original user input
    payload: str

    # Broad category
    type: str

    # Specific meaning
    intent: str

    # Extracted values
    parameters: Dict[str, Any] = field(default_factory=dict)

    # Recognized named objects
    entities: List[str] = field(default_factory=list)

    # Semantic labels
    tags: List[str] = field(default_factory=list)

    # Estimated urgency
    priority: float = 0.5

    # Classifier confidence
    confidence: float = 1.0

    # Additional runtime information
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Shared runtime state
    context: Dict[str, Any] = field(default_factory=dict)
















# from dataclasses import dataclass
# from typing import Dict, Any

# @dataclass
# class Event:
#     type: str
#     payload: str
#     context: Dict[str, Any]