

# Sample Execution

## Input

Distance (km): 2

Mode: vertical

Speed (km/h): 50

---

## Configuration

The selected route mode is:

vertical

RouteConfig applies the vertical distance multiplier:

1.3

Adjusted distance:

2 × 1.3 = 2.6 km

---

## Calculations

Travel Time:

2.6 ÷ 50 = 0.052 hours

---

## Structured Route Model

Route

Connection:
Start → End

Distance:
2.6 km

Cost:
Distance = 2.6
Time = 0.052
Score = 0.052

---

## Console Output

=== RESULT ===

Raw Distance: 2.0

Mode: vertical

Adjusted Distance: 2.6

Speed: 50.0

Time (hours): 0.052

=== MODEL DEBUG OUTPUT ===

Route(
Connection(Start -> End, 2.6 km),
Cost(distance=2.6, time=0.052, score=0.052)
)

---

## Purpose

This example demonstrates the interaction between:

* RouteConfig (configuration layer)
* RouteCalculator (computation layer)
* Route models (representation layer)
* Main workflow controller (orchestration layer)

The example shows how routing behavior is derived from configurable rules while maintaining a separation between system responsibilities.
