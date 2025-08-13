# 🏠 Sheli Mizrahi Insurance - Family Profile System Documentation

## **🎯 System Overview**

**Sheli Mizrahi Insurance Agency** - Afula, Israel  
**System:** AI-Powered Family Insurance Profile Management  
**Methodology:** BMAD (Breakthrough Method for Agile AI-Driven Development)

### **🌟 Purpose**
Create unified family insurance profiles by combining individual family member profiles uploaded through a modern web application, powered by AI agents and automated n8n workflows.

### **🎨 Brand Identity**
- **Primary Colors:** Blue theme (differentiated from Tax4US green, Rensto branding)
- **Location:** Afula, Israel
- **Language:** Hebrew (RTL) + English
- **Industry:** Insurance

## **🏗️ Architecture**

### **Frontend (Next.js 14)**
- **Framework:** Next.js 14 with TypeScript
- **UI Library:** shadcn/ui with custom blue theme
- **Animations:** Framer Motion
- **Styling:** Tailwind CSS with glassmorphism
- **Language:** Hebrew (RTL) + English

### **Backend (FastAPI)**
- **API:** FastAPI with MCP integration
- **Database:** PostgreSQL for family profiles
- **File Storage:** Cloud storage for uploaded documents
- **AI Integration:** OpenAI GPT-4 for profile analysis
- **Port:** 8001

### **Automation (n8n)**
- **Workflow Engine:** n8n with MCP servers
- **Integration:** GitMCP, MCP-USE, FastAPI-MCP
- **Deployment:** Vercel with GitHub Actions

## **🔧 Core Features**

### **1. Family Profile Management**
- Upload individual family member profiles
- AI-powered profile analysis and categorization
- Automatic family unit detection and grouping
- Unified family insurance profile generation

### **2. Document Processing**
- Multi-format document upload (PDF, DOC, images)
- OCR processing for handwritten documents
- AI-powered data extraction and validation
- Secure document storage and retrieval

### **3. Insurance Agent Dashboard**
- Real-time family profile overview
- Risk assessment and recommendations
- Policy comparison and optimization
- Client communication management

### **4. AI Agents**
- **Profile Analyzer Agent:** Processes uploaded profiles
- **Family Mapper Agent:** Identifies family relationships
- **Risk Assessment Agent:** Evaluates insurance needs
- **Policy Recommender Agent:** Suggests optimal coverage

## **🚀 Quick Start**

### **Prerequisites**
- Node.js 18+
- Python 3.8+
- n8n instance
- OpenAI API key

### **Installation**

```bash
# Clone the repository
git clone <repository>
cd sheli-mizrahi-insurance/family-profile-system

# Install frontend dependencies
npm install

# Install backend dependencies
cd insurance-api
pip install -r requirements.txt

# Set environment variables
export INSURANCE_USERNAME="shelimizrahi"
export INSURANCE_PASSWORD="insurance2024"
export OPENAI_API_KEY="your_openai_api_key_here"

# Start the system
./start-insurance-system.sh
```

### **Development**

```bash
# Start frontend development server
npm run dev

# Start backend API server
cd insurance-api
uvicorn app:app --host 0.0.0.0 --port 8001 --reload

# Import n8n workflow
# Import the family-insurance-workflow.json file into your n8n instance
```

## **📊 API Endpoints**

### **Family Management**
- `GET /families` - Get all family profiles
- `GET /families/{id}` - Get specific family profile
- `POST /families` - Create new family profile
- `PUT /families/{id}` - Update family profile
- `DELETE /families/{id}` - Delete family profile

### **Document Management**
- `POST /documents/upload` - Upload insurance document
- `GET /documents` - Get all uploaded documents
- `GET /documents/{id}` - Get specific document

### **Analysis**
- `POST /analyze/family` - Analyze family documents
- `GET /analytics/overview` - Get analytics overview

### **System**
- `GET /status` - Get API status

## **🤖 AI Agent Capabilities**

### **SheliMizrahiInsuranceAgent**
- **Family Document Analysis:** Extract information from uploaded documents
- **Risk Assessment:** Evaluate family risk levels
- **Profile Creation:** Generate unified family profiles
- **Recommendations:** Provide insurance recommendations
- **Cost Optimization:** Suggest cost-effective coverage

### **Supported Languages**
- Hebrew (primary)
- English (secondary)

### **Specializations**
- Life insurance
- Health insurance
- Property insurance
- Liability insurance
- Family coverage optimization

## **🔄 n8n Workflow**

### **Family Insurance Workflow**
1. **Webhook Trigger:** Receives family data
2. **Process Family Data:** Validates and processes input
3. **AI Analysis:** OpenAI analysis of family profile
4. **Save Family Profile:** Stores in database
5. **Create Comprehensive Profile:** Combines all data
6. **Response:** Returns complete profile

### **Workflow Features**
- Error handling and validation
- AI-powered analysis
- Multi-language support
- Risk scoring
- Cost estimation

## **🎨 UI Components**

### **Design System**
- **Colors:** Blue theme (primary: #3b82f6)
- **Typography:** Heebo font for Hebrew
- **Animations:** Framer Motion
- **Layout:** Glassmorphism effects

### **Key Components**
- Family Profile Cards
- Document Upload Interface
- Analytics Dashboard
- Risk Assessment Display
- Recommendation Engine

## **🔒 Security**

### **Authentication**
- Basic HTTP authentication
- Environment variable configuration
- Secure API endpoints

### **Data Protection**
- Encrypted document storage
- Secure file uploads
- API rate limiting
- CORS configuration

## **📈 Analytics & Reporting**

### **Metrics Tracked**
- Total families managed
- Total policies
- Total value
- Risk distribution
- Document processing status

### **Reports Generated**
- Family profile summaries
- Risk assessment reports
- Coverage recommendations
- Cost analysis
- Performance metrics

## **🔗 Integration Points**

### **MCP Servers**
- **GitMCP:** https://github.com/idosal/git-mcp
- **MCP-USE:** https://github.com/mcp-use/mcp-use
- **FastAPI-MCP:** https://github.com/tadata-org/fastapi_mcp

### **External Services**
- OpenAI GPT-4 for AI analysis
- Cloud storage for documents
- Email notifications
- SMS alerts

## **🚀 Deployment**

### **Vercel Deployment**
```bash
# Deploy to Vercel
vercel --prod

# Environment variables
VERCEL_TOKEN=your_vercel_token
VERCEL_USER_ID=your_user_id
VERCEL_TEAM_ID=your_team_id
VERCEL_PROJECT_ID=your_project_id
```

### **GitHub Actions**
- Automatic deployment on push to main
- Build and test automation
- Environment variable management

## **📋 Configuration**

### **Environment Variables**
```bash
# API Configuration
INSURANCE_USERNAME=shelimizrahi
INSURANCE_PASSWORD=insurance2024

# AI Configuration
OPENAI_API_KEY=your_openai_api_key

# Database Configuration
DATABASE_URL=your_database_url

# File Storage
STORAGE_BUCKET=your_storage_bucket
```

### **n8n Credentials**
- OpenAI API Key
- Insurance API Basic Auth
- Webhook URLs

## **🔧 Troubleshooting**

### **Common Issues**
1. **Port Conflicts:** Ensure port 8001 is available
2. **Authentication:** Check environment variables
3. **File Uploads:** Verify storage permissions
4. **AI Analysis:** Validate OpenAI API key

### **Logs**
- Frontend: Browser console
- Backend: uvicorn logs
- n8n: n8n execution logs

## **📞 Support**

### **Contact Information**
- **Agency:** Sheli Mizrahi Insurance Agency
- **Location:** Afula, Israel
- **Email:** support@shelimizrahi.co.il

### **Documentation**
- API Documentation: http://localhost:8001/docs
- System Status: http://localhost:8001/status
- GitHub Repository: [Repository URL]

---

**Built with ❤️ for Sheli Mizrahi Insurance Agency - Afula, Israel**
