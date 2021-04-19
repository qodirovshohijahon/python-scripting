    class DateFormatter extends Date {
        getFormattedDate() {
            const months = [
                "Yanvar",
                "Fevral",
                "Mart",
                "Aprel",
                "May",
                "Iyun",
                "Iyul",
                "Avgust",
                "Sentabr",
                "Oktabr",
                "Noyabr",
                "Dekabr",
            ];
            return `${this.getDate()}-${months[this.getMonth()]
                }, ${this.getFullYear()} - yil`;
        }
    }
module.exports.datesInUzbekFormatted = function getDatesInUzbek() {
    let date = '2021 1 12'
    return new DateFormatter(date).getFormattedDate()
}
    // usage
    //console.log(new DateFormatter("2021 1 12").getFormattedDate());