from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class UserDetails(BaseModel):
    updated_at: str
    id: int
    email: str
    full_name: str


class Security(BaseModel):
    mfa_enabled: bool
    mfa_enforced: bool


class Location(BaseModel):
    country: str
    state: Optional[str]
    city: str


class EvidenceDatum(BaseModel):
    login_name: str
    role: str
    user_details: UserDetails
    security: Security
    location: Location


class EvidenceTwo(BaseModel):
    evidence_id: int
    evidence_data: List[EvidenceDatum]

    def as_special_List(self) -> list:
        data_list = []
        for data in self.evidence_data:
            schema_as_dict = {}
            schema_as_dict["id"] = int(data.user_details.id)
            schema_as_dict["full name"] = data.user_details.full_name
            schema_as_dict["email"] = data.user_details.email
            schema_as_dict["updated at"] = data.user_details.updated_at
            schema_as_dict["country"] = data.location.country
            schema_as_dict["state"] = data.location.state
            schema_as_dict["city"] = data.location.city
            data_list.append(schema_as_dict)
        return data_list
