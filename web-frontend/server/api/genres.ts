import { defineEventHandler } from 'h3';

export default defineEventHandler(async (event) => {
  try {
    const response = await fetch(`http://localhost:8000/genres`);
    if (!response.ok) {
      throw new Error(`Failed to fetch genres: ${response.status} ${response.statusText}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching genres:', error);
    return { error: 'Failed to fetch genres' };
  }
});
