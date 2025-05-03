# System Architecture

The system consists of:
- **Natural Language Interface (NLI)**: Captures user instructions.
- **OpenStack Agent**: Maps NL to OpenStack API calls (simulated here).
- **Dialog Engine**: Handles context, response generation.
- **Config Module**: Stores OpenStack credentials.

## Flow Diagram
1. User inputs NL instruction.
2. `app.py` passes it to `OpenStackAgent`.
3. `OpenStackAgent` interprets and executes it.
4. Output returned to user.

(See `dialog_flow.png`)
