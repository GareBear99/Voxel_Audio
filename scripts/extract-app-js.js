#!/usr/bin/env node
const fs = require("fs");
const html = fs.readFileSync("index.html", "utf8");
const match = html.match(/<script>([\s\S]*?)<\/script>/);
if (!match) {
  console.error("No script block found.");
  process.exit(1);
}
fs.writeFileSync("app.extracted.js", match[1]);
console.log("Wrote app.extracted.js");
