import sqlite3


class load:

    def __init__(self):
        pass

    def load_data(self, db_name, table_name, universities_list):
        # Criar o banco e se concectar nele
        con = sqlite3.connect(f"{db_name}.db")
        c = con.cursor()

        # Criar a tabela no banco
        c.execute(
            f"""
        CREATE TABLE IF NOT EXISTS {table_name}
                (
                id INTERGER PRIMARY KEY,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
                );
        """
        )

        for university in universities_list:
            c.execute(
                f"""INSERT INTO {table_name} (name, country, state_province, web_pages, domains) VALUES (?,?,?,?,?);""",
                (
                    university.get("name"),
                    university.get("country"),
                    university.get("state-province"),
                    ", ".join(university.get("web_pages", [])),
                    ", ".join(university.get("domains", [])),
                ),
            )

        con.commit()
        con.close()

        return print("Banco de dados criado com sucesso!")
