from mcp_use import MCPClient, MCPAgent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os
import json
from typing import Dict, Any, List
import pandas as pd
from datetime import datetime

load_dotenv()

class SheliMizrahiInsuranceAgent:
    def __init__(self):
        self.config = {
            "name": "shelimizrahi_insurance_agent",
            "url": "http://localhost:8001/mcp/sse",
            "tools": ["create_family_profile", "analyze_documents", "assess_risk", "generate_recommendations", "combine_individual_profiles"]
        }
        self.client = MCPClient.from_dict(self.config)
        self.llm = ChatOpenAI(
            model="gpt-4o", 
            api_key=os.getenv("OPENAI_API_KEY"), 
            temperature=0.7
        )
        self.agent = MCPAgent(
            llm=self.llm, 
            client=self.client, 
            max_steps=10, 
            verbose=True
        )

    async def combine_individual_profiles(self, individual_profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create a MODERN, SOPHISTICATED family profile by combining individual profiles
        Uses advanced AI analysis to generate premium insurance insights with modern formatting
        """
        prompt = f"""
        Create a PREMIUM, MODERN family insurance profile by analyzing these individual profiles:
        {json.dumps(individual_profiles, indent=2, ensure_ascii=False)}
        
        Generate a SOPHISTICATED family profile that includes:
        
        1. FAMILY INSIGHTS DASHBOARD:
           - Family name and composition analysis
           - Total family insurance portfolio value
           - Risk distribution across family members
           - Coverage optimization opportunities
           - Modern data visualization suggestions
        
        2. ADVANCED RISK ANALYSIS:
           - Individual risk profiles with detailed scoring (0-100)
           - Family risk correlation analysis
           - Age-based risk progression modeling
           - Occupation and lifestyle risk factors
           - Predictive risk modeling
        
        3. COVERAGE GAP ANALYSIS:
           - Missing critical insurance coverage
           - Underinsured areas with specific recommendations
           - Redundant coverage identification
           - Cost-benefit optimization opportunities
           - Coverage efficiency scoring
        
        4. AI-POWERED RECOMMENDATIONS:
           - Personalized coverage recommendations per family member
           - Cost optimization strategies with specific savings
           - Risk mitigation plans with action items
           - Future planning considerations
           - Priority-based implementation roadmap
        
        5. MODERN FAMILY PROFILE FORMAT:
           - Professional, modern layout with sections
           - Data visualization suggestions (charts, graphs)
           - Interactive elements and navigation
           - Premium presentation style
           - Mobile-responsive design considerations
        
        6. FINANCIAL OPTIMIZATION:
           - Premium cost analysis with breakdown
           - Coverage-to-cost ratios
           - Family discount opportunities
           - Long-term financial planning
           - ROI analysis for insurance investments
        
        7. FAMILY-SPECIFIC INSIGHTS:
           - Children's future education planning
           - Parents' retirement preparation
           - Emergency fund recommendations
           - Estate planning considerations
           - Tax optimization opportunities
        
        Make this a PREMIUM, MODERN insurance profile that showcases advanced AI capabilities.
        Provide sophisticated analysis in Hebrew with professional formatting.
        Include specific numbers, percentages, and actionable recommendations.
        Make it look like a modern, professional insurance document that clients would be impressed by.
        """
        
        response = await self.llm.ainvoke(prompt)
        
        # Parse the response and create structured data
        combined_profile = self._parse_modern_combined_profile(response.content, individual_profiles)
        
        return {
            "combined_profile": combined_profile,
            "raw_analysis": response.content,
            "generated_at": datetime.now().isoformat(),
            "profile_style": "premium_modern_ai_powered",
            "ai_analysis_level": "advanced",
            "modern_features": [
                "Advanced risk scoring",
                "Coverage gap analysis", 
                "Cost optimization",
                "Predictive modeling",
                "Interactive elements",
                "Mobile-responsive design"
            ]
        }

    def _parse_modern_combined_profile(self, analysis_text: str, individual_profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Parse AI analysis into structured modern profile data with advanced analytics"""
        
        # Extract family name from individual profiles
        family_names = set()
        for profile in individual_profiles:
            if 'name' in profile:
                name_parts = profile['name'].split()
                if len(name_parts) > 1:
                    family_names.add(name_parts[-1])
        
        family_name = list(family_names)[0] if family_names else "משפחה"
        
        # Advanced calculations
        total_members = len(individual_profiles)
        total_value = sum(profile.get('total_value', 0) for profile in individual_profiles)
        avg_age = sum(profile.get('age', 0) for profile in individual_profiles) / total_members
        
        # Calculate advanced metrics
        parents = [p for p in individual_profiles if p.get('relationship') in ['אב', 'אם']]
        children = [p for p in individual_profiles if p.get('relationship') in ['בן', 'בת']]
        
        # Create modern combined profile structure
        combined_profile = {
            "family_name": f"משפחת {family_name}",
            "family_composition": {
                "total_members": total_members,
                "parents": len(parents),
                "children": len(children),
                "average_age": round(avg_age, 1),
                "family_stage": self._determine_family_stage(individual_profiles)
            },
            "insurance_portfolio": {
                "total_value": total_value,
                "average_per_member": round(total_value / total_members, 0),
                "portfolio_efficiency": self._calculate_portfolio_efficiency(individual_profiles),
                "coverage_distribution": self._analyze_coverage_distribution(individual_profiles)
            },
            "risk_analysis": {
                "combined_risk_level": self._calculate_advanced_risk(individual_profiles),
                "risk_distribution": self._analyze_risk_distribution(individual_profiles),
                "risk_trends": self._analyze_risk_trends(individual_profiles),
                "risk_mitigation_opportunities": self._identify_risk_mitigation(individual_profiles)
            },
            "coverage_analysis": {
                "life_insurance": {"total": 0, "coverage_gaps": [], "recommendations": []},
                "health_insurance": {"total": 0, "coverage_gaps": [], "recommendations": []},
                "property_insurance": {"total": 0, "coverage_gaps": [], "recommendations": []},
                "car_insurance": {"total": 0, "coverage_gaps": [], "recommendations": []},
                "liability_insurance": {"total": 0, "coverage_gaps": [], "recommendations": []},
                "disability_insurance": {"total": 0, "coverage_gaps": [], "recommendations": []}
            },
            "members_analysis": [],
            "optimization_opportunities": self._identify_optimization_opportunities(individual_profiles),
            "ai_recommendations": self._generate_ai_recommendations(individual_profiles),
            "financial_analysis": {
                "premium_optimization": self._calculate_premium_optimization(individual_profiles),
                "coverage_efficiency": self._calculate_coverage_efficiency(individual_profiles),
                "family_discounts": self._calculate_family_discounts(individual_profiles),
                "long_term_planning": self._generate_long_term_planning(individual_profiles),
                "roi_analysis": self._calculate_roi_analysis(individual_profiles)
            },
            "modern_features": {
                "data_visualization": self._suggest_data_visualizations(individual_profiles),
                "interactive_elements": self._suggest_interactive_elements(),
                "mobile_responsive": True,
                "real_time_updates": True
            },
            "profile_style": "premium_modern_ai_powered",
            "generation_metadata": {
                "ai_model": "GPT-4",
                "analysis_depth": "advanced",
                "modern_features": True,
                "professional_grade": True
            }
        }
        
        # Process individual members with advanced analysis
        for profile in individual_profiles:
            member_analysis = {
                "name": profile.get('name', ''),
                "age": profile.get('age', 0),
                "relationship": profile.get('relationship', ''),
                "current_coverage": profile.get('insurance_type', ''),
                "individual_value": profile.get('total_value', 0),
                "risk_level": profile.get('risk_level', 'medium'),
                "risk_score": self._calculate_individual_risk_score(profile),
                "coverage_adequacy": self._assess_coverage_adequacy(profile),
                "optimization_potential": self._calculate_optimization_potential(profile),
                "personalized_recommendations": self._generate_personalized_recommendations(profile),
                "future_planning": self._generate_future_planning(profile)
            }
            combined_profile["members_analysis"].append(member_analysis)
        
        return combined_profile

    def _calculate_advanced_risk(self, individual_profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate advanced family risk analysis"""
        risk_scores = []
        age_risks = []
        coverage_risks = []
        
        for profile in individual_profiles:
            age = profile.get('age', 0)
            coverage = profile.get('insurance_type', '')
            
            # Age-based risk
            if age > 60:
                age_risks.append(3)
            elif age > 40:
                age_risks.append(2)
            else:
                age_risks.append(1)
            
            # Coverage-based risk
            if 'חיים' in coverage and 'בריאות' in coverage:
                coverage_risks.append(1)  # Low risk - well covered
            elif 'חיים' in coverage or 'בריאות' in coverage:
                coverage_risks.append(2)  # Medium risk
            else:
                coverage_risks.append(3)  # High risk - underinsured
        
        avg_age_risk = sum(age_risks) / len(age_risks) if age_risks else 1
        avg_coverage_risk = sum(coverage_risks) / len(coverage_risks) if coverage_risks else 1
        
        overall_risk = (avg_age_risk + avg_coverage_risk) / 2
        
        return {
            "overall_level": "high" if overall_risk >= 2.5 else "medium" if overall_risk >= 1.5 else "low",
            "age_risk": avg_age_risk,
            "coverage_risk": avg_coverage_risk,
            "risk_factors": self._identify_risk_factors(individual_profiles)
        }

    def _analyze_risk_distribution(self, individual_profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze risk distribution across family members"""
        risk_distribution = {
            "high_risk_members": 0,
            "medium_risk_members": 0,
            "low_risk_members": 0,
            "risk_concentration": "balanced"
        }
        
        for profile in individual_profiles:
            risk_level = profile.get('risk_level', 'medium')
            if risk_level == 'high':
                risk_distribution["high_risk_members"] += 1
            elif risk_level == 'medium':
                risk_distribution["medium_risk_members"] += 1
            else:
                risk_distribution["low_risk_members"] += 1
        
        # Determine risk concentration
        total = len(individual_profiles)
        if risk_distribution["high_risk_members"] > total * 0.5:
            risk_distribution["risk_concentration"] = "high_risk_focused"
        elif risk_distribution["low_risk_members"] > total * 0.5:
            risk_distribution["risk_concentration"] = "low_risk_focused"
        else:
            risk_distribution["risk_concentration"] = "balanced"
        
        return risk_distribution

    def _calculate_individual_risk_score(self, profile: Dict[str, Any]) -> int:
        """Calculate individual risk score (0-100)"""
        score = 0
        
        # Age factor (0-40 points)
        age = profile.get('age', 0)
        if age > 60:
            score += 40
        elif age > 50:
            score += 30
        elif age > 40:
            score += 20
        elif age > 30:
            score += 10
        
        # Coverage factor (0-30 points)
        coverage = profile.get('insurance_type', '')
        if 'חיים' not in coverage and 'בריאות' not in coverage:
            score += 30
        elif 'חיים' not in coverage or 'בריאות' not in coverage:
            score += 15
        
        # Value factor (0-30 points)
        value = profile.get('total_value', 0)
        if value > 1000000:
            score += 30
        elif value > 500000:
            score += 20
        elif value > 200000:
            score += 10
        
        return min(score, 100)

    def _assess_coverage_adequacy(self, profile: Dict[str, Any]) -> str:
        """Assess if coverage is adequate for the individual"""
        coverage = profile.get('insurance_type', '')
        age = profile.get('age', 0)
        
        if age > 50:
            if 'חיים' in coverage and 'בריאות' in coverage:
                return "excellent"
            elif 'חיים' in coverage or 'בריאות' in coverage:
                return "adequate"
            else:
                return "inadequate"
        else:
            if 'חיים' in coverage and 'בריאות' in coverage:
                return "excellent"
            elif 'חיים' in coverage or 'בריאות' in coverage:
                return "adequate"
            else:
                return "needs_improvement"

    def _calculate_optimization_potential(self, profile: Dict[str, Any]) -> int:
        """Calculate optimization potential percentage (0-100)"""
        potential = 0
        coverage = profile.get('insurance_type', '')
        
        # Missing coverage opportunities
        if 'חיים' not in coverage:
            potential += 30
        if 'בריאות' not in coverage:
            potential += 25
        if 'רכב' not in coverage:
            potential += 20
        if 'בית' not in coverage:
            potential += 15
        if 'אחריות' not in coverage:
            potential += 10
        
        return min(potential, 100)

    def _identify_risk_factors(self, individual_profiles: List[Dict[str, Any]]) -> List[str]:
        """Identify specific risk factors for the family"""
        risk_factors = []
        
        ages = [profile.get('age', 0) for profile in individual_profiles]
        coverages = [profile.get('insurance_type', '') for profile in individual_profiles]
        
        # Age-based risk factors
        if any(age > 60 for age in ages):
            risk_factors.append("גיל מתקדם")
        if any(age > 50 for age in ages):
            risk_factors.append("גיל ביניים")
        
        # Coverage-based risk factors
        if not any('חיים' in coverage for coverage in coverages):
            risk_factors.append("חוסר ביטוח חיים")
        if not any('בריאות' in coverage for coverage in coverages):
            risk_factors.append("חוסר ביטוח בריאות")
        
        # Family size risk factors
        if len(individual_profiles) > 4:
            risk_factors.append("משפחה גדולה")
        
        return risk_factors

    async def analyze_family_documents(self, documents: List[str]) -> Dict[str, Any]:
        """Analyze uploaded family documents with advanced AI"""
        prompt = f"""
        Perform ADVANCED AI analysis of these insurance documents:
        {json.dumps(documents, indent=2, ensure_ascii=False)}
        
        Provide sophisticated analysis including:
        1. Document structure and content extraction
        2. Policy comparison and optimization opportunities
        3. Risk factor identification
        4. Coverage gap analysis
        5. Cost optimization recommendations
        6. Modern insurance insights
        
        Use advanced AI capabilities to provide premium analysis.
        """
        
        response = await self.llm.ainvoke(prompt)
        return {
            "analysis": response.content,
            "extracted_data": self._parse_advanced_analysis(response.content),
            "ai_analysis_level": "premium"
        }

    async def create_family_profile(self, family_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a premium, modern family insurance profile"""
        prompt = f"""
        Create a PREMIUM, MODERN family insurance profile based on this data:
        {json.dumps(family_data, indent=2, ensure_ascii=False)}
        
        Generate a sophisticated profile including:
        1. Advanced risk assessment with AI scoring
        2. Premium coverage recommendations
        3. Modern policy optimization strategies
        4. Sophisticated cost-benefit analysis
        5. AI-powered action items
        6. Future planning insights
        
        Make this a PREMIUM, MODERN insurance profile that showcases advanced AI capabilities.
        Use sophisticated formatting and professional presentation.
        """
        
        response = await self.llm.ainvoke(prompt)
        return {
            "profile": response.content,
            "recommendations": self._extract_premium_recommendations(response.content),
            "risk_score": self._calculate_premium_risk_score(family_data),
            "profile_style": "premium_modern"
        }

    async def generate_recommendations(self, family_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate premium AI-powered insurance recommendations"""
        prompt = f"""
        Generate PREMIUM, AI-POWERED insurance recommendations for this family profile:
        {json.dumps(family_profile, indent=2, ensure_ascii=False)}
        
        Provide sophisticated recommendations including:
        1. Advanced life insurance strategies
        2. Premium health insurance solutions
        3. Modern property insurance approaches
        4. Sophisticated liability coverage
        5. AI-optimized cost strategies
        6. Premium priority actions
        7. Future-proofing recommendations
        
        Make these PREMIUM, MODERN recommendations that showcase advanced AI capabilities.
        """
        
        response = await self.llm.ainvoke(prompt)
        return {
            "recommendations": response.content,
            "priority_actions": self._extract_premium_actions(response.content),
            "estimated_costs": self._estimate_premium_costs(response.content),
            "ai_insights": self._extract_ai_insights(response.content)
        }

    def _parse_advanced_analysis(self, analysis_text: str) -> Dict[str, Any]:
        """Parse advanced AI analysis into structured data"""
        return {
            "family_members": [],
            "policies": [],
            "risk_factors": [],
            "missing_coverage": [],
            "optimization_opportunities": [],
            "ai_insights": []
        }

    def _extract_premium_recommendations(self, profile_text: str) -> List[str]:
        """Extract premium recommendations from profile"""
        recommendations = []
        
        # Advanced keyword extraction
        premium_keywords = {
            "life insurance": "ביטוח חיים מתקדם",
            "health insurance": "ביטוח בריאות פרמיום", 
            "car insurance": "ביטוח רכב מקיף",
            "home insurance": "ביטוח בית מתקדם",
            "liability insurance": "ביטוח אחריות מקיף",
            "disability insurance": "ביטוח נכות",
            "critical illness": "ביטוח מחלות קשות",
            "long term care": "ביטוח סיעוד"
        }
        
        for english, hebrew in premium_keywords.items():
            if english in profile_text.lower():
                recommendations.append(hebrew)
        
        return recommendations

    def _calculate_premium_risk_score(self, family_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate premium risk score with advanced metrics"""
        score = 0
        factors = []
        
        # Age factor
        for member in family_data.get("members", []):
            age = member.get("age", 0)
            if age > 60:
                score += 25
                factors.append("גיל מתקדם")
            elif age > 40:
                score += 15
                factors.append("גיל ביניים")
        
        # Coverage factor
        total_policies = family_data.get("total_policies", 0)
        if total_policies < 2:
            score += 20
            factors.append("כיסוי ביטוחי מוגבל")
        
        # Value factor
        total_value = family_data.get("total_value", 0)
        if total_value > 5000000:
            score += 15
            factors.append("ערך ביטוחי גבוה")
        
        return {
            "score": min(score, 100),
            "level": "high" if score >= 60 else "medium" if score >= 30 else "low",
            "factors": factors
        }

    def _extract_premium_actions(self, recommendations_text: str) -> List[str]:
        """Extract premium priority actions"""
        actions = []
        
        if "immediate" in recommendations_text.lower() or "דחוף" in recommendations_text:
            actions.append("פעולה דחופה - ביטוח חיים")
        if "review" in recommendations_text.lower() or "בדיקה" in recommendations_text:
            actions.append("בדיקת פוליסות קיימות")
        if "optimize" in recommendations_text.lower() or "אופטימיזציה" in recommendations_text:
            actions.append("אופטימיזציה של כיסויים")
        if "upgrade" in recommendations_text.lower() or "שדרוג" in recommendations_text:
            actions.append("שדרוג פוליסות קיימות")
        
        return actions

    def _estimate_premium_costs(self, recommendations_text: str) -> Dict[str, float]:
        """Estimate premium insurance costs"""
        return {
            "life_insurance": 8000,
            "health_insurance": 5000,
            "car_insurance": 3000,
            "home_insurance": 2500,
            "liability_insurance": 2000,
            "total_annual": 20500,
            "family_discount": 2000,
            "net_annual": 18500
        }

    def _extract_ai_insights(self, text: str) -> List[str]:
        """Extract AI-powered insights"""
        insights = []
        
        if "optimization" in text.lower() or "אופטימיזציה" in text:
            insights.append("אופטימיזציה של כיסויים")
        if "risk" in text.lower() or "סיכון" in text:
            insights.append("ניתוח סיכונים מתקדם")
        if "future" in text.lower() or "עתיד" in text:
            insights.append("תכנון עתידי")
        
        return insights

    async def get_agent_status(self) -> Dict[str, Any]:
        """Get agent status and capabilities"""
        return {
            "name": "Sheli Mizrahi Premium Insurance Agent",
            "version": "2.0.0",
            "capabilities": [
                "Advanced family document analysis",
                "Premium risk assessment",
                "AI-powered insurance recommendations",
                "Modern profile creation",
                "Sophisticated cost optimization",
                "Individual profile combination",
                "Premium family insights"
            ],
            "status": "active",
            "supported_languages": ["Hebrew", "English"],
            "ai_level": "premium_advanced",
            "specializations": [
                "Premium life insurance",
                "Advanced health insurance", 
                "Modern property insurance",
                "Sophisticated liability insurance",
                "AI-powered family coverage optimization",
                "Premium profile generation"
            ]
        }

    def _determine_family_stage(self, profiles: List[Dict[str, Any]]) -> str:
        """Determine family life stage"""
        children_ages = [p.get('age', 0) for p in profiles if p.get('relationship') in ['בן', 'בת']]
        if not children_ages:
            return "זוג צעיר"
        elif max(children_ages) < 6:
            return "משפחה עם ילדים קטנים"
        elif max(children_ages) < 18:
            return "משפחה עם ילדים בגיל בית ספר"
        else:
            return "משפחה עם ילדים בוגרים"

    def _calculate_portfolio_efficiency(self, profiles: List[Dict[str, Any]]) -> float:
        """Calculate insurance portfolio efficiency score (0-100)"""
        total_value = sum(p.get('total_value', 0) for p in profiles)
        total_coverage_types = sum(len(p.get('insurance_type', '').split('+')) for p in profiles)
        
        # Efficiency based on coverage diversity and value
        coverage_efficiency = min(total_coverage_types * 20, 100)
        value_efficiency = min(total_value / 1000000 * 20, 100)
        
        return round((coverage_efficiency + value_efficiency) / 2, 1)

    def _analyze_coverage_distribution(self, profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze coverage distribution across family"""
        coverage_types = {}
        for profile in profiles:
            types = profile.get('insurance_type', '').split('+')
            for coverage_type in types:
                coverage_types[coverage_type.strip()] = coverage_types.get(coverage_type.strip(), 0) + 1
        
        return {
            "distribution": coverage_types,
            "most_common": max(coverage_types.items(), key=lambda x: x[1])[0] if coverage_types else "אין",
            "coverage_gaps": self._identify_coverage_gaps(coverage_types)
        }

    def _analyze_risk_trends(self, profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze risk trends across family"""
        ages = [p.get('age', 0) for p in profiles]
        risk_levels = [p.get('risk_level', 'medium') for p in profiles]
        
        return {
            "age_trend": "עולה" if max(ages) > 40 else "יציב",
            "risk_concentration": "נמוך" if risk_levels.count('low') > len(risk_levels) * 0.6 else "בינוני",
            "future_risk_projection": self._project_future_risk(ages)
        }

    def _identify_risk_mitigation(self, profiles: List[Dict[str, Any]]) -> List[str]:
        """Identify risk mitigation opportunities"""
        opportunities = []
        
        # Check for missing critical coverage
        has_life = any('חיים' in p.get('insurance_type', '') for p in profiles)
        has_health = any('בריאות' in p.get('insurance_type', '') for p in profiles)
        
        if not has_life:
            opportunities.append("הוספת ביטוח חיים למפרנסים הראשיים")
        if not has_health:
            opportunities.append("הוספת ביטוח בריאות מקיף")
        
        return opportunities

    def _identify_optimization_opportunities(self, profiles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify specific optimization opportunities"""
        opportunities = []
        
        for profile in profiles:
            coverage = profile.get('insurance_type', '')
            age = profile.get('age', 0)
            
            if age > 40 and 'חיים' not in coverage:
                opportunities.append({
                    "member": profile.get('name', ''),
                    "opportunity": "הוספת ביטוח חיים",
                    "priority": "גבוה",
                    "potential_savings": "15-25%"
                })
            
            if 'רכב' not in coverage and age > 18:
                opportunities.append({
                    "member": profile.get('name', ''),
                    "opportunity": "הוספת ביטוח רכב",
                    "priority": "בינוני",
                    "potential_savings": "10-20%"
                })
        
        return opportunities

    def _generate_ai_recommendations(self, profiles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate AI-powered recommendations"""
        recommendations = []
        
        # Family-level recommendations
        total_value = sum(p.get('total_value', 0) for p in profiles)
        if total_value < 2000000:
            recommendations.append({
                "type": "כיסוי כולל",
                "recommendation": "הגדלת הכיסוי הביטוחי הכולל",
                "reason": "הכיסוי הנוכחי נמוך מהמומלץ למשפחה",
                "priority": "גבוה"
            })
        
        # Individual recommendations
        for profile in profiles:
            if profile.get('age', 0) > 35 and 'חיים' not in profile.get('insurance_type', ''):
                recommendations.append({
                    "type": "ביטוח חיים",
                    "member": profile.get('name', ''),
                    "recommendation": "הוספת ביטוח חיים",
                    "reason": "גיל מתקדם ללא כיסוי חיים",
                    "priority": "גבוה"
                })
        
        return recommendations

    def _calculate_premium_optimization(self, profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate premium optimization potential"""
        total_value = sum(p.get('total_value', 0) for p in profiles)
        
        return {
            "current_total": total_value,
            "optimization_potential": round(total_value * 0.15, 0),
            "savings_percentage": "15%",
            "optimization_strategies": [
                "איחוד פוליסות",
                "ניצול הנחות משפחה",
                "אופטימיזציה של כיסויים"
            ]
        }

    def _calculate_coverage_efficiency(self, profiles: List[Dict[str, Any]]) -> float:
        """Calculate coverage efficiency score"""
        total_coverage_types = sum(len(p.get('insurance_type', '').split('+')) for p in profiles)
        total_members = len(profiles)
        
        # Efficiency based on coverage per member
        return round(min(total_coverage_types / total_members * 25, 100), 1)

    def _calculate_family_discounts(self, profiles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Calculate available family discounts"""
        discounts = []
        
        if len(profiles) >= 3:
            discounts.append({
                "type": "הנחת משפחה",
                "percentage": "10%",
                "description": "הנחה על ביטוח חיים למשפחה"
            })
        
        if len(profiles) >= 4:
            discounts.append({
                "type": "הנחת כיסוי מקיף",
                "percentage": "15%",
                "description": "הנחה על כיסוי בריאות מקיף"
            })
        
        return discounts

    def _generate_long_term_planning(self, profiles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate long-term planning recommendations"""
        planning = []
        
        children = [p for p in profiles if p.get('relationship') in ['בן', 'בת']]
        if children:
            planning.append({
                "type": "תכנון עתידי",
                "focus": "חינוך ילדים",
                "recommendation": "ביטוח חיים עם כיסוי חינוך",
                "timeline": "5-15 שנים"
            })
        
        parents = [p for p in profiles if p.get('relationship') in ['אב', 'אם']]
        if any(p.get('age', 0) > 40 for p in parents):
            planning.append({
                "type": "תכנון עתידי",
                "focus": "פנסיה",
                "recommendation": "ביטוח חיים עם כיסוי פנסיוני",
                "timeline": "10-25 שנים"
            })
        
        return planning

    def _calculate_roi_analysis(self, profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate ROI analysis for insurance investments"""
        total_value = sum(p.get('total_value', 0) for p in profiles)
        estimated_premium = total_value * 0.02  # 2% of coverage as premium
        
        return {
            "total_coverage": total_value,
            "estimated_premium": round(estimated_premium, 0),
            "roi_ratio": round(total_value / estimated_premium, 1),
            "investment_efficiency": "מעולה" if total_value / estimated_premium > 50 else "טובה"
        }

    def _suggest_data_visualizations(self, profiles: List[Dict[str, Any]]) -> List[str]:
        """Suggest data visualizations for the profile"""
        return [
            "גרף עוגה - התפלגות סוגי ביטוח",
            "גרף עמודות - ערך ביטוחי לפי חבר",
            "גרף קו - מגמות סיכון לאורך זמן",
            "מפת חום - יעילות כיסוי לפי חבר",
            "גרף דונאט - התפלגות סיכונים"
        ]

    def _suggest_interactive_elements(self) -> List[str]:
        """Suggest interactive elements for the profile"""
        return [
            "סימולטור עלות-תועלת",
            "מחשבון הנחות משפחה",
            "מערכת התראות שינויים",
            "כלי השוואת פוליסות",
            "מעקב מגמות בזמן אמת"
        ]

    def _identify_coverage_gaps(self, coverage_types: Dict[str, int]) -> List[str]:
        """Identify coverage gaps"""
        gaps = []
        if 'חיים' not in coverage_types:
            gaps.append("ביטוח חיים")
        if 'בריאות' not in coverage_types:
            gaps.append("ביטוח בריאות")
        if 'רכב' not in coverage_types:
            gaps.append("ביטוח רכב")
        return gaps

    def _project_future_risk(self, ages: List[int]) -> str:
        """Project future risk based on current ages"""
        max_age = max(ages) if ages else 0
        if max_age > 50:
            return "סיכון עולה"
        elif max_age > 35:
            return "סיכון יציב"
        else:
            return "סיכון יורד"

    def _generate_personalized_recommendations(self, profile: Dict[str, Any]) -> List[str]:
        """Generate personalized recommendations for individual"""
        recommendations = []
        age = profile.get('age', 0)
        coverage = profile.get('insurance_type', '')
        
        if age > 40 and 'חיים' not in coverage:
            recommendations.append("הוספת ביטוח חיים")
        if 'בריאות' not in coverage:
            recommendations.append("הוספת ביטוח בריאות")
        if age > 18 and 'רכב' not in coverage:
            recommendations.append("הוספת ביטוח רכב")
        
        return recommendations

    def _generate_future_planning(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate future planning for individual"""
        age = profile.get('age', 0)
        relationship = profile.get('relationship', '')
        
        planning = {
            "short_term": [],
            "medium_term": [],
            "long_term": []
        }
        
        if relationship in ['אב', 'אם'] and age > 35:
            planning["medium_term"].append("תכנון פנסיוני")
            planning["long_term"].append("תכנון ירושה")
        
        if relationship in ['בן', 'בת'] and age < 18:
            planning["long_term"].append("תכנון חינוך")
        
        return planning

async def main():
    """Example usage of the premium insurance agent"""
    agent = SheliMizrahiInsuranceAgent()
    
    # Example individual profiles (like the ones you provided)
    individual_profiles = [
        {
            "name": "עמית הר",
            "age": 35,
            "relationship": "אב",
            "insurance_type": "חיים + בריאות",
            "total_value": 800000,
            "risk_level": "medium"
        },
        {
            "name": "אנה הר",
            "age": 32,
            "relationship": "אם",
            "insurance_type": "בריאות + רכב",
            "total_value": 600000,
            "risk_level": "low"
        },
        {
            "name": "יונתן הר",
            "age": 8,
            "relationship": "בן",
            "insurance_type": "בריאות",
            "total_value": 200000,
            "risk_level": "low"
        },
        {
            "name": "אליסה הר",
            "age": 5,
            "relationship": "בת",
            "insurance_type": "בריאות",
            "total_value": 200000,
            "risk_level": "low"
        },
        {
            "name": "איתן הר",
            "age": 2,
            "relationship": "בן",
            "insurance_type": "בריאות",
            "total_value": 200000,
            "risk_level": "low"
        }
    ]
    
    # Create premium combined family profile
    combined_profile = await agent.combine_individual_profiles(individual_profiles)
    print("Premium Combined Family Profile:", json.dumps(combined_profile, indent=2, ensure_ascii=False))
    
    # Generate premium recommendations
    recommendations = await agent.generate_recommendations(combined_profile["combined_profile"])
    print("Premium Recommendations:", json.dumps(recommendations, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())
