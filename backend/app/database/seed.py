import os

from dotenv import load_dotenv
import psycopg


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = DATABASE_URL.replace(
    "postgresql+psycopg://",
    "postgresql://"
)


def seed():

    with psycopg.connect(DATABASE_URL) as connection:

        with connection.cursor() as cursor:

            # Criar usuário
            cursor.execute("""
                INSERT INTO users (name, email, password_hash)
                VALUES (%s, %s, %s)
                RETURNING id;
            """, (
                "Usuário Teste",
                "usuario@myspotify.com",
                "senha_hash_exemplo"
            ))

            user_id = cursor.fetchone()[0]


            # Criar artista 1
            cursor.execute("""
                INSERT INTO artists (name, spotify_id)
                VALUES (%s, %s)
                RETURNING id;
            """, (
                "Charlie Brown Jr.",
                "charlie_brown_jr"
            ))

            charlie_id = cursor.fetchone()[0]


            # Criar artista 2
            cursor.execute("""
                INSERT INTO artists (name, spotify_id)
                VALUES (%s, %s)
                RETURNING id;
            """, (
                "Legião Urbana",
                "legiao_urbana"
            ))

            legiao_id = cursor.fetchone()[0]


            # Criar artista 3
            cursor.execute("""
                INSERT INTO artists (name, spotify_id)
                VALUES (%s, %s)
                RETURNING id;
            """, (
                "Matuê",
                "matue"
            ))

            matue_id = cursor.fetchone()[0]


            # Criar álbum
            cursor.execute("""
                INSERT INTO albums (name, spotify_id)
                VALUES (%s, %s)
                RETURNING id;
            """, (
                "Acústico MTV",
                "acustico_mtv"
            ))

            album_id = cursor.fetchone()[0]


            # Criar músicas
            cursor.execute("""
                INSERT INTO songs (
                    title,
                    spotify_id,
                    duration_ms,
                    artist_id,
                    album_id
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """, (
                "Só os Loucos Sabem",
                "so_os_loucos_sabem",
                230000,
                charlie_id,
                album_id
            ))

            song1_id = cursor.fetchone()[0]


            cursor.execute("""
                INSERT INTO songs (
                    title,
                    spotify_id,
                    duration_ms,
                    artist_id,
                    album_id
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """, (
                "Tempo Perdido",
                "tempo_perdido",
                300000,
                legiao_id,
                album_id
            ))

            song2_id = cursor.fetchone()[0]


            cursor.execute("""
                INSERT INTO songs (
                    title,
                    spotify_id,
                    duration_ms,
                    artist_id,
                    album_id
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """, (
                "Quer Voar",
                "quer_voar",
                180000,
                matue_id,
                album_id
            ))

            song3_id = cursor.fetchone()[0]


            # Criar playlist
            cursor.execute("""
                INSERT INTO playlists (
                    name,
                    description,
                    user_id
                )
                VALUES (%s, %s, %s)
                RETURNING id;
            """, (
                "Minhas Favoritas",
                "Playlist inicial do MySpotify",
                user_id
            ))

            playlist_id = cursor.fetchone()[0]


            # Adicionar músicas à playlist
            cursor.execute("""
                INSERT INTO playlist_songs (
                    playlist_id,
                    song_id
                )
                VALUES (%s, %s)
            """, (
                playlist_id,
                song1_id
            ))


            cursor.execute("""
                INSERT INTO playlist_songs (
                    playlist_id,
                    song_id
                )
                VALUES (%s, %s)
            """, (
                playlist_id,
                song2_id
            ))


            cursor.execute("""
                INSERT INTO playlist_songs (
                    playlist_id,
                    song_id
                )
                VALUES (%s, %s)
            """, (
                playlist_id,
                song3_id
            ))

    print("Seed concluída com sucesso!")


try:
    seed()

except Exception as error:
    print(f"Erro ao executar seed: {error}")