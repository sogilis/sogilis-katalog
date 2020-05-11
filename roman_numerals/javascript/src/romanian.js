/**
 * Translates romanian numbers
 */
function translateRomanian(input) {
    if (!input) {
        return undefined;
    }
    return input.split("").length;
}

exports.translateRomanian = translateRomanian;
