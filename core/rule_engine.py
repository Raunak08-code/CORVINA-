import json
import os 

RULES_PATH = os.path.join("config","rules.json")
TEMPLATES_DIR = "templates"

def load_rules():
    with open(RULES_PATH,"r") as f:
        return json.load(f)
    
def get_reply_templates(intent):
    rules = load_rules()

    template_file = rules.get(intent,rules.get("general"))

    template_path = os.path.join(TEMPLATES_DIR,template_file)

    if not os.path.exists(template_path):
        return "No template found"
    
    with open(template_path,"r") as f:
        return f.read()
