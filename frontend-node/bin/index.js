const axios = require("axios");
const readline = require("readline");

const command = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const apiUrl = "https://e882nk6qt7.execute-api.us-west-2.amazonaws.com/dev";

function createIssue() {
	command.question("Enter the JSON object to create: ", (jsonObject) => {
		axios
			.post(`${apiUrl}/create`, JSON.parse(jsonObject))
			.then((response) => {
				console.log("Create Response:", response.data);
				command.close();
			})
			.catch((error) => {
				console.error("Create Error:", error.message);
				command.close();
			});
	});
}

function readIssue(id) {
	axios
		.get(`${apiUrl}/read/${id}`)
		.then((response) => {
			console.log("Read Response:", response.data);
			command.close();
		})
		.catch((error) => {
			console.error("Read Error:", error.message);
			command.close();
		});
}

function updateIssue() {
	command.question("Enter the JSON object to update: ", (jsonObject) => {
		axios
			.put(`${apiUrl}/update`, JSON.parse(jsonObject))
			.then((response) => {
				console.log("Update Response:", response.data);
				command.close();
			})
			.catch((error) => {
				console.error("Update Error:", error.message);
				command.close();
			});
	});
}

function deleteIssue(id) {
	axios
		.delete(`${apiUrl}/delete/${id}`)
		.then(() => {
			console.log(`Issue with ID ${id} deleted successfully.`);
			command.close();
		})
		.catch((error) => {
			console.error("Delete Error:", error.message);
			command.close();
		});
}

// Main menu
console.log("Choose an operation:");
console.log("1. Create Issue");
console.log("2. Read Issue");
console.log("3. Update Issue");
console.log("4. Delete Issue");

command.question("Enter the operation number: ", (choice) => {
	switch (choice) {
		case "1":
			createIssue();
			break;
		case "2":
			command.question("Enter the ID of the issue to read: ", (id) => {
				readIssue(id);
			});
			break;
		case "3":
			updateIssue();
			break;
		case "4":
			command.question("Enter the ID of the issue to delete: ", (id) => {
				deleteIssue(id);
			});
			break;
		default:
			console.error("Invalid choice. Please choose a valid operation.");
			command.close();
	}
});
