import os

from dotenv import load_dotenv
import psycopg


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = DATABASE_URL.replace(
    "postgresql+psycopg://",
    "postgresql://"
)


def migrate():

    migrations_dir = "migrations"

    files = sorted(os.listdir(migrations_dir))

    with psycopg.connect(DATABASE_URL) as connection:

        for file in files:

            if not file.endswith(".sql"):
                continue

            file_path = os.path.join(migrations_dir, file)

            with open(file_path, "r") as migration_file:
                sql = migration_file.read()

            print(f"Executando: {file}")

            with connection.cursor() as cursor:
                cursor.execute(sql)

    print("Migrations concluídas!")


try:
    migrate()

except Exception as error:
    print(f"Erro ao executar migrations: {error}")