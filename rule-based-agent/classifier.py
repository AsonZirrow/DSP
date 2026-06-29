

from dataclasses import dataclass, field
from typing import Dict, Any, List
import re
import time


# =========================
# 0. CLASSIFICATION OBJECT
# =========================

@dataclass
class Classification:
    raw_text: str

    normalized_text: str = ""
    valid: bool = True

    type: str = "unknown"
    intent: str = "unknown"

    parameters: Dict[str, Any] = field(default_factory=dict)
    entities: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    priority: float = 0.5
    confidence: float = 1.0

    metadata: Dict[str, Any] = field(default_factory=dict)


# =========================
# 1. NORMALIZATION
# =========================

def normalize_input(c: Classification) -> Classification:
    text = c.raw_text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    c.normalized_text = text
    return c


# =========================
# 2. VALIDATION
# =========================

def validate_input(c: Classification) -> Classification:
    if not c.normalized_text:
        c.valid = False
    return c


# =========================
# 3. TYPE DETECTION
# =========================

def detect_type(c: Classification) -> Classification:
    text = c.normalized_text

    if text in ["hi", "hello", "hey", "how are you"]:
        c.type = "chat"
    elif text.startswith("run") or text.startswith("execute"):
        c.type = "command"
    elif "cpu" in text or "system" in text:
        c.type = "system"
    elif "delete" in text:
        c.type = "command"
    else:
        c.type = "chat"

    return c


# =========================
# 4. INTENT DETECTION
# =========================

def detect_intent(c: Classification) -> Classification:
    text = c.normalized_text

    if text in ["hi", "hello", "hey", "how are you"]:
        c.intent = "greeting"
    elif "run scan" in text or "nmap" in text:
        c.intent = "network_scan"
    elif "cpu" in text:
        c.intent = "system_check"
    elif "delete" in text:
        c.intent = "dangerous_action"
    else:
        c.intent = "unknown"

    return c


# =========================
# 5. PARAMETER EXTRACTION
# =========================

def extract_parameters(c: Classification) -> Classification:
    text = c.normalized_text

    # Example: extract IP address
    ip_match = re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", text)
    if ip_match:
        c.parameters["ip"] = ip_match.group()

    # Example: extract tool name
    if "nmap" in text:
        c.parameters["tool"] = "nmap"

    return c


# =========================
# 6. ENTITY EXTRACTION
# =========================

def extract_entities(c: Classification) -> Classification:
    text = c.normalized_text

    known_tools = ["nmap", "chrome", "python"]

    c.entities = [tool for tool in known_tools if tool in text]

    return c


# =========================
# 7. TAG GENERATION
# =========================

def generate_tags(c: Classification) -> Classification:
    tags = []

    if c.type == "chat":
        tags.append("conversation")

    if c.intent == "greeting":
        tags.append("friendly")

    if c.intent == "dangerous_action":
        tags.append("risky")

    if c.type == "command":
        tags.append("execution")

    c.tags = tags
    return c


# =========================
# 8. PRIORITY ESTIMATION
# =========================

def estimate_priority(c: Classification) -> Classification:
    text = c.normalized_text

    if "urgent" in text:
        c.priority = 0.9
    elif c.intent == "dangerous_action":
        c.priority = 1.0
    else:
        c.priority = 0.5

    return c


# =========================
# 9. CONFIDENCE SCORE
# =========================

def estimate_confidence(c: Classification) -> Classification:
    if c.intent == "unknown":
        c.confidence = 0.4
    else:
        c.confidence = 0.9

    return c


# =========================
# 10. METADATA
# =========================

def generate_metadata(c: Classification) -> Classification:
    c.metadata = {
        "timestamp": time.time(),
        "length": len(c.raw_text)
    }
    return c


# =========================
# 11. BUILD EVENT
# =========================

def build_event(c: Classification):
    from event import Event

    return Event(
        type=c.type,
        intent=c.intent,
        payload=c.raw_text,
        parameters=c.parameters,
        entities=c.entities,
        tags=c.tags,
        priority=c.priority,
        confidence=c.confidence,
        metadata=c.metadata,
        context={}
    )


# =========================
# PIPELINE RUNNER
# =========================

def classify(text: str):
    c = Classification(raw_text=text)

    pipeline = [
        normalize_input,
        validate_input,
        detect_type,
        detect_intent,
        extract_parameters,
        extract_entities,
        generate_tags,
        estimate_priority,
        estimate_confidence,
        generate_metadata
    ]

    for step in pipeline:
        try:
            c = step(c)
        except Exception:
            # fail-safe: pipeline continues even if a step breaks
            continue

    return build_event(c)
















# from event import Event


# def classify_input(text: str) -> str:
#     """
#     Determine the high-level event type from raw user input.
#     This is intentionally simple for V1.
#     """

#     text = text.lower().strip()

#     if text in ["hi", "hello", "hey", "how are you"]:
#         return "chat"

#     if text.startswith("run") or text.startswith("execute"):
#         return "command"

#     if "cpu" in text or "system" in text:
#         return "system"

#     if "delete" in text:
#         return "command"

#     # Default fallback
#     return "chat"


# def build_event(text: str) -> Event:
#     """
#     Convert raw user input into a standardized Event object.
#     """

#     event_type = classify_input(text)

#     return Event(
#         type=event_type,
#         payload=text,
#         context={}
#     )