/*
 * Copyright (c) 2023 Prabhav Mehra <<url>>
 *
 * Created Date: Tuesday, September 26th 2023, 9:21:00 pm
 * Author: Prabhav Mehra
 *
 * Copyright © 2023 Telepsych.AI Pty Ltd. All rights reserved.
 * This code is the property of Telepsych.AI Pty Ltd and is protected by the
 * Copyright Act 1968 (Cth) and its amendments. Unauthorized reproduction
 * or distribution of this code, or any portion thereof, is strictly prohibited.
 *
 * For inquiries regarding the use or licensing of this code, please contact
 * Telepsych.AI Pty Ltd at the following address:
 *
 * Telepsych.AI Pty Ltd South Yarra Melbourne, VIC, 3141 Australia Email:
 * telepsychaus@gmail.com
 *
 * Thank you for respecting our intellectual property rights.
 */
const axios = require("axios");
const readline = require("readline");

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const apiUrl = "https://e882nk6qt7.execute-api.us-west-2.amazonaws.com/dev";

function createIssue() {
	rl.question("Enter the JSON object to create: ", (jsonObject) => {
		axios
			.post(`${apiUrl}/create`, JSON.parse(jsonObject))
			.then((response) => {
				console.log("Create Response:", response.data);
				rl.close();
			})
			.catch((error) => {
				console.error("Create Error:", error.message);
				rl.close();
			});
	});
}

function readIssue(id) {
	axios
		.get(`${apiUrl}/read/${id}`)
		.then((response) => {
			console.log("Read Response:", response.data);
			rl.close();
		})
		.catch((error) => {
			console.error("Read Error:", error.message);
			rl.close();
		});
}

function updateIssue() {
	rl.question("Enter the JSON object to update: ", (jsonObject) => {
		axios
			.put(`${apiUrl}/update`, JSON.parse(jsonObject))
			.then((response) => {
				console.log("Update Response:", response.data);
				rl.close();
			})
			.catch((error) => {
				console.error("Update Error:", error.message);
				rl.close();
			});
	});
}

function deleteIssue(id) {
	axios
		.delete(`${apiUrl}/delete/${id}`)
		.then(() => {
			console.log(`Issue with ID ${id} deleted successfully.`);
			rl.close();
		})
		.catch((error) => {
			console.error("Delete Error:", error.message);
			rl.close();
		});
}

// Main menu
console.log("Choose an operation:");
console.log("1. Create Issue");
console.log("2. Read Issue");
console.log("3. Update Issue");
console.log("4. Delete Issue");

rl.question("Enter the operation number: ", (choice) => {
	switch (choice) {
		case "1":
			createIssue();
			break;
		case "2":
			rl.question("Enter the ID of the issue to read: ", (id) => {
				readIssue(id);
			});
			break;
		case "3":
			updateIssue();
			break;
		case "4":
			rl.question("Enter the ID of the issue to delete: ", (id) => {
				deleteIssue(id);
			});
			break;
		default:
			console.error("Invalid choice. Please choose a valid operation.");
			rl.close();
	}
});
