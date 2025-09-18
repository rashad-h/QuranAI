// API Configuration
// Change this to your deployed Lambda API Gateway URL when deploying
export const API_CONFIG = {
  // For local development
  // BASE_URL: 'http://localhost:8000',
  
  // For production (replace with your actual Lambda API Gateway URL)
  BASE_URL: 'https://93ugi0pu79.execute-api.eu-north-1.amazonaws.com/default/quranai-backend',
  
  ENDPOINTS: {
    QURAN_QUESTION: '/quran_question',
    FIQH_QUESTION: '/fiqh_question'
  }
}

// Get the current API base URL
export const getApiUrl = (endpoint) => {
  return `${API_CONFIG.BASE_URL}${endpoint}`
}
