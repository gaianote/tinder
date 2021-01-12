import axios from 'axios'


export const closeClientProxy = () => {
  return axios({
      url: '/api/config/client/proxy',
      method: 'PUT',
      data:{"status":false}
  })
}

export const openClientProxy = () => {
    return axios({
        url: '/api/config/client/proxy',
        method: 'PUT',
        data:{"status":true}
    })
  }