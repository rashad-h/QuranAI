<template>
  <div class="min-h-screen bg-islamic-cream">
    <!-- Header -->
    <header class="bg-islamic-green text-white shadow-lg">
      <div class="container mx-auto px-4 py-6">
        <h1 class="text-3xl font-bold text-center">QuranAI</h1>
        <p class="text-center text-islamic-gold mt-2">Islamic Study Assistant</p>
      </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
      <!-- Tab Navigation -->
      <div class="flex justify-center mb-8">
        <div class="bg-white rounded-lg shadow-md p-1 flex">
          <button
            @click="activeTab = 'quran'"
            :class="[
              'px-6 py-3 rounded-md font-medium transition-all duration-200',
              activeTab === 'quran' 
                ? 'bg-islamic-green text-white shadow-md' 
                : 'text-islamic-green hover:bg-gray-50'
            ]"
          >
            Quran Q&A
          </button>
          <button
            @click="activeTab = 'fiqh'"
            :class="[
              'px-6 py-3 rounded-md font-medium transition-all duration-200',
              activeTab === 'fiqh' 
                ? 'bg-islamic-green text-white shadow-md' 
                : 'text-islamic-green hover:bg-gray-50'
            ]"
          >
            Fiqh Assistant
          </button>
        </div>
      </div>

      <!-- Tab Content -->
      <div class="max-w-4xl mx-auto">
        <!-- Quran Q&A Tab -->
        <div v-if="activeTab === 'quran'" class="space-y-6">
          <QuranQA />
        </div>

        <!-- Fiqh Assistant Tab -->
        <div v-if="activeTab === 'fiqh'" class="space-y-6">
          <FiqhAssistant />
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-islamic-green text-white text-center py-4 mt-12">
      <p>&copy; 2025 QuranAI</p>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue'
import QuranQA from './components/QuranQA.vue'
import FiqhAssistant from './components/FiqhAssistant.vue'

export default {
  name: 'App',
  components: {
    QuranQA,
    FiqhAssistant
  },
  setup() {
    const activeTab = ref('quran')

    return {
      activeTab
    }
  }
}
</script>
