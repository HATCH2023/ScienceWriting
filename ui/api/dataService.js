import axios from 'axios';

export const getArticlesForKeywords = (keywords, index = 0) =>
  axios.get(`/python-api/articles?keywords=${encodeURIComponent(keywords)}&index=${index}`);

export const getSummary = (url) =>
  axios.get(`/python-api/summarize?url=${encodeURIComponent(url)}`);

export const getPlatformContent = (summary) =>
  axios.post('/python-api/platformContent', { summary });

export const getArtificialImages = (summary) =>
  axios.post('/python-api/getImages', { summary });

export const postFacebook = (path, caption) =>
  axios.post('/python-api/postFacebook', { path, caption });

export const postTwitter = (path, caption) =>
  axios.post('/python-api/postTwitter', { path, caption });

export const postLinkedIn = (path, caption) =>
  axios.post('/python-api/postLinkedIn', { path, caption });

export const postInstagram = (path, caption) =>
  axios.post('/python-api/postInstagram', { path, caption });
