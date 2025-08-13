from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_mcp import FastApiMCP
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import json
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Sheli Mizrahi Insurance API", version="1.0.0")
security = HTTPBasic()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class FamilyMember(BaseModel):
    id: str
    name: str
    age: int
    relationship: str
    insurance_type: str
    status: str
    documents: int
    last_updated: str

class FamilyProfile(BaseModel):
    id: str
    family_name: str
    members: List[FamilyMember]
    total_policies: int
    total_value: float
    risk_level: str
    last_assessment: str
    status: str

class UploadedDocument(BaseModel):
    id: str
    name: str
    type: str
    size: str
    uploaded_at: str
    status: str
    family_member: Optional[str] = None

# Mock database
families_db = {}
documents_db = {}

def wp_auth(credentials: HTTPBasicCredentials = Depends(security)):
    """Basic authentication for insurance API"""
    if credentials.username != os.getenv("INSURANCE_USERNAME", "admin") or \
       credentials.password != os.getenv("INSURANCE_PASSWORD", "password"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials

@app.get("/")
def read_root():
    return {"message": "Sheli Mizrahi Insurance API", "version": "1.0.0"}

@app.get("/families")
def get_families(creds=Depends(wp_auth)):
    """Get all family profiles"""
    return {
        "success": True,
        "families": list(families_db.values()),
        "count": len(families_db)
    }

@app.get("/families/{family_id}")
def get_family(family_id: str, creds=Depends(wp_auth)):
    """Get specific family profile"""
    if family_id not in families_db:
        raise HTTPException(status_code=404, detail="Family not found")
    return {
        "success": True,
        "family": families_db[family_id]
    }

@app.post("/families")
def create_family(family: FamilyProfile, creds=Depends(wp_auth)):
    """Create new family profile"""
    family_id = str(uuid.uuid4())
    family.id = family_id
    families_db[family_id] = family.dict()
    return {
        "success": True,
        "family_id": family_id,
        "message": "Family profile created successfully"
    }

@app.put("/families/{family_id}")
def update_family(family_id: str, family: FamilyProfile, creds=Depends(wp_auth)):
    """Update family profile"""
    if family_id not in families_db:
        raise HTTPException(status_code=404, detail="Family not found")
    
    family.id = family_id
    families_db[family_id] = family.dict()
    return {
        "success": True,
        "message": "Family profile updated successfully"
    }

@app.delete("/families/{family_id}")
def delete_family(family_id: str, creds=Depends(wp_auth)):
    """Delete family profile"""
    if family_id not in families_db:
        raise HTTPException(status_code=404, detail="Family not found")
    
    del families_db[family_id]
    return {
        "success": True,
        "message": "Family profile deleted successfully"
    }

@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    family_member: Optional[str] = Form(None),
    creds=Depends(wp_auth)
):
    """Upload insurance document"""
    try:
        # Generate document ID
        doc_id = str(uuid.uuid4())
        
        # Calculate file size
        file_size = len(await file.read())
        await file.seek(0)  # Reset file pointer
        
        # Create document record
        document = UploadedDocument(
            id=doc_id,
            name=file.filename,
            type="insurance_document",
            size=f"{file_size / 1024 / 1024:.1f} MB",
            uploaded_at=datetime.now().isoformat(),
            status="processing",
            family_member=family_member
        )
        
        # Store document
        documents_db[doc_id] = document.dict()
        
        # TODO: Process document with AI
        # This would integrate with OpenAI for document analysis
        
        return {
            "success": True,
            "document_id": doc_id,
            "message": "Document uploaded successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@app.get("/documents")
def get_documents(creds=Depends(wp_auth)):
    """Get all uploaded documents"""
    return {
        "success": True,
        "documents": list(documents_db.values()),
        "count": len(documents_db)
    }

@app.get("/documents/{document_id}")
def get_document(document_id: str, creds=Depends(wp_auth)):
    """Get specific document"""
    if document_id not in documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    return {
        "success": True,
        "document": documents_db[document_id]
    }

@app.post("/analyze/family")
def analyze_family_documents(family_id: str, creds=Depends(wp_auth)):
    """Analyze family documents and create unified profile"""
    if family_id not in families_db:
        raise HTTPException(status_code=404, detail="Family not found")
    
    # TODO: Implement AI analysis
    # This would use OpenAI to analyze documents and create family profile
    
    return {
        "success": True,
        "message": "Family analysis completed",
        "analysis_id": str(uuid.uuid4())
    }

@app.get("/analytics/overview")
def get_analytics_overview(creds=Depends(wp_auth)):
    """Get analytics overview"""
    total_families = len(families_db)
    total_documents = len(documents_db)
    total_value = sum(family.get("total_value", 0) for family in families_db.values())
    
    # Calculate risk distribution
    risk_levels = {}
    for family in families_db.values():
        risk = family.get("risk_level", "unknown")
        risk_levels[risk] = risk_levels.get(risk, 0) + 1
    
    return {
        "success": True,
        "analytics": {
            "total_families": total_families,
            "total_documents": total_documents,
            "total_value": total_value,
            "risk_distribution": risk_levels,
            "average_family_size": sum(len(family.get("members", [])) for family in families_db.values()) / max(total_families, 1)
        }
    }

@app.get("/status")
def get_status():
    """Get API status"""
    return {
        "status": "operational",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "families_count": len(families_db),
        "documents_count": len(documents_db)
    }

# Initialize MCP
mcp = FastApiMCP(app)
mcp.mount()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
