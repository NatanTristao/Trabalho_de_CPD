# Trabalho_de_CPD

INF01124 — Classificação e Pesquisa de Dados

## Overview
In this project, we explore the FIFA21 - Players dataset (data from Kaggle, extracted from the website sofifa.com). The records cover players from Career Mode in FIFA 15 through FIFA 21. From this data, the datasets used in this work were generated.


## Data structures implemented

### Structure 1 — Player storage (Hash table)
A hash table stores player information.  
- **Key:** player id  
- **Value:** fields from `players.csv` plus aggregated review info (computed from user review files).

### Structure 2 — Name searches (TRIE)
A TRIE was built to support prefix searches on players' short names.

### Structure 3 — User reviews (Hash table)
A hash table maps `user id` → list of reviews (player id + rating).  
Use case: list which players a user reviewed and the ratings they gave.

### Structure 4 — Tags (Hash table)
Tags from `tags.csv` are stored in a hash table that maps a tag string → list of players that received that tag.  
This supports searching by tag and combining tags (intersections).

---

## Queries / Searches

### Search 1 — Player name prefix
Return players whose *short name* starts with a given string.  
Each result line includes: `player id`, `short name`, `long name`, `positions`, `global average rating`, and `number of ratings`.

### Search 2 — Players reviewed by a user
Return up to 30 players reviewed by a given user. For each player show: `user's rating`, `global average`, and `rating count`.

### Search 3 — Top players by position
Return top players for a specific position. Rules:
- Only consider players with **at least 1000 ratings** (to avoid bias from few reviews).
- Accepts a parameter `N` to limit the number of returned players.

### Search 4 — Players matching tags intersection
Given a list of tags, return players that belong to the **intersection** of those tags.  
Output requirements:
- Sorted by **global average rating (descending)**  
- Global rating printed with **6 decimal places**  
- Compact output formatted in tabulated columns

## Members
- Rayan Raddatz de Matos ([@rddtz](https://github.com/rddtz))
- Natan Feijó Tristão ([@NatanTristao](https://github.com/NatanTristao))
