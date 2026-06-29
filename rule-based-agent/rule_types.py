

from dataclasses import dataclass
from typing import Callable, Dict, Any

@dataclass
class Rule:
    name: str
    match: Callable[[dict], bool]
    score: Callable[[dict], float]
    action: str

    # main.py, event.py, engine.py, actions.py, rule_types.py and rules as folder containing the following chat_rules.py, command_rules.py, security_rules.py and system_rules.py