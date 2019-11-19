#!/usr/bin/env node
"use strict";
exports.__esModule = true;
var romanian_1 = require("./romanian");
if (process.argv[2]) {
    console.log(romanian_1.translateRomanian(process.argv[2]));
}
else {
    console.log("Please provide some romanian characters as CLI argument");
}
