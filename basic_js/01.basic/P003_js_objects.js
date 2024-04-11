function objExpl() {
	var car = {
		'name': 'HYUNDAI',
		'model': 'HYN-90',
		'type': 'PETROL',
		'qty': 80
	}

	console.log(`Name: ${car.name}, Model: ${car.model}, Type: $
	{car.type}, Quantity: ${car.qty}`) }

function objBracketConvention() {
	let fullname = {
		'firstname': 'neeraj',
		'middle-name': 'singh',
		'last_name': 'junior'
		// 110: true 	// not working expected key error;;
	}

	// case 1: ok
	console.log(fullname)

	/* case 2: not ok 
	Because key is not a full fledged string to be act as a 
	object key, So we can't user dot object convention for 
	this case. 
	Refer case 2.1
	*/ 
	// console.log("middle name: " + fullname.middle-name)
	
	// case 2.1
	console.log("middle name: " + fullname['middle-name'])

	let testObj = {
		110: true
	}

	// case 4: not ok (refer case 2 explanation)
	// console.log("test field: " + fullname.110)
	abc = '110'
	console.log("test field: " + fullname.abc )

	// // case 4.1
	console.log("test-field: " + testObj['110'])

}

function main() {
	// objExpl()
	objBracketConvention()
}

main()
