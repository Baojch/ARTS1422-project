import mitt from 'mitt'
 
type Events = {
  stylename: string
  gameid: number
  timestamp: string
  gamename: string
}
 
const bus = mitt<Events>()
export default bus