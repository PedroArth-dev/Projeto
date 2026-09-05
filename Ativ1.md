# Atividade 1 — MySpotify

## 1. Quais tabelas você definiu inicialmente?

Inicialmente, foram definidas seis tabelas para o banco de dados da aplicação MySpotify:

- `users` — armazena os usuários cadastrados.
- `artists` — armazena os artistas das músicas.
- `albums` — armazena os álbuns.
- `songs` — armazena as músicas e suas informações relacionadas à API do Spotify.
- `playlists` — armazena as playlists criadas pelos usuários.
- `playlist_songs` — relaciona as músicas às playlists, permitindo uma relação muitos-para-muitos.

As principais relações entre as tabelas são:

- Um usuário pode possuir várias playlists.
- Uma playlist pode possuir várias músicas.
- Uma música pode estar presente em várias playlists.
- Uma música pertence a um artista.
- Uma música pode estar associada a um álbum.

---

## 2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.

Sim. Foram definidas inicialmente **quatro migrations**, seguindo a abordagem apresentada no capítulo 5 do livro, utilizando arquivos SQL numerados e executados em ordem.

As migrations estão localizadas em `backend/migrations/`:

| Migration | Descrição |
|---|---|
| `001_create_users.sql` | Cria a tabela `users`, responsável pelo cadastro e armazenamento dos usuários. |
| `002_create_artists_albums_songs.sql` | Cria as tabelas `artists`, `albums` e `songs`, responsáveis pelo armazenamento das informações musicais. |
| `003_create_playlists.sql` | Cria a tabela `playlists` e estabelece sua relação com os usuários. |
| `004_create_playlist_songs.sql` | Cria a tabela `playlist_songs`, responsável pela relação entre playlists e músicas. |

As migrations serão executadas por um script responsável por localizar os arquivos `.sql` dentro da pasta `backend/migrations/`, ordená-los pelo número inicial e executar cada arquivo no banco PostgreSQL.

---

## 3. Qual o caminho do arquivo que gera a seed do seu banco?

O arquivo responsável pela seed será:

`backend/app/database/seed.py`

Ele será utilizado para inserir dados iniciais no banco de dados, como usuários, artistas, álbuns, músicas e playlists de teste. A seed é mantida separada das migrations, pois as migrations são responsáveis pela estrutura do banco, enquanto a seed é responsável pelos dados iniciais.

---

## 4. Quais os endpoints que você irá implementar inicialmente? Cada endpoint deve ser um método e um path. Explique em um parágrafo por que você resolveu priorizar a implementação desses endpoints.

Inicialmente, serão implementados os seguintes endpoints:

| Método | Path | Função |
|---|---|---|
| `POST` | `/users` | Cadastrar um novo usuário. |
| `POST` | `/auth/login` | Realizar o login do usuário. |
| `GET` | `/users/{user_id}` | Buscar informações de um usuário. |
| `GET` | `/songs` | Listar músicas disponíveis. |
| `GET` | `/songs/{song_id}` | Buscar uma música específica. |
| `POST` | `/songs` | Cadastrar uma música. |
| `GET` | `/playlists` | Listar playlists. |
| `GET` | `/playlists/{playlist_id}` | Buscar uma playlist específica. |
| `POST` | `/playlists` | Criar uma nova playlist. |
| `PUT` | `/playlists/{playlist_id}` | Atualizar uma playlist. |
| `DELETE` | `/playlists/{playlist_id}` | Excluir uma playlist. |
| `POST` | `/playlists/{playlist_id}/songs/{song_id}` | Adicionar uma música à playlist. |
| `DELETE` | `/playlists/{playlist_id}/songs/{song_id}` | Remover uma música da playlist. |

A implementação desses endpoints será priorizada porque eles representam as funcionalidades principais da aplicação. Primeiro, é necessário permitir que o usuário seja cadastrado e autenticado. Depois, a aplicação precisa conseguir consultar e armazenar músicas, incluindo informações obtidas pela API do Spotify. Por fim, os endpoints de playlists permitem implementar uma das principais funcionalidades do MySpotify: criar playlists e adicionar ou remover músicas delas. Dessa forma, esses endpoints formam a base para posteriormente conectar o backend aos frontends Web e Mobile.

---

## 5. Você está usando algum framework para escrever os endpoints da sua API? Se sim, qual?

Sim. O framework escolhido para desenvolver a API é o **FastAPI**, utilizando Python.

O FastAPI será responsável pela criação dos endpoints REST da aplicação. Para realizar a comunicação com o banco de dados PostgreSQL, será utilizado o **SQLAlchemy** como ORM.

As migrations, serão feitas seguindo a abordagem apresentada no capítulo 5 do livro, elas serão escritas manualmente em arquivos `.sql` numerados e executadas em sequência por um script de migration.

A estrutura inicial relacionada ao backend ficará aproximadamente assim:

`backend/`
- `migrations/`
  - `001_create_users.sql`
  - `002_create_artists_albums_songs.sql`
  - `003_create_playlists.sql`
  - `004_create_playlist_songs.sql`
- `migrate.py`
- `app/`
  - `database/`
    - `seed.py`
  - `main.py`
  - `models/`
  - `routes/`
  - `schemas/`
