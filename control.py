from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"
print(DATA_DIR)


#read
def read_leads():
    if not DB_PATH.exists():
        return []
    
    try:
        return json.loads(DB_PATH.read_text(encoding="UTF-8"))
    except json.JSONDecodeError:
        return []
    

#CREAT
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
# lista é criada do zero toda vez que é criada uma nova, arrumar isso!