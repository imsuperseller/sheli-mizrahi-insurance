#!/usr/bin/env python3
import pandas as pd
import json
import os
from datetime import datetime

def analyze_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        filename = os.path.basename(file_path)
        member_name = filename.split(' הר ביטוח')[0]
        
        insurance_data = []
        total_premium = 0
        
        for idx, row in df.iterrows():
            if pd.notna(row.iloc[0]) and str(row.iloc[0]).isdigit():
                premium = 0
                try:
                    if pd.notna(row.iloc[7]):
                        premium = float(str(row.iloc[7]).replace(',', ''))
                except:
                    pass
                
                insurance_entry = {
                    'main_branch': str(row.iloc[1]) if pd.notna(row.iloc[1]) else '',
                    'company': str(row.iloc[4]) if pd.notna(row.iloc[4]) else '',
                    'premium': premium,
                    'policy_number': str(row.iloc[9]) if pd.notna(row.iloc[9]) else ''
                }
                insurance_data.append(insurance_entry)
                total_premium += premium
        
        return {
            'name': member_name,
            'insurance_policies': insurance_data,
            'total_monthly_premium': total_premium,
            'policy_count': len(insurance_data)
        }
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return {}

def main():
    print("🚀 BMAD METHOD - FAMILY PROFILE SYSTEM TEST")
    print("=" * 60)
    
    data_dir = "test-data"
    family_members = []
    
    print("🔍 ANALYZING FAMILY MEMBER FILES...")
    print("=" * 50)
    
    excel_files = [f for f in os.listdir(data_dir) if f.endswith('.xlsx')]
    
    for file in excel_files:
        file_path = os.path.join(data_dir, file)
        member_data = analyze_excel_file(file_path)
        if member_data:
            family_members.append(member_data)
            print(f"✅ {member_data['name']}: {member_data['policy_count']} policies, ₪{member_data['total_monthly_premium']:.2f}/month")
    
    print(f"\n📊 TOTAL FAMILY MEMBERS: {len(family_members)}")
    
    # Generate combined profile
    total_premium = sum(member['total_monthly_premium'] for member in family_members)
    total_policies = sum(member['policy_count'] for member in family_members)
    
    combined_profile = {
        'family_name': 'משפחת הר',
        'analysis_date': datetime.now().strftime('%d/%m/%Y'),
        'total_members': len(family_members),
        'total_monthly_premium': total_premium,
        'total_policies': total_policies,
        'family_members': family_members
    }
    
    # Save to JSON
    with open('combined-family-profile.json', 'w', encoding='utf-8') as f:
        json.dump(combined_profile, f, ensure_ascii=False, indent=2)
    
    print("\n📋 FAMILY PROFILE SUMMARY")
    print("=" * 50)
    print(f"👨‍👩‍👧‍👦 Family: {combined_profile['family_name']}")
    print(f"👥 Members: {combined_profile['total_members']}")
    print(f"💰 Total Monthly Premium: ₪{combined_profile['total_monthly_premium']:.2f}")
    print(f"📄 Total Policies: {combined_profile['total_policies']}")
    
    print("\n📊 MEMBER BREAKDOWN:")
    for member in combined_profile['family_members']:
        print(f"  • {member['name']}: {member['policy_count']} policies, ₪{member['total_monthly_premium']:.2f}/month")
    
    print("\n✅ BMAD ANALYSIS COMPLETE!")
    print("💾 Profile saved to: combined-family-profile.json")

if __name__ == "__main__":
    main()
