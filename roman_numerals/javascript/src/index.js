const {translateRomanian} = require("./romanian");

function main(input) {
    const count = translateRomanian(input);
    console.log(`${input}:${count}`);
}

main(process.argv[2]);
