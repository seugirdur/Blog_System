<script setup lang="ts">

</script>

<template>

  <div class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8">

    <div class="absolute inset-0">

      <div class="bg-white h-1/3 sm:h-2/3"> </div>

    </div>

    <div class="relative max-w-7x1 mx-auto">

      <div class="text-center">

        <h2 class="text-3x1 tracking-tight from-extrabold text-gray-900 sm:text-4x1">

          Exibindo Postagens

        </h2>

        <p class="mt-3 max-w-2x1 mx-auto text-x1 text-gray-500 sm:mt-4">

          ====    Blof Coffee Tag    ====
        </p>

      </div>

      <div class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">

        <div v-for="posts in APIData" :key="posts.id" class="flex flex-col rounded-lg shadow-lg overflow-hidden">

          <router-link :to="{ name: 'BlogPost', params: { id: posts.id, title: posts.title, slug: posts.slug, content: posts.content}}">

            <p>{{ posts.title }}</p>

          </router-link>


          {{ posts.content }}

        </div>

      </div>


    </div>

  </div>



</template>

<script>
 import {getApi} from "@/axios-api";

  export default {
    name: 'BlogView',
    components: {},
    props: [],
    data () {
      return {
        APIData: [],
      }
    },
    computed: {

    },
    mounted () {
      this.getPosts();
    },
    methods: {
      async getPosts() {
        try {
          const response = await getApi.get('/blog/post/');
          this.APIData = response.data;
          console.log(this.APIData);
        } catch (error) {
          console.log(error);
        }
      }
    }
  }

</script>

<style scoped>

</style>