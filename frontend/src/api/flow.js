import axios from 'axios'


export const getFlowDetail = (flowId) => {
  return axios({
    url: '/api/flow/' + flowId
  })
}

export const getFlowList = (page_num,page_size) => {
  return axios({
    url: `/api/flow?page_num=${page_num}&page_size=${page_size}`
  })
}

export const deleteAllFlow = () => {
  return axios({
    url: '/api/flow',
    method: 'DELETE',
    data: { ids: null }
  })
}

export const saveSelectedFlow = (ids) => {
  return axios({
    url: '/api/flow',
    method: 'POST',
    data: { ids }
  })
}

export const deleteSelectedFlow = (ids) => {
  return axios({
    url: '/api/flow',
    method: 'DELETE',
    data: { ids }
  })
}