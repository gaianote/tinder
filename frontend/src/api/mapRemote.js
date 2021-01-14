import axios from 'axios'


export const getMapRemoteRules = () => {
  return axios({
    url: `/api/map`
  })
}

export const addMapRule  = (rules) => {
  return axios({
    url: '/api/map',
    method: 'POST',
    data: rules
  })
}


export const deleteMapRule = (rid) => {
  return axios({
    url: '/api/map',
    method: 'DELETE',
    data: { rid :  rid}
  })
}

export const updateMapRule  = (rules) => {
    return axios({
      url: '/api/map',
      method: 'PUT',
      data: rules
    })
  }