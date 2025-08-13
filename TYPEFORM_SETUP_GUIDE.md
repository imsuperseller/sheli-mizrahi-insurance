# Typeform Setup Guide for Sheli Mizrahi Insurance Agent Requests

## 🎯 Overview
This guide will help you create a Typeform that integrates with the Sheli Mizrahi Insurance dashboard for AI agent requests.

## 📋 Step 1: Create Typeform Account
1. Go to [typeform.com](https://typeform.com)
2. Sign up or log in to your account
3. Click "Create new form"

## 🏗️ Step 2: Create the Form Structure

### Form Settings:
- **Title**: "בקשה לסוכן AI נוסף - Sheli Mizrahi Insurance"
- **Language**: Hebrew (עברית)
- **Theme**: Choose a professional theme (blue/purple gradient recommended)

### Add These Fields in Order:

#### 1. Welcome Screen
- **Type**: Welcome screen
- **Title**: "בקשה לסוכן AI נוסף"
- **Description**: "מלאו את הפרטים ונציג שלנו יצור איתכם קשר"

#### 2. Name Field
- **Type**: Short text
- **Question**: "שם מלא"
- **Description**: "הזינו את שמכם המלא"
- **Required**: Yes

#### 3. Email Field
- **Type**: Email
- **Question**: "כתובת אימייל"
- **Description**: "הזינו כתובת אימייל פעילה"
- **Required**: Yes

#### 4. Phone Field
- **Type**: Phone number
- **Question**: "מספר טלפון"
- **Description**: "הזינו מספר טלפון ליצירת קשר"
- **Required**: No

#### 5. Agent Type Field
- **Type**: Multiple choice
- **Question**: "סוג הסוכן הנדרש"
- **Description**: "בחרו את סוג הסוכן AI הנדרש לכם"
- **Options**:
  - שירות לקוחות
  - מכירות
  - תביעות
  - כתיבת פוליסות
  - ניתוח נתונים
  - סוכן מותאם אישית
- **Required**: Yes

#### 6. Description Field
- **Type**: Long text
- **Question**: "תיאור הצרכים"
- **Description**: "תארו בפירוט את הצרכים שלכם והתפקידים שהסוכן AI אמור לבצע"
- **Required**: No

#### 7. Thank You Screen
- **Type**: Thank you screen
- **Title**: "תודה!"
- **Description**: "הבקשה שלכם נשלחה בהצלחה! נציג שלנו יצור איתכם קשר בקרוב."

## 🔧 Step 3: Get Form ID
1. After creating the form, click "Share" in the top right
2. Copy the form URL (it will look like: `https://form.typeform.com/to/XXXXXXXX`)
3. The form ID is the part after `/to/` (e.g., if URL is `https://form.typeform.com/to/ABC123`, the form ID is `ABC123`)

## 🔗 Step 4: Update Backend Configuration
Once you have the form ID, update the backend configuration:

1. Open `api.py`
2. Find the line: `"form_id": "YOUR_TYPEFORM_ID"`
3. Replace `YOUR_TYPEFORM_ID` with your actual form ID

## 🎨 Step 5: Customize Appearance (Optional)
- **Colors**: Use purple/blue gradient to match the dashboard
- **Logo**: Add Sheli Mizrahi Insurance logo
- **Background**: Choose a professional background
- **Font**: Use a readable Hebrew font

## 📊 Step 6: Test the Integration
1. Start the backend server
2. Go to the dashboard
3. Click "בקשה לסוכן נוסף"
4. Fill out the form
5. Check the backend logs for the submission

## 🔔 Step 7: Set Up Notifications (Optional)
You can set up webhook notifications to:
- Send email notifications to your team
- Post to Slack/Discord
- Store in a database
- Send SMS notifications

## 📝 Field Mapping Reference
| Dashboard Field | Typeform Field | Type |
|----------------|----------------|------|
| fullName | שם מלא | Short text |
| email | כתובת אימייל | Email |
| phone | מספר טלפון | Phone |
| agentType | סוג הסוכן הנדרש | Multiple choice |
| description | תיאור הצרכים | Long text |

## 🚀 Step 8: Go Live
1. Test the form thoroughly
2. Publish the form
3. Share the dashboard URL with Sheli
4. Monitor submissions in Typeform dashboard

## 🔧 Troubleshooting
- **API Key Issues**: Make sure your Typeform API key is valid and has proper permissions
- **Form Not Loading**: Check if the form ID is correct
- **Submissions Not Working**: Verify the backend endpoint is running
- **Hebrew Text Issues**: Ensure the form is set to Hebrew language

## 📞 Support
If you need help with the Typeform setup, refer to:
- [Typeform Help Center](https://help.typeform.com)
- [Typeform API Documentation](https://developer.typeform.com)
