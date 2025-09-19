// API Configuration
// Change this to your deployed Lambda API Gateway URL when deploying
export const API_CONFIG = {
  // For local development
  // BASE_URL: 'http://localhost:8000',
  
  // For production (replace with your actual Lambda API Gateway URL)
  BASE_URL: 'https://tfaownvmmkgoxbs4hrg2cehvci0tzrrp.lambda-url.eu-north-1.on.aws',
  
  ENDPOINTS: {
    QURAN_QUESTION: '/quran_question',
    FIQH_QUESTION: '/fiqh_question'
  }
}

// Get the current API base URL
export const getApiUrl = (endpoint) => {
  return `${API_CONFIG.BASE_URL}${endpoint}`
}
