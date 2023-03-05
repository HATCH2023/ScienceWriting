import axios from 'axios';

export const getArticlesForKeywords = (keywords, index = 0) =>
  axios.get(`/python-api/articles?keywords=${encodeURIComponent(keywords)}&index=${index}`);

export const getSummary = (url) =>
  axios.get(`/python-api/summarize?url=${encodeURIComponent(url)}`);

export const getPlatormContent = (summary) =>
  axios.post('/python-api/platformContent', { summary });
