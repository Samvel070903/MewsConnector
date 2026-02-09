"""
Modèles pour les clients (profils invités).
============================================
"""

from __future__ import annotations

from typing import NotRequired, Required, TypedDict

from mews.models.base import Address, Document


class Customer(TypedDict, total=False):
    """
    Profil client conforme à 100% avec la structure réelle de l'API Mews.
    
    Ce modèle est basé sur la documentation officielle et les réponses réelles
    de l'API Mews Connector. Tous les champs sont typés strictement pour
    garantir la sécurité des entrées et sorties.
    """
    # Identifiants
    Id: str  # UUID du client
    ChainId: NotRequired[str]  # UUID de la chaîne hôtelière
    Number: NotRequired[str]  # Numéro de client (ex: "1456")
    
    # Informations personnelles de base
    Title: NotRequired[str | None]  # "Mr", "Mrs", "Ms", "Miss", "Dr", etc.
    Sex: NotRequired[str | None]  # "Male", "Female", etc.
    Gender: NotRequired[str | None]  # "Male", "Female", "Other", etc.
    FirstName: NotRequired[str | None]
    LastName: str  # Obligatoire selon l'API
    SecondLastName: NotRequired[str | None]  # Deuxième nom de famille
    
    # Informations de nationalité et langue
    NationalityCode: NotRequired[str | None]  # Code ISO 3166-1 alpha-2
    PreferredLanguageCode: NotRequired[str | None]  # Code ISO 639-1 de langue préférée
    LanguageCode: NotRequired[str | None]  # Code ISO 639-1 de langue actuelle
    
    # Informations de naissance
    BirthDate: NotRequired[str | None]  # Format "YYYY-MM-DD"
    BirthDateUtc: NotRequired[str | None]  # Format ISO 8601 UTC
    BirthPlace: NotRequired[str | None]  # Lieu de naissance (ex: "Pescara (BI)")
    
    # Informations professionnelles
    Occupation: NotRequired[str | None]  # Profession (ex: "Giornalista")
    
    # Informations de contact
    Email: NotRequired[str | None]
    HasOtaEmail: NotRequired[bool]  # Indique si l'email provient d'une OTA
    Phone: NotRequired[str | None]  # Format international recommandé
    
    # Informations fiscales et administratives
    TaxIdentificationNumber: NotRequired[str | None]  # Numéro d'identification fiscale
    ItalianFiscalCode: NotRequired[str | None]  # Code fiscal italien (Codice Fiscale)
    ItalianDestinationCode: NotRequired[str | None]  # Code destination italien
    
    # Codes de fidélité et comptabilité
    LoyaltyCode: NotRequired[str | None]  # Code de fidélité
    AccountingCode: NotRequired[str | None]  # Code comptable
    BillingCode: NotRequired[str | None]  # Code de facturation
    
    # Notes et informations supplémentaires
    Notes: NotRequired[str | None]  # Notes libres sur le client
    CarRegistrationNumber: NotRequired[str | None]  # Numéro d'immatriculation du véhicule
    DietaryRequirements: NotRequired[str | None]  # Exigences alimentaires
    
    # Dates de création et modification
    CreatedUtc: NotRequired[str]  # Format ISO 8601 UTC
    UpdatedUtc: NotRequired[str]  # Format ISO 8601 UTC
    DeletedUtc: NotRequired[str | None]  # Format ISO 8601 UTC si supprimé
    
    # Documents d'identité (peuvent être None ou des objets Document)
    Passport: NotRequired[Document | None]
    IdentityCard: NotRequired[Document | None]
    Visa: NotRequired[Document | None]
    DriversLicense: NotRequired[Document | None]
    
    # Adresse principale
    Address: NotRequired[Address | None]  # Adresse principale (objet complet)
    AddressId: NotRequired[str | None]  # UUID de l'adresse principale
    
    # Adresses multiples (pour compatibilité avec l'extent)
    Addresses: NotRequired[list[Address]]  # Liste de toutes les adresses
    
    # Documents multiples (pour compatibilité avec l'extent)
    Documents: NotRequired[list[Document]]  # Liste de tous les documents
    
    # Classifications et options
    Classifications: NotRequired[list[str]]  # Ex: ["Media", "Returning", "FriendOrFamily"]
    Options: NotRequired[list[str]]  # Ex: ["SendMarketingEmails", "Invoiceable"]
    
    # Catégorie et relations
    CategoryId: NotRequired[str | None]  # UUID de la catégorie de client
    CompanyId: NotRequired[str | None]  # UUID de l'entreprise associée
    MergeTargetId: NotRequired[str | None]  # UUID du client cible en cas de fusion
    
    # État et activité
    ActivityState: NotRequired[str]  # "Active", "Inactive", etc.
    IsActive: NotRequired[bool]  # Indicateur d'activité
    IsUpdatedByMe: NotRequired[bool | None]  # Indique si mis à jour par l'utilisateur actuel
    
    # Préférences d'espace
    PreferredSpaceFeatures: NotRequired[list[str]]  # Liste des caractéristiques d'espace préférées
    
    # Métadonnées de création/modification
    CreatorProfileId: NotRequired[str | None]  # UUID du profil créateur
    UpdaterProfileId: NotRequired[str | None]  # UUID du profil modificateur
    
    # Codes de fidélité multiples (pour compatibilité)
    LoyaltyCodes: NotRequired[list[str]]  # Liste de codes de fidélité


class CustomersResponse(TypedDict):
    """Réponse de customers/getAll."""
    Customers: list[Customer]
    Cursor: NotRequired[str]


class CustomerSearchResult(TypedDict, total=False):
    """Résultat de recherche de client."""
    Customer: Customer
    Score: NotRequired[float]


class CustomerSearchResponse(TypedDict):
    """Réponse de customers/search."""
    Results: list[CustomerSearchResult]


class CustomerAddResponse(TypedDict):
    """Réponse de customers/add."""
    Customer: Customer


class CustomerUpdateResponse(TypedDict):
    """Réponse de customers/update."""
    Customer: Customer


class CustomerMergeResponse(TypedDict):
    """Réponse de customers/merge."""
    Customer: Customer


# ============================================================================
# Modèles d'entrée sécurisés pour Customers (Input Models)
# ============================================================================

class CustomerInput(TypedDict, total=False):
    """
    Modèle d'entrée sécurisé pour créer ou mettre à jour un client.
    
    Ce modèle définit strictement les champs acceptés par l'API Mews
    pour les opérations customers/add et customers/update.
    Tous les champs sont optionnels sauf LastName pour la création.
    """
    # Champs obligatoires pour la création
    LastName: Required[str]  # Obligatoire pour customers/add
    
    # Informations personnelles
    FirstName: NotRequired[str | None]
    SecondLastName: NotRequired[str | None]
    Title: NotRequired[str | None]  # "Mr", "Mrs", "Ms", "Miss", "Dr", etc.
    Sex: NotRequired[str | None]  # "Male", "Female", etc.
    Gender: NotRequired[str | None]  # "Male", "Female", "Other", etc.
    
    # Informations de naissance
    BirthDate: NotRequired[str | None]  # Format "YYYY-MM-DD"
    BirthDateUtc: NotRequired[str | None]  # Format ISO 8601 UTC
    BirthPlace: NotRequired[str | None]
    
    # Informations professionnelles
    Occupation: NotRequired[str | None]
    
    # Informations de contact
    Email: NotRequired[str | None]
    Phone: NotRequired[str | None]
    
    # Informations de nationalité et langue
    NationalityCode: NotRequired[str | None]  # Code ISO 3166-1 alpha-2
    PreferredLanguageCode: NotRequired[str | None]  # Code ISO 639-1
    LanguageCode: NotRequired[str | None]  # Code ISO 639-1
    
    # Informations fiscales
    TaxIdentificationNumber: NotRequired[str | None]
    ItalianFiscalCode: NotRequired[str | None]
    ItalianDestinationCode: NotRequired[str | None]
    
    # Codes
    LoyaltyCode: NotRequired[str | None]
    AccountingCode: NotRequired[str | None]
    BillingCode: NotRequired[str | None]
    
    # Notes et informations supplémentaires
    Notes: NotRequired[str | None]
    CarRegistrationNumber: NotRequired[str | None]
    DietaryRequirements: NotRequired[str | None]
    
    # Relations
    CompanyId: NotRequired[str | None]
    CategoryId: NotRequired[str | None]
    AddressId: NotRequired[str | None]
    
    # Options et classifications
    Options: NotRequired[list[str]]
    Classifications: NotRequired[list[str]]
    PreferredSpaceFeatures: NotRequired[list[str]]
    
    # Adresse complète (pour création/mise à jour)
    Address: NotRequired[Address | None]
    
    # Documents (pour création/mise à jour)
    Passport: NotRequired[Document | None]
    IdentityCard: NotRequired[Document | None]
    Visa: NotRequired[Document | None]
    DriversLicense: NotRequired[Document | None]


class CustomerUpdateInput(TypedDict, total=False):
    """
    Modèle d'entrée sécurisé pour mettre à jour un client.
    
    Tous les champs sont optionnels. Seuls les champs fournis seront mis à jour.
    """
    # Tous les champs de CustomerInput sont disponibles pour la mise à jour
    # mais aucun n'est obligatoire
    LastName: NotRequired[str]
    FirstName: NotRequired[str | None]
    SecondLastName: NotRequired[str | None]
    Title: NotRequired[str | None]
    Sex: NotRequired[str | None]
    Gender: NotRequired[str | None]
    BirthDate: NotRequired[str | None]
    BirthDateUtc: NotRequired[str | None]
    BirthPlace: NotRequired[str | None]
    Occupation: NotRequired[str | None]
    Email: NotRequired[str | None]
    Phone: NotRequired[str | None]
    NationalityCode: NotRequired[str | None]
    PreferredLanguageCode: NotRequired[str | None]
    LanguageCode: NotRequired[str | None]
    TaxIdentificationNumber: NotRequired[str | None]
    ItalianFiscalCode: NotRequired[str | None]
    ItalianDestinationCode: NotRequired[str | None]
    LoyaltyCode: NotRequired[str | None]
    AccountingCode: NotRequired[str | None]
    BillingCode: NotRequired[str | None]
    Notes: NotRequired[str | None]
    CarRegistrationNumber: NotRequired[str | None]
    DietaryRequirements: NotRequired[str | None]
    CompanyId: NotRequired[str | None]
    CategoryId: NotRequired[str | None]
    AddressId: NotRequired[str | None]
    Options: NotRequired[list[str]]
    Classifications: NotRequired[list[str]]
    PreferredSpaceFeatures: NotRequired[list[str]]
    Address: NotRequired[Address | None]
    Passport: NotRequired[Document | None]
    IdentityCard: NotRequired[Document | None]
    Visa: NotRequired[Document | None]
    DriversLicense: NotRequired[Document | None]

