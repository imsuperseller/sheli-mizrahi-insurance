import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET() {
  try {
    // Read the combined family profile JSON file
    const filePath = path.join(process.cwd(), 'combined-family-profile.json')
    
    if (!fs.existsSync(filePath)) {
      return NextResponse.json({ error: 'Family profile not found' }, { status: 404 })
    }
    
    const fileContent = fs.readFileSync(filePath, 'utf-8')
    const familyProfile = JSON.parse(fileContent)
    
    return NextResponse.json(familyProfile)
  } catch (error) {
    console.error('Error reading family profile:', error)
    return NextResponse.json({ error: 'Failed to load family profile' }, { status: 500 })
  }
}
