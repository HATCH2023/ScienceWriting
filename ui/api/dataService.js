import axios from 'axios';

export const getArticlesForKeywords = (keywords, index = 0) =>
  axios.get(`/python-api/articles?keywords=${encodeURIComponent(keywords)}&index=${index}`);
