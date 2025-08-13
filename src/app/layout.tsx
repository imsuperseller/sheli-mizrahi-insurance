import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "שלי מזרחי ביטוח - מערכת ניהול פרופילי משפחה",
  description: "מערכת מתקדמת לניהול וניתוח פרופילי ביטוח משפחתיים",
  keywords: ["ביטוח", "משפחה", "ניהול", "פרופילים", "שלי מזרחי"],
  authors: [{ name: "Sheli Mizrahi Insurance" }],
  viewport: "width=device-width, initial-scale=1",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="he" dir="rtl">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        suppressHydrationWarning={true}
      >
        {children}
      </body>
    </html>
  );
}
