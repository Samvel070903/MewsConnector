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
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/api.svg" width="24" height="24" style="vertical-align: middle;"/><br/>
<strong>API Complète</strong><br/>
Support de tous les endpoints Mews
</td>
<td align="center" width="33%">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle;"><path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z" fill="currentColor"/></svg><br/>
<strong>Pagination Auto</strong><br/>
Gestion automatique des curseurs
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/typescript.svg" width="24" height="24" style="vertical-align: middle;"/><br/>
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
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/lock.svg" width="24" height="24" style="vertical-align: middle;"/><br/>
<strong>Sécurisé</strong><br/>
Gestion sécurisée des tokens
</td>
<td align="center" width="33%">
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/book.svg" width="24" height="24" style="vertical-align: middle;"/><br/>
<strong>Documentation</strong><br/>
Exemples pour chaque endpoint
</td>
</tr>
</table>

</div>

---

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/list.svg" width="20" height="20" style="vertical-align: middle;"/> Table des matières

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/rocket.svg" width="20" height="20" style="vertical-align: middle;"/> Installation

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/zap.svg" width="20" height="20" style="vertical-align: middle;"/> Démarrage rapide

<div style="background-color: #f6f8fa; padding: 20px; border-radius: 8px; border-left: 4px solid #0366d6; margin: 20px 0;">

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/lightbulb.svg" width="18" height="18" style="vertical-align: middle;"/> Exemple basique

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/key.svg" width="18" height="18" style="vertical-align: middle;"/> Configuration via variables d'environnement

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/book.svg" width="20" height="20" style="vertical-align: middle;"/> Documentation des opérations

<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50; margin: 15px 0;">

<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/info.svg" width="16" height="16" style="vertical-align: middle;"/> **Astuce** : Tous les endpoints supportant la pagination gèrent automatiquement les curseurs. Vous n'avez qu'à appeler la méthode et tous les résultats seront retournés.

</div>

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/settings.svg" width="18" height="18" style="vertical-align: middle;"/> Configuration

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/building.svg" width="18" height="18" style="vertical-align: middle;"/> Enterprises

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/users.svg" width="18" height="18" style="vertical-align: middle;"/> Customers

<div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; margin: 15px 0;">

<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/search.svg" width="16" height="16" style="vertical-align: middle;"/> **Pagination automatique** : Toutes les méthodes de récupération gèrent automatiquement la pagination.

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
<summary><strong><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/bookopen.svg" width="16" height="16" style="vertical-align: middle;"/> Voir tous les exemples Customers</strong></summary>

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/calendar.svg" width="18" height="18" style="vertical-align: middle;"/> Reservations

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
<summary><strong><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/bookopen.svg" width="16" height="16" style="vertical-align: middle;"/> Voir tous les exemples Reservations</strong></summary>

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/target.svg" width="18" height="18" style="vertical-align: middle;"/> Services

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/home.svg" width="18" height="18" style="vertical-align: middle;"/> Resources

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/dollar.svg" width="18" height="18" style="vertical-align: middle;"/> Rates

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/creditcard.svg" width="18" height="18" style="vertical-align: middle;"/> Payments

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800; margin: 15px 0;">

<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/info.svg" width="16" height="16" style="vertical-align: middle;"/> **Note** : La méthode `get_all()` utilise par défaut les 90 derniers jours si aucun filtre n'est fourni.

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/filetext.svg" width="18" height="18" style="vertical-align: middle;"/> Bills

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/bar-chart.svg" width="18" height="18" style="vertical-align: middle;"/> Accounting

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/building.svg" width="18" height="18" style="vertical-align: middle;"/> Companies

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/package.svg" width="18" height="18" style="vertical-align: middle;"/> Products

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/shopping-cart.svg" width="18" height="18" style="vertical-align: middle;"/> Outlets

```python
# Tous les points de vente
outlets = client.outlets.get_all()

# Éléments de point de vente
items = client.outlets.get_items(
    outlet_ids=["uuid-outlet"]
)
```

---

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/clipboard.svg" width="18" height="18" style="vertical-align: middle;"/> Orders

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/smartphone.svg" width="18" height="18" style="vertical-align: middle;"/> Devices

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/gift.svg" width="18" height="18" style="vertical-align: middle;"/> Loyalty

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

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ticket.svg" width="18" height="18" style="vertical-align: middle;"/> Vouchers

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/alert-triangle.svg" width="20" height="20" style="vertical-align: middle;"/> Gestion des erreurs

<div style="background-color: #ffebee; padding: 20px; border-radius: 8px; border-left: 4px solid #f44336; margin: 20px 0;">

### <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/alert-circle.svg" width="18" height="18" style="vertical-align: middle;"/> Exceptions disponibles

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/file.svg" width="20" height="20" style="vertical-align: middle;"/> Pagination

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/tool.svg" width="20" height="20" style="vertical-align: middle;"/> Développement

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

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/handshake.svg" width="20" height="20" style="vertical-align: middle;"/> Contribution

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

<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/lightbulb.svg" width="16" height="16" style="vertical-align: middle;"/> **Conseil** : Assurez-vous que vos changements passent les tests et respectent le style de code (Ruff).

</div>

---

## <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/file-text.svg" width="20" height="20" style="vertical-align: middle;"/> Licence

<div align="center">

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<div align="center">

**Fait avec ❤️ pour la communauté Python**

[<img src="https://img.shields.io/badge/Donnez_une_étoile-ffd700?style=for-the-badge&logo=github" height="30"/>](https://github.com/Samvel070903/MewsConnector) si ce projet vous est utile !

</div>
