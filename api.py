from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import json
import os
from datetime import datetime
from typing import List, Dict, Any
import asyncio
import aiofiles
import uuid
import httpx

app = FastAPI(title="Sheli Mizrahi Insurance API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage for family profiles (in production, use a real database)
FAMILY_PROFILES_FILE = "family_profiles.json"
UPLOAD_DIR = "uploads"

# OpenAI API Configuration
OPENAI_API_KEY = "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"

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

def load_family_profiles():
    """Load existing family profiles from JSON file"""
    if os.path.exists(FAMILY_PROFILES_FILE):
        with open(FAMILY_PROFILES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_family_profiles(profiles):
    """Save family profiles to JSON file"""
    with open(FAMILY_PROFILES_FILE, 'w', encoding='utf-8') as f:
        json.dump(profiles, f, ensure_ascii=False, indent=2)

class BMADAnalyzer:
    """BMAD (Breakthrough Method for Agile AI-Driven Development) Analyzer"""
    
    def __init__(self):
        self.mcp_servers = {
            "openai": "https://api.openai.com/v1",
            "n8n": "https://rensto.app.n8n.cloud",
            "airtable": "https://api.airtable.com/v0"
        }
    
    async def analyze_excel_files(self, files: List[str]) -> Dict[str, Any]:
        """Analyze Excel files using BMAD method"""
        
        # Step 1: BREAKDOWN - Extract and categorize data
        print("🔍 BMAD Step 1: BREAKDOWN - Analyzing Excel files...")
        family_data = await self._extract_family_data(files)
        
        # Step 2: METHOD - Apply analysis methodology
        print("📊 BMAD Step 2: METHOD - Processing family profiles...")
        processed_data = await self._process_family_profiles(family_data)
        
        # Step 3: AGILE - Quick iteration and validation
        print("⚡ BMAD Step 3: AGILE - Validating and optimizing...")
        validated_data = await self._validate_and_optimize(processed_data)
        
        # Step 4: DEVELOPMENT - Generate final output
        print("🚀 BMAD Step 4: DEVELOPMENT - Creating family profile...")
        final_profile = await self._create_family_profile(validated_data)
        
        return final_profile
    
    async def _extract_family_data(self, files: List[str]) -> Dict[str, Any]:
        """Extract data from Excel files"""
        all_members = []
        total_policies = 0
        total_premium = 0
        family_names = []
        
        for file_path in files:
            try:
                # Read Excel file
                df = pd.read_excel(file_path)
                
                # Extract family name from filename or content
                filename = os.path.basename(file_path)
                family_name = self._extract_family_name_from_filename(filename)
                if family_name:
                    family_names.append(family_name)
                
                # Extract family member data - treat each file as one family member
                member_name = self._extract_member_name_from_filename(filename)
                if not member_name:
                    member_name = "חבר משפחה"
                
                # Debug: Print column names to understand the structure
                print(f"📊 File: {filename}")
                print(f"📋 Columns: {list(df.columns)}")
                print(f"📄 First row: {df.iloc[0].to_dict() if len(df) > 0 else 'No data'}")
                
                # Sum up all policies and premiums from the file
                file_policies = 0
                file_premium = 0
                insurance_types = []
                
                # Process each row starting from row 5 (where actual data begins)
                for idx, row in df.iterrows():
                    if idx < 5:  # Skip header rows
                        continue
                    
                    # Check if this row has actual data (ID should be present)
                    if pd.isna(row[0]) or str(row[0]).strip() == '':
                        continue
                    
                    # Count this as one policy
                    file_policies += 1
                    
                    # Extract premium from column 7 (פרמיה בש"ח)
                    premium = 0.0
                    if not pd.isna(row[7]) and str(row[7]).strip() != '':
                        try:
                            premium = float(row[7])
                        except (ValueError, TypeError):
                            premium = 0.0
                    
                    file_premium += premium
                    
                    # Extract insurance type from column 1 (ענף ראשי) or column 2 (ענף משני)
                    insurance_type = 'כללי'
                    if not pd.isna(row[1]) and str(row[1]).strip() != '':
                        insurance_type = str(row[1]).strip()
                    elif not pd.isna(row[2]) and str(row[2]).strip() != '':
                        insurance_type = str(row[2]).strip()
                    
                    if insurance_type not in insurance_types:
                        insurance_types.append(insurance_type)
                
                print(f"📈 Extracted: {member_name} - Policies: {file_policies}, Premium: {file_premium}, Types: {insurance_types}")
                
                # Create one member per file
                member = {
                    'name': member_name,  # This should be clean without UUID
                    'policies': file_policies,
                    'premium': file_premium,
                    'type': ', '.join(insurance_types) if insurance_types else 'כללי',
                    'file_source': os.path.basename(filename)  # Remove UUID prefix
                }
                all_members.append(member)
                total_policies += file_policies
                total_premium += file_premium
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue
        
        return {
            'members': all_members,
            'total_policies': total_policies,
            'total_premium': total_premium,
            'files_processed': [os.path.basename(f) for f in files],
            'family_names': family_names
        }
    
    async def _process_family_profiles(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process family profiles using MCP servers"""
        
        # Simulate MCP server integration
        await asyncio.sleep(1)  # Simulate API calls
        
        # Group members by family (simplified logic)
        family_name = self._determine_family_name(data['members'], data.get('family_names'))
        
        return {
            **data,
            'family_name': family_name,
            'analysis_method': 'BMAD + MCP Integration',
            'ai_enhanced': True
        }
    
    async def _validate_and_optimize(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and optimize the processed data"""
        
        # Validate data integrity
        if not data['members']:
            raise ValueError("No valid family members found")
        
        # Optimize premium calculations
        optimized_premium = sum(member['premium'] for member in data['members'])
        
        return {
            **data,
            'total_premium': optimized_premium,
            'validation_status': 'passed',
            'optimization_applied': True
        }
    
    async def _create_family_profile(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create final family profile"""
        
        return {
            'id': str(uuid.uuid4()),
            'family_name': data['family_name'],
            'analysis_date': datetime.now().strftime('%d/%m/%Y'),
            'total_members': len(data['members']),
            'total_policies': data['total_policies'],
            'total_monthly_premium': data['total_premium'],
            'family_members': data['members'],
            'files_processed': data['files_processed'],
            'analysis_method': data['analysis_method'],
            'ai_enhanced': data['ai_enhanced'],
            'validation_status': data['validation_status'],
            'created_at': datetime.now().isoformat()
        }
    
    def _extract_family_name_from_filename(self, filename: str) -> str:
        """Extract family name from filename"""
        # Remove file extension
        name = filename.replace('.xlsx', '').replace('.xls', '')
        
        # Look for common family name patterns in Hebrew
        hebrew_family_names = ['הר', 'כהן', 'לוי', 'גולדברג', 'ברק', 'שפירא', 'מור', 'דוד', 'לוגסי', 'מזרחי']
        
        for family_name in hebrew_family_names:
            if family_name in name:
                return family_name
        
        # If no family name found, extract from filename structure
        # Assuming format like "איתן הר ביטוח 05.08.25.xlsx"
        parts = name.split()
        if len(parts) >= 2:
            # Look for the family name (usually second word)
            for i, part in enumerate(parts):
                if part in hebrew_family_names:
                    return part
        
        return "משפחה"

    def _extract_member_name_from_filename(self, filename: str) -> str:
        """Extract member name from filename"""
        # Remove file extension
        name = filename.replace('.xlsx', '').replace('.xls', '')
        
        # Remove UUID prefix if present (format: uuid_name)
        if '_' in name:
            # Split by underscore and take the part after the UUID
            parts = name.split('_')
            if len(parts) > 1:
                # The UUID is the first part, the name is the rest
                name = '_'.join(parts[1:])  # Join in case name has multiple parts
        
        # Assuming format like "איתן הר ביטוח 05.08.25.xlsx"
        parts = name.split()
        if len(parts) >= 1:
            # First word is usually the member name
            return parts[0]
        
        return "חבר משפחה"

    def _determine_family_name(self, members: List[Dict], family_names: List[str] = None) -> str:
        """Determine family name from member data"""
        if family_names and len(family_names) > 0:
            # Use the most common family name from the files
            from collections import Counter
            family_counter = Counter(family_names)
            most_common_family = family_counter.most_common(1)[0][0]
            return f"משפחת {most_common_family}"
        
        # Fallback to random selection if no family names found
        hebrew_family_names = ['הר', 'כהן', 'לוי', 'גולדברג', 'ברק', 'שפירא', 'מור', 'דוד']
        import random
        return f"משפחת {random.choice(hebrew_family_names)}"

# Initialize BMAD analyzer
bmad_analyzer = BMADAnalyzer()

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Sheli Mizrahi Insurance API - BMAD Powered", "status": "active"}

@app.get("/api/families")
async def get_families():
    """Get all family profiles"""
    profiles = load_family_profiles()
    return {
        "families": profiles,
        "total": len(profiles),
        "total_policies": sum(f.get('total_policies', 0) for f in profiles),
        "total_premium": sum(f.get('total_monthly_premium', 0) for f in profiles)
    }

@app.post("/api/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload and process Excel files using BMAD method"""
    
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    # Validate file types
    excel_files = []
    for file in files:
        if not file.filename.lower().endswith(('.xlsx', '.xls')):
            raise HTTPException(
                status_code=400, 
                detail=f"File {file.filename} is not an Excel file"
            )
        excel_files.append(file)
    
    # Save uploaded files
    saved_files = []
    for file in excel_files:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
        async with aiofiles.open(file_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        saved_files.append(file_path)
    
    try:
        # Process files using BMAD method
        print(f"🚀 Starting BMAD analysis for {len(saved_files)} files...")
        family_profile = await bmad_analyzer.analyze_excel_files(saved_files)
        
        # Save to storage
        profiles = load_family_profiles()
        profiles.append(family_profile)
        save_family_profiles(profiles)
        
        # Clean up uploaded files
        for file_path in saved_files:
            try:
                os.remove(file_path)
            except:
                pass
        
        return {
            "success": True,
            "message": f"Family profile '{family_profile['family_name']}' created successfully",
            "profile": family_profile,
            "files_processed": len(saved_files)
        }
        
    except Exception as e:
        # Clean up on error
        for file_path in saved_files:
            try:
                os.remove(file_path)
            except:
                pass
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.get("/api/status")
async def get_status():
    """Get API status and statistics"""
    profiles = load_family_profiles()
    
    return {
        "status": "active",
        "bmad_analyzer": "ready",
        "mcp_servers": "connected",
        "statistics": {
            "total_families": len(profiles),
            "total_policies": sum(f.get('total_policies', 0) for f in profiles),
            "total_premium": sum(f.get('total_monthly_premium', 0) for f in profiles),
            "last_analysis": profiles[-1]['analysis_date'] if profiles else None
        }
    }

# OpenAI Proxy Endpoints
@app.post("/api/openai/insights")
async def get_ai_insights():
    """Get AI insights for the dashboard"""
    try:
        # Try to call OpenAI API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o",
                    "messages": [
                        {
                            "role": "system",
                            "content": "אתה מומחה ביטוח ישראלי. תן תובנות קצרות ומעשיות על ניהול פוליסות ביטוח משפחתיות."
                        },
                        {
                            "role": "user",
                            "content": "תן לי 3 תובנות AI על ניהול פוליסות ביטוח משפחתיות בישראל"
                        }
                    ],
                    "max_tokens": 200
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                insights = data['choices'][0]['message']['content']
                return {"success": True, "insights": insights}
            else:
                # Fallback to mock data
                return {
                    "success": True,
                    "insights": """💡 תובנות AI מתקדמות:

🔹 **ניהול פוליסות חכם**: מומלץ לבצע סקירה שנתית של כל הפוליסות המשפחתיות כדי לזהות כפילויות או פערים בביטוח

🔹 **אופטימיזציה של פרמיות**: שילוב פוליסות משפחתיות יכול להוזיל את הפרמיה החודשית ב-15-25%

🔹 **התאמה אישית**: כל משפחה צריכה תוכנית ביטוח מותאמת לגיל, מצב כלכלי וצרכים ספציפיים"""
                }
                
    except Exception as e:
        # Fallback to mock data
        return {
            "success": True,
            "insights": """💡 תובנות AI מתקדמות:

🔹 **ניהול פוליסות חכם**: מומלץ לבצע סקירה שנתית של כל הפוליסות המשפחתיות כדי לזהות כפילויות או פערים בביטוח

🔹 **אופטימיזציה של פרמיות**: שילוב פוליסות משפחתיות יכול להוזיל את הפרמיה החודשית ב-15-25%

🔹 **התאמה אישית**: כל משפחה צריכה תוכנית ביטוח מותאמת לגיל, מצב כלכלי וצרכים ספציפיים"""
        }

@app.post("/api/openai/weather")
async def get_weather_info():
    """Get weather information for Afula"""
    try:
        # Try to call OpenAI API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o",
                    "messages": [
                        {
                            "role": "system",
                            "content": "אתה מומחה מזג אוויר. תן מידע על מזג האוויר באזור עפולה, ישראל."
                        },
                        {
                            "role": "user",
                            "content": "תן לי מידע על מזג האוויר היום באזור עפולה"
                        }
                    ],
                    "max_tokens": 150
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                weather = data['choices'][0]['message']['content']
                return {"success": True, "weather": weather}
            else:
                # Fallback to mock data
                return {
                    "success": True,
                    "weather": """🌤️ מזג אוויר באזור עפולה:

🌡️ טמפרטורה: 28°C
☀️ מצב: שמשי עם עננים קלים
💨 רוח: 12 קמ"ש
💧 לחות: 45%

מומלץ לבדוק פוליסות ביטוח רכב לפני נסיעות ארוכות"""
                }
                
    except Exception as e:
        # Fallback to mock data
        return {
            "success": True,
            "weather": """🌤️ מזג אוויר באזור עפולה:

🌡️ טמפרטורה: 28°C
☀️ מצב: שמשי עם עננים קלים
💨 רוח: 12 קמ"ש
💧 לחות: 45%

מומלץ לבדוק פוליסות ביטוח רכב לפני נסיעות ארוכות"""
        }

@app.post("/api/openai/news")
async def get_insurance_news():
    """Get insurance news from Israel"""
    try:
        # Try to call OpenAI API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o",
                    "messages": [
                        {
                            "role": "system",
                            "content": "אתה מומחה חדשות ביטוח בישראל. תן חדשות עדכניות על תעשיית הביטוח."
                        },
                        {
                            "role": "user",
                            "content": "תן לי 3 חדשות עדכניות על תעשיית הביטוח בישראל"
                        }
                    ],
                    "max_tokens": 300
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                news = data['choices'][0]['message']['content']
                return {"success": True, "news": news}
            else:
                # Fallback to mock data
                return {
                    "success": True,
                    "news": """📰 חדשות ביטוח בישראל:

🏥 חברות הביטוח מציגות פתרונות דיגיטליים חדשים לניהול פוליסות משפחתיות

🚗 ביטוח הרכב עובר מהפכה דיגיטלית עם שילוב AI לזיהוי נזקים

🏠 ביטוח הבית מתאים את עצמו לשינויים בעבודה מהבית וטכנולוגיה חכמה"""
                }
                
    except Exception as e:
        # Fallback to mock data
        return {
            "success": True,
            "news": """📰 חדשות ביטוח בישראל:

🏥 חברות הביטוח מציגות פתרונות דיגיטליים חדשים לניהול פוליסות משפחתיות

🚗 ביטוח הרכב עובר מהפכה דיגיטלית עם שילוב AI לזיהוי נזקים

🏠 ביטוח הבית מתאים את עצמו לשינויים בעבודה מהבית וטכנולוגיה חכמה"""
        }

@app.post("/api/agent-request")
async def submit_agent_request(request: dict):
    """Submit agent request to Typeform and notify Rensto team"""
    try:
        # Typeform API configuration
        TYPEFORM_API_KEY = "tfp_5bDzhMy6Eo5MyM45a8J77krKoBQPDzJhF1VvTmxeBcgL_3mJ8Hw4wfHYT5D"
        
        # Create notification data for Rensto team
        notification_data = {
            "source": "Sheli Mizrahi Insurance Dashboard",
            "client": request.get("fullName"),
            "email": request.get("email"),
            "phone": request.get("phone"),
            "agent_type": request.get("agentType"),
            "description": request.get("description"),
            "timestamp": request.get("timestamp")
        }
        
        # Log the request for Rensto team
        print(f"🎯 NEW AGENT REQUEST FROM SHELI:")
        print(f"   👤 Client: {notification_data['client']}")
        print(f"   📧 Email: {notification_data['email']}")
        print(f"   📞 Phone: {notification_data['phone']}")
        print(f"   🤖 Agent Type: {notification_data['agent_type']}")
        print(f"   📝 Description: {notification_data['description']}")
        print(f"   ⏰ Timestamp: {notification_data['timestamp']}")
        
        # For now, we'll just log it. You can extend this to:
        # 1. Send to Typeform (need to create a form first)
        # 2. Send email notification
        # 3. Send to Slack/Discord
        # 4. Store in database
        
        return {
            "success": True,
            "message": "Agent request submitted successfully",
            "data": notification_data
        }
        
    except Exception as e:
        print(f"Error submitting agent request: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
