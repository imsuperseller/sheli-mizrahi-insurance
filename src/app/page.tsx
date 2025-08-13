'use client'

import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  Users, 
  FileText, 
  Shield, 
  Upload, 
  Search, 
  Bell, 
  Settings, 
  User, 
  Plus,
  Home,
  Heart,
  Car,
  Building,
  Activity,
  TrendingUp,
  CheckCircle,
  AlertCircle,
  Clock,
  ChevronRight,
  Eye,
  Edit,
  Trash2
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Progress } from '@/components/ui/progress'
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog'
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger } from '@/components/ui/dropdown-menu'

// Types
interface FamilyMember {
  id: string
  name: string
  age: number
  relationship: string
  insuranceType: string
  status: 'active' | 'pending' | 'expired'
  documents: number
  lastUpdated: string
}

interface FamilyProfile {
  id: string
  familyName: string
  members: FamilyMember[]
  totalPolicies: number
  totalValue: number
  riskLevel: 'low' | 'medium' | 'high'
  lastAssessment: string
  status: 'complete' | 'incomplete' | 'review'
}

interface UploadedDocument {
  id: string
  name: string
  type: string
  size: string
  uploadedAt: string
  status: 'processing' | 'analyzed' | 'error'
  familyMember?: string
}

export default function SheliMizrahiDashboard() {
  const [families, setFamilies] = useState<FamilyProfile[]>([])
  const [uploadedDocs, setUploadedDocs] = useState<UploadedDocument[]>([])
  const [isUploading, setIsUploading] = useState(false)
  const [selectedFamily, setSelectedFamily] = useState<FamilyProfile | null>(null)
  const [isClient, setIsClient] = useState(false)

  // Ensure client-side rendering
  useEffect(() => {
    setIsClient(true)
  }, [])

  // Mock data
  useEffect(() => {
    if (!isClient) return

    setFamilies([
      {
        id: '1',
        familyName: 'משפחת כהן',
        members: [
          { id: '1', name: 'יוסי כהן', age: 45, relationship: 'אב', insuranceType: 'חיים + בריאות', status: 'active', documents: 3, lastUpdated: '2024-01-15' },
          { id: '2', name: 'שרה כהן', age: 42, relationship: 'אם', insuranceType: 'בריאות + רכב', status: 'active', documents: 2, lastUpdated: '2024-01-10' },
          { id: '3', name: 'דניאל כהן', age: 18, relationship: 'בן', insuranceType: 'רכב', status: 'pending', documents: 1, lastUpdated: '2024-01-12' }
        ],
        totalPolicies: 4,
        totalValue: 2500000,
        riskLevel: 'medium',
        lastAssessment: '2024-01-15',
        status: 'complete'
      },
      {
        id: '2',
        familyName: 'משפחת לוי',
        members: [
          { id: '4', name: 'דוד לוי', age: 38, relationship: 'אב', insuranceType: 'חיים + בריאות + רכב', status: 'active', documents: 4, lastUpdated: '2024-01-08' },
          { id: '5', name: 'רחל לוי', age: 35, relationship: 'אם', insuranceType: 'בריאות + בית', status: 'active', documents: 3, lastUpdated: '2024-01-05' }
        ],
        totalPolicies: 5,
        totalValue: 1800000,
        riskLevel: 'low',
        lastAssessment: '2024-01-08',
        status: 'complete'
      }
    ])

    setUploadedDocs([
      { id: '1', name: 'תעודת זהות - יוסי כהן.pdf', type: 'תעודה רשמית', size: '2.3 MB', uploadedAt: '2024-01-15', status: 'analyzed', familyMember: 'יוסי כהן' },
      { id: '2', name: 'פוליסת חיים - שרה כהן.pdf', type: 'פוליסה', size: '1.8 MB', uploadedAt: '2024-01-10', status: 'analyzed', familyMember: 'שרה כהן' },
      { id: '3', name: 'רישיון נהיגה - דניאל כהן.jpg', type: 'רישיון', size: '0.5 MB', uploadedAt: '2024-01-12', status: 'processing' }
    ])
  }, [isClient])

  const handleFileUpload = (files: FileList) => {
    if (!isClient) return
    
    setIsUploading(true)
    // Simulate upload process
    setTimeout(() => {
      const newDocs = Array.from(files).map((file, index) => ({
        id: `${Date.now()}-${index}`,
        name: file.name,
        type: 'מסמך חדש',
        size: `${(file.size / 1024 / 1024).toFixed(1)} MB`,
        uploadedAt: new Date().toISOString().split('T')[0],
        status: 'processing' as const
      }))
      setUploadedDocs(prev => [...newDocs, ...prev])
      setIsUploading(false)
    }, 2000)
  }

  const getRiskLevelColor = (level: string) => {
    switch (level) {
      case 'low': return 'text-green-600 bg-green-100'
      case 'medium': return 'text-yellow-600 bg-yellow-100'
      case 'high': return 'text-red-600 bg-red-100'
      default: return 'text-gray-600 bg-gray-100'
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'text-green-600'
      case 'pending': return 'text-yellow-600'
      case 'expired': return 'text-red-600'
      default: return 'text-gray-600'
    }
  }

  // Don't render until client-side
  if (!isClient) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">טוען...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50">
      {/* Header */}
      <motion.header 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="sticky top-0 z-50 border-b bg-white/90 backdrop-blur-lg shadow-sm"
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex h-16 items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="h-10 w-10 rounded-xl gradient-blue flex items-center justify-center shadow-lg">
                <Shield className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">שלי מזרחי ביטוח</h1>
                <p className="text-sm text-gray-600">מערכת ניהול פרופילי משפחה</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="relative max-w-md w-full">
                <Search className="absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400" />
                <input 
                  type="text" 
                  placeholder="חיפוש משפחות..." 
                  className="w-full pr-10 pl-4 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500/20 transition-all bg-white/80"
                />
              </div>

              <Button variant="outline" size="sm" className="relative">
                <Bell className="h-4 w-4" />
                <span className="absolute -top-1 -right-1 h-3 w-3 bg-red-500 rounded-full"></span>
              </Button>
              
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="outline" size="sm">
                    <User className="h-4 w-4" />
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuLabel>שלי מזרחי</DropdownMenuLabel>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem>הגדרות</DropdownMenuItem>
                  <DropdownMenuItem>התנתק</DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>
          </div>
        </div>
      </motion.header>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Tabs defaultValue="families" className="space-y-8">
          <TabsList className="grid w-full grid-cols-3 max-w-md mx-auto">
            <TabsTrigger value="families" className="flex items-center space-x-2">
              <Users className="h-4 w-4" />
              <span>משפחות</span>
            </TabsTrigger>
            <TabsTrigger value="documents" className="flex items-center space-x-2">
              <FileText className="h-4 w-4" />
              <span>מסמכים</span>
            </TabsTrigger>
            <TabsTrigger value="analytics" className="flex items-center space-x-2">
              <TrendingUp className="h-4 w-4" />
              <span>ניתוח</span>
            </TabsTrigger>
          </TabsList>

          {/* Families Tab */}
          <TabsContent value="families" className="space-y-8">
            <div className="flex justify-between items-center">
              <div>
                <h2 className="text-3xl font-bold text-gray-900">פרופילי משפחה</h2>
                <p className="text-gray-600 mt-2">ניהול וניתוח פרופילי ביטוח משפחתיים</p>
              </div>
              <Dialog>
                <DialogTrigger asChild>
                  <Button className="gradient-blue text-white shadow-lg hover:shadow-xl transition-all">
                    <Plus className="h-4 w-4 ml-2" />
                    משפחה חדשה
                  </Button>
                </DialogTrigger>
                <DialogContent className="max-w-md">
                  <DialogHeader>
                    <DialogTitle>הוספת משפחה חדשה</DialogTitle>
                    <DialogDescription>
                      העלה מסמכי משפחה כדי ליצור פרופיל ביטוח מאוחד
                    </DialogDescription>
                  </DialogHeader>
                  <div className="space-y-4">
                    <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-blue-400 transition-colors">
                      <Upload className="h-8 w-8 mx-auto text-gray-400 mb-2" />
                      <p className="text-sm text-gray-600">גרור קבצים לכאן או לחץ לבחירה</p>
                      <input 
                        type="file" 
                        multiple 
                        className="hidden" 
                        onChange={(e) => e.target.files && handleFileUpload(e.target.files)}
                      />
                    </div>
                  </div>
                </DialogContent>
              </Dialog>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
              {families.map((family) => (
                <motion.div
                  key={family.id}
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  whileHover={{ scale: 1.02 }}
                  className="group"
                >
                  <Card className="h-full hover:shadow-xl transition-all duration-300 border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                    <CardHeader className="pb-4">
                      <div className="flex justify-between items-start">
                        <div className="flex-1">
                          <CardTitle className="text-xl mb-2">{family.familyName}</CardTitle>
                          <CardDescription className="text-sm">
                            {family.members.length} חברי משפחה • {family.totalPolicies} פוליסות
                          </CardDescription>
                        </div>
                        <span className={`px-3 py-1 rounded-full text-xs font-medium ${getRiskLevelColor(family.riskLevel)}`}>
                          {family.riskLevel === 'low' ? 'סיכון נמוך' : 
                           family.riskLevel === 'medium' ? 'סיכון בינוני' : 'סיכון גבוה'}
                        </span>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="space-y-3">
                        {family.members.slice(0, 3).map((member) => (
                          <div key={member.id} className="flex justify-between items-center text-sm p-2 rounded-lg bg-gray-50/50">
                            <span className="font-medium">{member.name}</span>
                            <span className={`px-2 py-1 rounded-full text-xs ${getStatusColor(member.status)}`}>
                              {member.status === 'active' ? 'פעיל' : 
                               member.status === 'pending' ? 'ממתין' : 'פג תוקף'}
                            </span>
                          </div>
                        ))}
                        {family.members.length > 3 && (
                          <p className="text-xs text-gray-500 text-center">+{family.members.length - 3} נוספים</p>
                        )}
                      </div>
                      
                      <div className="pt-4 border-t border-gray-100 space-y-2">
                        <div className="flex justify-between text-sm">
                          <span className="text-gray-600">ערך כולל:</span>
                          <span className="font-bold text-lg text-blue-600">₪{family.totalValue.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-gray-600">עדכון אחרון:</span>
                          <span>{family.lastAssessment}</span>
                        </div>
                      </div>

                      <div className="flex gap-2 pt-4">
                        <Button className="flex-1" variant="outline" size="sm">
                          <Eye className="h-4 w-4 ml-1" />
                          צפה בפרטים
                        </Button>
                        <Button variant="outline" size="sm">
                          <Edit className="h-4 w-4" />
                        </Button>
                        <Button variant="outline" size="sm">
                          <Trash2 className="h-4 w-4" />
                        </Button>
                      </div>
                    </CardContent>
                  </Card>
                </motion.div>
              ))}
            </div>
          </TabsContent>

          {/* Documents Tab */}
          <TabsContent value="documents" className="space-y-8">
            <div className="flex justify-between items-center">
              <div>
                <h2 className="text-3xl font-bold text-gray-900">מסמכים שהועלו</h2>
                <p className="text-gray-600 mt-2">ניהול וניתוח מסמכי ביטוח</p>
              </div>
              <Button className="gradient-blue text-white shadow-lg">
                <Upload className="h-4 w-4 ml-2" />
                העלה מסמכים
              </Button>
            </div>

            <div className="space-y-4">
              {uploadedDocs.map((doc) => (
                <motion.div
                  key={doc.id}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  className="flex items-center justify-between p-6 bg-white rounded-xl border shadow-sm hover:shadow-md transition-all"
                >
                  <div className="flex items-center space-x-4">
                    <div className="h-12 w-12 rounded-lg bg-blue-100 flex items-center justify-center">
                      <FileText className="h-6 w-6 text-blue-600" />
                    </div>
                    <div>
                      <h3 className="font-semibold text-gray-900">{doc.name}</h3>
                      <p className="text-sm text-gray-600">
                        {doc.type} • {doc.size} • {doc.familyMember && `שייך ל: ${doc.familyMember}`}
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center space-x-4">
                    <span className="text-sm text-gray-500">{doc.uploadedAt}</span>
                    {doc.status === 'processing' && (
                      <div className="flex items-center space-x-2">
                        <Clock className="h-4 w-4 text-yellow-500" />
                        <span className="text-sm text-yellow-600">מעבד</span>
                      </div>
                    )}
                    {doc.status === 'analyzed' && (
                      <div className="flex items-center space-x-2">
                        <CheckCircle className="h-4 w-4 text-green-500" />
                        <span className="text-sm text-green-600">נותח</span>
                      </div>
                    )}
                    {doc.status === 'error' && (
                      <div className="flex items-center space-x-2">
                        <AlertCircle className="h-4 w-4 text-red-500" />
                        <span className="text-sm text-red-600">שגיאה</span>
                      </div>
                    )}
                  </div>
                </motion.div>
              ))}
            </div>
          </TabsContent>

          {/* Analytics Tab */}
          <TabsContent value="analytics" className="space-y-8">
            <div>
              <h2 className="text-3xl font-bold text-gray-900">ניתוח וסטטיסטיקות</h2>
              <p className="text-gray-600 mt-2">תובנות על פוליסות הביטוח</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <Card className="bg-gradient-to-br from-blue-50 to-blue-100 border-0 shadow-lg">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-blue-900">סה"כ משפחות</CardTitle>
                  <Users className="h-5 w-5 text-blue-600" />
                </CardHeader>
                <CardContent>
                  <div className="text-3xl font-bold text-blue-900">{families.length}</div>
                  <p className="text-xs text-blue-700">+2 החודש</p>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-br from-green-50 to-green-100 border-0 shadow-lg">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-green-900">סה"כ פוליסות</CardTitle>
                  <Shield className="h-5 w-5 text-green-600" />
                </CardHeader>
                <CardContent>
                  <div className="text-3xl font-bold text-green-900">
                    {families.reduce((sum, family) => sum + family.totalPolicies, 0)}
                  </div>
                  <p className="text-xs text-green-700">+5 החודש</p>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-br from-purple-50 to-purple-100 border-0 shadow-lg">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-purple-900">ערך כולל</CardTitle>
                  <TrendingUp className="h-5 w-5 text-purple-600" />
                </CardHeader>
                <CardContent>
                  <div className="text-3xl font-bold text-purple-900">
                    ₪{families.reduce((sum, family) => sum + family.totalValue, 0).toLocaleString()}
                  </div>
                  <p className="text-xs text-purple-700">+12% החודש</p>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-br from-orange-50 to-orange-100 border-0 shadow-lg">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-orange-900">מסמכים</CardTitle>
                  <FileText className="h-5 w-5 text-orange-600" />
                </CardHeader>
                <CardContent>
                  <div className="text-3xl font-bold text-orange-900">{uploadedDocs.length}</div>
                  <p className="text-xs text-orange-700">+8 החודש</p>
                </CardContent>
              </Card>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-xl">סוגי ביטוח</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-6">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-3">
                        <Heart className="h-5 w-5 text-red-500" />
                        <span className="font-medium">ביטוח חיים</span>
                      </div>
                      <span className="font-bold text-lg">45%</span>
                    </div>
                    <Progress value={45} className="h-3" />
                    
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-3">
                        <Activity className="h-5 w-5 text-blue-500" />
                        <span className="font-medium">ביטוח בריאות</span>
                      </div>
                      <span className="font-bold text-lg">35%</span>
                    </div>
                    <Progress value={35} className="h-3" />
                    
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-3">
                        <Car className="h-5 w-5 text-green-500" />
                        <span className="font-medium">ביטוח רכב</span>
                      </div>
                      <span className="font-bold text-lg">20%</span>
                    </div>
                    <Progress value={20} className="h-3" />
                  </div>
                </CardContent>
              </Card>

              <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-xl">רמת סיכון</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-6">
                    <div className="flex items-center justify-between">
                      <span className="font-medium">סיכון נמוך</span>
                      <span className="font-bold text-lg text-green-600">60%</span>
                    </div>
                    <Progress value={60} className="h-3" />
                    
                    <div className="flex items-center justify-between">
                      <span className="font-medium">סיכון בינוני</span>
                      <span className="font-bold text-lg text-yellow-600">30%</span>
                    </div>
                    <Progress value={30} className="h-3" />
                    
                    <div className="flex items-center justify-between">
                      <span className="font-medium">סיכון גבוה</span>
                      <span className="font-bold text-lg text-red-600">10%</span>
                    </div>
                    <Progress value={10} className="h-3" />
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}
