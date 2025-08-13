import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  experimental: {
    allowedDevOrigins: ['889fbcd03676.ngrok-free.app']
  },
  // Suppress hydration warnings in development
  reactStrictMode: true,
  swcMinify: true,
  // Handle RTL properly
  i18n: {
    locales: ['he'],
    defaultLocale: 'he',
  }
};

export default nextConfig;
