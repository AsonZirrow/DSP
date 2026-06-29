

# Architecture

## Overview

The Routing Decision Engine is organized into four independent layers:

1. Computation
2. Configuration
3. Representation
4. Orchestration

Each layer is responsible for a specific function and can evolve independently without requiring major changes to the rest of the system.

---

## System Flow

User Input
↓
Orchestration Layer (main.py)
↓
Configuration Layer (config.py)
↓
Computation Layer (calculator.py)
↓
Representation Layer (models.py)
↓
Output

---

## Computation Layer

File:

calculator.py

Purpose:

Perform mathematical operations.

Responsibilities:

* Travel-time calculation
* Distance adjustment
* Cost computation

Design Principle:

The computation layer performs calculations only.

It does not:

* Store configuration
* Make routing decisions
* Request user input
* Manage workflow execution

---

## Configuration Layer

File:

config.py

Purpose:

Store rules, defaults, and policies.

Responsibilities:

* Speed defaults
* Distance multipliers
* Routing modifiers
* Future decision rules

Design Principle:

Behavior should be configurable without modifying the computation layer.

---

## Representation Layer

File:

models.py

Purpose:

Represent domain concepts explicitly.

Current representations:

* Node
* Connection
* Cost
* Route

Design Principle:

Relationships should be modeled through structured objects rather than loose variables.

---

## Orchestration Layer

File:

main.py

Purpose:

Coordinate the execution flow.

Responsibilities:

* Collect user input
* Query configuration rules
* Trigger calculations
* Create representations
* Display results

Design Principle:

Workflow management should remain separate from both computation and configuration.

---

## Architectural Benefits

This separation provides:

* Modularity
* Maintainability
* Extensibility
* Clear responsibilities
* Easier testing

The architecture is intended to support future decision systems while maintaining a simple and understandable foundation.
