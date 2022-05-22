from models import EvidenceOne, EvidenceTwo
from pydantic import ValidationError
from app_logger import logger


async def parse_evidence(json_data: dict, evidence_id: int):
    """Parses evidence payload by evidence type,
    and converts incoming JSON to its equivalent pydantic model.

    Args:
        json_data (dictionary): JSON from incoming file.
        evidence_id (int): Evidence type.
    Returns:
        evidence: Evidence pydantic model.
    """
    try:
        if evidence_id == 1:
            return EvidenceOne(**json_data)
        elif evidence_id == 2:
            return EvidenceTwo(**json_data)
        else:
            logger.error("Invalid evidence_id provided")
            return None
    except ValidationError as e:
        logger.error(f'Invalid JSON input provided for evidence type {evidence_id}')
        return None