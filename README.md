# Mews Connector — Wrapper Python
<img width="480" height="105" alt="Mews2" src="https://github.com/user-attachments/assets/5c8785b4-d906-4cba-8b73-169e58912625" />


[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Un wrapper Python professionnel et entièrement typé pour l'[API Mews Connector](https://mews-systems.gitbook.io/connector-api/).

## 📋 Table des matières

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

## Installation

### Installation depuis le dépôt

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

## Démarrage rapide

```python
from mews import MewsClient

client = MewsClient(
    platform_address="https://api.mews-demo.com",
    client_token="E0D439EE522F44368DC78E1BFB03710C-...",
    access_token="C66EF7B239D24632943D115EDE9CB810-...",
    client="MonApp 1.0",
)
```

### Depuis les variables d'environnement

Créez un fichier `.env` :

```env
MEWS_PLATFORM_ADDRESS=https://api.mews-demo.com
MEWS_CLIENT_TOKEN=votre_token
MEWS_ACCESS_TOKEN=votre_token
MEWS_CLIENT=MonApp 1.0
```

```python
from mews import MewsClient
client = MewsClient()  # chargement automatique depuis .env
```

---

## Documentation des opérations

### Configuration

#### `get()`

Récupère la configuration complète de l'établissement.

```python
config = client.configuration.get()
print(config["Enterprise"]["Name"])
```

#### `get_countries()`

Récupère tous les pays supportés.

```python
countries = client.configuration.get_countries()
print(countries["Countries"])
```

#### `get_currencies()`

Récupère toutes les devises supportées.

```python
currencies = client.configuration.get_currencies()
print(currencies["Currencies"])
```

#### `get_languages()`

Récupère toutes les langues supportées.

```python
languages = client.configuration.get_languages()
print(languages["Languages"])
```

#### `get_tax_environments()`

Récupère les environnements fiscaux de l'établissement.

```python
tax_envs = client.configuration.get_tax_environments()
print(tax_envs["TaxEnvironments"])
```

---

### Enterprises

#### `get()`

Récupère les détails de l'établissement actuel.

```python
enterprises = client.enterprises.get()
print(enterprises["Enterprises"])
```

#### `get_departments()`

Récupère tous les départements.

```python
departments = client.enterprises.get_departments()
print(departments["Departments"])
```

#### `get_counters()`

Récupère tous les compteurs (ex. numérotation des factures).

```python
counters = client.enterprises.get_counters()
print(counters["Counters"])
```

#### `get_age_categories()`

Récupère les catégories d'âge.

```python
age_categories = client.enterprises.get_age_categories()
print(age_categories["AgeCategories"])
```

#### `get_cancellation_policies()`

Récupère les politiques d'annulation.

```python
policies = client.enterprises.get_cancellation_policies()
print(policies["CancellationPolicies"])
```

---

### Customers

#### `get_all()`

Récupère les clients avec des filtres optionnels. Pagination automatique.

```python
# Sans filtre (utilise UpdatedUtc des 90 derniers jours par défaut)
customers = client.customers.get_all()

# Par identifiants
customers = client.customers.get_all(customer_ids=["uuid1", "uuid2"])

# Par emails
customers = client.customers.get_all(emails=["client@example.com"])

# Par dates de mise à jour
customers = client.customers.get_all(
    updated_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)

# Avec extent pour inclure des sous-objets
customers = client.customers.get_all(
    customer_ids=["uuid1"],
    extent={"Addresses": True, "Documents": True}
)
```

#### `get_by_ids()`

Raccourci pour récupérer des clients par leurs identifiants.

```python
customers = client.customers.get_by_ids(["uuid1", "uuid2"])
```

#### `get_by_emails()`

Raccourci pour rechercher des clients par adresse email.

```python
customers = client.customers.get_by_emails(["client@example.com"])
```

#### `add()`

Crée un nouveau profil client.

```python
customer = client.customers.add(
    last_name="Dupont",
    first_name="Jean",
    email="jean.dupont@example.com",
    phone="+33123456789",
    nationality_code="FR"
)
print(customer["Customer"])
```

#### `update()`

Met à jour un client existant.

```python
customer = client.customers.update(
    customer_id="uuid-du-client",
    email="nouveau.email@example.com",
    phone="+33987654321"
)
print(customer["Customer"])
```

#### `merge()`

Fusionne deux profils clients.

```python
result = client.customers.merge(
    source_id="uuid-source",
    target_id="uuid-cible"
)
print(result["Customer"])
```

#### `search()`

Recherche des clients par nom.

```python
results = client.customers.search(name="Dupont")
print(results)
```

---

### Reservations

#### `get_all()`

Récupère les réservations avec des filtres optionnels. Pagination automatique.

```python
# Sans filtre (utilise UpdatedUtc des 90 derniers jours par défaut)
reservations = client.reservations.get_all()

# Par identifiants
reservations = client.reservations.get_all(reservation_ids=["uuid1", "uuid2"])

# Par client
reservations = client.reservations.get_all(customer_ids=["uuid-client"])

# Par états
reservations = client.reservations.get_all(states=["Confirmed", "Started"])

# Par dates
reservations = client.reservations.get_all(
    start_utc={"StartUtc": "2024-01-01T00:00:00Z", "EndUtc": "2024-12-31T23:59:59Z"}
)
```

#### `get_by_ids()`

Raccourci pour récupérer des réservations par leurs identifiants.

```python
reservations = client.reservations.get_by_ids(["uuid1", "uuid2"])
```

#### `price()`

Calcule le prix d'une réservation sans créer de réservation.

```python
pricing = client.reservations.price(
    service_id="uuid-service",
    start_utc="2024-06-01T14:00:00Z",
    end_utc="2024-06-05T11:00:00Z",
    adult_count=2,
    child_count=1,
    rate_id="uuid-rate"
)
print(pricing)
```

#### `add()`

Crée une ou plusieurs réservations.

```python
result = client.reservations.add(
    service_id="uuid-service",
    reservations=[
        {
            "StartUtc": "2024-06-01T14:00:00Z",
            "EndUtc": "2024-06-05T11:00:00Z",
            "AdultCount": 2,
            "ChildCount": 1,
            "CustomerId": "uuid-client"
        }
    ]
)
print(result["Reservations"])
```

#### `update()`

Met à jour une réservation existante.

```python
result = client.reservations.update(
    reservation_id="uuid-reservation",
    AdultCount=3,
    Notes="Demande spéciale"
)
print(result["Reservations"])
```

#### `confirm()`

Confirme une ou plusieurs réservations.

```python
result = client.reservations.confirm(["uuid-reservation-1", "uuid-reservation-2"])
print(result["Reservations"])
```

#### `cancel()`

Annule une ou plusieurs réservations.

```python
result = client.reservations.cancel(
    reservation_ids=["uuid-reservation-1"],
    reason="Annulation client"
)
print(result["Reservations"])
```

#### `start()`

Démarre (check-in) des réservations.

```python
result = client.reservations.start(["uuid-reservation-1"])
print(result["Reservations"])
```

#### `process()`

Traite (check-out) des réservations.

```python
result = client.reservations.process(["uuid-reservation-1"])
print(result["Reservations"])
```

#### `assign_resource()`

Assigne une ressource spécifique (chambre) à une réservation.

```python
result = client.reservations.assign_resource(
    reservation_id="uuid-reservation",
    resource_id="uuid-resource"
)
print(result["Reservations"])
```

#### `add_companion()`

Ajoute un accompagnant à une réservation.

```python
result = client.reservations.add_companion(
    reservation_id="uuid-reservation",
    customer_id="uuid-client"
)
print(result["Reservations"])
```

#### `delete_companion()`

Supprime un accompagnant d'une réservation.

```python
result = client.reservations.delete_companion(
    reservation_id="uuid-reservation",
    customer_id="uuid-client"
)
print(result["Reservations"])
```

---

### Services

#### `get_all()`

Récupère tous les services de l'établissement.

```python
services = client.services.get_all()
print(services["Services"])
```

#### `get_availability()`

Récupère la disponibilité des ressources pour un service.

```python
availability = client.services.get_availability(
    service_id="uuid-service",
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z",
    resource_category_id="uuid-category"
)
print(availability)
```

#### `get_pricing()`

Récupère la tarification d'un service sur une période.

```python
pricing = client.services.get_pricing(
    service_id="uuid-service",
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z"
)
print(pricing)
```

---

### Resources

#### `get_all()`

Récupère toutes les ressources (chambres, espaces…).

```python
# Toutes les ressources
resources = client.resources.get_all()

# Par identifiants
resources = client.resources.get_all(resource_ids=["uuid1", "uuid2"])

# Avec extent
resources = client.resources.get_all(extent={"Category": True})
print(resources["Resources"])
```

#### `get_categories()`

Récupère les catégories de ressources (types de chambre).

```python
categories = client.resources.get_categories()
print(categories["ResourceCategories"])
```

#### `update()`

Met à jour une ressource.

```python
result = client.resources.update(
    resource_id="uuid-resource",
    Name="Chambre 101",
    State="Clean"
)
print(result["Resource"])
```

#### `get_blocks()`

Récupère les blocages de ressources (hors service, maintenance…).

```python
blocks = client.resources.get_blocks(
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z",
    resource_ids=["uuid-resource"]
)
print(blocks["ResourceBlocks"])
```

#### `add_block()`

Crée un blocage de ressource.

```python
result = client.resources.add_block(
    resource_id="uuid-resource",
    start_utc="2024-06-15T00:00:00Z",
    end_utc="2024-06-20T23:59:59Z",
    reason="Maintenance"
)
print(result["ResourceBlock"])
```

#### `delete_block()`

Supprime un blocage de ressource.

```python
result = client.resources.delete_block("uuid-block")
print(result)
```

---

### Rates

#### `get_all()`

Récupère tous les tarifs.

```python
# Tous les tarifs
rates = client.rates.get_all()

# Par service
rates = client.rates.get_all(service_id="uuid-service")

# Avec extent
rates = client.rates.get_all(extent={"Prices": True})
print(rates["Rates"])
```

#### `get_pricing()`

Récupère la tarification d'un tarif spécifique sur une période.

```python
pricing = client.rates.get_pricing(
    rate_id="uuid-rate",
    start_utc="2024-06-01T00:00:00Z",
    end_utc="2024-06-30T23:59:59Z"
)
print(pricing)
```

#### `update_price()`

Met à jour les prix d'un tarif.

```python
result = client.rates.update_price(
    rate_id="uuid-rate",
    resource_category_id="uuid-category",
    price_updates=[
        {
            "StartUtc": "2024-06-01T00:00:00Z",
            "EndUtc": "2024-06-15T23:59:59Z",
            "Value": 150.00
        }
    ]
)
print(result)
```

---

### Payments

#### `get_all()`

Récupère les paiements avec des filtres optionnels. Pagination automatique.

```python
# Sans filtre (utilise CreatedUtc des 90 derniers jours par défaut)
payments = client.payments.get_all()

# Par identifiants de paiements
payments = client.payments.get_all(payment_ids=["uuid1", "uuid2"])

# Par factures
payments = client.payments.get_all(bill_ids=["uuid-bill"])

# Par réservations
payments = client.payments.get_all(reservation_ids=["uuid-reservation"])

# Par dates de création
payments = client.payments.get_all(
    created_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)
```

#### `add()`

Ajoute un paiement.

```python
result = client.payments.add(
    customer_id="uuid-client",
    amount=150.50,
    currency="EUR",
    payment_type="CreditCard",
    notes="Paiement réservation"
)
print(result["Payment"])
```

---

### Bills

#### `get_all()`

Récupère les factures avec des filtres optionnels. Pagination automatique.

```python
# Sans filtre (utilise CreatedUtc des 90 derniers jours par défaut)
bills = client.bills.get_all()

# Par identifiants de factures
bills = client.bills.get_all(bill_ids=["uuid1", "uuid2"])

# Par clients
bills = client.bills.get_all(customer_ids=["uuid-client"])

# Par dates de création
bills = client.bills.get_all(
    created_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)

# Par dates de clôture
bills = client.bills.get_all(
    closed_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)
```

#### `close()`

Clôture une facture ouverte.

```python
result = client.bills.close(bill_id="uuid-bill")
print(result["Bill"])
```

#### `get_pdf()`

Récupère une facture au format PDF (retourne des données en base64).

```python
result = client.bills.get_pdf(bill_id="uuid-bill")
print(result["PdfData"])  # Données base64
```

---

### Accounting

#### `get_all()`

Récupère les éléments comptables avec des filtres optionnels. Pagination automatique.

```python
# Sans filtre (utilise ConsumedUtc des 90 derniers jours par défaut)
items = client.accounting.get_all()

# Par dates de consommation
items = client.accounting.get_all(
    start_utc="2024-01-01T00:00:00Z",
    end_utc="2024-12-31T23:59:59Z"
)

# Par clients
items = client.accounting.get_all(customer_ids=["uuid-client"])

# Par factures
items = client.accounting.get_all(bill_ids=["uuid-bill"])

# Par états
items = client.accounting.get_all(states=["Open", "Closed"])

# Avec extent
items = client.accounting.get_all(extent={"Product": True})
```

---

### Companies

#### `get_all()`

Récupère les entreprises. Pagination automatique.

```python
# Toutes les entreprises
companies = client.companies.get_all()

# Par identifiants
companies = client.companies.get_all(company_ids=["uuid1", "uuid2"])

# Par noms
companies = client.companies.get_all(names=["Entreprise A"])
```

#### `add()`

Crée une entreprise.

```python
result = client.companies.add(name="Entreprise ABC")
print(result["Company"])
```

#### `update()`

Met à jour une entreprise.

```python
result = client.companies.update(
    company_id="uuid-company",
    Name="Entreprise XYZ",
    TaxIdentificationNumber="123456789"
)
print(result["Company"])
```

#### `delete()`

Supprime une entreprise.

```python
result = client.companies.delete(company_id="uuid-company")
print(result)
```

---

### Products

#### `get_all()`

Récupère tous les produits.

```python
# Tous les produits
products = client.products.get_all()

# Par service
products = client.products.get_all(service_id="uuid-service")
print(products["Products"])
```

#### `add_to_reservation()`

Ajoute un produit à une réservation.

```python
result = client.products.add_to_reservation(
    reservation_id="uuid-reservation",
    product_id="uuid-product",
    count=2
)
print(result["Reservation"])
```

---

### Outlets

#### `get_all()`

Récupère tous les points de vente.

```python
outlets = client.outlets.get_all()
print(outlets["Outlets"])
```

#### `get_items()`

Récupère les éléments de point de vente (tickets/lignes POS). Pagination automatique.

```python
# Tous les éléments
items = client.outlets.get_items()

# Par points de vente
items = client.outlets.get_items(outlet_ids=["uuid-outlet"])

# Par dates de clôture
items = client.outlets.get_items(
    closed_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)
```

---

### Orders

#### `get_all()`

Récupère les commandes de services avec des filtres optionnels. Pagination automatique.

```python
# Sans filtre (utilise CreatedUtc des 90 derniers jours par défaut)
orders = client.orders.get_all()

# Par service
orders = client.orders.get_all(service_id="uuid-service")

# Par clients
orders = client.orders.get_all(customer_ids=["uuid-client"])

# Par états
orders = client.orders.get_all(states=["Pending", "Confirmed"])

# Par dates de création
orders = client.orders.get_all(
    created_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)
```

#### `add()`

Crée une commande de service.

```python
result = client.orders.add(
    service_id="uuid-service",
    customer_id="uuid-client"
)
print(result["ServiceOrder"])
```

#### `cancel()`

Annule une commande de service.

```python
result = client.orders.cancel(
    order_id="uuid-order",
    reason="Annulation client"
)
print(result["ServiceOrder"])
```

---

### Devices

#### `get_all()`

Récupère tous les appareils enregistrés.

```python
devices = client.devices.get_all()
print(devices["Devices"])
```

#### `get_commands()`

Récupère les commandes d'appareils. Pagination automatique.

```python
# Toutes les commandes
commands = client.devices.get_commands()

# Par appareils
commands = client.devices.get_commands(device_ids=["uuid-device"])

# Par états
commands = client.devices.get_commands(states=["Pending", "Processed"])

# Par dates de création
commands = client.devices.get_commands(
    created_utc={
        "StartUtc": "2024-01-01T00:00:00Z",
        "EndUtc": "2024-12-31T23:59:59Z"
    }
)
```

#### `update_command()`

Met à jour l'état d'une commande d'appareil.

```python
result = client.devices.update_command(
    command_id="uuid-command",
    state="Processed"
)
print(result["DeviceCommand"])
```

---

### Loyalty

#### `get_programs()`

Récupère tous les programmes de fidélité.

```python
programs = client.loyalty.get_programs()
print(programs["LoyaltyPrograms"])
```

#### `get_memberships()`

Récupère les adhésions de fidélité. Pagination automatique.

```python
# Toutes les adhésions
memberships = client.loyalty.get_memberships()

# Par clients
memberships = client.loyalty.get_memberships(customer_ids=["uuid-client"])

# Par programmes
memberships = client.loyalty.get_memberships(loyalty_program_ids=["uuid-program"])
```

#### `add_membership()`

Ajoute une adhésion de fidélité à un client.

```python
result = client.loyalty.add_membership(
    customer_id="uuid-client",
    loyalty_program_id="uuid-program",
    code="MEMBER123"
)
print(result["LoyaltyMembership"])
```

#### `get_tiers()`

Récupère les niveaux de fidélité d'un programme.

```python
tiers = client.loyalty.get_tiers(loyalty_program_id="uuid-program")
print(tiers["LoyaltyTiers"])
```

---

### Vouchers

#### `get_all()`

Récupère les bons. Pagination automatique.

```python
# Tous les bons
vouchers = client.vouchers.get_all()

# Par identifiants
vouchers = client.vouchers.get_all(voucher_ids=["uuid1", "uuid2"])

# Par services
vouchers = client.vouchers.get_all(service_ids=["uuid-service"])
```

#### `add()`

Crée un bon.

```python
result = client.vouchers.add(
    service_id="uuid-service",
    rate_id="uuid-rate",
    code="PROMO2024",
    start_utc="2024-01-01T00:00:00Z",
    end_utc="2024-12-31T23:59:59Z"
)
print(result["Voucher"])
```

#### `delete()`

Supprime un bon.

```python
result = client.vouchers.delete(voucher_id="uuid-voucher")
print(result)
```

---

## Gestion des erreurs

```python
from mews import MewsClient, MewsAuthError, MewsRateLimitError, MewsAPIError

try:
    client.configuration.get()
except MewsAuthError:
    print("Token invalide ou expiré")
except MewsRateLimitError:
    print("Limite de requêtes atteinte — réessayez plus tard")
except MewsAPIError as e:
    print(f"Erreur API : {e.message} [{e.error_code}]")
```

## Pagination

Les endpoints supportant la pagination ``Limitation`` de Mews sont automatiquement paginés :

```python
# Retourne TOUS les clients, en gérant les curseurs de manière transparente
tous_les_clients = client.customers.get_all(page_size=200)
```

## Développement

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

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
