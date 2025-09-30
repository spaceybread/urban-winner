import * as fs from 'fs';
import * as readline from 'readline';

async function processFileLines(filePath) {
	let kp = [
	["X", "X", "1", "X", "X"], 
	["X", "2", "3", "4", "X"], 
	["5", "6", "7", "8", "9"], 
	["X", "A", "B", "C", "X"], 
	["X", "X", "D", "X", "X"] 
	]; 

	let pos = [2, 0]; 

	const fileStream = fs.createReadStream(filePath);

	const rl = readline.createInterface({
input: fileStream,
crlfDelay: Infinity
});

let code = [0, 0, 0, 0];
let c_idx = 0; 
for await (const line of rl) {

	for (const char of line) {
		if (char == "U") {
			if (pos[0] != 0 && kp[pos[0] - 1][pos[1]] != "X") {
				pos[0] -= 1; 
			}
		} else if (char == "D") {
			if (pos[0] != 4 && kp[pos[0] + 1][pos[1]] != "X") {
				pos[0] += 1; 
			}
		} else if (char == "R") {
			if (pos[1] != 4 && kp[pos[0]][pos[1] + 1] != "X") {
				pos[1] += 1; 
			}
		} else if (char == "L") {
			if (pos[1] != 0 && kp[pos[0]][pos[1] - 1] != "X") {
				pos[1] -= 1; 
			}
		}
	}

	code[c_idx] = kp[pos[0]][pos[1]]; 
	c_idx += 1; 
}
console.log(code);
console.log('Finished reading file.');
}

processFileLines('input.txt');
