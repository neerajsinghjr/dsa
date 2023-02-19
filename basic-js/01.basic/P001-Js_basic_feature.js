/*
-------------------------------------------------------------------------------------
-> Title: Javascript Basic Feature
-> Attempted: 14/02/2023
-> Description: 
-------------------------------------------------------------------------------------

**** Basic Javascript Programs !!!

-------------------------------------------------------------------------------------
*/


function datatypExpl() {
	const personID = "123abc";
	const quotient = personID / 2;

	console.log(typeof quotient === NaN)
	console.log(quotient);
	console.log(isNaN(quotient))
}

function stringExpl() {
	const num1 = 1290
	const num2 = -1290
	const num3 = 12.90

	console.log(`num1: ${num1} || num2 : ${num2} || num3: ${num3}`)
}

function datatypeExpl() {
	count = 20
	message = "Hello World";

	console.log(count)
	console.log(typeof count)
	console.log(message)
	console.log(typeof message)

	isAdmin = false && true
	console.log(isAdmin)
}

function unaryOperatorExpl() {
	//--- increment or decrement operator;
	var number = 10
	console.log(number)
	number++
	console.log(number)
	number++
	console.log(number)

	var num = 1
	console.log(num)
	++num
	console.log(num)
	++num
	console.log(num)
}

function undefinedAndNullExpl() {
	// const age 
	console.log(age)

	const name = null;
	const age = null;
	console.log(name);
	console.log(age);

	// undefined variable 
	let name1 = undefined
	let name2 = null 
	const name3 = undefined
	const name4 = null

	console.log(typeof name1)
	console.log(typeof name2)
	console.log(name1 == name2)
	console.log(name1 === name2)
	console.log(name3)
	console.log(name4)

	// checking scope of variable;
	let a = 10
	console.log(a)
	if(a == 10) {
		console.log(a)
		a = 20
		console.log(a)
	}
	console.log(a)
}

function objectExpl() {
	// const profile = {
	// 	first name : "Neeraj",	// Incorrect: Unexpected Variable;
	// 	middle_name : "Singh",		// Correct
	// 	last-name : "Junior"		// Incorrect: Unexpected Token '-';
	// }
	// console.log(profile)

	const car = {
	  model: 2011,
	  fuelType: "diesel",
	  "full Name" : "Hyundai Verna"
	};

	console.log(car["full Name"])
	console.log(car.model);
	console.log(car['fullName'])

	const profile = {
		"first name" : "Neeraj",
		middle_name : "Singh",
		"last-name" : "Junior"
	}

	console.log(profile["first name"])

	const subjectWithCode = {
	   101 : "Physics",
	   102 : "English",
	   103 : "Chemistry",
	   104 : "Computer with cpp"
	}

	console.log(subjectWithCode[101])

	const person = {
		name : "Adam Jensen",
		age : 26,
		isAdmin : true
	};

	person.profession = "Software Engineer"
	console.log(person)  

	const subjects = {
	  101: "Physics",
	  102: "Biology",
	  103: "Chemistry"
	};

	subjects[104] = "Computer";
	// Same as subjects[200] = "Mathematics"
	subjects[100 * 2] = "Mathematics"; 

	console.log(subjects);
}

function objectKeyAndValues() {
	const subjects = {
	  101: ["Physics","P2"],
	  102: "Biology",
	  103: "Chemistry"
	};

	console.log(subjects);
	console.log(Object.keys(subjects))
	console.log(Object.values(subjects))
	console.log(Object.entries(subjects))
}

function objectShorthand() {
	const model = 2011;
	const fuelType = "diesel";

	const car = {
		models,
		fuelTypes,
	};

	console.log(car);
}

function main() {
	objectShorthand()
	// objectKeyAndValues()
	// objectExpl()
	// undefinedAndNullExpl()
	// unaryOperatorExpl()
	// stringExpl()
	// datatypeExpl()
}

main()