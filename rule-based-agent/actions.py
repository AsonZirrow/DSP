

def respond_greeting(event):
    return "Hello 👋 (chat rule triggered)"

def run_command(event):
    return f"Executing command: {event.payload}"

def system_alert(event):
    return f"System alert handled: {event.payload}"

def security_block(event):
    return f"Security rule triggered: {event.payload}"

ACTIONS = {
    "respond_greeting": respond_greeting,
    "run_command": run_command,
    "system_alert": system_alert,
    "security_block": security_block,
}