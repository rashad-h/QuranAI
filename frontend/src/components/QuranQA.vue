<template>
  <div class="bg-white rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-semibold text-islamic-green mb-6">Quran Q&A</h2>
    
    <!-- Input Form -->
    <div class="space-y-4 mb-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Surah/Ayah Reference (optional)
        </label>
        <input
          v-model="ayahReference"
          type="text"
          placeholder="e.g., Surah 2:255 or Al-Baqarah 255"
          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-islamic-green focus:border-transparent"
        />
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Your Question
        </label>
        <textarea
          v-model="question"
          rows="4"
          placeholder="Ask about the meaning, context, or interpretation of the ayah..."
          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-islamic-green focus:border-transparent"
        ></textarea>
      </div>
      
      <button
        @click="submitQuestion"
        :disabled="loading || (!ayahReference && !question)"
        class="w-full bg-islamic-green text-white py-3 px-6 rounded-lg font-medium hover:bg-opacity-90 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
      >
        {{ loading ? 'Getting Answer...' : 'Ask Question' }}
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-8">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-islamic-green"></div>
      <p class="mt-2 text-gray-600">Processing your question...</p>
    </div>

    <!-- Response Display -->
    <div v-if="response && !loading" class="bg-gray-50 rounded-lg p-6">
      <h3 class="text-lg font-semibold text-islamic-green mb-4">Answer</h3>
      
      <!-- Summary -->
      <div class="mb-6">
        <h4 class="font-medium text-gray-900 mb-2">Tafsir Summary</h4>
        <p class="text-gray-700 leading-relaxed">{{ response.summary }}</p>
      </div>
      
      <!-- Word by Word (if available) -->
      <div v-if="response.word_by_word && response.word_by_word.length > 0" class="mb-6">
        <h4 class="font-medium text-gray-900 mb-2">Word-by-Word Translation</h4>
        <div class="grid grid-cols-2 gap-2 text-sm">
          <div
            v-for="(word, index) in response.word_by_word"
            :key="index"
            :class="[
              'p-2 rounded',
              index % 2 === 0 ? 'bg-white text-islamic-green font-medium' : 'bg-islamic-cream text-gray-700'
            ]"
          >
            {{ word }}
          </div>
        </div>
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
  name: 'QuranQA',
  setup() {
    const ayahReference = ref('')
    const question = ref('')
    const response = ref(null)
    const loading = ref(false)
    const error = ref('')

    // Use configured API endpoint

    const submitQuestion = async () => {
      if (!ayahReference.value && !question.value) {
        error.value = 'Please provide either an ayah reference or a question.'
        return
      }

      loading.value = true
      error.value = ''
      response.value = null

      try {
        const requestData = {
          ayah_or_reference: ayahReference.value || 'General Quran question',
          question: question.value
        }

        const result = await axios.post(getApiUrl(API_CONFIG.ENDPOINTS.QURAN_QUESTION), requestData)
        response.value = result.data
      } catch (err) {
        error.value = 'Failed to get answer. Please try again.'
        console.error('Error:', err)
      } finally {
        loading.value = false
      }
    }

    return {
      ayahReference,
      question,
      response,
      loading,
      error,
      submitQuestion
    }
  }
}
</script>
