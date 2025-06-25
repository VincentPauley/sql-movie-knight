<template>
  <div>
    <h1>Movie Knight</h1>
    <ul>
      <li v-for="genre in genres" :key="genre.id">
        {{genre.name}}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      genresFetched: false,
      genres: []
    }
  },
  mounted() {
    if (!this.genresFetched) {
      fetch('http://localhost:3000/api/genres')
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
