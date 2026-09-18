from pathlib import Path
import json, csv

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

# FUNÇÃO QUE RECEBE O TEXTO DA BUSCA E RETORNA UMA LISTA COM OS RESULTADOS
def read_leads_search(query):

    leads = read_leads() # lista de dicionário / lista de leads / array of dict
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()
        #print(txt_lead)

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results
    print(read_leads_search("Alexandre"))

# EXPORTAR LEADS COMO CSV
def export_csv():
    path_csv = DATA_DIR / "leads.csv"

    leads = read_leads()
    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)

        return path_csv
    except PermissionError:
        return None



