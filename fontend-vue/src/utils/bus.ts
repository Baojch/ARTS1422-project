import mitt from 'mitt'
 
type Events = {
  sendMsg: string
  gameid: number
}
 
const bus = mitt<Events>()
export default bus