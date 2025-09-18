<template>
  <div class="bg-white rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-semibold text-islamic-green mb-6">Fiqh Assistant</h2>
    
    <!-- Input Form -->
    <div class="space-y-4 mb-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Select Madhhab
        </label>
        <select
          v-model="selectedMadhhab"
          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-islamic-green focus:border-transparent"
        >
          <option value="Hanafi">Hanafi</option>
          <option value="Shafi'i">Shafi'i</option>
          <option value="Maliki">Maliki</option>
          <option value="Hanbali">Hanbali</option>
        </select>
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Your Fiqh Question
        </label>
        <textarea
          v-model="question"
          rows="4"
          placeholder="Ask about prayer, fasting, business transactions, family matters, etc..."
          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-islamic-green focus:border-transparent"
        ></textarea>
      </div>
      
      <!-- Quick Topic Suggestions -->
      <div>
        <p class="text-sm text-gray-600 mb-2">Quick suggestions:</p>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="topic in quickTopics"
            :key="topic"
            @click="question = topic"
            class="px-3 py-1 text-sm bg-islamic-cream text-islamic-green rounded-full hover:bg-islamic-gold hover:text-white transition-colors"
          >
            {{ topic }}
          </button>
        </div>
      </div>
      
      <button
        @click="submitQuestion"
        :disabled="loading || !question.trim()"
        class="w-full bg-islamic-green text-white py-3 px-6 rounded-lg font-medium hover:bg-opacity-90 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
      >
        {{ loading ? 'Getting Ruling...' : 'Get Fiqh Ruling' }}
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-8">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-islamic-green"></div>
      <p class="mt-2 text-gray-600">Consulting fiqh sources...</p>
    </div>

    <!-- Response Display -->
    <div v-if="response && !loading" class="bg-gray-50 rounded-lg p-6">
      <h3 class="text-lg font-semibold text-islamic-green mb-4">
        Ruling ({{ selectedMadhhab }} Madhhab)
      </h3>
      
      <!-- Answer -->
      <div class="mb-6">
        <h4 class="font-medium text-gray-900 mb-2">Ruling</h4>
        <p class="text-gray-700 leading-relaxed">{{ response.answer }}</p>
      </div>
      
      <!-- Steps (if available) -->
      <div v-if="response.steps && response.steps.length > 0" class="mb-6">
        <h4 class="font-medium text-gray-900 mb-2">Step-by-Step Guidance</h4>
        <ol class="space-y-2">
          <li
            v-for="(step, index) in response.steps"
            :key="index"
            class="flex items-start"
          >
            <span class="bg-islamic-green text-white rounded-full w-6 h-6 flex items-center justify-center text-sm font-medium mr-3 mt-0.5">
              {{ index + 1 }}
            </span>
            <span class="text-gray-700">{{ step }}</span>
          </li>
        </ol>
      </div>
      
      <!-- References -->
      <div v-if="response.references && response.references.length > 0">
        <h4 class="font-medium text-gray-900 mb-2">References</h4>
        <ul class="text-sm text-gray-600 space-y-1">
          <li v-for="(ref, index) in response.references" :key="index" class="flex items-start">
            <span class="text-islamic-gold mr-2">•</span>
            {{ ref }}
          </li>
        </ul>
      </div>
    </div>

    <!-- Error State -->
    <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { getApiUrl, API_CONFIG } from '../config.js'

export default {
  name: 'FiqhAssistant',
  setup() {
    const selectedMadhhab = ref('Hanafi')
    const question = ref('')
    const response = ref(null)
    const loading = ref(false)
    const error = ref('')

    const quickTopics = [
      'Prayer times and conditions',
      'Fasting requirements',
      'Zakat calculation',
      'Business transactions',
      'Marriage contracts',
      'Inheritance laws'
    ]

    // Use configured API endpoint

    const submitQuestion = async () => {
      if (!question.value.trim()) {
        error.value = 'Please enter a question.'
        return
      }

      loading.value = true
      error.value = ''
      response.value = null

      try {
        const requestData = {
          question: question.value,
          madhhab: selectedMadhhab.value
        }

        const result = await axios.post(getApiUrl(API_CONFIG.ENDPOINTS.FIQH_QUESTION), requestData)
        response.value = result.data
      } catch (err) {
        error.value = 'Failed to get ruling. Please try again.'
        console.error('Error:', err)
      } finally {
        loading.value = false
      }
    }

    return {
      selectedMadhhab,
      question,
      response,
      loading,
      error,
      quickTopics,
      submitQuestion
    }
  }
}
</script>
