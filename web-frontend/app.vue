<template>
  <NuxtLayout>
    <v-app>
    <h1>Movie Knight</h1>

    <h3>Selected Genres</h3>
    <ul>
      <li v-for="genreId in selectedGenres" :key="genreId">
        {{ genreId }}
      </li>
    </ul>
    <h3>Main Genres {{mainGenres.length}}</h3>
    <!-- <ul>
      <li v-for="mainGenre in mainGenres" :key="mainGenre.id" >
        {{mainGenre.name}}
      </li>
    </ul> -->
    <v-container fluid>
      <v-checkbox
        v-for="mainGenre in mainGenres"
        :key="mainGenre.id"
        v-model="selectedGenres"
        :value="mainGenre.id"
        :label="mainGenre.name"
        dense
        class="custom-checkbox"
      ></v-checkbox>
    </v-container>

    <h3>Sub-Genres {{subGenres.length}}</h3>
    <ul>
      <li v-for="subGenre in subGenres" :key="subGenre.id" >
        {{subGenre.name}}
      </li>
    </ul> 
    <h3>Tag-Genres {{tagGenres.length}}</h3>
    <ul>
      <li v-for="tagGenre in tagGenres" :key="tagGenre.id" >
        {{tagGenre.name}}
      </li>
    </ul> 
  </v-app>
  </NuxtLayout>
</template>

<style scoped>
.v-selection-control--density-default {
  height: auto !important;
}
</style>

<script lang="ts">
export default {
  data() {
    return {
      genresFetched: false,
      genres: [],
      selectedGenres: []
    }
  },
  computed: {
    mainGenres() {
      return this.genres.filter(genre => genre.level === 1)
    },
    subGenres() {
      return this.genres.filter(genre => genre.level === 2)
    },
    tagGenres() {
      return this.genres.filter(genre => genre.level === 3)
    },
  },
  mounted() {
    if (!this.genresFetched) {
      fetch('http://localhost:3001/api/genres')
        .then(async(r) => {
          const result = await r.json()
          this.genresFetched = true
          this.genres = result.genres
        })
        .catch(e => {
          console.error('Error fetching genres:', e);
          this.genresFetched = true
        })
    }
  }
};
</script>
