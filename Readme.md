# MySpotify

Uma aplicação inspirada no Spotify, desenvolvida com o objetivo de reproduzir de forma simplificada algumas das principais funcionalidades de uma plataforma de streaming de músicas.

## Objetivo

O **MySpotify** tem como objetivo desenvolver uma aplicação de música simples e intuitiva, permitindo que o usuário tenha acesso a funcionalidades básicas de gerenciamento e reprodução de músicas.

A proposta é utilizar o Spotify como referência, criando uma versão simplificada da plataforma, com foco nas funcionalidades essenciais e na integração entre **frontend, backend e banco de dados**.

O projeto contará com uma versão **Web** e uma aplicação **Mobile nativa**, ambas conectadas ao mesmo backend.

## Funcionalidades

### Usuário

* Cadastro de novos usuários;
* Login e autenticação;
* Acesso às informações da própria conta.

### Músicas

* Buscar músicas;
* Visualizar informações das músicas;
* Cadastrar músicas disponíveis na base utilizada pelo sistema;
* Reproduzir músicas, de acordo com as possibilidades da tecnologia e da API utilizada.

### Playlists

* Criar playlists;
* Visualizar playlists criadas pelo usuário;
* Adicionar músicas às playlists;
* Remover músicas das playlists;
* Visualizar as músicas presentes em cada playlist.

### Interface

* Página inicial com músicas disponíveis;
* Página de busca;
* Página de playlists;
* Player de música;
* Navegação entre as principais áreas da aplicação;
* Interface adaptada para Web e Mobile.

## Estrutura inicial do projeto

O projeto será dividido em três partes principais:

```
MySpotify/
│
├── frontend-web/
│   └── Aplicação Web
│
├── frontend-mobile/
│   └── Aplicação Mobile Nativa
│
├── backend/
│   └── API e regras de negócio
│
└── README.md
```

## Arquitetura

A aplicação será estruturada seguindo uma arquitetura cliente-servidor.

```
                  ┌──────────────────────┐
                  │      MySpotify       │
                  │       Backend        │
                  │      API REST        │
                  └──────────┬───────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
     ┌─────────────────┐           ┌─────────────────┐
     │   Frontend Web  │           │ Frontend Mobile │
     │                 │           │ React Native +  │
     │                 │           │     Expo        │
     └─────────────────┘           └─────────────────┘
              │                             │
              └──────────────┬──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │    Database     │
                    │   (Supabase)    │
                    └─────────────────┘
```

O **backend** será responsável pelas regras de negócio da aplicação, gerenciamento das músicas e playlists, autenticação, comunicação com o banco de dados e disponibilização da API utilizada pelos dois frontends.

O **Frontend Web** será responsável pela interface acessada através de navegadores.

O **Frontend Mobile** será desenvolvido como uma aplicação nativa utilizando **React Native com Expo**, permitindo que o sistema seja executado em dispositivos móveis.

Os dois frontends utilizarão o mesmo backend e compartilharão os dados armazenados no banco de dados.

## Frontend Mobile

O desenvolvimento mobile será realizado utilizando **React Native com Expo**.

O **React Native** é uma tecnologia para desenvolvimento de aplicações nativas utilizando React e JavaScript. Ele permite desenvolver aplicações para plataformas como Android e iOS reutilizando grande parte do código, enquanto utiliza componentes e recursos nativos de cada plataforma.

O **Expo** será utilizado como framework de desenvolvimento para facilitar a configuração, execução e desenvolvimento da aplicação React Native.

A escolha dessa tecnologia está relacionada ao objetivo do projeto de possuir uma aplicação **mobile nativa**, e não apenas uma página Web responsiva ou uma PWA.

## Banco de Dados

O banco de dados escolhido para o projeto será o **PostgreSQL**, utilizando o **Supabase** como plataforma de suporte ao banco e aos serviços relacionados.

O PostgreSQL é um sistema de gerenciamento de banco de dados relacional. Ele permite organizar as informações do MySpotify em diferentes tabelas relacionadas entre si.

A estrutura inicial poderá conter entidades como:

```
Usuários
   │
   ├── Playlists
   │       │
   │       └── Músicas
   │
   └── Informações da conta

Músicas
   │
   ├── Artistas
   ├── Álbuns
   └── Outras informações
```

Essa estrutura permitirá representar relações como:

* Um usuário pode possuir várias playlists;
* Uma playlist pode possuir várias músicas;
* Uma música pode estar presente em várias playlists;
* Um artista pode possuir várias músicas;
* Um álbum pode possuir várias músicas.

O **Supabase** será utilizado como uma plataforma complementar ao PostgreSQL, oferecendo recursos como autenticação de usuários e APIs para comunicação com o banco de dados. O Supabase utiliza PostgreSQL internamente e pode gerar uma API REST baseada no esquema do banco.

## Tecnologias

### Frontend Web

* HTML;
* CSS;
* JavaScript.

### Frontend Mobile

* React Native;
* Expo;
* JavaScript/TypeScript.

### Backend

* Python;
* API REST.

### Banco de Dados

* PostgreSQL;
* Supabase.

### Integração

* API do Spotify.

## Integração com o Spotify

O projeto utilizará o Spotify como referência e poderá utilizar sua API para obter informações relacionadas às músicas, artistas, álbuns e outros dados disponibilizados pela plataforma.

A integração será realizada de acordo com as possibilidades e limitações oferecidas pela API e pelas tecnologias utilizadas no desenvolvimento.

A aplicação não tem como objetivo reproduzir integralmente o Spotify, mas desenvolver uma versão simplificada com algumas de suas principais funcionalidades.

## Fluxo básico da aplicação

1. O usuário realiza seu cadastro ou login;
2. O sistema autentica o usuário;
3. O usuário acessa a página inicial;
4. O usuário pode pesquisar músicas;
5. O sistema apresenta as músicas disponíveis;
6. O usuário pode selecionar e reproduzir uma música;
7. O usuário pode criar uma playlist;
8. O usuário pode adicionar músicas à playlist;
9. O usuário pode remover músicas da playlist;
10. As informações das playlists e dos usuários são armazenadas no banco de dados;
11. As mesmas informações podem ser acessadas através da aplicação Web ou Mobile.

## Escopo inicial

A primeira versão do MySpotify terá como foco:

* Autenticação de usuários;
* Busca de músicas;
* Gerenciamento de músicas;
* Criação de playlists;
* Visualização de playlists;
* Adição de músicas às playlists;
* Remoção de músicas das playlists;
* Reprodução de músicas, conforme as possibilidades da API utilizada;
* Interface Web;
* Aplicação Mobile nativa;
* Comunicação entre os frontends e o backend;
* Persistência dos dados em banco de dados.

Funcionalidades mais avançadas presentes no Spotify original, como recomendações personalizadas, podcasts, letras de músicas, reprodução offline, planos de assinatura e algoritmos complexos de recomendação, não fazem parte do escopo inicial do projeto.

## Objetivo acadêmico

O projeto tem como finalidade aplicar, de forma prática, os conhecimentos adquiridos durante a disciplina de programação, trabalhando conceitos de:

* Desenvolvimento de interfaces;
* Programação frontend;
* Desenvolvimento backend;
* Desenvolvimento de aplicações mobile;
* APIs;
* Banco de dados;
* Autenticação;
* Comunicação entre sistemas;
* Arquitetura cliente-servidor;
* Desenvolvimento Web;
* Desenvolvimento para dispositivos móveis.

## Status do projeto

Neste momento, o projeto encontra-se na fase de definição da proposta e levantamento das funcionalidades. O desenvolvimento será realizado posteriormente a partir dos requisitos definidos e dos feedbacks recebidos.

## Observação

O MySpotify é um projeto acadêmico inspirado em funcionalidades de plataformas de streaming existentes. O projeto não possui vínculo oficial com o Spotify.
