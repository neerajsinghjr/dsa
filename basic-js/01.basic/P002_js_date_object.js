let d = new Date()
let dt = '2023-07-19 10:10:10'
let today = new Date(d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), d.getSeconds())
let follow_up_on = new Date(dt)
console.log("follow_up_on "+ follow_up_on)
console.log("today: " + today)
if(follow_up_on.getTime() < today.getTime()) {
	console.log("if")
} else {
	console.log("else")
}