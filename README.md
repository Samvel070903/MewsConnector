<div align="center">

# <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40"/> Mews Connector — Wrapper Python

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![GitHub stars](https://img.shields.io/github/stars/Samvel070903/MewsConnector?style=social)](https://github.com/Samvel070903/MewsConnector)

**Un wrapper Python professionnel et entièrement typé pour l'[API Mews Connector](https://mews-systems.gitbook.io/connector-api/)**

[<img src="https://img.shields.io/badge/Installation-2ea44f?style=flat-square" height="20"/>](#installation) • [<img src="https://img.shields.io/badge/Documentation-0366d6?style=flat-square" height="20"/>](#documentation-des-opérations) • [<img src="https://img.shields.io/badge/Exemples-ff9800?style=flat-square" height="20"/>](#démarrage-rapide) • [<img src="https://img.shields.io/badge/Contribuer-6f42c1?style=flat-square" height="20"/>](#contribution)

</div>

---

<div align="center">

### <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle;"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="currentColor"/></svg> Fonctionnalités

<table>
<tr>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg><br/>
<strong>API Complète</strong><br/>
Support de tous les endpoints Mews
</td>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle;"><path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z" fill="currentColor"/></svg><br/>
<strong>Pagination Auto</strong><br/>
Gestion automatique des curseurs
</td>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 7.48 7.48 0 0 0-1.01-.436c-.41-.18-.785-.38-1.126-.6a4.086 4.086 0 0 1-.926-.87 2.556 2.556 0 0 1-.537-1.244c-.06-.47-.09-.99-.09-1.56 0-.612.108-1.148.323-1.607.216-.46.516-.843.902-1.15a4.494 4.494 0 0 1 1.353-.657 5.364 5.364 0 0 1 1.688-.257zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z"/></svg><br/>
<strong>Typage Fort</strong><br/>
Entièrement typé avec type hints
</td>
</tr>
<tr>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle;"><path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z" fill="currentColor"/></svg><br/>
<strong>Retry Automatique</strong><br/>
Gestion intelligente des erreurs
</td>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg><br/>
<strong>Sécurisé</strong><br/>
Gestion sécurisée des tokens
</td>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg><br/>
<strong>Documentation</strong><br/>
Exemples pour chaque endpoint
</td>
</tr>
</table>

</div>

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z"/></svg> Table des matières

<details>
<summary>Cliquez pour voir la table des matières complète</summary>

- [Installation](#installation)
- [Démarrage rapide](#démarrage-rapide)
- [Documentation des opérations](#documentation-des-opérations)
  - [Configuration](#configuration)
  - [Enterprises](#enterprises)
  - [Customers](#customers)
  - [Reservations](#reservations)
  - [Services](#services)
  - [Resources](#resources)
  - [Rates](#rates)
  - [Payments](#payments)
  - [Bills](#bills)
  - [Accounting](#accounting)
  - [Companies](#companies)
  - [Products](#products)
  - [Outlets](#outlets)
  - [Orders](#orders)
  - [Devices](#devices)
  - [Loyalty](#loyalty)
  - [Vouchers](#vouchers)
- [Gestion des erreurs](#gestion-des-erreurs)
- [Pagination](#pagination)
- [Développement](#développement)
- [Contribution](#contribution)

</details>

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M2.81 14.12L5.64 11.3l-1.41-1.41L1.4 12.71c-.39.39-.39 1.02 0 1.41l.7.7 1.41-1.41zm16.62-1.41c.39-.39.39-1.02 0-1.41l-.7-.7-1.41 1.41 2.83 2.83 1.41-1.41zm-.71-4.95l-1.41-1.41-2.12 2.12 1.41 1.41 2.12-2.12zm-9.9 0L9.17 7.76l-1.41 1.41L8.46 10.6l1.41-1.41zM20.46 2.29l-1.41 1.41-2.12-2.12 1.41-1.41c.39-.39 1.02-.39 1.41 0l.71.71c.39.39.39 1.02 0 1.41zm-14.02 0L3.64 3.05l2.12 2.12 1.41-1.41c.39-.39.39-1.02 0-1.41l-.71-.71c-.39-.39-1.02-.39-1.41 0zM12 6c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm-1 8h2v2h-2v-2zm0-4h2v2h-2v-2z"/></svg> Installation

<div align="center">

### Installation depuis le dépôt GitHub

```bash
pip install git+https://github.com/Samvel070903/MewsConnector.git
```

### Installation en mode développement

```bash
git clone https://github.com/Samvel070903/MewsConnector.git
cd MewsConnector
pip install -e .
```

### Installation avec dépendances de développement

```bash
pip install -e ".[dev]"
```

</div>

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M13 3L4 14h7v7l9-11h-7z"/></svg> Démarrage rapide

<div style="background-color: #f6f8fa; padding: 20px; border-radius: 8px; border-left: 4px solid #0366d6; margin: 20px 0;">

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M9 21c0 .5.4 1 1 1h4c.6 0 1-.5 1-1v-1H9v1zm3-19C8.1 2 5 5.1 5 9c0 2.4 1.2 4.5 3 5.7V17c0 .5.4 1 1 1h6c.6 0 1-.5 1-1v-2.3c1.8-1.3 3-3.4 3-5.7 0-3.9-3.1-7-7-7z"/></svg> Exemple basique

```python
from mews import MewsClient

client = MewsClient(
    platform_address="https://api.mews-demo.com",
    client_token="E0D439EE522F44368DC78E1BFB03710C-...",
    access_token="C66EF7B239D24632943D115EDE9CB810-...",
    client="MonApp 1.0",
)

# Récupérer la configuration de l'établissement
config = client.configuration.get()
print(config["Enterprise"]["Name"])

# Lister les clients
customers = client.customers.get_all()

# Créer un client
client.customers.add(
    first_name="Jean",
    last_name="Dupont",
    email="j@example.com"
)
```

</div>

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M17 8h-1V6c0-2.76-2.24-5-5-5S6 3.24 6 6v2H5c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM9 6c0-1.66 1.34-3 3-3s3 1.34 3 3v2H9V6zm9 14H6V10h12v10zm-6-3c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z"/></svg> Configuration via variables d'environnement

<div style="background-color: #fff4e6; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800; margin: 15px 0;">

**Créez un fichier `.env` :**

```env
MEWS_PLATFORM_ADDRESS=https://api.mews-demo.com
MEWS_CLIENT_TOKEN=votre_token
MEWS_ACCESS_TOKEN=votre_token
MEWS_CLIENT=MonApp 1.0
```

**Puis utilisez :**

```python
from mews import MewsClient
client = MewsClient()  # chargement automatique depuis .env
```

</div>

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg> Documentation des opérations

<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50; margin: 15px 0;">

<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> **Astuce** : Tous les endpoints supportant la pagination gèrent automatiquement les curseurs. Vous n'avez qu'à appeler la méthode et tous les résultats seront retournés.

</div>

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.07.62-.07.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg> Configuration

<table>
<tr>
<th>Méthode</th>
<th>Description</th>
<th>Exemple</th>
</tr>
<tr>
<td><code>get()</code></td>
<td>Configuration complète de l'établissement</td>
<td>

```python
config = client.configuration.get()
```

</td>
</tr>
<tr>
<td><code>get_countries()</code></td>
<td>Liste des pays supportés</td>
<td>

```python
countries = client.configuration.get_countries()
```

</td>
</tr>
<tr>
<td><code>get_currencies()</code></td>
<td>Liste des devises</td>
<td>

```python
currencies = client.configuration.get_currencies()
```

</td>
</tr>
<tr>
<td><code>get_languages()</code></td>
<td>Liste des langues</td>
<td>

```python
languages = client.configuration.get_languages()
```

</td>
</tr>
<tr>
<td><code>get_tax_environments()</code></td>
<td>Environnements fiscaux</td>
<td>

```python
tax_envs = client.configuration.get_tax_environments()
```

</td>
</tr>
</table>

#### Exemple complet

```python
# Récupérer la configuration
config = client.configuration.get()
print(config["Enterprise"]["Name"])

# Obtenir les pays
countries = client.configuration.get_countries()
print(countries["Countries"])
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg> Enterprises

<table>
<tr>
<th>Méthode</th>
<th>Description</th>
</tr>
<tr>
<td><code>get()</code></td>
<td>Détails de l'établissement</td>
</tr>
<tr>
<td><code>get_departments()</code></td>
<td>Tous les départements</td>
</tr>
<tr>
<td><code>get_counters()</code></td>
<td>Compteurs (numérotation factures)</td>
</tr>
<tr>
<td><code>get_age_categories()</code></td>
<td>Catégories d'âge</td>
</tr>
<tr>
<td><code>get_cancellation_policies()</code></td>
<td>Politiques d'annulation</td>
</tr>
</table>

#### Exemple

```python
enterprises = client.enterprises.get()
departments = client.enterprises.get_departments()
counters = client.enterprises.get_counters()
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg> Customers

<div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; margin: 15px 0;">

<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg> **Pagination automatique** : Toutes les méthodes de récupération gèrent automatiquement la pagination.

</div>

#### Méthodes principales

| Méthode | Description | Pagination |
|---------|-------------|------------|
| `get_all()` | Liste tous les clients avec filtres | <img src="https://img.shields.io/badge/Auto-success?style=flat-square" height="16"/> |
| `get_by_ids()` | Par identifiants | <img src="https://img.shields.io/badge/Auto-success?style=flat-square" height="16"/> |
| `get_by_emails()` | Par emails | <img src="https://img.shields.io/badge/Auto-success?style=flat-square" height="16"/> |
| `add()` | Créer un client | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `update()` | Mettre à jour | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `merge()` | Fusionner deux profils | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `search()` | Recherche par nom | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |

#### Exemples

<details>
<summary><strong><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M21 5c-1.11-.35-2.33-.5-3.5-.5-1.95 0-4.05.4-5.5 1.5-1.45-1.1-3.55-1.5-5.5-1.5S2.45 4.9 1 6v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1zm0 13.5c-1.1-.35-2.3-.5-3.5-.5-1.7 0-4.15.65-5.5 1.5V8c1.35-.85 3.8-1.5 5.5-1.5 1.2 0 2.4.15 3.5.5v11.5z"/></svg> Voir tous les exemples Customers</strong></summary>

```python
# Récupérer tous les clients (pagination auto)
customers = client.customers.get_all()

# Par identifiants
customers = client.customers.get_all(
    customer_ids=["uuid1", "uuid2"]
)

# Par emails
customers = client.customers.get_all(
    emails=["client@example.com"]
)

# Par dates de mise à jour
customers = client.customers.get_all(
    updated_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)

# Créer un client
customer = client.customers.add(
    last_name="Dupont",
    first_name="Jean",
    email="jean.dupont@example.com",
    phone="+33123456789",
    nationality_code="FR"
)

# Mettre à jour
customer = client.customers.update(
    customer_id="uuid-du-client",
    email="nouveau.email@example.com"
)

# Fusionner deux profils
result = client.customers.merge(
    source_id="uuid-source",
    target_id="uuid-cible"
)
```

</details>

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg> Reservations

#### Méthodes principales

| Méthode | Description | Pagination |
|---------|-------------|------------|
| `get_all()` | Liste toutes les réservations | <img src="https://img.shields.io/badge/Auto-success?style=flat-square" height="16"/> |
| `get_by_ids()` | Par identifiants | <img src="https://img.shields.io/badge/Auto-success?style=flat-square" height="16"/> |
| `price()` | Calculer le prix | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `add()` | Créer une réservation | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `update()` | Mettre à jour | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `confirm()` | Confirmer | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `cancel()` | Annuler | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `start()` | Check-in | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `process()` | Check-out | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `assign_resource()` | Assigner une chambre | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `add_companion()` | Ajouter accompagnant | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |
| `delete_companion()` | Supprimer accompagnant | <img src="https://img.shields.io/badge/Non-critical?style=flat-square" height="16"/> |

#### Exemples

<details>
<summary><strong><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M21 5c-1.11-.35-2.33-.5-3.5-.5-1.95 0-4.05.4-5.5 1.5-1.45-1.1-3.55-1.5-5.5-1.5S2.45 4.9 1 6v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1zm0 13.5c-1.1-.35-2.3-.5-3.5-.5-1.7 0-4.15.65-5.5 1.5V8c1.35-.85 3.8-1.5 5.5-1.5 1.2 0 2.4.15 3.5.5v11.5z"/></svg> Voir tous les exemples Reservations</strong></summary>

```python
# Récupérer les réservations
reservations = client.reservations.get_all(
    states=["Confirmed", "Started"]
)

# Calculer le prix
pricing = client.reservations.price(
    service_id="uuid-service",
    start_utc="2024-06-01T14:00:00Z",
    end_utc="2024-06-05T11:00:00Z",
    adult_count=2,
    child_count=1
)

# Créer une réservation
result = client.reservations.add(
    service_id="uuid-service",
    reservations=[{
        "StartUtc": "2024-06-01T14:00:00Z",
        "EndUtc": "2024-06-05T11:00:00Z",
        "AdultCount": 2,
        "CustomerId": "uuid-client"
    }]
)

# Confirmer
client.reservations.confirm(["uuid-reservation"])

# Check-in
client.reservations.start(["uuid-reservation"])

# Check-out
client.reservations.process(["uuid-reservation"])
```

</details>

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm.31-8.86c-1.77-.45-2.34-.94-2.34-1.67 0-.84.79-1.43 2.1-1.43 1.38 0 1.9.66 1.94 1.64h1.71c-.05-1.34-.87-2.57-2.49-2.97V5H10.9v1.69c-1.51.32-2.72 1.3-2.72 2.81 0 1.79 1.49 2.69 3.66 3.21 1.95.46 2.34 1.24 2.34 2.05 0 .73-.4 1.24-1.65 1.24-1.38 0-2-.61-2.1-1.64H8.04c.1 1.7 1.36 2.66 2.86 2.97V19h2.34v-1.67c1.52-.29 2.72-1.16 2.72-2.77 0-2.1-1.9-2.96-3.65-3.42z"/></svg> Services

```python
# Tous les services
services = client.services.get_all()

# Disponibilité
availability = client.services.get_availability(
    service_id="uuid-service",
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z"
)

# Tarification
pricing = client.services.get_pricing(
    service_id="uuid-service",
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z"
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg> Resources

```python
# Toutes les ressources
resources = client.resources.get_all()

# Catégories
categories = client.resources.get_categories()

# Mettre à jour une ressource
client.resources.update(
    resource_id="uuid-resource",
    Name="Chambre 101",
    State="Clean"
)

# Blocages
blocks = client.resources.get_blocks(
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z"
)

# Créer un blocage
client.resources.add_block(
    resource_id="uuid-resource",
    start_utc="2024-06-15T00:00:00Z",
    end_utc="2024-06-20T23:59:59Z",
    reason="Maintenance"
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/></svg> Rates

```python
# Tous les tarifs
rates = client.rates.get_all()

# Tarification d'un tarif
pricing = client.rates.get_pricing(
    rate_id="uuid-rate",
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z"
)

# Mettre à jour les prix
client.rates.update_price(
    rate_id="uuid-rate",
    resource_category_id="uuid-category",
    price_updates=[{
        "StartUtc": "2024-06-01T00:00:00Z",
        "EndUtc": "2024-06-15T23:59:59Z",
        "Value": 150.00
    }]
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg> Payments

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800; margin: 15px 0;">

<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> **Note** : La méthode `get_all()` utilise par défaut les 90 derniers jours si aucun filtre n'est fourni.

</div>

```python
# Tous les paiements
payments = client.payments.get_all()

# Par facture
payments = client.payments.get_all(bill_ids=["uuid-bill"])

# Ajouter un paiement
result = client.payments.add(
    customer_id="uuid-client",
    amount=150.50,
    currency="EUR",
    payment_type="CreditCard",
    notes="Paiement réservation"
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg> Bills

```python
# Toutes les factures
bills = client.bills.get_all()

# Par client
bills = client.bills.get_all(customer_ids=["uuid-client"])

# Clôturer une facture
result = client.bills.close(bill_id="uuid-bill")

# Récupérer le PDF (base64)
result = client.bills.get_pdf(bill_id="uuid-bill")
pdf_data = result["PdfData"]
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M5 9.2h3V19H5zM10.6 5h2.8v14h-2.8zm5.6 8H19v6h-2.8z"/></svg> Accounting

```python
# Éléments comptables
items = client.accounting.get_all()

# Par dates
items = client.accounting.get_all(
    start_utc="2024-01-01T00:00:00Z",
    end_utc="2024-12-31T23:59:59Z"
)

# Par états
items = client.accounting.get_all(states=["Open", "Closed"])
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg> Companies

```python
# Toutes les entreprises
companies = client.companies.get_all()

# Créer
result = client.companies.add(name="Entreprise ABC")

# Mettre à jour
result = client.companies.update(
    company_id="uuid-company",
    Name="Entreprise XYZ"
)

# Supprimer
result = client.companies.delete(company_id="uuid-company")
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"/></svg> Products

```python
# Tous les produits
products = client.products.get_all()

# Ajouter à une réservation
result = client.products.add_to_reservation(
    reservation_id="uuid-reservation",
    product_id="uuid-product",
    count=2
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M7 18c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12L8.1 13h7.45c.75 0 1.41-.41 1.75-1.03L21.7 4H5.21l-.94-2H1zm16 16c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg> Outlets

```python
# Tous les points de vente
outlets = client.outlets.get_all()

# Éléments de point de vente
items = client.outlets.get_items(
    outlet_ids=["uuid-outlet"]
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm7 18H5V5h2v3h10V5h2v16z"/></svg> Orders

```python
# Toutes les commandes
orders = client.orders.get_all()

# Créer une commande
result = client.orders.add(
    service_id="uuid-service",
    customer_id="uuid-client"
)

# Annuler
result = client.orders.cancel(
    order_id="uuid-order",
    reason="Annulation client"
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M17 1.01L7 1c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-1.99-2-1.99zM17 19H7V5h10v14z"/></svg> Devices

```python
# Tous les appareils
devices = client.devices.get_all()

# Commandes d'appareils
commands = client.devices.get_commands(
    states=["Pending", "Processed"]
)

# Mettre à jour une commande
result = client.devices.update_command(
    command_id="uuid-command",
    state="Processed"
)
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"/></svg> Loyalty

```python
# Programmes de fidélité
programs = client.loyalty.get_programs()

# Adhésions
memberships = client.loyalty.get_memberships(
    customer_ids=["uuid-client"]
)

# Ajouter une adhésion
result = client.loyalty.add_membership(
    customer_id="uuid-client",
    loyalty_program_id="uuid-program",
    code="MEMBER123"
)

# Niveaux de fidélité
tiers = client.loyalty.get_tiers(loyalty_program_id="uuid-program")
```

---

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M20 4H4c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 6H4V6h16v4zm-2 2H6c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zm-2 6H8v-4h8v4z"/></svg> Vouchers

```python
# Tous les bons
vouchers = client.vouchers.get_all()

# Créer un bon
result = client.vouchers.add(
    service_id="uuid-service",
    rate_id="uuid-rate",
    code="PROMO2024",
    start_utc="2024-01-01T00:00:00Z",
    end_utc="2024-12-31T23:59:59Z"
)

# Supprimer
result = client.vouchers.delete(voucher_id="uuid-voucher")
```

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg> Gestion des erreurs

<div style="background-color: #ffebee; padding: 20px; border-radius: 8px; border-left: 4px solid #f44336; margin: 20px 0;">

### <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg> Exceptions disponibles

Le wrapper fournit des exceptions spécifiques pour chaque type d'erreur :

</div>

```python
from mews import (
    MewsClient,
    MewsAuthError,
    MewsRateLimitError,
    MewsAPIError,
    MewsValidationError,
    MewsNotFoundError
)

try:
    client.configuration.get()
except MewsAuthError:
    print("❌ Token invalide ou expiré")
except MewsRateLimitError:
    print("⏱️ Limite de requêtes atteinte — réessayez plus tard")
except MewsValidationError:
    print("✏️ Erreur de validation des données")
except MewsNotFoundError:
    print("🔍 Ressource non trouvée")
except MewsAPIError as e:
    print(f"⚠️ Erreur API : {e.message} [{e.error_code}]")
```

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg> Pagination

<div style="background-color: #e8f5e9; padding: 20px; border-radius: 8px; border-left: 4px solid #4caf50; margin: 20px 0;">

### <img src="https://img.shields.io/badge/Auto-success?style=flat-square" height="18" style="vertical-align: middle;"/> Pagination automatique

Les endpoints supportant la pagination `Limitation` de Mews gèrent automatiquement les curseurs. Vous obtenez **tous** les résultats sans vous soucier de la pagination.

</div>

```python
# Retourne TOUS les clients, en gérant les curseurs automatiquement
tous_les_clients = client.customers.get_all(page_size=200)

# Même chose pour les réservations, paiements, factures, etc.
toutes_les_reservations = client.reservations.get_all()
tous_les_paiements = client.payments.get_all()
```

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg> Développement

### Prérequis

- Python 3.9 ou supérieur
- pip

### Installation des dépendances de développement

```bash
pip install -e ".[dev]"
```

### Exécution des tests

```bash
pytest
```

### Formatage et linting

```bash
ruff check .
ruff format .
```

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M20.34 9.32l-1.41-1.41c-.56-.56-1.45-.56-2.01 0L16 9.5l-2.83-2.83c-.56-.56-1.45-.56-2.01 0l-1.41 1.41c-.56.56-.56 1.45 0 2.01L10.5 13l-2.83 2.83c-.56.56-.56 1.45 0 2.01l1.41 1.41c.56.56 1.45.56 2.01 0L13 16.5l2.83 2.83c.56.56 1.45.56 2.01 0l1.41-1.41c.56-.56.56-1.45 0-2.01L15.5 13l2.83-2.83c.57-.56.57-1.45.01-2.01zM9.5 8.5l-2.83-2.83c-.56-.56-1.45-.56-2.01 0L3.5 7.5c-.56.56-.56 1.45 0 2.01L6.33 12.34c.56.56 1.45.56 2.01 0L10.5 11.5l-1-1zm-4-4l-1.41-1.41c-.56-.56-1.45-.56-2.01 0L1.5 3.5c-.56.56-.56 1.45 0 2.01L4.33 8.34c.56.56 1.45.56 2.01 0L7.5 7.5l-2-2z"/></svg> Contribution

<div align="center">

Les contributions sont les bienvenues ! 🎉

</div>

### Comment contribuer

1. **Forkez** le projet
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Commitez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrez** une Pull Request

<div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; margin: 15px 0;">

<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M9 21c0 .5.4 1 1 1h4c.6 0 1-.5 1-1v-1H9v1zm3-19C8.1 2 5 5.1 5 9c0 2.4 1.2 4.5 3 5.7V17c0 .5.4 1 1 1h6c.6 0 1-.5 1-1v-2.3c1.8-1.3 3-3.4 3-5.7 0-3.9-3.1-7-7-7z"/></svg> **Conseil** : Assurez-vous que vos changements passent les tests et respectent le style de code (Ruff).

</div>

---

## <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg> Licence

<div align="center">

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<div align="center">

**Fait avec ❤️ pour la communauté Python**

[<img src="https://img.shields.io/badge/Donnez_une_étoile-ffd700?style=for-the-badge&logo=github" height="30"/>](https://github.com/Samvel070903/MewsConnector) si ce projet vous est utile !

</div>
