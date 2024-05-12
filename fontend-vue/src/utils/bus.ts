import mitt from 'mitt'
 
type Events = {
  stylename: string
  gameid: number
}
 
const bus = mitt<Events>()
export default bus