from config import openstack_config

class OpenStackAgent:
    def __init__(self):
        self.instances = {}
        print("OpenStackAgent initialized.")

    def handle_query(self, query: str) -> str:
        query_lower = query.lower()
        print(f"[DEBUG] Query received: {query_lower}")

        name = self.extract_instance_name(query_lower)
        print(f"[DEBUG] Extracted instance name: {name if name else 'demo-instance (default)'}")

        if any(phrase in query_lower for phrase in ["create instance", "create vm", "launch instance", "launch vm", "start instance", "start vm"]):
            return self.confirm_and_execute(f"Are you sure you want to create instance '{name or 'demo-instance'}'?", lambda: self.create_instance(name or "demo-instance"))

        elif any(phrase in query_lower for phrase in ["delete instance", "delete vm", "remove instance", "terminate vm"]):
            return self.confirm_and_execute(f"Are you sure you want to delete instance '{name or 'demo-instance'}'?", lambda: self.delete_instance(name or "demo-instance"))

        elif any(phrase in query_lower for phrase in ["list instances", "show instances", "list vms", "show vms"]):
            return self.list_instances()

        else:
            return "I'm sorry, I don't understand the request."

    def confirm_and_execute(self, prompt, action_callback):
        confirm = input(f"{prompt} (yes/no): ").strip().lower()
        if confirm == "yes":
            return action_callback()
        else:
            return "Action cancelled by user."

    def extract_instance_name(self, query: str) -> str:
        import re
        match = re.search(r"(called|named)\s+([\w\-]+)", query)
        if match:
            return match.group(2)
        return ""

    def create_instance(self, name):
        if name in self.instances:
            print(f"[DEBUG] Instance '{name}' already exists.")
            return f"Instance '{name}' already exists."
        self.instances[name] = "ACTIVE"
        print(f"[DEBUG] Instance '{name}' created.")
        return f"Instance '{name}' created successfully."

    def delete_instance(self, name):
        if name in self.instances:
            del self.instances[name]
            print(f"[DEBUG] Instance '{name}' deleted.")
            return f"Instance '{name}' deleted."
        print(f"[DEBUG] Instance '{name}' not found.")
        return f"No instance named '{name}' found."

    def list_instances(self):
        if not self.instances:
            print("[DEBUG] No instances found.")
            return "No instances currently running."
        print(f"[DEBUG] Listing instances: {', '.join(self.instances.keys())}")
        return "Instances: " + ", ".join(self.instances.keys())


if __name__ == "__main__":
    agent = OpenStackAgent()

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting agent.")
            break
        response = agent.handle_query(user_input)
        print(f"Agent: {response}")





