from agent import OpenStackAgent
import json

def run_dialog():
    agent = OpenStackAgent()
    print("Welcome to OpenStack Agent! Type 'exit' to quit.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break
        response = agent.handle_query(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    run_dialog()
