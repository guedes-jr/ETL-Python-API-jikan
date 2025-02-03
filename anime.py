import argparse
import requests
import sqlite3
import json

# === ETAPA 1: EXTRAÇÃO ===
def extract():
    url = "https://api.jikan.moe/v4/top/anime"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()["data"]  # Retorna apenas a lista de animes
    else:
        print(f"Erro ao acessar API: {response.status_code}")
        return []

# === ETAPA 2: TRANSFORMAÇÃO ===
def transform(data):
    transformed_data = []
    for anime in data:
        transformed_data.append({
            "id": anime["mal_id"],
            "titulo": anime["title"],
            "tipo": anime["type"],
            "episodios": anime["episodes"] if anime["episodes"] else 0,
            "nota": anime["score"] if anime["score"] else 0.0
        })
    return transformed_data

# === ETAPA 3: CARGA NO BANCO DE DADOS ===
def load(data, data_type="json"):
    if data_type == "csv":
        with open("animes.csv", "w") as file:
            file.write("id,titulo,tipo,episodios,nota\n")
            for anime in data:
                file.write(f"{anime['id']},{anime['titulo']},{anime['tipo']},{anime['episodios']},{anime['nota']}\n")
    elif data_type == "json":
        with open("animes.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        conn = sqlite3.connect("animes.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS animes (
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                tipo TEXT,
                episodios INTEGER,
                nota REAL
            )
        """)

        for anime in data:
            cursor.execute("""
                INSERT OR IGNORE INTO animes (id, titulo, tipo, episodios, nota)
                VALUES (?, ?, ?, ?, ?)
            """, (anime["id"], anime["titulo"], anime["tipo"], anime["episodios"], anime["nota"]))
        
        conn.commit()
        conn.close()
    print(f"ETL concluído com sucesso! Dados inseridos no banco 'animes.{data_type if data_type != 'sqlite' else 'db'}'.")


# === EXECUTANDO O ETL ===
# === PARSER PARA FLAGS ===
def main():
    parser = argparse.ArgumentParser(description="ETL de animes usando a API Jikan")
    parser.add_argument("--output", choices=["sqlite", "json", "csv"], required=True, help="Formato de saída dos dados")

    args = parser.parse_args()

    data = extract()
    if data:
        transformed_data = transform(data)
        load(transformed_data, args.output)
    
if __name__ == "__main__":
    main()
