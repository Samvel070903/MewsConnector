"""Opérations sur les clients — CRUD et recherche de profils invités."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, cast

from mews.models import (
    Customer,
    CustomerAddResponse,
    CustomerInput,
    CustomerMergeResponse,
    CustomerSearchResponse,
    CustomerUpdateInput,
    CustomerUpdateResponse,
)
from mews.operations import BaseOperations


class CustomerOperations(BaseOperations):
    """Opérations sur les profils clients (invités).

    .. note::
        Le endpoint Mews ``customers/getAll`` **nécessite** au moins un
        filtre (``CustomerIds``, ``Emails``, ``CreatedUtc``, ``UpdatedUtc`",
        ``DeletedUtc``, ``FirstNames``, ``LastNames``, ``LoyaltyCodes`",
        ``CompanyIds``).  Si vous appelez :meth:`get_all` sans aucun filtre,
        une fenêtre ``UpdatedUtc`` par défaut couvrant les *days_back*
        derniers jours est automatiquement appliquée.
    """

    def get_all(
        self,
        *,
        customer_ids: list[str] | None = None,
        emails: list[str] | None = None,
        first_names: list[str] | None = None,
        last_names: list[str] | None = None,
        loyalty_codes: list[str] | None = None,
        company_ids: list[str] | None = None,
        created_utc: dict[str, str] | None = None,
        updated_utc: dict[str, str] | None = None,
        deleted_utc: dict[str, str] | None = None,
        extent: dict[str, bool] | None = None,
        page_size: int = 100,
        days_back: int = 90,
    ) -> list[Customer]:
        """Récupère les clients avec des filtres optionnels. Pagination automatique.

        Si **aucun** filtre n'est fourni, une fenêtre ``UpdatedUtc`` par
        défaut couvrant les *days_back* derniers jours (par défaut 90 —
        l'API Mews impose un intervalle maximum d'environ 3 mois) est
        utilisée pour que l'appel API réussisse.

        Args:
            customer_ids: Filtrer par identifiants.
            emails: Filtrer par adresses email.
            first_names: Filtrer par prénom.
            last_names: Filtrer par nom de famille.
            loyalty_codes: Filtrer par codes de fidélité.
            company_ids: Filtrer par identifiants d'entreprise.
            created_utc: ``{"StartUtc": "...", "EndUtc": "..."}``.
            updated_utc: Même format — filtrer par date de mise à jour.
            deleted_utc: Même format — filtrer par date de suppression.
            extent: Sous-objets à inclure, par ex.
                ``{"Addresses": True, "Documents": True}``.
            page_size: Taille de page (max 1000).
            days_back: Lorsqu'aucun filtre n'est fourni, remonter de ce
                nombre de jours via ``UpdatedUtc`` (par défaut ``90``).

        Returns:
            Liste de Customer typés.
        """
        payload: dict[str, Any] = {}
        if customer_ids:
            payload["CustomerIds"] = customer_ids
        if emails:
            payload["Emails"] = emails
        if first_names:
            payload["FirstNames"] = first_names
        if last_names:
            payload["LastNames"] = last_names
        if loyalty_codes:
            payload["LoyaltyCodes"] = loyalty_codes
        if company_ids:
            payload["CompanyIds"] = company_ids
        if created_utc:
            payload["CreatedUtc"] = created_utc
        if updated_utc:
            payload["UpdatedUtc"] = updated_utc
        if deleted_utc:
            payload["DeletedUtc"] = deleted_utc
        if extent:
            payload["Extent"] = extent

        # Mews exige au moins un filtre — on applique un filtre par défaut raisonnable
        _filter_keys = {
            "CustomerIds", "Emails", "FirstNames", "LastNames",
            "LoyaltyCodes", "CompanyIds", "CreatedUtc", "UpdatedUtc", "DeletedUtc",
        }
        if not (_filter_keys & payload.keys()):
            now = datetime.now(timezone.utc)
            payload["UpdatedUtc"] = {
                "StartUtc": (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

        result = self._paginate("customers/getAll", payload, "Customers", page_size=page_size)
        return cast(list[Customer], result)

    def get_by_ids(self, customer_ids: list[str], **kwargs: Any) -> list[Customer]:
        """Raccourci : récupère des clients par leurs identifiants."""
        return self.get_all(customer_ids=customer_ids, **kwargs)

    def get_by_emails(self, emails: list[str], **kwargs: Any) -> list[Customer]:
        """Raccourci : recherche des clients par adresse email."""
        return self.get_all(emails=emails, **kwargs)

    def add(
        self,
        *,
        last_name: str,
        first_name: str | None = None,
        second_last_name: str | None = None,
        title: str | None = None,
        sex: str | None = None,
        gender: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        nationality_code: str | None = None,
        preferred_language_code: str | None = None,
        language_code: str | None = None,
        birth_date: str | None = None,
        birth_date_utc: str | None = None,
        birth_place: str | None = None,
        occupation: str | None = None,
        tax_identification_number: str | None = None,
        italian_fiscal_code: str | None = None,
        italian_destination_code: str | None = None,
        loyalty_code: str | None = None,
        accounting_code: str | None = None,
        billing_code: str | None = None,
        notes: str | None = None,
        car_registration_number: str | None = None,
        dietary_requirements: str | None = None,
        company_id: str | None = None,
        category_id: str | None = None,
        address_id: str | None = None,
        options: list[str] | None = None,
        classifications: list[str] | None = None,
        preferred_space_features: list[str] | None = None,
        address: dict[str, Any] | None = None,
        passport: dict[str, Any] | None = None,
        identity_card: dict[str, Any] | None = None,
        visa: dict[str, Any] | None = None,
        drivers_license: dict[str, Any] | None = None,
        **extra: Any,
    ) -> CustomerAddResponse:
        """
        Crée un nouveau profil client avec validation stricte des entrées.

        Args:
            last_name: Obligatoire — nom de famille.
            first_name: Prénom (optionnel).
            second_last_name: Deuxième nom de famille (optionnel).
            title: Titre de civilité ("Mr", "Mrs", "Ms", "Miss", "Dr", etc.).
            sex: Sexe ("Male", "Female", etc.).
            gender: Genre ("Male", "Female", "Other", etc.).
            email: Adresse email.
            phone: Téléphone au format international.
            nationality_code: Code ISO 3166-1 alpha-2 de nationalité.
            preferred_language_code: Code ISO 639-1 de langue préférée.
            language_code: Code ISO 639-1 de langue actuelle.
            birth_date: Date de naissance au format "YYYY-MM-DD".
            birth_date_utc: Date de naissance au format ISO 8601 UTC.
            birth_place: Lieu de naissance.
            occupation: Profession.
            tax_identification_number: Numéro d'identification fiscale.
            italian_fiscal_code: Code fiscal italien (Codice Fiscale).
            italian_destination_code: Code destination italien.
            loyalty_code: Code de fidélité.
            accounting_code: Code comptable.
            billing_code: Code de facturation.
            notes: Notes en texte libre.
            car_registration_number: Numéro d'immatriculation du véhicule.
            dietary_requirements: Exigences alimentaires.
            company_id: UUID de l'entreprise associée.
            category_id: UUID de la catégorie de client.
            address_id: UUID de l'adresse principale.
            options: Liste d'options (ex: ["SendMarketingEmails", "Invoiceable"]).
            classifications: Liste de classifications (ex: ["Media", "Returning"]).
            preferred_space_features: Liste des caractéristiques d'espace préférées.
            address: Dictionnaire d'adresse complète (Address).
            passport: Dictionnaire de document passeport (Document).
            identity_card: Dictionnaire de carte d'identité (Document).
            visa: Dictionnaire de visa (Document).
            drivers_license: Dictionnaire de permis de conduire (Document).
            **extra: Champs supplémentaires (utiliser avec précaution).

        Returns:
            CustomerAddResponse avec le Customer créé.

        Raises:
            MewsAPIError: Si la création échoue.
            MewsValidationError: Si les données fournies sont invalides.
        """
        # Construction du payload avec validation stricte
        payload: CustomerInput = {"LastName": last_name}
        
        # Ajout des champs optionnels uniquement s'ils sont fournis
        if first_name is not None:
            payload["FirstName"] = first_name
        if second_last_name is not None:
            payload["SecondLastName"] = second_last_name
        if title is not None:
            payload["Title"] = title
        if sex is not None:
            payload["Sex"] = sex
        if gender is not None:
            payload["Gender"] = gender
        if email is not None:
            payload["Email"] = email
        if phone is not None:
            payload["Phone"] = phone
        if nationality_code is not None:
            payload["NationalityCode"] = nationality_code
        if preferred_language_code is not None:
            payload["PreferredLanguageCode"] = preferred_language_code
        if language_code is not None:
            payload["LanguageCode"] = language_code
        if birth_date is not None:
            payload["BirthDate"] = birth_date
        if birth_date_utc is not None:
            payload["BirthDateUtc"] = birth_date_utc
        if birth_place is not None:
            payload["BirthPlace"] = birth_place
        if occupation is not None:
            payload["Occupation"] = occupation
        if tax_identification_number is not None:
            payload["TaxIdentificationNumber"] = tax_identification_number
        if italian_fiscal_code is not None:
            payload["ItalianFiscalCode"] = italian_fiscal_code
        if italian_destination_code is not None:
            payload["ItalianDestinationCode"] = italian_destination_code
        if loyalty_code is not None:
            payload["LoyaltyCode"] = loyalty_code
        if accounting_code is not None:
            payload["AccountingCode"] = accounting_code
        if billing_code is not None:
            payload["BillingCode"] = billing_code
        if notes is not None:
            payload["Notes"] = notes
        if car_registration_number is not None:
            payload["CarRegistrationNumber"] = car_registration_number
        if dietary_requirements is not None:
            payload["DietaryRequirements"] = dietary_requirements
        if company_id is not None:
            payload["CompanyId"] = company_id
        if category_id is not None:
            payload["CategoryId"] = category_id
        if address_id is not None:
            payload["AddressId"] = address_id
        if options is not None:
            payload["Options"] = options
        if classifications is not None:
            payload["Classifications"] = classifications
        if preferred_space_features is not None:
            payload["PreferredSpaceFeatures"] = preferred_space_features
        if address is not None:
            payload["Address"] = address  # type: ignore[assignment]
        if passport is not None:
            payload["Passport"] = passport  # type: ignore[assignment]
        if identity_card is not None:
            payload["IdentityCard"] = identity_card  # type: ignore[assignment]
        if visa is not None:
            payload["Visa"] = visa  # type: ignore[assignment]
        if drivers_license is not None:
            payload["DriversLicense"] = drivers_license  # type: ignore[assignment]
        
        # Ajout des champs supplémentaires si fournis
        if extra:
            payload.update(extra)  # type: ignore[assignment]

        return cast(CustomerAddResponse, self._post("customers/add", payload))

    def update(
        self,
        customer_id: str,
        *,
        last_name: str | None = None,
        first_name: str | None = None,
        second_last_name: str | None = None,
        title: str | None = None,
        sex: str | None = None,
        gender: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        nationality_code: str | None = None,
        preferred_language_code: str | None = None,
        language_code: str | None = None,
        birth_date: str | None = None,
        birth_date_utc: str | None = None,
        birth_place: str | None = None,
        occupation: str | None = None,
        tax_identification_number: str | None = None,
        italian_fiscal_code: str | None = None,
        italian_destination_code: str | None = None,
        loyalty_code: str | None = None,
        accounting_code: str | None = None,
        billing_code: str | None = None,
        notes: str | None = None,
        car_registration_number: str | None = None,
        dietary_requirements: str | None = None,
        company_id: str | None = None,
        category_id: str | None = None,
        address_id: str | None = None,
        options: list[str] | None = None,
        classifications: list[str] | None = None,
        preferred_space_features: list[str] | None = None,
        address: dict[str, Any] | None = None,
        passport: dict[str, Any] | None = None,
        identity_card: dict[str, Any] | None = None,
        visa: dict[str, Any] | None = None,
        drivers_license: dict[str, Any] | None = None,
        **extra: Any,
    ) -> CustomerUpdateResponse:
        """
        Met à jour un client existant avec validation stricte des entrées.

        Tous les paramètres sont optionnels. Seuls les champs fournis seront mis à jour.

        Args:
            customer_id: UUID du client à mettre à jour (obligatoire).
            last_name: Nom de famille.
            first_name: Prénom.
            second_last_name: Deuxième nom de famille.
            title: Titre de civilité.
            sex: Sexe.
            gender: Genre.
            email: Adresse email.
            phone: Téléphone.
            nationality_code: Code de nationalité ISO 3166-1 alpha-2.
            preferred_language_code: Code de langue préférée ISO 639-1.
            language_code: Code de langue actuelle ISO 639-1.
            birth_date: Date de naissance "YYYY-MM-DD".
            birth_date_utc: Date de naissance ISO 8601 UTC.
            birth_place: Lieu de naissance.
            occupation: Profession.
            tax_identification_number: Numéro d'identification fiscale.
            italian_fiscal_code: Code fiscal italien.
            italian_destination_code: Code destination italien.
            loyalty_code: Code de fidélité.
            accounting_code: Code comptable.
            billing_code: Code de facturation.
            notes: Notes.
            car_registration_number: Numéro d'immatriculation.
            dietary_requirements: Exigences alimentaires.
            company_id: UUID de l'entreprise.
            category_id: UUID de la catégorie.
            address_id: UUID de l'adresse.
            options: Liste d'options.
            classifications: Liste de classifications.
            preferred_space_features: Liste de caractéristiques d'espace.
            address: Dictionnaire d'adresse complète.
            passport: Dictionnaire de document passeport.
            identity_card: Dictionnaire de carte d'identité.
            visa: Dictionnaire de visa.
            drivers_license: Dictionnaire de permis de conduire.
            **extra: Champs supplémentaires (utiliser avec précaution).

        Returns:
            CustomerUpdateResponse avec le Customer mis à jour.

        Raises:
            MewsAPIError: Si la mise à jour échoue.
            MewsValidationError: Si les données fournies sont invalides.
        """
        # Construction du payload avec validation stricte
        payload: CustomerUpdateInput = {"CustomerId": customer_id}  # type: ignore[assignment]
        
        # Ajout des champs uniquement s'ils sont fournis (pas None)
        if last_name is not None:
            payload["LastName"] = last_name
        if first_name is not None:
            payload["FirstName"] = first_name
        if second_last_name is not None:
            payload["SecondLastName"] = second_last_name
        if title is not None:
            payload["Title"] = title
        if sex is not None:
            payload["Sex"] = sex
        if gender is not None:
            payload["Gender"] = gender
        if email is not None:
            payload["Email"] = email
        if phone is not None:
            payload["Phone"] = phone
        if nationality_code is not None:
            payload["NationalityCode"] = nationality_code
        if preferred_language_code is not None:
            payload["PreferredLanguageCode"] = preferred_language_code
        if language_code is not None:
            payload["LanguageCode"] = language_code
        if birth_date is not None:
            payload["BirthDate"] = birth_date
        if birth_date_utc is not None:
            payload["BirthDateUtc"] = birth_date_utc
        if birth_place is not None:
            payload["BirthPlace"] = birth_place
        if occupation is not None:
            payload["Occupation"] = occupation
        if tax_identification_number is not None:
            payload["TaxIdentificationNumber"] = tax_identification_number
        if italian_fiscal_code is not None:
            payload["ItalianFiscalCode"] = italian_fiscal_code
        if italian_destination_code is not None:
            payload["ItalianDestinationCode"] = italian_destination_code
        if loyalty_code is not None:
            payload["LoyaltyCode"] = loyalty_code
        if accounting_code is not None:
            payload["AccountingCode"] = accounting_code
        if billing_code is not None:
            payload["BillingCode"] = billing_code
        if notes is not None:
            payload["Notes"] = notes
        if car_registration_number is not None:
            payload["CarRegistrationNumber"] = car_registration_number
        if dietary_requirements is not None:
            payload["DietaryRequirements"] = dietary_requirements
        if company_id is not None:
            payload["CompanyId"] = company_id
        if category_id is not None:
            payload["CategoryId"] = category_id
        if address_id is not None:
            payload["AddressId"] = address_id
        if options is not None:
            payload["Options"] = options
        if classifications is not None:
            payload["Classifications"] = classifications
        if preferred_space_features is not None:
            payload["PreferredSpaceFeatures"] = preferred_space_features
        if address is not None:
            payload["Address"] = address  # type: ignore[assignment]
        if passport is not None:
            payload["Passport"] = passport  # type: ignore[assignment]
        if identity_card is not None:
            payload["IdentityCard"] = identity_card  # type: ignore[assignment]
        if visa is not None:
            payload["Visa"] = visa  # type: ignore[assignment]
        if drivers_license is not None:
            payload["DriversLicense"] = drivers_license  # type: ignore[assignment]
        
        # Ajout des champs supplémentaires si fournis
        if extra:
            payload.update(extra)  # type: ignore[assignment]

        return cast(CustomerUpdateResponse, self._post("customers/update", payload))

    def merge(self, source_id: str, target_id: str) -> CustomerMergeResponse:
        """Fusionne deux profils clients.

        Le profil *source* est fusionné **dans** le profil *cible*.

        Returns:
            CustomerMergeResponse avec le Customer fusionné.
        """
        return cast(CustomerMergeResponse, self._post("customers/merge", {
            "SourceCustomerId": source_id,
            "TargetCustomerId": target_id,
        }))

    def search(self, name: str, **kwargs: Any) -> CustomerSearchResponse:
        """Recherche des clients par nom (raccourci pratique).

        Returns:
            CustomerSearchResponse avec les résultats de recherche.
        """
        payload: dict[str, Any] = {"Name": name, **kwargs}
        return cast(CustomerSearchResponse, self._post("customers/search", payload))
