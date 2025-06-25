<template>
  <div>
    <h1>Movie Knight</h1>

    <h3>Main Genres {{mainGenres.length}}</h3>
    <ul>
      <li v-for="mainGenre in mainGenres" :key="mainGenre.id" >
        {{mainGenre.name}}
      </li>
    </ul>
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
