import json
from fastapi import File, UploadFile, APIRouter, HTTPException
from parsers import parse_evidence

router = APIRouter()


@router.post("/evidence/upload")
async def upload_accept_file(data: UploadFile = File(...)):
    """Accepts request as file.
    Converts the payload to Evidence model, and retruns a predefined JSON structure
    by calling as_special_List() on the Evidence instance.

    Args:
        data (UploadFile, optional): JSON file. Defaults to File(...).
    Returns:
        result: JSON sub structure, extracted from the evidence.
    """
    json_data = json.load(data.file)
    try:
        evidence_id = int(json_data['evidence_id'])
    except:
        raise HTTPException(status_code=404, detail="evidence_id not found")

    evidence = await parse_evidence(json_data, evidence_id)
    if evidence:
        result = evidence.as_special_List()
    else:
        raise HTTPException(status_code=400, detail="evidence processing failed")
    return result
