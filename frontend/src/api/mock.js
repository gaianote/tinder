import axios from 'axios'


export const getMockRules = () => {
  return axios({
    url: `/api/mock`
  })
}

export const getMockRuleDetail = (rid) => {
  return axios({
    url: `/api/mock?rid=${rid}`
  })
}

export const addMockRule = (rules) => {
  return axios({
    url: '/api/mock',
    method: 'POST',
    data: rules
  })
}


export const deleteMockRule = (rid) => {
  return axios({
    url: '/api/mock',
    method: 'DELETE',
    data: { rid :  rid}
  })
}

export const updateMockRule  = (rules) => {
    return axios({
      url: '/api/mock',
      method: 'PUT',
      data: rules
    })
  }